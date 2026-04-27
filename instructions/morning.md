# PennyAlpha_Bot — Morning Research Instructions (9:15 AM EST)

RESEARCH MODE ONLY. Do not produce trading signals. Append findings to TRADES.md.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read State
Read TRADES.md. Note any tickers in ARCHIVE LOG closed within the last 30 days — skip these throughout.

## Step 1 — Screen for Candidates (max 6 WebSearches)
Use WebSearch to find penny stock movers passing all filters. Run these searches:

1. Search: "penny stocks high relative volume today site:finviz.com OR site:barchart.com OR site:marketbeat.com"
2. Search: "biotech penny stocks FDA catalyst moving today RVOL"
3. Search: "AI chip penny stocks unusual volume today"
4. Search: "uranium lithium defence penny stocks moving today high volume"

From results, extract tickers where ALL of the following appear true:
- Price $0.50–$5.00
- Relative Volume (RVOL) > 2.0
- Daily dollar volume >= $500k
- Bid/ask spread <= 3%
- Price above 20-day moving average

Discard any ticker in the ARCHIVE LOG. Target 15–20 candidates.
Sector mix: ~70% Biotech / ~20% AI-Infrastructure or Chips / ~10% Energy (uranium, lithium) or Defence/Space.

Assign a preliminary Tech Score (0–5):
- Price above 20-day MA: +1
- Price above 50-day MA: +1
- RVOL > 3.0: +1
- At least 15% upside to nearest resistance: +1
- Higher lows pattern visible recently: +1

Discard any ticker with Tech Score < 3.

## Step 2 — Deep Research (max 19 WebSearches total, ~1-2 per ticker)
For each surviving candidate:

a) SEC Validation — search "[TICKER] SEC 8-K OR 10-Q OR S-1 2026". Drop if no recent filing confirms the catalyst.

b) FDA/PDUFA Calendar — search "[TICKER] FDA PDUFA date 2026". Flag "TOMORROW CATALYST" if date is next trading day. Note date or N/A.

c) Dilution Check — from 10-Q, estimate cash runway. Flag "HIGH DILUTION RISK" if under 4 months.

d) Short Squeeze — search "[TICKER] short interest float". Flag "SQUEEZE CANDIDATE" if short float > 20%.

e) Insider Activity — search "[TICKER] Form 4 insider buying 2026". Note Y or N.

f) Earnings Date — search "[TICKER] earnings date". Flag "EARNINGS <7D" if within 7 days.

g) Analyst Activity — any upgrades, initiations, or price target changes in last 14 days? Note Y or N.

h) Technical levels — note 9-day MA, 200-day MA, VWAP, 52-week high if available.

## Step 3 — Append to WEEKLY RESEARCH LOG
Only log tickers with Tech Score >= 3. Append under ## WEEKLY RESEARCH LOG. Never overwrite existing entries.

### YYYY-MM-DD Morning Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | Above SMA9 | Above SMA20 | Above SMA200 | Above VWAP | Resistance | 52W High | Upside% | Flags | Catalyst (SEC) | FDA Date | Earnings | Analyst | Insider |
|--------|-------|------|-----------|--------|-----------|-----------|------------|-------------|-----------|-----------|---------|---------|-------|----------------|----------|----------|---------|---------|
| TICK | $X.XX | X.Xx | $XXXk | X.X% | X/5 | Y/N | Y/N | Y/N | Y/N | $X.XX | $X.XX | X% | [flags] | [SEC ref] | [date/N/A] | [date/N/A] | Y/N | Y/N |

Do not modify MONDAY SIGNALS or ACTIVE POSITIONS sections.

## Step 4 — Send Email Summary
Write the following to /tmp/send_email.py with the actual subject and body filled in, then run it with `python3 /tmp/send_email.py`:

```python
import os, json, urllib.request

subject = "PennyAlpha Morning Scan — YYYY-MM-DD"
body = """Morning Scan Summary — YYYY-MM-DD

Candidates screened: X | Passed filters: X

Ticker | Company | Price | Tech Score | Flags | Catalyst
---------------------------------------------------------
[one row per qualifying ticker]

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
git commit -m "Research: morning scan YYYY-MM-DD"
git push
```

