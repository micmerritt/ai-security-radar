#!/usr/bin/env python3
"""
AI Security Radar - v1.1 Collector (arXiv)

What it does:
- Reads keywords from sources/keywords.yml
- Queries arXiv Atom API for recent matching papers
- Filters out likely non-security noise
- Categorizes results into readable sections
- Writes radar/latest.md and prepends a run section to radar/weekly-digest.md

No external dependencies.
"""

from __future__ import annotations

import datetime as dt
import html
import os
import re
import sys
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any, Dict, List


# ----------------------------
# Paths
# ----------------------------
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KEYWORDS_FILE = os.path.join(REPO_ROOT, "sources", "keywords.yml")
LATEST_MD = os.path.join(REPO_ROOT, "radar", "latest.md")
WEEKLY_MD = os.path.join(REPO_ROOT, "radar", "weekly-digest.md")


# ----------------------------
# Collection + display knobs
# ----------------------------
RECENT_DAYS = 10
MAX_PULL = 30
MAX_SHOW_LATEST = 14
MAX_SHOW_WEEKLY = 6

# ----------------------------
# Issue automation settings
# ----------------------------
OPEN_ISSUES_FOR_TOP_N = 3
ISSUE_LABELS = ["radar", "paper"]

ARXIV_ATOM_ENDPOINT = "https://export.arxiv.org/api/query"

# If a paper doesn't hit at least one of these "security-ish" terms
# in title+abstract, we drop it to reduce noise (video gen, medical ML, etc.).
STRONG_SECURITY_TERMS = [
    "prompt injection",
    "indirect prompt",
    "instruction injection",
    "jailbreak",
    "backdoor",
    "poison",
    "data poisoning",
    "model extraction",
    "membership inference",
    "privacy leakage",
    "data leakage",
    "exfiltration",
    "vulnerability",
    "exploit",
    "attack",
    "adversarial",
    "red team",
]

WEAK_SECURITY_TERMS = [
    "agent",
    "tool call",
    "tool-calling",
    "function calling",
    "rag",
    "retrieval",
    "vector",
    "embedding",
    "guardrail",
    "sandbox",
    "leak",
]

# Category rules are simple keyword matches over title+abstract.
CATEGORY_RULES: Dict[str, List[str]] = {
    "Agent & Tool Security": ["agent", "tool call", "tool-calling", "function calling", "workflow", "side effect", "mcp", "model context protocol"],
    "Prompt Injection": ["prompt injection", "indirect prompt", "instruction injection", "unicode", "invisible"],
    "RAG & Retrieval Attacks": ["rag", "retrieval", "vector", "embedding", "knowledge base", "document poisoning", "context injection"],
    "Poisoning & Backdoors": ["poison", "data poisoning", "training data", "backdoor", "trojan"],
    "Model Extraction & Privacy": ["model extraction", "membership inference", "privacy leakage", "data leakage", "exfiltration"],
    "Adversarial ML": ["adversarial example", "adversarial", "evasion", "robust", "robustness"],
}


def _utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _read_keywords_from_simple_yaml(path: str) -> List[str]:
    """
    Minimal YAML reader for this file shape:

    keywords:
      - prompt injection
      - rag poisoning
      - ...

    Avoids external deps (PyYAML).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing keywords file: {path}")

    keywords: List[str] = []
    in_keywords_block = False
    with open(path, "r", encoding="utf-8") as f:
        for raw in f.readlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if re.match(r"^keywords\s*:\s*$", line):
                in_keywords_block = True
                continue
            if in_keywords_block:
                m = re.match(r"^-+\s*(.+?)\s*$", line)
                if m:
                    kw = m.group(1).strip().strip('"').strip("'")
                    if kw:
                        keywords.append(kw)
                else:
                    # stop if list ends
                    if re.match(r"^[A-Za-z0-9_]+\s*:\s*$", line):
                        break

    # De-dupe while preserving order
    seen = set()
    out: List[str] = []
    for k in keywords:
        kl = k.lower()
        if kl not in seen:
            seen.add(kl)
            out.append(k)
    return out


def _build_arxiv_search_query(keywords: List[str]) -> str:
    """
    Build an arXiv query string that searches in title+abstract.
    """
    clauses = []
    for kw in keywords:
        safe = kw.replace('"', "")
        if " " in safe:
            safe = f'"{safe}"'
        clauses.append(f"ti:{safe} OR abs:{safe}")
    return "(" + ") OR (".join(clauses) + ")"


def _fetch_arxiv_atom(search_query: str, max_results: int) -> str:
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_ATOM_ENDPOINT + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ai-security-radar/1.1 (GitHub Actions; contact: noreply)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _fetch_with_retries(search_query: str, max_results: int, tries: int = 3) -> str:
    last: Exception | None = None
    for _ in range(tries):
        try:
            return _fetch_arxiv_atom(search_query, max_results=max_results)
        except Exception as ex:
            last = ex
    assert last is not None
    raise last


def _parse_arxiv_entries(atom_xml: str) -> List[Dict[str, Any]]:
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
    }
    root = ET.fromstring(atom_xml)

    entries: List[Dict[str, Any]] = []
    for e in root.findall("atom:entry", ns):
        title = (e.findtext("atom:title", default="", namespaces=ns) or "").strip()
        summary = (e.findtext("atom:summary", default="", namespaces=ns) or "").strip()
        published = (e.findtext("atom:published", default="", namespaces=ns) or "").strip()
        updated = (e.findtext("atom:updated", default="", namespaces=ns) or "").strip()

        entry_id = (e.findtext("atom:id", default="", namespaces=ns) or "").strip()
        link = entry_id
        for l in e.findall("atom:link", ns):
            if l.get("rel") == "alternate" and l.get("href"):
                link = l.get("href")
                break

        authors = []
        for a in e.findall("atom:author", ns):
            name = (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
            if name:
                authors.append(name)

        title = html.unescape(re.sub(r"\s+", " ", title)).strip()
        summary = html.unescape(re.sub(r"\s+", " ", summary)).strip()

        entries.append(
            {
                "title": title,
                "summary": summary,
                "published": published,
                "updated": updated,
                "link": link,
                "authors": authors,
            }
        )
    return entries


def _parse_iso_utc(s: str) -> dt.datetime | None:
    if not s:
        return None
    try:
        # arXiv uses ISO8601 like 2026-03-02T18:22:01Z
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        return dt.datetime.fromisoformat(s).astimezone(dt.timezone.utc)
    except Exception:
        return None


def _filter_recent(entries: List[Dict[str, Any]], days: int) -> List[Dict[str, Any]]:
    cutoff = _utc_now() - dt.timedelta(days=days)
    out: List[Dict[str, Any]] = []
    for e in entries:
        t = _parse_iso_utc(e.get("published", "")) or _parse_iso_utc(e.get("updated", ""))
        if t and t >= cutoff:
            e["_ts"] = t
            out.append(e)
    return out


def _is_security_related(entry: Dict[str, Any]) -> bool:
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()

    if any(term in text for term in STRONG_SECURITY_TERMS):
        return True

    weak_hits = sum(1 for term in WEAK_SECURITY_TERMS if term in text)
    return weak_hits >= 2


def _categorize(entry: Dict[str, Any]) -> str:
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
    for cat, terms in CATEGORY_RULES.items():
        if any(t in text for t in terms):
            return cat
    return "Other (Review)"


def _build_idea_stub(category: str) -> str:
    # Deterministic, lightweight templates (no model calls)
    if category == "Prompt Injection":
        return "Create a prompt injection test corpus + evaluation harness for your agent or RAG pipeline."
    if category == "Agent & Tool Security":
        return "Build a tool-call abuse harness: mutate inputs and verify tool constraints, permissions, and side effects."
    if category == "RAG & Retrieval Attacks":
        return "Build a RAG poisoning harness: inject poisoned docs, measure retrieval changes, and capture failure modes."
    if category == "Poisoning & Backdoors":
        return "Build a minimal poisoning simulator plus simple detectors (trigger search, label flip tests, anomaly baselines)."
    if category == "Model Extraction & Privacy":
        return "Create a leakage test suite: can the system reveal secrets, training snippets, identifiers, or hidden policies?"
    if category == "Adversarial ML":
        return "Build a robustness benchmark harness with standard perturbations and report concrete failure modes."
    return "Turn this into a repeatable check: a small reproducer, dataset slice, or CI test for the described risk."


def _format_latest_md(run_ts: dt.datetime, keywords: List[str], entries: List[Dict[str, Any]]) -> str:
    run_date = run_ts.astimezone(dt.timezone.utc).strftime("%Y-%m-%d")
    kw_line = ", ".join(keywords[:12]) + ("…" if len(keywords) > 12 else "")

    lines: List[str] = []
    lines.append("# AI Security Radar\n")
    lines.append(f"_Last updated (UTC): **{run_date}**_\n")
    lines.append("## What this is\n")
    lines.append(
        "A curated, continuously-updated view of emerging AI security research signals "
        "and the build ideas they suggest.\n"
    )
    lines.append("## Tracked keywords\n")
    lines.append(f"{kw_line}\n")

    lines.append("## New / recent research (arXiv)\n")
    if not entries:
        lines.append("_No recent security-relevant matches in the selected window._\n")
        return "\n".join(lines).rstrip() + "\n"

    # Group entries by category, with preferred ordering
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for e in entries[:MAX_SHOW_LATEST]:
        groups.setdefault(e.get("category", "Other (Review)"), []).append(e)

    preferred_order = list(CATEGORY_RULES.keys()) + ["Other (Review)"]
    for cat in preferred_order:
        if cat not in groups:
            continue

        lines.append(f"### {cat}\n")
        for e in groups[cat]:
            title = e["title"]
            link = e["link"]
            published = e.get("published", "")[:10]
            authors = e.get("authors", [])
            author_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
            summary = textwrap.shorten(e.get("summary", ""), width=260, placeholder="…")

            lines.append(f"**{title}**  ")
            lines.append(f"- **Date:** {published}")
            lines.append(f"- **Authors:** {author_str if author_str else 'Unknown'}")
            lines.append(f"- **Link:** {link}")
            lines.append(f"- **Security insight:** {summary}")
            lines.append(f"- **Build idea:** {_build_idea_stub(cat)}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _prepend_weekly_digest(run_ts: dt.datetime, entries: List[Dict[str, Any]]) -> str:
    """
    Prepend a run section to weekly-digest.md. Keeps existing content below.
    """
    run_date = run_ts.astimezone(dt.timezone.utc).strftime("%Y-%m-%d")
    header = "# AI Security Radar Weekly Digest\n\n"
    existing = ""
    if os.path.exists(WEEKLY_MD):
        with open(WEEKLY_MD, "r", encoding="utf-8") as f:
            existing = f.read()

    body = existing
    if existing.startswith(header):
        body = existing[len(header):]
    else:
        body = re.sub(r"^\s*#\s+AI Security Radar Weekly Digest\s*\n+", "", existing, flags=re.IGNORECASE)

    top: List[str] = []
    top.append(f"## Radar Run — {run_date} (UTC)\n")

    if not entries:
        top.append("- No recent security-relevant arXiv matches in the selected window.\n")
    else:
        top.append("Top items:\n")
        for e in entries[:MAX_SHOW_WEEKLY]:
            title = e["title"]
            link = e["link"]
            pub = e.get("published", "")[:10]
            cat = e.get("category", "Other (Review)")
            top.append(f"- **{title}** ({pub}) [{cat}]  \n  {link}\n")

        top.append("Theme signal (manual):\n")
        top.append("- _Add 1–2 sentences after you skim the list. What pattern is emerging?_ \n")

        top.append("Build idea (manual):\n")
        top.append("- _What should exist that does not exist yet?_ (tool, harness, lab, checklist)\n")

    new_content = header + "\n".join(top).rstrip() + "\n\n---\n\n" + body.lstrip()
    return new_content


def _github_api_request(method: str, url: str, token: str, payload: dict | None = None) -> dict:
    data = None
    if payload is not None:
        import json
        data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-security-radar/1.1",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        if raw.strip():
            import json
            return json.loads(raw)
        return {}


def _issue_already_exists(repo: str, token: str, issue_title: str, arxiv_id: str) -> bool:
    """
    Returns True if an issue already exists (open or closed) for this radar item.

    We prefer searching by arXiv id in the issue body (most reliable),
    and fall back to title if arXiv id is missing.
    """
    # Use GitHub's search API (covers open + closed)
    # Docs: https://docs.github.com/en/rest/search/search
    base = "https://api.github.com/search/issues"

    def search(q: str) -> bool:
        url = f"{base}?q={urllib.parse.quote(q)}&per_page=5"
        data = _github_api_request("GET", url, token)
        return bool(data.get("total_count", 0))

    # Prefer body marker search (stable)
    if arxiv_id:
        q = f'repo:{repo} is:issue "arXiv: {arxiv_id}"'
        if search(q):
            return True

    # Fallback: title match
    q = f'repo:{repo} is:issue in:title "{issue_title}"'
    return search(q)


def _open_radar_issues(entries: List[Dict[str, Any]]) -> None:
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")  # e.g., owner/name
    if not token or not repo:
        return

    repo_api = f"https://api.github.com/repos/{repo}"

    def normalize_label(s: str) -> str:
        s = s.lower().strip()
        s = s.replace("&", "and")
        s = re.sub(r"[^a-z0-9\- ]+", "", s)
        s = s.replace(" ", "-")
        s = re.sub(r"-{2,}", "-", s)
        return s[:50] if s else "other"

    for e in entries[:OPEN_ISSUES_FOR_TOP_N]:
        title = (e.get("title") or "").strip()
        if not title:
            continue

        issue_title = f"Radar: {title}"
       
        cat = e.get("category", "Other (Review)")
        pub = (e.get("published") or "")[:10]
        link = e.get("link") or ""
        insight = textwrap.shorten(e.get("summary", ""), width=420, placeholder="…")
        build_idea = _build_idea_stub(cat)

        arxiv_id = ""
        if link:
            arxiv_id = link.rstrip("/").split("/")[-1]

        if _issue_already_exists(repo, token, issue_title, arxiv_id):
            continue
        
        body = (
            f"**Category:** {cat}\n\n"
            f"**Date:** {pub}\n\n"
            f"**Link:** {link}\n\n"
            f"**arXiv:** {arxiv_id}\n\n"
            f"**Security insight:** {insight}\n\n"
            f"**Build idea:** {build_idea}\n\n"
            f"**Writing angle:** What would you tell a CISO about this in 5 sentences?\n"
            "\n---\n\n"
            "## LinkedIn post draft (short)\n"
            "- Hook: The real risk isn’t the model, it’s the pipeline.\n"
            f"- Signal: {title}\n"
            f"- Why it matters: {insight}\n"
            f"- What to do: {build_idea}\n"
            "- Question: What are you doing to test this class of failure?\n"
            "\n"
            "## Medium outline (long)\n"
            "1. The problem in plain language\n"
            "2. What the paper shows (key idea)\n"
            "3. Threat model (attacker goal + access)\n"
            "4. Where defenses break in real systems\n"
            "5. Practical mitigations (engineering controls)\n"
            "6. What to test next (your harness idea)\n"
        )

        labels = list(ISSUE_LABELS)
        labels.append(normalize_label(cat))

        payload = {
            "title": issue_title,
            "body": body,
            "labels": labels,
        }
        _github_api_request("POST", f"{repo_api}/issues", token, payload)

def main() -> int:
    try:
        keywords = _read_keywords_from_simple_yaml(KEYWORDS_FILE)
        if not keywords:
            raise ValueError("No keywords found in sources/keywords.yml")

        query = _build_arxiv_search_query(keywords)

        atom = _fetch_with_retries(query, max_results=MAX_PULL, tries=3)
        entries = _parse_arxiv_entries(atom)
        entries = _filter_recent(entries, days=RECENT_DAYS)

        # Reduce noise: keep only security-related entries
        entries = [e for e in entries if _is_security_related(e)]

        # Categorize
        for e in entries:
            e["category"] = _categorize(e)

        # Sort by time desc
        entries.sort(
            key=lambda x: x.get("_ts", dt.datetime.min.replace(tzinfo=dt.timezone.utc)),
            reverse=True,
        )

        run_ts = _utc_now()

        latest_md = _format_latest_md(run_ts, keywords, entries)
        weekly_md = _prepend_weekly_digest(run_ts, entries)

        os.makedirs(os.path.dirname(LATEST_MD), exist_ok=True)
        with open(LATEST_MD, "w", encoding="utf-8") as f:
            f.write(latest_md)

        with open(WEEKLY_MD, "w", encoding="utf-8") as f:
            f.write(weekly_md)

        # Create GitHub issues for top radar items
        _open_radar_issues(entries)

        print(f"Updated {os.path.relpath(LATEST_MD, REPO_ROOT)} and {os.path.relpath(WEEKLY_MD, REPO_ROOT)}")
        return 0

    except Exception as ex:
        print(f"[ERROR] {ex}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1
        
if __name__ == "__main__":
    raise SystemExit(main())
