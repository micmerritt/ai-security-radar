#!/usr/bin/env python3
"""
Generate a weekly AI Security Radar report from GitHub Issues and email it.

- Fetches issues labeled "radar" created in the last N days
- Groups by category label
- Formats a markdown report
- Emails it via SMTP

Requires env vars:
- GITHUB_TOKEN
- GITHUB_REPOSITORY

Email/SMTP env vars (store these as GitHub Actions secrets):
- EMAIL_TO
- EMAIL_FROM
- SMTP_HOST
- SMTP_PORT (e.g., 587)
- SMTP_USER
- SMTP_PASS
- SMTP_TLS ("true" or "false")  # usually true for 587
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import smtplib
import ssl
import textwrap
import urllib.parse
import urllib.request
from email.message import EmailMessage
from typing import Any, Dict, List


DAYS_BACK = 7
MAX_ISSUES = 30

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
            "User-Agent": "ai-security-radar/weekly-report-email",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        return json.loads(raw) if raw.strip() else {}


def _search_issues(repo: str, token: str, created_after: str) -> List[Dict[str, Any]]:
    q = f'repo:{repo} is:issue label:radar created:>={created_after}'
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": q, "per_page": str(MAX_ISSUES), "sort": "created", "order": "desc"}
    )
    data = _github_api_request(url, token)
    return data.get("items", []) or []


def _extract_arxiv_id(body: str) -> str:
    m = re.search(r"^\*\*arXiv:\*\*\s*(.+)$", body, flags=re.IGNORECASE | re.MULTILINE)
    return m.group(1).strip() if m else ""


def _pick_category_label(labels: List[Dict[str, Any]]) -> str:
    names = [l.get("name", "") for l in labels]
    names = [n for n in names if n and n not in ("radar", "paper")]
    if not names:
        return "other"
    for c in CATEGORY_ORDER:
        if c in names:
            return c
    return names[0]


def _format_report(repo: str, week_ending: str, created_after: str, issues: List[Dict[str, Any]]) -> str:
    lines: List[str] = []
    lines.append("# AI Security Radar Weekly Report\n")
    lines.append(f"_Repo:_ `{repo}`  \n")
    lines.append(f"_Week ending (UTC):_ **{week_ending}**  \n")
    lines.append(f"_Issues included: created since_ **{created_after}**  \n")

    lines.append("\n## Executive signal\n")
    lines.append(
        "This week’s radar concentrated on agent pipelines and prompt injection style failures. "
        "Use the sections below to pull one post, one newsletter block, and one deeper Medium essay.\n"
    )

    if not issues:
        lines.append("\n_No radar issues were created in the selected window._\n")
        return "\n".join(lines).rstrip() + "\n"

    groups: Dict[str, List[Dict[str, Any]]] = {}
    for it in issues:
        cat = _pick_category_label(it.get("labels", []))
        groups.setdefault(cat, []).append(it)

    lines.append("\n## Highlights by category\n")

    all_cats = list(groups.keys())
    ordered = [c for c in CATEGORY_ORDER if c in groups] + [c for c in all_cats if c not in CATEGORY_ORDER]

    for cat in ordered:
        pretty = cat.replace("-", " ").title()
        lines.append(f"\n### {pretty}\n")
        for it in groups[cat]:
            title = (it.get("title", "") or "").replace("Radar: ", "").strip()
            url = it.get("html_url", "")
            body = it.get("body", "") or ""
            arxiv_id = _extract_arxiv_id(body)

            insight = ""
            m = re.search(r"^\*\*Security insight:\*\*\s*(.+)$", body, flags=re.IGNORECASE | re.MULTILINE)
            if m:
                insight = m.group(1).strip()
            if not insight:
                insight = textwrap.shorten(re.sub(r"\s+", " ", body), width=220, placeholder="…")

            lines.append(f"- **{title}**  \n  {url}")
            if arxiv_id:
                lines.append(f"  \n  arXiv: {arxiv_id}")
            lines.append(f"  \n  _Takeaway:_ {textwrap.shorten(insight, width=240, placeholder='…')}\n")

    lines.append("\n## Newsletter block (copy/paste)\n")
    lines.append(
        "AI Security Radar (Weekly)\n\n"
        "This week’s theme is the agent pipeline. Multiple papers and defenses are converging on a basic reality: "
        "once an LLM can call tools or ingest external context, attackers can steer behavior through indirect prompt injection, "
        "poisoned retrieval context, or workflow manipulation.\n\n"
        "If you are deploying agentic systems, treat every external input as untrusted, gate tool permissions, and start testing "
        "for tool-call abuse the same way you test web apps for injection.\n"
    )

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


def _send_email(subject: str, body_md: str) -> None:
    email_to = os.getenv("EMAIL_TO")
    email_from = os.getenv("EMAIL_FROM")
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    smtp_tls = (os.getenv("SMTP_TLS", "true").strip().lower() == "true")

    missing = [k for k in ["EMAIL_TO", "EMAIL_FROM", "SMTP_HOST", "SMTP_USER", "SMTP_PASS"] if not os.getenv(k)]
    if missing:
        raise ValueError(f"Missing email env vars: {', '.join(missing)}")

    msg = EmailMessage()
    msg["To"] = email_to
    msg["From"] = email_from
    msg["Subject"] = subject

    # Email clients vary; send both plain text and a simple HTML version.
    msg.set_content(body_md)

    # Minimal HTML wrapper (keeps formatting readable)
    html_body = "<pre style='font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; white-space: pre-wrap;'>" + (
        body_md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    ) + "</pre>"
    msg.add_alternative(html_body, subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
        if smtp_tls:
            server.starttls(context=context)
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


def main() -> int:
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo:
        print("[ERROR] Missing GITHUB_TOKEN or GITHUB_REPOSITORY env vars.")
        return 1

    now = _utc_now()
    created_after = _iso_day(now - dt.timedelta(days=DAYS_BACK))
    week_ending = _iso_day(now)

    issues = _search_issues(repo, token, created_after)
    report_md = _format_report(repo, week_ending, created_after, issues)

    subject = f"AI Security Radar Weekly Report (UTC week ending {week_ending})"
    _send_email(subject, report_md)

    print("Weekly report emailed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
