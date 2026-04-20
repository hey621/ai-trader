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

If the output contains MARKET_CLOSED, the market is not open. Send a brief email to hey@bradscanvas.com with subject "PennyAlpha — Market Closed [DATE]" and body "No scan performed — market is closed." Then stop. Do not proceed further.

This calls the Polygon API and outputs one JSON object per line for each stock passing:
- Price $0.50–$5.00
- RVOL >= 2.0
- Daily dollar volume >= $500k
- Bid/ask spread <= 3%
- Price above 20-day SMA

Each JSON line contains: ticker, price, rvol, dollar_vol, spread, sma20, above_sma20, resistance, upside_pct, tech_score.

Discard any ticker in the ARCHIVE LOG. Discard any ticker with tech_score < 3. Target 15–20 survivors. Aim for ~70% Biotech / ~20% AI-Infrastructure or Chips / ~10% Energy (uranium, lithium) or Defence/Space by sector. Use one WebSearch per ticker to confirm sector if unsure.

## Step 2 — Deep Research (max 25 WebSearches total)
For each surviving candidate, run all of these checks:

a) SEC Validation — find a recent 8-K, 10-Q, or S-1 confirming the news catalyst. Drop the ticker if none found.

b) FDA/PDUFA Calendar — search for any FDA decision date, Phase II/III readout, or PDUFA date within 60 days. Note the date or N/A.

c) Dilution Check — estimate cash runway from the most recent 10-Q. Flag "HIGH DILUTION RISK" if under 4 months of runway.

d) Short Squeeze Potential — find short float percentage. Flag "SQUEEZE CANDIDATE" if above 20%.

e) Insider Activity — search Form 4 filings for insider purchases in the last 30 days. Note Y or N.

f) Earnings Date — search for the next earnings report date. Flag "EARNINGS <7D" if within 7 days.

g) Analyst Activity — any upgrades, initiations, or price target changes in the last 14 days? Note Y or N.

h) Additional SMAs — note whether price is above the 9-day MA (momentum) and 200-day MA (long-term trend).

i) VWAP — is price trading above today's VWAP? Note Y or N.

j) 52-Week High — what is the 52-week high? Calculate upside to 52-week high as a secondary resistance target.

## Step 3 — Append to WEEKLY RESEARCH LOG
Only log tickers with tech_score >= 3. Append to TRADES.md under ## WEEKLY RESEARCH LOG. Never overwrite existing entries.

### YYYY-MM-DD Morning Scan
| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | SMA9 | SMA20 | SMA200 | Above VWAP | Resistance | 52W High | Upside% | Flags | Catalyst (SEC) | FDA Date | Earnings | Analyst | Insider |
|--------|-------|------|-----------|--------|-----------|------|-------|--------|-----------|-----------|---------|---------|-------|----------------|----------|----------|---------|---------|
| TICK | $X.XX | X.Xx | $XXXk | X.X% | X/5 | Y/N | $X.XX | Y/N | Y/N | $X.XX | $X.XX | X% | [flags] | [SEC ref] | [date/N/A] | [date/N/A] | Y/N | Y/N |

Do not modify MONDAY SIGNALS or ACTIVE POSITIONS sections.

## Step 4 — Commit and Push
