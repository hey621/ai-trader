# PennyAlpha_Bot — Afternoon Execution Scan (2:30 PM EST)

EXECUTION MODE. You MUST place at least 1 trade today. Screen afternoon runners and place bracket orders. Also populate WATCHLIST for tomorrow.

Credentials: $GITHUB_TOKEN, $RESEND_KEY, $ALPACA_API_KEY, $ALPACA_SECRET_KEY

## Step 0 — Read State
Run: `cat TRADES.md`
Note:
- ACTIVE POSITIONS count (slots used). Max 5. If already at 5, skip to Step 6.
- ARCHIVE LOG (skip any ticker closed within 30 days)

## Step 1 — Screen for Afternoon Runners (max 6 WebSearches)
Search for stocks still moving with momentum into the afternoon session:

1. "penny stocks high volume afternoon momentum today 2026"
2. "biotech penny stocks running afternoon session today"
3. "small cap stocks breakout afternoon session today high RVOL"
4. "penny stocks FDA PDUFA catalyst today OR tomorrow 2026"

Criteria (ALL must be true):
- Price $0.25–$25.00
- RVOL ≥ 1.2 (confirmed)
- Dollar volume ≥ $100k
- Spread ≤ 5%
- Not in ARCHIVE LOG

Target 5–8 candidates.

## Step 2 — Score Each Candidate (max 10 WebSearches)
For each candidate:
a) **Catalyst** — search "[TICKER] news OR SEC 8-K 2026". No catalyst = flag UNCONFIRMED, do NOT drop.
b) **Dilution** — drop ONLY if HIGH DILUTION RISK (runway < 4 months).
c) **Technical** — above SMA20? Near high of day? Above VWAP?
d) **Short float** — note SQUEEZE CANDIDATE if > 20%.

Score each 1–5. Drop only if score < 2 OR HIGH DILUTION RISK.

**GUARANTEED MINIMUM TRADE RULE:** If no candidates reach score 2, take the single highest RVOL stock regardless. You must always have at least 1 candidate to execute.

Conviction tier: score ≥ 5 = HIGH ($150) | 3–4 = MED ($100) | 1–2 = LOW ($75)

## Step 3 — Select Entries and Execute
Rank by score. Fill available slots (max 5 total across all active positions).
For each selected entry set:
- Entry: current ask price
- Stop: entry × 0.90
- Target: nearest resistance (fallback: entry × 1.20)

1. Write them to the `## EXECUTION QUEUE` section in TRADES.md:
```
| Ticker | BUY | $X.XX | $X.XX | $X.XX | HIGH/MED/LOW | one-line catalyst |
```

NOTE: Do NOT attempt to call the Alpaca API or run any scripts. The workflow will execute trade.py automatically after this agent finishes.

3. Update the `## WATCHLIST` section with any promising tickers NOT yet entered, for tomorrow:
```
## WATCHLIST
_Updated: YYYY-MM-DD afternoon scan_

| Ticker | Close Price | Catalyst | Expected | Score | Flags |
|--------|------------|---------|---------|-------|-------|
```

## Step 4 — Log to Research Log
Append `### YYYY-MM-DD Afternoon Scan` under `## WEEKLY RESEARCH LOG` for all candidates reviewed.

## Step 5 — Email Brad + Commit and Push
**Always send.** Write outbox.json then commit it.

```python
import json

subject = "PennyAlpha Afternoon — YYYY-MM-DD"
body = """Afternoon Scan — YYYY-MM-DD

Slots: X/5 used

ENTRIES TODAY:
Ticker | Entry | Stop | Target | Conviction | Catalyst
[rows, or "No entries — no candidates cleared minimum threshold."]

WATCHLIST FOR TOMORROW:
Ticker | Close | Catalyst | Score
[rows, or "Nothing queued."]

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
git commit -m "Afternoon scan + execution YYYY-MM-DD"
git push
```
