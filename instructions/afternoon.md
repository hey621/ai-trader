# PennyAlpha_Bot — Afternoon Research Instructions (3:30 PM EST)

RESEARCH MODE ONLY. Do not produce trading signals. Append findings to TRADES.md.
Focus on stocks building momentum into close and next-day catalysts.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read State
Run: cat TRADES.md
Note tickers in ARCHIVE LOG closed within 30 days — skip these.
Note tickers already logged in today's Morning Scan — avoid duplicates unless conviction changed significantly (e.g. new SEC filing, RVOL spike).

## Step 1 — Polygon Screen
Run: python3 screen.py

If the output contains MARKET_CLOSED, send a brief email to hey@bradscanvas.com: subject "PennyAlpha — Market Closed [DATE]", body "No scan performed." Then stop.

Same filters as morning: price $0.50–$5.00, RVOL >= 2.0, dollar vol >= $500k, spread <= 3%, above 20-day SMA. Discard tech_score < 3.

Afternoon priority — weight toward tickers with:
- After-hours catalyst expected (earnings tonight, FDA tomorrow)
- Closing near the high of day (bullish close)
- RVOL still accelerating into close

Target 15–20 candidates. ~70% Biotech / ~20% AI-Infrastructure or Chips / ~10% Energy (uranium, lithium) or Defence/Space.

## Step 2 — Deep Research (max 25 WebSearches total)
For each surviving candidate:

a) SEC Validation — find recent 8-K, 10-Q, or S-1 confirming catalyst. Drop if none.

b) FDA/PDUFA Calendar — any FDA date within 60 days? Flag "TOMORROW CATALYST" if FDA date is the next trading day.

c) Dilution Check — cash runway from 10-Q. Flag "HIGH DILUTION RISK" if under 4 months.

d) Short Squeeze — short float %? Flag "SQUEEZE CANDIDATE" if above 20%.

e) Insider Activity — Form 4 buys in last 30 days? Y or N.

f) After-Hours Setup — any earnings release or news event expected tonight or pre-market tomorrow? Note it.

g) Earnings Date — next earnings report date. Flag "EARNINGS <7D" if within 7 days.

h) Analyst Activity — any upgrades, initiations, or price target changes in last 14 days? Y or N.

i) Additional SMAs — price above 9-day MA (momentum) and 200-day MA (trend)? Note Y/N for each.

j) VWAP — trading above today's VWAP? Y or N.

k) 52-Week High — calculate upside to 52-week high as secondary resistance target.

## Step 3 — Append to WEEKLY RESEARCH LOG
Only log tickers with tech_score >= 3. Append only — never overwrite existing entries.

### YYYY-MM-DD Afternoon Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | SMA9 | SMA20 | SMA200 | Above VWAP | Resistance | 52W High | Upside% | Flags | Catalyst (SEC) | FDA Date | Earnings | Analyst | Insider |
|--------|-------|------|-----------|--------|-----------|------|-------|--------|-----------|-----------|---------|---------|-------|----------------|----------|----------|---------|---------|

## Step 4 — Commit and Push
