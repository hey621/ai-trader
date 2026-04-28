# PennyAlpha_Bot — Friday Position Close (3:30 PM EST)

Force-close ALL open positions before the weekend. Penny stocks must not hold over weekends.

Credentials: $GITHUB_TOKEN, $RESEND_KEY, $ALPACA_API_KEY, $ALPACA_SECRET_KEY

## Step 1 — Check Active Positions
Run: `cat TRADES.md`
Check ACTIVE POSITIONS. If the placeholder row `| — |` is the only entry, there are no open positions — skip to Step 4 (send "no positions to close" email).

## Step 2 — Close All on Alpaca
Run `python3 close.py` first to sync any positions already closed by bracket orders.

Then force-close everything remaining:
```python
import os
from alpaca.trading.client import TradingClient
trading = TradingClient(os.environ['ALPACA_API_KEY'], os.environ['ALPACA_SECRET_KEY'], paper=True)
result = trading.close_all_positions(cancel_orders=True)
print(f"Closed {len(result)} position(s).")
```

## Step 3 — Update TRADES.md
For each ticker still in ACTIVE POSITIONS after close.py:
- Search "[TICKER] stock price today" to get the exit price
- Calculate result: WIN if exit > entry, LOSS if exit < entry
- Move to CLOSED TRADES
- Add to ARCHIVE LOG with Eligible Again = today + 30 days
- Clear ACTIVE POSITIONS to placeholder row

## Step 4 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Friday close: all positions closed YYYY-MM-DD"
git push
```

## Step 5 — Email Brad
Write outbox.json then commit it — a GitHub Action will send the email automatically.

```python
import json

subject = "PennyAlpha Friday Close — YYYY-MM-DD"
body = """Friday Close — YYYY-MM-DD

POSITIONS CLOSED:
Ticker | Entry | Exit | Result | P&L%
[rows, or "No open positions."]

Weekly P&L: $X.XX
Total trades this week: X (X wins, X losses)

All positions flat for the weekend.
"""

with open('outbox.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

Add outbox.json to the commit in Step 4:
```
git add TRADES.md outbox.json
```
