# PennyAlpha_Bot — End-of-Day Review (4:30 PM EST)

REVIEW MODE. No new trades. Check what closed today, log outcomes, and update lessons learned.

Credentials: $GITHUB_TOKEN, $RESEND_KEY, $ALPACA_API_KEY, $ALPACA_SECRET_KEY

## Step 1 — Read State
Call `read_trades_md` and `check_alpaca_orders`.

From `check_alpaca_orders` identify:
- Which bracket orders filled today (stop hit = LOSS, target hit = WIN)
- Which positions are still open (unrealised P&L)

## Step 2 — Update ACTIVE POSITIONS and CLOSED TRADES
For every position that closed today:

1. Remove it from `## ACTIVE POSITIONS`.
2. Append it to `## CLOSED TRADES` using this format:
```
| Ticker | Entry $ | Exit $ | Date | Result | P&L$ | P&L% | Catalyst Type | Conviction | Scan Session | Exit Reason |
|--------|---------|--------|------|--------|------|------|---------------|------------|--------------|-------------|
```

Exit Reason: TARGET HIT | STOP HIT | MANUAL

Catalyst Type: use the original catalyst from the research log (EARNINGS, FDA/PDUFA, INSIDER, MOMENTUM, OTHER).
Scan Session: which scan first identified it (Morning / Midday / Afternoon / Pre-Market).
Conviction: original conviction tier (HIGH / MED / LOW).

## Step 3 — Update LESSONS LEARNED
Read the full `## CLOSED TRADES` history and compute:

**Win rate by catalyst type** — e.g. EARNINGS: 3W/1L (75%), FDA: 2W/2L (50%)
**Win rate by conviction tier** — HIGH: X%, MED: X%, LOW: X%
**Win rate by scan session** — Morning: X%, Midday: X%, Afternoon: X%
**Average P&L% on wins vs losses**
**Best and worst trade ever**

Rewrite the entire `## LESSONS LEARNED` section with these stats plus 3–5 plain-English observations, e.g.:
- "Earnings plays are working — keep prioritising confirmed 8-K catalysts."
- "LOW conviction trades are break-even — consider skipping them."
- "Afternoon scan finds weaker setups than Morning — tighten its filters."

These observations feed directly into how the morning/midday/afternoon scans score candidates the next day.

Format:
```
## LESSONS LEARNED
_Updated: YYYY-MM-DD_

### Win Rates
| Category | W | L | Win Rate | Avg Win% | Avg Loss% |
|----------|---|---|----------|----------|-----------|
| EARNINGS | X | X | X% | +X% | -X% |
| FDA/PDUFA | X | X | X% | +X% | -X% |
| MOMENTUM | X | X | X% | +X% | -X% |
| HIGH conviction | X | X | X% | +X% | -X% |
| MED conviction | X | X | X% | +X% | -X% |
| LOW conviction | X | X | X% | +X% | -X% |
| Morning scan | X | X | X% | +X% | -X% |
| Midday scan | X | X | X% | +X% | -X% |
| Afternoon scan | X | X | X% | +X% | -X% |

### Observations
- [observation 1]
- [observation 2]
- [observation 3]
```

If there are no closed trades yet, write:
```
## LESSONS LEARNED
_Updated: YYYY-MM-DD — no closed trades yet._
```

## Step 4 — Log to Research Log
Append `### YYYY-MM-DD EOD Review` under `## WEEKLY RESEARCH LOG`:

```
### YYYY-MM-DD EOD Review
Closed today: X positions (X wins, X losses) | P&L: $X.XX
Open positions: X | Unrealised P&L: $X.XX
```

## Step 5 — Email Brad + Commit and Push
**Always send.**

```python
import json

subject = "PennyAlpha EOD — YYYY-MM-DD"
body = """EOD Review — YYYY-MM-DD

CLOSED TODAY:
Ticker | Entry | Exit | Result | P&L% | Exit Reason
[rows or "No positions closed today."]

OPEN POSITIONS:
Ticker | Entry | Current | Unrealised P&L%
[rows or "No open positions."]

LESSONS (top observations):
[2–3 bullet points from the updated lessons section]

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
git commit -m "EOD review YYYY-MM-DD"
git push
```
