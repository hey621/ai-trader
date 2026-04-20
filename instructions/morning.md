# PennyAlpha_Bot — Morning Research Instructions (9:15 AM EST)

RESEARCH MODE ONLY. Do not produce trading signals. Append findings to TRADES.md.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read State
Run: cat TRADES.md
Note any tickers in ARCHIVE LOG closed within the last 30 days. Skip these in all steps.

## Step 1 — Polygon Screen
Run: python3 screen.py

This calls the Polygon API and outputs one JSON object per line for each stock passing:
- Price $0.50–$5.00
- RVOL >= 2.0
- Daily dollar volume >= $500k
- Bid/ask spread <= 3%
- Price above 20-day SMA

Each JSON line contains: ticker, price, rvol, dollar_vol, spread, sma20, above_sma20, resistance, upside_pct, tech_score.

Discard any ticker in the ARCHIVE LOG. Target 8–12 survivors. Aim for ~70% Biotech / ~30% AI-Infrastructure or Chips by sector (use one WebSearch to confirm sector if unsure).

## Step 2 — Deep Research (max 15 WebSearches total)
For each surviving candidate, run all of these checks:

a) SEC Validation — find a recent 8-K, 10-Q, or S-1 confirming the news catalyst. Drop the ticker if none found.

b) FDA/PDUFA Calendar — search for any FDA decision date, Phase II/III readout, or PDUFA date within 60 days. Note the date or N/A.

c) Dilution Check — estimate cash runway from the most recent 10-Q. Flag "HIGH DILUTION RISK" if under 4 months of runway.

d) Short Squeeze Potential — find short float percentage. Flag "SQUEEZE CANDIDATE" if above 20%.

e) Insider Activity — search Form 4 filings for insider purchases in the last 30 days. Note Y or N.

## Step 3 — Append to WEEKLY RESEARCH LOG
Append the following to TRADES.md under the ## WEEKLY RESEARCH LOG section. Never overwrite existing entries — only append.

### YYYY-MM-DD Morning Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | SMA20 | Resistance | Upside% | Flags | Catalyst (SEC) | FDA Date | Insider |
|--------|-------|------|-----------|--------|-----------|-------|-----------|---------|-------|----------------|----------|---------|
| TICK | $X.XX | X.Xx | $XXXk | X.X% | X/5 | $X.XX | $X.XX | X% | [flags] | [SEC ref] | [date/N/A] | Y/N |

Do not modify MONDAY SIGNALS or ACTIVE POSITIONS sections.

## Step 4 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: morning scan YYYY-MM-DD"
git push
```
