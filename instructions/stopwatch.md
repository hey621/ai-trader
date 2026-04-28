# PennyAlpha_Bot — Daily Stop Loss Watch (12:00 PM EST)

Mid-day automated position management. Trail stops, close positions, email Brad if action was taken.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY
- Alpaca key: $ALPACA_API_KEY
- Alpaca secret: $ALPACA_SECRET_KEY

## Step 1 — Trail Stops
Run: `python3 stopwatch.py`

This checks current prices against each active position and:
- Trails the stop on Alpaca to breakeven if the position is up ≥10%
- Trails the stop to +10% if the position is up ≥20%
- Updates TRADES.md with new stop prices
- Prints NO_ACTIVE_POSITIONS, ALL_CLEAR, or position status lines

If output is NO_ACTIVE_POSITIONS — skip all remaining steps. Exit.

## Step 2 — Close Positions
Run: `python3 close.py`

This closes any position where stop or target has been hit (including positions already closed by Alpaca bracket orders). Updates TRADES.md automatically.

Output will be either:
- `ALL_CLEAR: No positions closed.` — no further action needed except commit if stopwatch trailed any stops
- One or more closed position lines — requires commit and email

## Step 3 — Email (only if positions closed) + Commit and Push
If close.py closed one or more positions, write outbox.json — a GitHub Action will send the email automatically:

```python
import json

subject = "ACTION — PennyAlpha Position Closed YYYY-MM-DD"
body = """Position Update — YYYY-MM-DD

CLOSED:
Ticker | Entry | Exit | Result | P&L%
[one row per closed position]

Next morning scan will reflect these closes.
"""

with open('outbox.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

If either script modified TRADES.md (stops trailed or positions closed), commit and push:
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md outbox.json
git commit -m "Alert: position update YYYY-MM-DD"
git push
```

If neither script changed anything, skip this step. If only stops were trailed (no closes), omit outbox.json from the commit.
