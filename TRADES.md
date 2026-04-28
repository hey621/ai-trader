# TRADES.md — PennyAlpha_Bot Workspace
_Last updated: 2026-04-28_
_Last reviewed: 2026-04-27 (Weekly Review — Week of 2026-04-21)_

---

## EXECUTION QUEUE
_Populated by morning execution scan. Consumed and cleared by trade.py._

| Ticker | Signal | Entry | Stop | Target | Conviction | Catalyst |
|--------|--------|-------|------|--------|------------|---------|

---

## WATCHLIST
_Updated: 2026-04-28 afternoon scan_

| Ticker | Close Price | Catalyst | Expected | Score | Flags |
|--------|------------|---------|---------|-------|-------|
| MDAI | ~$1.87 (Apr 28 est.) | BARDA $54.9M committed (non-dilutive, part of $150M Project BioShield); FDA De Novo 510(k) submitted (DeepView burn AI); 2025 results positive | Earnings 2026-05-12; FDA De Novo decision pending | 4/5 | New CEO 4/17; CCO resigned 2/1; below SMA200; low RVOL today (~0.09x) |
| BZAI | ~$2.115 (Apr 27 close) | Indonesia AI inference MOU (Datacomm); NeoTensr $50M contract; Nokia AI deal expanded 4/17; Q1 rev $2.7M; $130M FY guide | Q2 AI platform launch; continued Asia/enterprise deal momentum | 3/5 | CEO holds 5.7M shares; analyst Strong Buy, target $5.50; vol 7.3M Apr 27 (~2x avg); -6% from $2.25 scan entry |

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

### 2026-04-27 Afternoon Scan

| Ticker | Price | RVOL | Dollar Vol | Above SMA20 | Catalyst | Dilution | Short Float | Score | Result |
|--------|-------|------|-----------|-------------|---------|---------|------------|-------|--------|
| ASTC | ~$3.31 | ~107x (2.63M vs avg 24.58K) | ~$8.7M | Y (est.; 52W low $1.92, recovered strongly) | DHS $1B airport screening initiative; 1st Detect TSA-approved mass-spec; ADX 50, Strong Buy 88% conf | $30M mixed shelf Jan 2026 (not yet drawn) | Unknown | 3/5 | **PASS** — added to watchlist |
| PDYN | $6.12 | N/A | N/A | N/A | Defense AI/drone; Northern Strike 26-2 participation; Northland Outperform initiation | None noted | N/A | — | **FAIL** — above $5.00 ceiling |
| SIDU | ~$3.20 | N/A | N/A | N/A | $58.5M registered direct offering priced $4.35 on 4/21 (dilution overhang) | HIGH — 13.45M new shares at $4.35 | N/A | — | **FAIL** — HIGH DILUTION RISK |
| EDIT | ~$2.91 | N/A | N/A | N/A | EDIT-401 preclinical (HoY data); IND filing mid-2026; earnings 2026-05-11 | None noted | N/A | 2/5 | **FAIL** — no confirmed near-term catalyst |
| CDXS | ~$2.28 | N/A | N/A | N/A | ECOsynthesis commercialisation; $38M Merck licence; Q1 2026 earnings 2026-05-07 | 18.71% share count increase YoY | Unknown | 2/5 | **FAIL** — no near-term catalyst; moderate dilution |

### 2026-04-28 Afternoon Scan

| Ticker | Price | RVOL | Dollar Vol | Above SMA20 | Catalyst | Dilution | Short Float | Score | Result |
|--------|-------|------|-----------|-------------|---------|---------|------------|-------|--------|
| MDAI | ~$1.87 | ~0.09x (low today) | ~$120K est. | Y (52W range $1.13–$3.21; holding above recent lows) | BARDA $54.9M non-dilutive; FDA De Novo pending; earnings 2026-05-12 approaching | None detected | Unknown | 4/5 | **PASS — carried forward; May 12 earnings catalyst building** |
| BZAI | ~$2.115 | ~2.0x (7.3M vol Apr 27, avg ~3.7M) | ~$7.7M Apr 27 | Y (above SMA9/20; 52W range $1.00–$6.76) | Indonesia Datacomm AI MOU; NeoTensr $50M contract; Nokia AI expanded; Q2 platform launch | None detected | Unknown | 3/5 | **PASS — carried forward; new Asia deal adds catalyst layer** |
| ASTC | ~$3.26–3.76 | Low (~57K intraday) | ~$200K est. | Y | DHS $1B initiative; TSA mass-spec | **HIGH — $32.5M bought deal offering confirmed active (increased from $30M shelf)** | Unknown | — | **FAIL — removed from watchlist; active dilutive offering confirmed** |
| SCNI | ~$0.74 | Very high (most active Apr 27) | Est. high | Unknown | — | HIGH — $2.61M private placement announced | Unknown | — | **FAIL — HIGH DILUTION RISK; private placement** |
| ATOM | ~$8.58 | High (38.93% gainer) | High | Y | Synopsys GaN collaboration; semiconductor tech breakout | HIGH — $25M registered direct offering | N/A | — | **FAIL — above $5.00 ceiling; active dilution offering** |
| REPL | ~$2.x (post-crash) | Very high (post-FDA rejection) | High | N | — | None noted | N/A | — | **FAIL — FDA rejected lead drug RP1 (melanoma BLA); stock down 62–64%** |
| UAMY | ~$10.27 | ~1.3x avg | ~$108M | N/A | Antimony critical minerals; tariff exposure | None noted | N/A | — | **FAIL — above $5.00 ceiling** |
| USEG | ~$1.00 | High (premarket mover) | Unknown | Unknown | Oil & gas small cap | HIGH — $8.8M stock offering at $1 | Unknown | — | **FAIL — HIGH DILUTION RISK; offering at current price** |
| KNSA | ~$43.61 | Normal | High | N/A | Q1 2026 earnings Apr 28 BMO | None noted | N/A | — | **FAIL — above $5.00 ceiling** |

---

## CLOSED TRADES

| Ticker | Entry | Exit | Result | Close Date | Eligible Again |
|--------|-------|------|--------|------------|----------------|
| —      | —     | —    | —      | —          | —              |

---

## ARCHIVE LOG
_Tickers archived here are ineligible for re-suggestion for 30 days from close date._

---

## RESEARCH ARCHIVE
_Research log entries older than 14 days from the current review date are moved here automatically._

_No archived entries yet._
