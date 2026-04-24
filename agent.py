#!/usr/bin/env python3
"""PennyAlpha agent — calls Anthropic API with Tavily web search."""
import os
import sys
import json
import time
import requests
from datetime import datetime

import anthropic

RESEND_KEY = os.environ.get("RESEND_KEY", "")
TAVILY_KEY = os.environ.get("TAVILY_API_KEY", "")


def tavily_search(query: str) -> str:
    r = requests.post(
        "https://api.tavily.com/search",
        json={"api_key": TAVILY_KEY, "query": query, "max_results": 3, "search_depth": "basic"},
        timeout=30,
    )
    r.raise_for_status()
    results = r.json().get("results", [])
    out = []
    for res in results:
        out.append(f"**{res['title']}**\n{res['url']}\n{res.get('content', '')[:300]}")
    return "\n\n".join(out) or "No results found."


def read_trades_md() -> str:
    with open("TRADES.md") as f:
        return f.read()


def write_trades_md(content: str) -> str:
    with open("TRADES.md", "w") as f:
        f.write(content)
    return "TRADES.md written."


def send_email(subject: str, body: str) -> str:
    if not RESEND_KEY:
        return "RESEND_KEY not set — email skipped."
    r = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {RESEND_KEY}"},
        json={
            "from": "onboarding@resend.dev",
            "to": "hey@bradscanvas.com",
            "subject": subject,
            "text": body,
        },
        timeout=30,
    )
    r.raise_for_status()
    return f"Email sent ({r.status_code})."


TOOLS = [
    {
        "name": "web_search",
        "description": (
            "Search the web for current stock info, SEC filings, FDA/PDUFA dates, "
            "prices, volume, pre-market movers, insider filings, analyst activity."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
    {
        "name": "read_trades_md",
        "description": "Read the current TRADES.md file.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "write_trades_md",
        "description": (
            "Overwrite TRADES.md with the complete new content. "
            "Call this once when you have finished all updates."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"content": {"type": "string", "description": "Full file content"}},
            "required": ["content"],
        },
    },
    {
        "name": "send_email",
        "description": "Send an email to hey@bradscanvas.com via Resend.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "body": {"type": "string"},
            },
            "required": ["subject", "body"],
        },
    },
]

TASK_FILES = {
    "morning": "instructions/morning.md",
    "afternoon": "instructions/afternoon.md",
    "monday_premarket": "instructions/premarket_monday.md",
    "monday": "instructions/monday.md",
}

ALREADY_RAN_MARKERS = {
    "morning": lambda d: f"### {d} Morning Scan",
    "afternoon": lambda d: f"### {d} Afternoon Scan",
    "monday_premarket": lambda d: f"### {d} Pre-Market (Monday)",
    "monday": lambda d: f"Week of {d}",
}


def already_ran_today(task: str, today: str) -> bool:
    try:
        return ALREADY_RAN_MARKERS[task](today) in read_trades_md()
    except Exception:
        return False


def run(task: str) -> None:
    with open(TASK_FILES[task]) as f:
        instruction = f.read()

    today = datetime.utcnow().strftime("%Y-%m-%d")

    if already_ran_today(task, today):
        print(f"Already ran {task} today ({today}) — skipping duplicate.", flush=True)
        return

    trades = read_trades_md()

    scan_label = {"morning": "Morning", "afternoon": "Afternoon"}.get(task)
    email_instruction = ""
    if scan_label:
        email_instruction = (
            f"\nAfter calling write_trades_md, send a summary email using send_email with:\n"
            f"  subject: PennyAlpha {scan_label} Scan — {today}\n"
            f"  body: A plain-text summary including:\n"
            f"    - Number of candidates screened and how many passed\n"
            f"    - A table of all tickers logged to the research log (Ticker | Price | Tech Score | Flags | Catalyst)\n"
            f"    - A brief note on any tickers screened out for notable reasons\n"
            f"  Keep it concise — Brad reads this on his phone."
        )

    system = (
        f"You are PennyAlpha_Bot. Today is {today} UTC.\n"
        "Use web_search for ALL internet lookups — including pre-market movers, prices, SEC filings, and FDA dates.\n"
        "Do NOT attempt to run Python scripts (premarket.py, screen.py, stopwatch.py) — use web_search instead.\n"
        "Do NOT run git commands — the CI workflow commits and pushes after you finish.\n"
        "Do NOT reference GITHUB_TOKEN or RESEND_KEY — use the send_email tool instead.\n"
        f"When you have finished all updates, call write_trades_md with the COMPLETE file content.{email_instruction}"
    )

    messages = [
        {
            "role": "user",
            "content": f"{instruction}\n\n---\nCurrent TRADES.md:\n```\n{trades}\n```",
        }
    ]

    client = anthropic.Anthropic()

    for _ in range(60):
        for attempt in range(4):
            try:
                resp = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=8096,
                    system=system,
                    tools=TOOLS,
                    messages=messages,
                )
                break
            except anthropic.RateLimitError:
                if attempt == 3:
                    raise
                wait = 60 * (attempt + 1)
                print(f"Rate limited — waiting {wait}s before retry {attempt + 2}/4", flush=True)
                time.sleep(wait)
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason == "end_turn":
            break

        tool_results = []
        for block in resp.content:
            if block.type != "tool_use":
                continue
            inp = block.input
            print(f"[tool] {block.name} | {str(inp)[:100]}", flush=True)
            try:
                if block.name == "web_search":
                    out = tavily_search(inp["query"])
                elif block.name == "read_trades_md":
                    out = read_trades_md()
                elif block.name == "write_trades_md":
                    out = write_trades_md(inp["content"])
                elif block.name == "send_email":
                    out = send_email(inp["subject"], inp["body"])
                else:
                    out = f"Unknown tool: {block.name}"
            except Exception as e:
                out = f"Error: {e}"
            tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": out})

        messages.append({"role": "user", "content": tool_results})

    print("Agent finished.", flush=True)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "morning"
    if task not in TASK_FILES:
        print(f"Unknown task: {task}. Choose from: {', '.join(TASK_FILES)}")
        sys.exit(1)
    run(task)
