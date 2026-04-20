# PennyAlpha_Bot — Monday Pre-Market Scan (8:00 AM EST)

Scan for stocks already moving before the open. Findings feed into the Monday 8:45 AM aggregation.
Do NOT produce trading signals. Append to WEEKLY RESEARCH LOG only.

Credentials:
- GitHub token: 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
- Resend key: re_7HPmdVCU_3k58K1kqtmsZQbGowdZVukig

## Step 1 — Pre-Market Screen
```
python3 premarket.py
```

This returns JSON lines for stocks with: price $0.50–$5.00, pre-market move >= 5%, previous dollar volume >= $500k, spread <= 3%. Each line includes: ticker, prev_close, pm_price, pm_change_pct, direction (UP/DOWN), spread, rvol, sma20, above_sma20.

Focus on UP movers only unless a DOWN mover has a specific short thesis.
Cross-reference with ARCHIVE LOG — skip any ticker closed within 30 days.

## Step 2 — Quick Catalyst Check (max 8 WebSearches)
For each surviving candidate (target 4–6), quickly verify:
a) What is driving the pre-market move? Find the news or catalyst.
b) Is there an SEC filing (8-K) confirming it? If not, flag UNCONFIRMED CATALYST — lower conviction.
c) Is there a PDUFA or FDA date today or this week?
d) Any dilution risk (recent S-1 or ATM offering)?

No need for full deep research — the afternoon/morning scans this week will do that. This is a quick pre-market priority flag only.

## Step 3 — Append to WEEKLY RESEARCH LOG
Add a clearly labelled pre-market section at the top of this week's log:

### YYYY-MM-DD Pre-Market (Monday)
| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| TICK | $X.XX | $X.XX | +X.X% | UP | X.X% | Y/N | [one line] | Y/N |

Flag any ticker here with a star (*) next to its name in the Monday aggregation — pre-market movers with confirmed catalysts get +2 conviction bonus in Step 2 of monday.md.

Do not modify MONDAY SIGNALS or ACTIVE POSITIONS.

## Step 4 — Commit and Push
```
git config user.email bot@pennyalpha.local
git config user.name PennyAlpha_Bot
git remote set-url origin https://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@github.com/hey621/ai-trader.git
git add TRADES.md
git commit -m "Research: Monday pre-market scan YYYY-MM-DD"
git push
```
