# PennyAlpha_Bot — Morning Execution Scan (10:15 AM EST)

EXECUTION MODE. You MUST place at least 1 trade today. Screen, score, and place bracket orders.

Credentials: $GITHUB_TOKEN, $RESEND_KEY, $ALPACA_API_KEY, $ALPACA_SECRET_KEY

## Step 0 — Read State
Run: `cat TRADES.md`
Note:
- ACTIVE POSITIONS count (slots used). Max 5. If already at 5, skip to Step 6.
- WATCHLIST (candidates queued by yesterday's afternoon scan or today's pre-market scan)
- ARCHIVE LOG (skip any ticker closed within 30 days)

## Step 1 — Screen for Candidates (max 6 WebSearches)
Search for stocks moving RIGHT NOW with confirmed volume:

1. "penny stocks high relative volume today site:finviz.com OR site:barchart.com OR site:marketbeat.com"
2. "biotech penny stocks moving today high volume confirmed catalyst"
3. "AI chip penny stocks unusual volume today"
4. "penny stocks momentum movers high RVOL today"

Also include any tickers from the WATCHLIST section.

Extract tickers where ALL are true:
- Price $0.25–$25.00
- RVOL ≥ 1.2 (confirmed intraday)
- Dollar volume ≥ $100k
- Spread ≤ 5%
- Not in ARCHIVE LOG

Target 10–15 candidates.

## Step 2 — Score Each Candidate (max 15 WebSearches)
For each candidate:

a) **Catalyst** — search "[TICKER] news OR SEC 8-K 2026". No confirmed catalyst = flag UNCONFIRMED, do NOT drop.
b) **Dilution** — search "[TICKER] S-1 OR offering OR ATM 2026". Drop ONLY if HIGH DILUTION RISK (runway < 4 months).
c) **Technicals** — above SMA9, SMA20, SMA200? Above VWAP? Note resistance and 52W high.
d) **Short float** — search "[TICKER] short interest". Flag SQUEEZE CANDIDATE if > 20%.
e) **Insider** — search "[TICKER] Form 4 insider buying 2026". Note Y/N.
f) **FDA/PDUFA** — search "[TICKER] FDA PDUFA 2026". Flag if within 14 days.

**Tech Score (0–5):**
+1 above SMA20 | +1 above SMA50 | +1 RVOL > 3.0 | +1 upside to resistance ≥ 15% | +1 higher lows pattern

**Conviction Score:**
Base = Tech Score
+1 for each prior scan the ticker appeared in (check WATCHLIST and recent research log)
+2 if FDA/PDUFA within 14 days
+1 if insider buying confirmed
+1 if SQUEEZE CANDIDATE
-2 if HIGH DILUTION RISK
+1 if confirmed SEC catalyst

**Drop only if conviction score < 2 or HIGH DILUTION RISK.**

Conviction tier: score ≥ 5 = HIGH ($150) | 3–4 = MED ($100) | 1–2 = LOW ($75)

**GUARANTEED MINIMUM TRADE RULE:** If no candidates reach conviction score 2, take the single highest RVOL / strongest-momentum stock found regardless of score and assign conviction LOW. You must always have at least 1 candidate to execute.

## Step 3 — Select Entries
Rank by conviction score. Fill available slots (max 5 total across all active positions).
Sector cap: max 3 in any single sector (Biotech, AI/Chip, Energy/Defence).

For each selected entry set:
- Entry: current ask price
- Stop: entry × 0.90
- Target: nearest resistance from research (fallback: entry × 1.20)

## Step 4 — Execute
If candidates qualified:

1. Write them to the `## EXECUTION QUEUE` section in TRADES.md using this format:
```
| Ticker | BUY | $X.XX | $X.XX | $X.XX | HIGH/MED/LOW | one-line catalyst |
```

2. Run: `python3 trade.py`
   (Reads EXECUTION QUEUE, places bracket orders on Alpaca, clears the queue, updates ACTIVE POSITIONS)

3. Clear the `## WATCHLIST` section in TRADES.md after reviewing it (add a "Reviewed YYYY-MM-DD" line).

## Step 5 — Log to Research Log
Append `### YYYY-MM-DD Morning Scan` under `## WEEKLY RESEARCH LOG` for all candidates reviewed (pass and fail) using the standard table format. Always append — never overwrite.

## Step 6 — Email Brad + Commit and Push
**Always send — even if no entries today.** Write outbox.json then commit it — a GitHub Action will send the email automatically.

```python
import json

subject = "PennyAlpha Morning — YYYY-MM-DD"
body = """Morning Scan — YYYY-MM-DD

Slots: X/5 used

ENTRIES TODAY:
Ticker | Entry | Stop | Target | Conviction | Catalyst
[rows, or "No entries today — no candidates cleared the threshold."]

ACTIVE POSITIONS:
[one line per position: Ticker | Entry | Current | P&L%]

Brad reads this on his phone — keep it short.
"""

with open('outbox.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

Always append at minimum a one-line `### YYYY-MM-DD Morning Scan` header (even if no candidates qualified) so there is always something to commit.
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md outbox.json
git commit -m "Morning scan + execution YYYY-MM-DD"
git push
```
