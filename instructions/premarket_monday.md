# PennyAlpha_Bot — Daily Pre-Market Scan (9:00 AM EST)

Scan for stocks already moving before the open. Findings feed into the 10:15 AM morning execution scan.
Do NOT produce trading signals. Append to WEEKLY RESEARCH LOG only.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 1 — Pre-Market Screen
Use WebSearch to find pre-market movers. Run these searches:

1. Search: "pre-market gainers penny stocks today moving +5% site:finviz.com OR site:marketbeat.com OR site:benzinga.com"
2. Search: "biotech penny stocks pre-market movers today FDA catalyst"
3. Search: "penny stocks high pre-market volume movers today"

From results, extract tickers where ALL of the following appear true:
- Price $0.50–$5.00
- Pre-market move >= 5% (UP movers preferred; DOWN only with specific short thesis)
- Previous day dollar volume >= $500k
- Bid/ask spread <= 3%

Cross-reference with ARCHIVE LOG — skip any ticker closed within 30 days.
Target 4–6 candidates.

## Step 2 — Quick Catalyst Check (max 8 WebSearches)
For each surviving candidate (target 4–6), quickly verify:
a) What is driving the pre-market move? Find the news or catalyst.
b) Is there an SEC filing (8-K) confirming it? If not, flag UNCONFIRMED CATALYST — lower conviction.
c) Is there a PDUFA or FDA date today or this week?
d) Any dilution risk (recent S-1 or ATM offering)?

No need for full deep research — the afternoon/morning scans this week will do that. This is a quick pre-market priority flag only.

## Step 3 — Update WATCHLIST and Research Log
Write qualifying candidates to the `## WATCHLIST` section in TRADES.md so the 10:15 AM morning execution scan picks them up:

```
## WATCHLIST
_Updated: YYYY-MM-DD pre-market scan_

| Ticker | Close Price | Catalyst | Expected | Score | Flags |
|--------|------------|---------|---------|-------|-------|
| TICK | $X.XX | one line | pre-market today | X/5 | flags |
```

Pre-market movers with confirmed catalysts score +2 conviction in the morning execution scan.

Also append a `### YYYY-MM-DD Pre-Market` section under `## WEEKLY RESEARCH LOG` with the full table:

| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|

Do not modify ACTIVE POSITIONS.

## Step 4 — Send Email Summary
**Always send this email — even if zero candidates qualified.** Write the following to /tmp/send_email.py with the actual subject and body filled in, then run it with `python3 /tmp/send_email.py`:

```python
import json

subject = "PennyAlpha Pre-Market — YYYY-MM-DD"
body = """Pre-Market Summary — YYYY-MM-DD

Candidates screened: X | Passed filters: X

TICKER | PM Move% | Direction | Catalyst | SEC Confirmed
--------------------------------------------------------------
[one row per passing ticker, or "No qualifying candidates."]

Screened out: [brief note on any notable rejections]

Brad reads this on his phone — keep it short.
"""

with open('/tmp/email.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

Then send with curl:
```bash
curl -s -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer $RESEND_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/email.json
```

## Step 5 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: pre-market scan YYYY-MM-DD"
git push
```

