# PennyAlpha_Bot — Afternoon Research Instructions (3:30 PM EST)

RESEARCH MODE ONLY. Do not produce trading signals. Append findings to TRADES.md.
Focus on stocks building momentum into close and next-day catalysts.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read State
Read TRADES.md. Note tickers in ARCHIVE LOG closed within 30 days — skip these.
Note tickers already logged in today's Morning Scan — avoid duplicates unless conviction changed significantly.

## Step 1 — Screen for Candidates (max 6 WebSearches)
Use WebSearch to find afternoon movers and next-day setups:

1. Search: "penny stocks high volume into close today site:finviz.com OR site:barchart.com"
2. Search: "biotech penny stocks FDA catalyst tomorrow PDUFA after hours"
3. Search: "AI chip energy defence penny stocks momentum close today"
4. Search: "penny stocks unusual volume afternoon movers today"

From results, extract tickers where ALL appear true:
- Price $0.50–$5.00
- RVOL > 2.0 heading into close
- Daily dollar volume >= $500k
- Bid/ask spread <= 3%
- Price above 20-day moving average

Discard any ticker in ARCHIVE LOG. Discard Tech Score < 3. Target 15–20 candidates.
Sector mix: ~70% Biotech / ~20% AI-Infrastructure or Chips / ~10% Energy or Defence/Space.

Afternoon priority — weight toward:
- Stocks with after-hours catalyst expected (earnings tonight, FDA tomorrow)
- Closing near high of day
- RVOL still accelerating into close

## Step 2 — Deep Research (max 19 WebSearches total)
For each surviving candidate:

a) SEC Validation — search "[TICKER] SEC 8-K OR 10-Q OR S-1 2026". Drop if none confirms catalyst.

b) FDA/PDUFA — search "[TICKER] FDA PDUFA date 2026". Flag "TOMORROW CATALYST" if next trading day.

c) Dilution Check — cash runway from 10-Q. Flag "HIGH DILUTION RISK" if under 4 months.

d) Short Squeeze — search "[TICKER] short interest float". Flag "SQUEEZE CANDIDATE" if > 20%.

e) Insider Activity — search "[TICKER] Form 4 insider buying 2026". Note Y or N.

f) After-Hours Setup — any earnings or news expected tonight/pre-market tomorrow? Note it.

g) Earnings Date — flag "EARNINGS <7D" if within 7 days.

h) Analyst Activity — upgrades or price target changes in last 14 days? Y or N.

i) Technical levels — note 9-day MA, 200-day MA, VWAP, 52-week high if available.

## Step 3 — Append to WEEKLY RESEARCH LOG
Only log tickers with Tech Score >= 3. Append only — never overwrite.

### YYYY-MM-DD Afternoon Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | Above SMA9 | Above SMA20 | Above SMA200 | Above VWAP | Resistance | 52W High | Upside% | Flags | Catalyst (SEC) | FDA Date | Earnings | Analyst | Insider |
|--------|-------|------|-----------|--------|-----------|-----------|------------|-------------|-----------|-----------|---------|---------|-------|----------------|----------|----------|---------|---------|

## Step 4 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: afternoon scan YYYY-MM-DD"
git push
```
