# PennyAlpha_Bot — Monday Pre-Market Scan (8:00 AM EST)

Scan for stocks already moving before the open. Findings feed into the Monday 8:45 AM aggregation.
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

## Step 3 — Append to WEEKLY RESEARCH LOG
Add a clearly labelled pre-market section at the top of this week's log:

### YYYY-MM-DD Pre-Market (Monday)
| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| TICK | $X.XX | $X.XX | +X.X% | UP | X.X% | Y/N | [one line] | Y/N |

Flag any ticker here with a star (*) next to its name in the Monday aggregation — pre-market movers with confirmed catalysts get +2 conviction bonus in Step 2 of monday.md.

Do not modify MONDAY SIGNALS or ACTIVE POSITIONS.

## Step 4 — Send Email Summary
**Always send this email — even if zero candidates qualified.** Write the following to /tmp/send_email.py with the actual subject and body filled in, then run it with `python3 /tmp/send_email.py`:

```python
import os, json, urllib.request

subject = "PennyAlpha Pre-Market Monday — YYYY-MM-DD"
body = """Pre-Market Monday Summary — YYYY-MM-DD

Candidates screened: X | Passed filters: X

TICKER | PM Move% | Direction | Catalyst | SEC Confirmed
--------------------------------------------------------------
[one row per passing ticker]

Screened out: [brief note on any notable rejections]

Brad reads this on his phone — keep it short.
"""

payload = json.dumps({
    "from": "onboarding@resend.dev",
    "to": "hey@bradscanvas.com",
    "subject": subject,
    "text": body,
}).encode()
req = urllib.request.Request(
    "https://api.resend.com/emails",
    data=payload,
    headers={"Authorization": f"Bearer {os.environ['RESEND_KEY']}", "Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(r.status, r.read().decode())
```

## Step 5 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: Monday pre-market scan YYYY-MM-DD"
git push
```

