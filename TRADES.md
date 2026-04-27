# TRADES.md — PennyAlpha_Bot Workspace
_Last updated: 2026-04-27_

---

## EXECUTION QUEUE
_Populated by morning execution scan. Consumed and cleared by trade.py._

| Ticker | Signal | Entry | Stop | Target | Conviction | Catalyst |
|--------|--------|-------|------|--------|------------|---------|

---

## WATCHLIST
_Populated by afternoon/pre-market scans. Reviewed by next morning execution scan._

_No watchlist candidates._

---

## ACTIVE POSITIONS

| Ticker | Entry Price | Entry Date | Deployed | Shares | Current Price | $ P&L | % P&L | Stop | Target | Status |
|--------|-------------|------------|----------|--------|---------------|-------|-------|------|--------|--------|
| —      | —           | —          | —        | —      | —             | —     | —     | —    | —      | —      |

**Total Deployed:** $0 / $500
**Realised P&L:** $0.00
**Unrealised P&L:** $0.00

---

## WEEKLY RESEARCH LOG

_Candidates found during daily scans. Aggregated each Monday to produce signals._

### 2026-04-27 Morning Scan

| Ticker | Price | RVOL | Dollar Vol | Spread | Tech Score | Above SMA9 | Above SMA20 | Above SMA200 | Above VWAP | Resistance | 52W High | Upside% | Flags | Catalyst (SEC) | FDA Date | Earnings | Analyst | Insider |
|--------|-------|------|-----------|--------|-----------|-----------|------------|-------------|-----------|-----------|---------|---------|-------|----------------|----------|----------|---------|---------|
| BZAI | $2.25 | ~2.0x | ~$3.5M | ~1.5% | 3/5 | Y | Y | Y | Y | $3.20 | N/A | 42% | — | 8-K: NeoTensr $50M deal; Nokia AI deal expanded 4/17; AI Services platform Q2 launch; $130M FY guide | N/A | N/A | Y (Strong Buy, target $5.50) | Y (CEO holds 5.7M shares) |
| MDAI | $1.99 | ~2.5x | ~$2M | ~2% | 4/5 | Y | Y | N | Y | $2.50 | N/A | 26% | — | 8-K: BARDA $54.9M committed (non-dilutive); FDA De Novo 510(k) submitted (DeepView burn); new CEO 4/17, CFO eff. 5/4 | N/A | 2026-05-12 | Y (Strong Buy, avg target $5.47) | N (CCO resigned 2/1) |

**Screened out:** TNXP ($12.61 — above $5 ceiling); BBAI ($3.70 below 20-day SMA $4.00, RVOL ~0.68x — note 28.11% short float for future watch); BTAI (going concern warning, SMA20 < SMA60, HIGH DILUTION RISK); UROY (SMA20 < SMA60 bearish trend, short interest 11.13%); GCTS/CELZ (insufficient data within search budget).

---

## CLOSED TRADES

| Ticker | Entry | Exit | Result | Close Date | Eligible Again |
|--------|-------|------|--------|------------|----------------|
| —      | —     | —    | —      | —          | —              |

---

## ARCHIVE LOG
_Tickers archived here are ineligible for re-suggestion for 30 days from close date._
