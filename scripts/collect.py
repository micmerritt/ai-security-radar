#!/usr/bin/env python3
"""
AI Security Radar - v1 Collector

- Reads keywords from sources/keywords.yml
- Queries arXiv Atom API for recent matching papers
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
from typing import List, Dict, Any, Tuple


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KEYWORDS_FILE = os.path.join(REPO_ROOT, "sources", "keywords.yml")
LATEST_MD = os.path.join(REPO_ROOT, "radar", "latest.md")
WEEKLY_MD = os.path.join(REPO_ROOT, "radar", "weekly-digest.md")

ARXIV_ATOM_ENDPOINT = "https://export.arxiv.org/api/query"


def _utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _read_keywords_from_simple_yaml(path: str) -> List[str]:
    """
    Minimal YAML reader for this file shape:

    keywords:
      - prompt injection
      - rag poisoning
      - ...

    We intentionally avoid PyYAML dependency.
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
                    # Stop if the keywords list ends and another section begins
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
    Build an arXiv query string.
    We use a conservative OR query across title+abstract to keep results relevant.
    """
    # arXiv supports search in title (ti:) and abstract (abs:)
    # We'll OR keywords across both fields.
    clauses = []
    for kw in keywords:
        safe = kw.replace('"', "")
        # Wrap multiword phrases in quotes for better precision.
        if " " in safe:
            safe = f'"{safe}"'
        clauses.append(f"ti:{safe} OR abs:{safe}")

    # Group all clauses into a big OR
    return "(" + ") OR (".join(clauses) + ")"


def _fetch_arxiv_atom(search_query: str, max_results: int = 12, sort_by: str = "submittedDate") -> str:
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": sort_by,
        "sortOrder": "descending",
    }
    url = ARXIV_ATOM_ENDPOINT + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ai-security-radar/1.0 (GitHub Actions; contact: noreply)",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _parse_arxiv_entries(atom_xml: str) -> List[Dict[str, Any]]:
    """
    Parse arXiv Atom feed entries.
    """
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    root = ET.fromstring(atom_xml)

    entries: List[Dict[str, Any]] = []
    for e in root.findall("atom:entry", ns):
        title = (e.findtext("atom:title", default="", namespaces=ns) or "").strip()
        summary = (e.findtext("atom:summary", default="", namespaces=ns) or "").strip()
        published = (e.findtext("atom:published", default="", namespaces=ns) or "").strip()
        updated = (e.findtext("atom:updated", default="", namespaces=ns) or "").strip()

        # Prefer "id" as canonical URL; also try link rel=alternate
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

        # Clean up whitespace and HTML entities
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


def _filter_recent(entries: List[Dict[str, Any]], days: int = 10) -> List[Dict[str, Any]]:
    """
    Keep only entries published/updated within N days (UTC).
    """
    cutoff = _utc_now() - dt.timedelta(days=days)

    def parse_iso(s: str) -> dt.datetime | None:
        if not s:
            return None
        try:
            # arXiv uses ISO8601 like 2026-03-02T18:22:01Z
            if s.endswith("Z"):
                s = s[:-1] + "+00:00"
            return dt.datetime.fromisoformat(s).astimezone(dt.timezone.utc)
        except Exception:
            return None

    recent: List[Dict[str, Any]] = []
    for e in entries:
        t = parse_iso(e.get("published", "")) or parse_iso(e.get("updated", ""))
        if t and t >= cutoff:
            e["_ts"] = t
            recent.append(e)
    return recent


def _format_latest_md(run_ts: dt.datetime, keywords: List[str], entries: List[Dict[str, Any]]) -> str:
    run_date = run_ts.astimezone(dt.timezone.utc).strftime("%Y-%m-%d")
    kw_line = ", ".join(keywords[:12]) + ("…" if len(keywords) > 12 else "")

    lines = []
    lines.append("# AI Security Radar\n")
    lines.append(f"_Last updated (UTC): **{run_date}**_\n")
    lines.append("## What this is\n")
    lines.append(
        "A curated, continuously-updated view of emerging AI security research signals "
        "and the build ideas they suggest.\n"
    )
    lines.append("## Tracked keywords\n")
    lines.append(f"`{kw_line}`\n")

    lines.append("## New / recent research (arXiv)\n")
    if not entries:
        lines.append("_No recent matches in the selected window._\n")
    else:
        for e in entries[:10]:
            title = e["title"]
            link = e["link"]
            published = e.get("published", "")[:10]
            authors = e.get("authors", [])
            author_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
            summary = e.get("summary", "")
            # Keep summary short
            summary = textwrap.shorten(summary, width=260, placeholder="…")

            lines.append(f"### {title}\n")
            lines.append(f"- **Date:** {published}\n")
            lines.append(f"- **Authors:** {author_str if author_str else 'Unknown'}\n")
            lines.append(f"- **Link:** {link}\n")
            lines.append(f"- **Why it matters:** {summary}\n")

            # Light “build hook” prompt so you can expand later
            lines.append(
                "- **Build hook:** What would a minimal test harness / dataset / detection rule look like for this?\n"
            )
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

    # Ensure header exists once
    body = existing
    if existing.startswith(header):
        body = existing[len(header):]
    else:
        # Strip any stray top-level header to avoid duplication
        body = re.sub(r"^\s*#\s+AI Security Radar Weekly Digest\s*\n+", "", existing, flags=re.IGNORECASE)

    top = []
    top.append(f"## Radar Run — {run_date} (UTC)\n")
    if not entries:
        top.append("- No recent arXiv matches in the selected window.\n")
    else:
        top.append("Top items:\n")
        for e in entries[:5]:
            title = e["title"]
            link = e["link"]
            pub = e.get("published", "")[:10]
            top.append(f"- **{title}** ({pub})  \n  {link}\n")

        top.append("Theme signal (manual):\n")
        top.append("- _Add 1–2 sentences here after you skim the list._\n")

        top.append("Build idea (manual):\n")
        top.append("- _What should exist that does not exist yet?_ (tool, harness, lab, checklist)\n")

    new_content = header + "\n".join(top).rstrip() + "\n\n---\n\n" + body.lstrip()
    return new_content


def main() -> int:
    try:
        keywords = _read_keywords_from_simple_yaml(KEYWORDS_FILE)
        if not keywords:
            raise ValueError("No keywords found in sources/keywords.yml")

        query = _build_arxiv_search_query(keywords)

        atom = _fetch_arxiv_atom(query, max_results=25)
        entries = _parse_arxiv_entries(atom)
        entries = _filter_recent(entries, days=10)

        # Sort by timestamp if available
        entries.sort(key=lambda x: x.get("_ts", dt.datetime.min.replace(tzinfo=dt.timezone.utc)), reverse=True)

        run_ts = _utc_now()

        latest_md = _format_latest_md(run_ts, keywords, entries)
        weekly_md = _prepend_weekly_digest(run_ts, entries)

        os.makedirs(os.path.dirname(LATEST_MD), exist_ok=True)
        with open(LATEST_MD, "w", encoding="utf-8") as f:
            f.write(latest_md)

        with open(WEEKLY_MD, "w", encoding="utf-8") as f:
            f.write(weekly_md)

        print(f"Updated {os.path.relpath(LATEST_MD, REPO_ROOT)} and {os.path.relpath(WEEKLY_MD, REPO_ROOT)}")
        return 0

    except Exception as ex:
        print(f"[ERROR] {ex}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
