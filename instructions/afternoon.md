# PennyAlpha_Bot — Afternoon Research Instructions (3:30 PM EST)

RESEARCH MODE ONLY. Do not produce trading signals. Append findings to TRADES.md.
Focus on stocks building momentum into close and next-day catalysts.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read State
Run: cat TRADES.md
Note tickers in ARCHIVE LOG closed within 30 days — skip these.
Note tickers already logged in today's Morning Scan — avoid duplicates unless conviction changed significantly.

## Step 1 — Polygon Screen
Run: python3 screen.py

Same filters as morning: price $0.50–$5.00, RVOL >= 2.0, dollar vol >= $500k, spread <= 3%, above 20-day SMA.

Afternoon priority — weight toward tickers with:
- After-hours catalyst expected (earnings tonight, FDA tomorrow)
- Closing near the high of day (bullish close)
- RVOL still accelerating into close

Target 8–12 candidates. ~70% Biotech / ~30% AI-Infrastructure or Chips.

## Step 2 — Deep Research (max 15 WebSearches total)
For each surviving candidate:

a) SEC Validation — find recent 8-K, 10-Q, or S-1 confirming catalyst. Drop if none.

b) FDA/PDUFA Calendar — any FDA date within 60 days? Flag "TOMORROW CATALYST" if FDA date is the next trading day.

c) Dilution Check — cash runway from 10-Q. Flag "HIGH DILUTION RISK" if under 4 months.

d) Short Squeeze — short float %? Flag "SQUEEZE CANDIDATE" if above 20%.

e) Insider Activity — Form 4 buys in last 30 days? Y or N.

f) After-Hours Setup — any earnings release or news event expected tonight or pre-market tomorrow? Note it.

## Step 3 — Append to WEEKLY RESEARCH LOG
Append only — never overwrite existing entries.

### YYYY-MM-DD Afternoon Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | SMA20 | Resistance | Upside% | Flags | Catalyst (SEC) | FDA Date | Insider |
|--------|-------|------|-----------|--------|-----------|-------|-----------|---------|-------|----------------|----------|---------|

## Step 4 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: afternoon scan YYYY-MM-DD"
git push
```
