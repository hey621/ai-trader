# TRADES.md — PennyAlpha_Bot Workspace
_Last updated: 2026-04-28 (morning scan)_
_Last reviewed: 2026-04-27 (Weekly Review — Week of 2026-04-21)_

---

## EXECUTION QUEUE
_Populated by morning execution scan. Consumed and cleared by trade.py._

| Ticker | Signal | Entry | Stop | Target | Conviction | Catalyst |
|--------|--------|-------|------|--------|------------|---------|

---

## WATCHLIST
_Updated: 2026-04-28 pre-market scan_
_Reviewed 2026-04-28 morning scan — MDAI RVOL ~0.09x (fail), BZAI RVOL ~0.65x (fail); both dropped. Watchlist cleared._

| Ticker | Close Price | Catalyst | Expected | Score | Flags |
|--------|------------|---------|---------|-------|-------|

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

### 2026-04-28 Pre-Market

_Macro context: Nasdaq 100 -1.2% pre-market; S&P 500 -0.6%; Russell 2000 -0.8% — broad risk-off open. Confirmed upward pre-market movers (BBBY +23.9%, OMCL +21%, LendingClub +10%) all priced above $5 ceiling. No penny-range ($0.50–$5.00) stocks confirmed ≥5% UP pre-market. Zero new candidates added to watchlist. Existing MDAI and BZAI remain active._

| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| BBBY | ~$4.33 est. | ~$5.36 | +23.9% | UP | Low est. | Unknown | Q1 FY2026 earnings beat; first revenue growth in 19 quarters; $60M cost reduction plan | 8-K pending | **FAIL: PM price above $5 ceiling** |
| GLND | ~$7.00 est. | ~$6.90 | ~-1.2% | DOWN | Unknown | Unknown | $70M public offering priced at $4.00; Halliburton drilling deal | 8-K: offering filed | **FAIL: above $5; active dilutive offering** |
| HYMC | ~$38.0 est. | ~$37.60 | ~-1.2% | DOWN | Unknown | Unknown | Q1 10-Q: $189M cash, no debt; 55% resource increase (gold/silver) | 10-Q filed Apr 28 | **FAIL: above $5 ceiling** |
| ERAS | ~$19.0 est. | ~$11.49 | ~-40% | DOWN | Unknown | Unknown | REVOLUTION Phase 1: treatment-related death (24mg dose, Grade 3 pneumonitis) | Data disclosed | **FAIL: above $5; severe DOWN mover** |
| VISN | ~$19.6 est. | ~$10.01 | ~-49.7% | DOWN | Unknown | Unknown | $10/share cash dividend ex-date Apr 28 (mechanical DROP) | Dividend 8-K | **FAIL: above $5; ex-dividend DROP** |
| CMPX | $1.79 | ~$1.95 est. | ~+9% est. | UP (technical bounce) | Unknown | N (post-crash) | COMPANION-002 death (Apr 27); Jefferies Buy $9 PT "overreaction"; $230M+ liquidity; Apr 28 confirmed range $1.82–$2.18 | Trial data 8-K filed | **FAIL: catalyst negative (treatment death); bounce speculative/technical only; no confirmed positive catalyst** |
| BBAI | ~$3.64 | ~$3.46 | ~-5% | DOWN | Unknown | N (36% YTD loss) | Authorized share doubling approved Apr 22; Q1 earnings May 5; $900M contract opportunity unresolved | 8-K: share authorization | **FAIL: DOWN mover; no confirmed PM catalyst** |
| DVLT | ~$0.72 | ~$0.73 | ~+1% | FLAT | Unknown | Unknown | Dream Bowl 2026 meme coin airdrop to holders | Unconfirmed | **FAIL: <5% PM move; speculative/unconfirmed catalyst** |
| ATAI | ~$4.93 est. | ~$4.85 | ~-1.7% | DOWN | Unknown | Unknown | White House psychedelics EO (prior catalyst); no new catalyst today | No | **FAIL: DOWN mover; no new catalyst** |
| ABCL | ~$3.66 | ~$3.76 | ~+2.7% | UP | Unknown | Unknown | Q1 2026 earnings due 2026-05-11; ABCL635 Phase II readout Q3 2026 | No | **FAIL: <5% PM move; no same-day catalyst** |
| SLNH | Unknown | ~$1.42 | Unknown | Unknown | Unknown | Unknown | Insufficient data — no confirmed catalyst found | No | **FAIL: insufficient data** |
| LWLG | ~$13.97 | ~$13.97 | Unknown | Unknown | Unknown | Unknown | — | Unknown | **FAIL: above $5 ceiling** |
| SYRE | ~$64.80 | ~$64.80 | Unknown | Unknown | Unknown | Unknown | — | Unknown | **FAIL: above $5 ceiling** |
| SGMT | ~$5.89 (Apr 27 PM open) | ~$8.00 est. | ~+35% est. | UP | Unknown | Unknown | $175M Series A offering at $6/share (closing Apr 28); Phase 3 denifanstat acne (positive China Phase 3 data) | S-1/prospectus filed | **FAIL: above $5 ceiling (offering $6, trading ~$7–9)** |
| ORKA | ~$70 est. | ~$93 est. | ~+33% (Apr 28 PM) | UP | Unknown | Unknown | Phase 2a EVERLAST-A: 63.5% PASI 100 at Week 16; once-yearly dosing; Guggenheim PT $200, BTIG PT $151 | Data disclosed (Apr 27) | **FAIL: way above $5 ceiling (~$90+)** |
| MANE | ~$67.84 (Apr 24 close) | ~$81 est. (Apr 28 open) | ~+19% PM Apr 28 | UP | Unknown | Unknown | Phase 2/3 VDPHL01 oral minoxidil positive pivotal hair loss results; secondary public offering launched Apr 27 | 8-K: data + offering filed | **FAIL: way above $5 ceiling (~$80–$100); active dilutive offering** |

**Screened out summary (16 tickers screened, 0 passed):** All confirmed UP movers (BBBY +23.9%, SGMT ~+35%, ORKA ~+33% PM, MANE ~+19% PM, ABCL +2.7%) either above $5 ceiling or below 5% threshold. CMPX ($1.79 → range $1.82–$2.18; ~+9% technical bounce) in penny range but catalyst negative (treatment death); no confirmed positive catalyst. Apr 28 macro: tech risk-off (OpenAI missed targets; Oracle -7.5%, Nvidia -2–5%); S&P -0.17%, Nasdaq -0.55%. No PDUFA on Apr 28. Apr 27 record closes (Intel/TXN beats) already priced in.

### 2026-04-28 Morning Scan

| Ticker | Price | RVOL | Dollar Vol | Spread | Above SMA20 | Catalyst (SEC) | Dilution | Short Float | Tech Score | Conviction | Result |
|--------|-------|------|-----------|--------|-------------|----------------|---------|------------|-----------|-----------|--------|
| BZAI | ~$2.19 | ~0.65x (10.44M vs avg 15.95M) | ~$22.9M | ~1.5% est. | Y | 8-K: NeoTensr $50M; Nokia AI expanded; Indonesia MOU | None detected | Unknown | — | — | **FAIL — RVOL 0.65x < 2.0 threshold** |
| MDAI | ~$1.87 | ~0.09x | ~$120K est. | ~2% est. | Y | 8-K: BARDA $54.9M; FDA De Novo pending | None detected | Unknown | — | — | **FAIL — RVOL 0.09x < 2.0 threshold** |
| PACB | ~$1.42 | Unconfirmed | Unconfirmed | Unknown | Unknown | Trillion Gene Atlas deal (Anthropic/NVIDIA partnership, Mar 2026); earnings May 7, 2026 | None noted | Unknown | — | — | **FAIL — RVOL unconfirmed; discarded per rules** |
| CELZ | ~$1.90 | Unconfirmed | Unconfirmed | Unknown | Unknown | Unknown | Unknown | Unknown | — | — | **FAIL — RVOL unconfirmed; discarded per rules** |
| GCTS | ~$1.18 | Unconfirmed | Unconfirmed | Unknown | Unknown | Unknown | Unknown | Unknown | — | — | **FAIL — RVOL unconfirmed; discarded per rules** |

**Screened out summary (5 tickers screened, 0 passed):** Both watchlist names (BZAI, MDAI) confirmed-fail on RVOL < 2.0. Market-wide search yielded no penny-range tickers with confirmed intraday RVOL ≥ 2.0. Broad screeners showed no live scanner data accessible; PACB/CELZ/GCTS RVOL unconfirmed → discarded. **No entries today.**

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
