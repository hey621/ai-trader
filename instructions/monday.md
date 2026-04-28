# PennyAlpha_Bot — Monday Weekly Review (9:45 AM EST)

REVIEW MODE only. Recap last week's performance. No trading decisions — the morning execution scan handles entries.

Credentials: $GITHUB_TOKEN, $RESEND_KEY

## Step 1 — Read State
Run: `cat TRADES.md`
Read CLOSED TRADES, ACTIVE POSITIONS, ARCHIVE LOG.

## Step 2 — Calculate Weekly P&L
Find all trades closed last week (Friday's close + any mid-week closes).
Calculate:
- Total trades: W wins / L losses
- Win rate: W/(W+L)%
- Total realised P&L: $X.XX
- Best trade: TICKER (+X%)
- Worst trade: TICKER (−X%)
- Current active positions: X (list tickers)
- Capital deployed: $X / $500

## Step 3 — Move Old Research to Archive
Move all `### YYYY-MM-DD` research log entries older than 14 days from `## WEEKLY RESEARCH LOG` into a `## RESEARCH ARCHIVE` section at the bottom of the file (create it if it doesn't exist). Keep the last 14 days of entries in place.

## Step 4 — Commit and Push
Only commit if TRADES.md changed (research archiving moved content).
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Weekly review + archive YYYY-MM-DD"
git push
```

## Step 5 — Email Weekly Summary
Write outbox.json then commit it — a GitHub Action will send the email automatically.

```python
import json

subject = "PennyAlpha Weekly Review — Week of YYYY-MM-DD"
body = """Weekly Review — Week of YYYY-MM-DD

LAST WEEK'S TRADES:
Ticker | Entry | Exit | Result | P&L%
[rows, or "No closed trades last week."]

Summary: X trades | X wins | X losses | Win rate X% | P&L $X.XX
Best: TICKER +X% | Worst: TICKER -X%

CURRENTLY ACTIVE: X positions ($X deployed / $500)
[list active tickers]
"""

with open('outbox.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

Add outbox.json to the commit in Step 4:
```
git add TRADES.md outbox.json
```
