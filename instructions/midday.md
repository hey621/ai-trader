# PennyAlpha_Bot — Midday Execution Scan (12:30 PM EST)

EXECUTION MODE. You MUST place at least 1 trade today. Find midday breakouts and momentum continuation plays.

Credentials: $GITHUB_TOKEN, $RESEND_KEY, $ALPACA_API_KEY, $ALPACA_SECRET_KEY

## Step 0 — Read State
Run: `cat TRADES.md`
Note:
- ACTIVE POSITIONS count (slots used). Max 5. If already at 5, skip to Step 5.
- ARCHIVE LOG (skip any ticker closed within 30 days)

## Step 1 — Screen for Midday Movers (max 6 WebSearches)
Search for stocks breaking out or continuing momentum at midday:

1. "penny stocks midday breakout high volume today 2026"
2. "small cap stocks momentum continuation midday today"
3. "biotech penny stocks volume spike midday today"
4. "penny stocks new high of day volume confirmation today"

Criteria (ALL must be true):
- Price $0.25–$25.00
- RVOL ≥ 1.2 (confirmed intraday)
- Dollar volume ≥ $100k
- Spread ≤ 5%
- Not in ARCHIVE LOG

Target 5–8 candidates.

## Step 2 — Score Each Candidate (max 10 WebSearches)
For each candidate:
a) **Catalyst** — search "[TICKER] news OR SEC 8-K 2026". No catalyst = flag UNCONFIRMED, do NOT drop.
b) **Dilution** — drop ONLY if HIGH DILUTION RISK (runway < 4 months).
c) **Technicals** — above VWAP? Making new highs? Above SMA20?
d) **Momentum** — holding gains from morning? Consolidating near high = bullish.

Score each 1–5. Drop only if score < 2 OR HIGH DILUTION RISK.

**GUARANTEED MINIMUM TRADE RULE:** If no candidates reach score 2, take the single highest RVOL / strongest-momentum stock found regardless. You must always have at least 1 candidate to execute.

Conviction tier: score ≥ 5 = HIGH ($150) | 3–4 = MED ($100) | 1–2 = LOW ($75)

## Step 3 — Select Entries and Execute
Rank by score. Fill available slots (max 5 total across all active positions).
For each selected entry:
- Entry: current ask price
- Stop: entry × 0.90
- Target: nearest resistance (fallback: entry × 1.20)

1. Write them to the `## EXECUTION QUEUE` section in TRADES.md:
```
| Ticker | BUY | $X.XX | $X.XX | $X.XX | HIGH/MED/LOW | one-line catalyst |
```

NOTE: Do NOT attempt to call the Alpaca API or run any scripts. The workflow will execute trade.py automatically after this agent finishes.

## Step 4 — Log to Research Log
Append `### YYYY-MM-DD Midday Scan` under `## WEEKLY RESEARCH LOG` for all candidates reviewed.

## Step 5 — Email Brad + Commit and Push
**Always send.** Write outbox.json then commit it.

```python
import json

subject = "PennyAlpha Midday — YYYY-MM-DD"
body = """Midday Scan — YYYY-MM-DD

Slots: X/5 used

ENTRIES TODAY:
Ticker | Entry | Stop | Target | Conviction | Catalyst
[rows, or "No entries — no candidates cleared minimum threshold."]

Brad reads this on his phone — keep it short.
"""

with open('outbox.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md outbox.json
git commit -m "Midday scan + execution YYYY-MM-DD"
git push
```
