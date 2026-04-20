# PennyAlpha_Bot — Daily Stop Loss Watch (12:00 PM EST)

Lightweight mid-day check. Only email Brad if something needs action.

Credentials:
- GitHub token: $GITHUB_TOKEN
- Resend key: $RESEND_KEY

## Step 1 — Run Position Check
```
python3 stopwatch.py
```

This reads ACTIVE POSITIONS from TRADES.md, fetches current prices from Polygon, and prints one of:
- NO_ACTIVE_POSITIONS — do nothing, exit.
- ALL_CLEAR: No stops or targets hit. — do nothing, exit.
- STOP LOSS HIT or TARGET HIT lines — these require action.

## Step 2 — If ALL_CLEAR or NO_ACTIVE_POSITIONS
Do nothing. Do not email. Do not commit. Exit.

## Step 3 — If Any STOP LOSS HIT or TARGET HIT Alerts
Update TRADES.md:
- Move the affected ticker from ACTIVE POSITIONS to CLOSED TRADES. Label WIN if target hit, LOSS if stop hit.
- Add ticker to ARCHIVE LOG with Eligible Again = today + 30 days.
- Update Total Deployed and Unrealised P&L in ACTIVE POSITIONS section.

Commit and push:
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Alert: stop/target triggered YYYY-MM-DD"
git push
```

Then email hey@bradscanvas.com via Resend API (Bearer $RESEND_KEY):
- From: onboarding@resend.dev
- Subject: ACTION NEEDED — PennyAlpha Alert [DATE]
- Body: List each alert line clearly. State whether it was a stop loss (LOSS) or target (WIN). End with: "Update your positions — next Monday signal will reflect this close."
