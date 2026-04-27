# PennyAlpha_Bot — Afternoon Watch Scan (4:30 PM EST)

WATCH MODE. Find next-day setups. Populate WATCHLIST for tomorrow's morning execution scan.

Credentials: $GITHUB_TOKEN, $RESEND_KEY

## Step 0 — Read State
Run: `cat TRADES.md`
Note ACTIVE POSITIONS and ARCHIVE LOG (skip any ticker closed within 30 days).

## Step 1 — Screen for Next-Day Setups (max 6 WebSearches)
Search for stocks with catalysts expected tonight or tomorrow, or strong closes:

1. "biotech penny stocks FDA PDUFA catalyst tomorrow OR tonight 2026"
2. "penny stocks earnings after hours tonight small cap"
3. "penny stocks high volume close today momentum"
4. "AI chip energy defence penny stocks catalyst tomorrow premarket"

Criteria (ALL must be true):
- Price $0.50–$5.00
- Dollar volume ≥ $500k today
- Catalyst expected tonight/tomorrow OR strong close with RVOL ≥ 1.5 into close
- Not in ARCHIVE LOG

Target 5–8 candidates.

## Step 2 — Quick Validate (max 10 WebSearches)
For each candidate:
a) **Catalyst** — confirm with SEC 8-K or known FDA/earnings date. Drop if unconfirmed.
b) **Dilution** — drop if HIGH DILUTION RISK.
c) **Technical** — above SMA20? Closing near high of day?
d) **Short float** — note SQUEEZE CANDIDATE if > 20%.

Score each 1–5 (rough: 5 = strong confirmed catalyst + above MA + clean, 1 = weak).
Drop score < 3.

## Step 3 — Update WATCHLIST in TRADES.md
Replace the entire `## WATCHLIST` section with today's candidates:

```
## WATCHLIST
_Updated: YYYY-MM-DD afternoon scan_

| Ticker | Close Price | Catalyst | Expected | Score | Flags |
|--------|------------|---------|---------|-------|-------|
| TICK | $X.XX | one line | tonight/tomorrow | X/5 | flags |
```

If nothing qualifies write: `_No watchlist candidates — YYYY-MM-DD_`

## Step 4 — Log to Research Log
Append `### YYYY-MM-DD Afternoon Scan` under `## WEEKLY RESEARCH LOG` with the standard full table for all candidates reviewed (pass and fail).

## Step 5 — Commit and Push
Always commit even if watchlist is empty.
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://$GITHUB_TOKEN@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: afternoon scan YYYY-MM-DD"
git push
```

## Step 6 — Email Brad
**Always send.** Write /tmp/send_email.py and run it:

```python
import json

subject = "PennyAlpha Afternoon Watch — YYYY-MM-DD"
body = """Afternoon Watch — YYYY-MM-DD

WATCHLIST FOR TOMORROW:
Ticker | Close | Catalyst | Expected | Score
[rows, or "Nothing queued for tomorrow."]

These will be reviewed in tomorrow's 10:15 AM execution scan.

Brad reads this on his phone — keep it short.
"""

with open('/tmp/email.json', 'w') as f:
    json.dump({"from": "bot@mail.bradscanvas.com", "to": "hey@bradscanvas.com", "subject": subject, "text": body}, f)
```

Then send with curl:
```bash
curl -s -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer $RESEND_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/email.json
```
