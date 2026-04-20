# PennyAlpha_Bot — Monday Aggregation Instructions (8:45 AM EST)

SIGNAL MODE. Read the full week of research and produce final BUY / SELL / HOLD signals.
This is the only output Brad acts on. Email signals to hey@bradscanvas.com.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 0 — Read Full State
Run: cat TRADES.md
Read everything: MONDAY SIGNALS, ACTIVE POSITIONS, WEEKLY RESEARCH LOG, CLOSED TRADES, ARCHIVE LOG.

## Step 1 — Review Existing Positions (SELL or HOLD)
For each ticker in ACTIVE POSITIONS, use WebSearch or python3 screen.py to get the current price.
- SELL if: up >= 20% from entry, down >= 10% from entry (stop loss hit), or original catalyst is resolved/broken.
- HOLD if: thesis still intact, within stop loss, has not hit target yet.

Move SELL decisions to CLOSED TRADES with WIN (>= +20%) or LOSS (<= -10%) label.

## Step 2 — Score the Week's Research
Read all entries in WEEKLY RESEARCH LOG. For each unique ticker, calculate a conviction score:

Base score = Tech Score from screen.py (0–5)
+1 for each additional scan the ticker appeared in (beyond the first)
+2 if FDA/PDUFA date is within 14 days
+1 if insider buying confirmed (Y)
+1 if flagged SQUEEZE CANDIDATE
-2 if flagged HIGH DILUTION RISK
Disqualified if in ARCHIVE LOG within 30 days

Rank all candidates by conviction score, highest first.

## Step 3 — Select BUY Candidates
Budget: $500 total. Max 5 active positions at $100 each.
Count current HOLD positions. Fill remaining open slots with top-ranked candidates.

For each BUY candidate, run python3 screen.py and confirm:
- Price still $0.50–$5.00
- Spread still <= 3%
- Still above 20-day SMA

Drop any candidate that no longer passes. Use up to 5 WebSearches to verify SEC catalysts are still valid.

## Step 4 — Update TRADES.md
Rewrite the file completely, preserving all sections. Changes:

MONDAY SIGNALS — replace entirely with this week's signals:
| Ticker | Signal | Entry Target | Stop Loss | Conviction | Catalyst Summary |
|--------|--------|-------------|-----------|------------|-----------------|
| TICK | BUY | $X.XX | $X.XX | HIGH/MED/LOW | one sentence |
| TICK | HOLD | $X.XX (entry) | $X.XX | HIGH/MED/LOW | one sentence |
| TICK | SELL | — | — | — | reason for exit |

ACTIVE POSITIONS — update prices and P&L. Add new BUYs. Remove SELLs.

WEEKLY RESEARCH LOG — clear it entirely (new week starts fresh).

CLOSED TRADES — append any new SELLs with entry price, exit price, result, date.

ARCHIVE LOG — append any closed tickers with Eligible Again = today + 30 days.

## Step 5 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Monday signals YYYY-MM-DD"
git push
```

## Step 6 — Email Signals to Brad
Send a clean email to hey@bradscanvas.com containing only the MONDAY SIGNALS table plus a one-line P&L summary.

Use curl to call the Resend API:
- Endpoint: https://api.resend.com/emails
- Authorization: Bearer $RESEND_KEY
- From: onboarding@resend.dev
- To: hey@bradscanvas.com
- Subject: PennyAlpha Monday Signals — [DATE]
- Body: the MONDAY SIGNALS table as plain text, then: "Total deployed: $X / $500 | Unrealised P&L: $X.XX"
