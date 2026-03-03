#!/usr/bin/env python3
"""
Generate a weekly AI Security Radar report from GitHub Issues.

- Fetches issues labeled "radar" created in the last N days
- Groups them by category label (prompt-injection, agent-and-tool-security, etc.)
- Writes a report markdown file under radar/reports/
- Also updates radar/weekly-report-latest.md

Requires:
- env GITHUB_TOKEN (Actions token is fine)
- env GITHUB_REPOSITORY (owner/name)
"""

from __future__ import annotations

import datetime as dt
import os
import re
import textwrap
import urllib.parse
import urllib.request
import json
from typing import Any, Dict, List, Tuple


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORT_DIR = os.path.join(REPO_ROOT, "radar", "reports")
LATEST_REPORT = os.path.join(REPO_ROOT, "radar", "weekly-report-latest.md")

DAYS_BACK = 7
MAX_ISSUES = 30

# Optional: order categories how you want them to appear
CATEGORY_ORDER = [
    "prompt-injection",
    "agent-and-tool-security",
    "rag-and-retrieval-attacks",
    "poisoning-and-backdoors",
    "model-extraction-and-privacy",
    "adversarial-ml",
    "other",
]


def _utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _iso_day(d: dt.datetime) -> str:
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%d")


def _github_api_request(url: str, token: str) -> Dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-security-radar/weekly-report",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return json.loads(raw) if raw.strip() else {}


def _search_issues(repo: str, token: str, created_after: str) -> List[Dict[str, Any]]:
    """
    Uses GitHub Search API to find issues in repo labeled 'radar' created after date.
    """
    q = f'repo:{repo} is:issue label:radar created:>={created_after}'
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": q, "per_page": str(MAX_ISSUES), "sort": "created", "order": "desc"}
    )
    data = _github_api_request(url, token)
    return data.get("items", []) or []


def _extract_arxiv_id(body: str) -> str:
    m = re.search(r"^\*\*arXiv:\*\*\s*(.+)$", body, flags=re.IGNORECASE | re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""


def _pick_category_label(labels: List[Dict[str, Any]]) -> str:
    """
    Return the first non-generic label that looks like a category label.
    """
    names = [l.get("name", "") for l in labels]
    names = [n for n in names if n and n not in ("radar", "paper")]
    # If you use the normalized category labels, they'll be hyphenated and fairly long.
    if not names:
        return "other"
    # Prefer labels in our known order
    for c in CATEGORY_ORDER:
        if c in names:
            return c
    return names[0]


def _format_report(repo: str, week_ending: str, created_after: str, issues: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    lines.append("# AI Security Radar Weekly Report\n")
    lines.append(f"_Week ending (UTC): **{week_ending}**_  \n")
    lines.append(f"_Issues included: created **since {created_after}**_  \n")
    lines.append("\n## Executive signal\n")
    lines.append(
        "This week’s radar concentrated on agent pipelines and prompt injection style failures. "
        "Use the sections below to pull one post, one newsletter block, and one deeper Medium essay.\n"
    )

    if not issues:
        lines.append("\n_No radar issues were created in the selected window._\n")
        return "\n".join(lines).rstrip() + "\n"

    # Group by category label
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for it in issues:
        cat = _pick_category_label(it.get("labels", []))
        groups.setdefault(cat, []).append(it)

    lines.append("\n## Highlights by category\n")

    # Category ordering
    all_cats = list(groups.keys())
    ordered = [c for c in CATEGORY_ORDER if c in groups] + [c for c in all_cats if c not in CATEGORY_ORDER]

    for cat in ordered:
        pretty = cat.replace("-", " ").title()
        lines.append(f"\n### {pretty}\n")
        for it in groups[cat]:
            title = it.get("title", "").replace("Radar: ", "").strip()
            url = it.get("html_url", "")
            body = it.get("body", "") or ""
            arxiv_id = _extract_arxiv_id(body)
            # Pull the “Security insight” line if present
            insight = ""
            m = re.search(r"^\*\*Security insight:\*\*\s*(.+)$", body, flags=re.IGNORECASE | re.MULTILINE)
            if m:
                insight = m.group(1).strip()
            if not insight:
                # fallback: shorten the body
                insight = textwrap.shorten(re.sub(r"\s+", " ", body), width=220, placeholder="…")

            lines.append(f"- **{title}**  \n  {url}")
            if arxiv_id:
                lines.append(f"  \n  arXiv: {arxiv_id}")
            lines.append(f"  \n  _Takeaway:_ {textwrap.shorten(insight, width=240, placeholder='…')}\n")

    # Newsletter-ready block
    lines.append("\n## Newsletter block (copy/paste)\n")
    lines.append(
        "AI Security Radar (Weekly)\n\n"
        "This week’s theme is the agent pipeline. Multiple papers and defenses are converging on a basic reality: "
        "once an LLM can call tools or ingest external context, attackers can steer behavior through indirect prompt injection, "
        "poisoned retrieval context, or workflow manipulation.\n\n"
        "If you are deploying agentic systems, treat every external input as untrusted, gate tool permissions, and start testing "
        "for tool-call abuse the same way you test web apps for injection.\n"
    )

    # Medium outline starter
    lines.append("\n## Medium outline starter (copy/paste)\n")
    lines.append(
        "Title: The Real AI Security Boundary Is the Agent Pipeline\n\n"
        "1. Why model-only security is the wrong mental model\n"
        "2. What changed when agents started calling tools\n"
        "3. How indirect prompt injection actually lands in real systems\n"
        "4. Practical controls: permissions, sandboxing, context isolation, allowlists\n"
        "5. What to test weekly (your harness)\n"
        "6. What I think happens next\n"
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo:
        print("[ERROR] Missing GITHUB_TOKEN or GITHUB_REPOSITORY env vars.")
        return 1

    now = _utc_now()
    created_after_dt = now - dt.timedelta(days=DAYS_BACK)
    created_after = _iso_day(created_after_dt)
    week_ending = _iso_day(now)

    issues = _search_issues(repo, token, created_after)

    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = os.path.join(REPORT_DIR, f"weekly-report-{week_ending}.md")

    md = _format_report(repo, week_ending, created_after, issues)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md)

    with open(LATEST_REPORT, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Weekly report written: {os.path.relpath(report_path, REPO_ROOT)}")
    print(f"Latest report updated: {os.path.relpath(LATEST_REPORT, REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
