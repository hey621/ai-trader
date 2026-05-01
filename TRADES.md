# TRADES.md — PennyAlpha_Bot Workspace
_Last updated: 2026-05-01 (Morning Execution Scan 10:15 AM EST)_
_Last reviewed: 2026-04-27 (Weekly Review — Week of 2026-04-21)_

---

## EXECUTION QUEUE
_Populated by morning execution scan. Consumed and cleared by trade.py._

| Ticker | Signal | Entry | Stop | Target | Conviction | Catalyst |
|--------|--------|-------|------|--------|------------|---------|

---

## WATCHLIST
_Updated: 2026-05-01 pre-market scan_
_Reviewed 2026-05-01 (Morning Execution Scan — all watchlist entries assessed; BYND cleared below)_

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

### 2026-04-29 Pre-Market (Monday)

_Scan time: 8:00 AM EST | Criteria: price $0.50–$5.00, PM move ≥5% UP, prev dollar vol ≥$500K, spread ≤3%_

| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| — | — | — | — | — | — | — | — | — |

**⚠️ SCAN NOTE — API UNAVAILABLE:** `premarket.py` failed with HTTP 403 (POLYGON_KEY not configured). Manual web scan performed (8 searches, per 8-search maximum). No specific penny stock in the $0.50–$5.00 range with PM move ≥5%, prev dollar vol ≥$500K, and spread ≤3% was identified from available public sources.

**Market context (8:00 AM EST):** Futures flat (S&P 500 +0.07%, Nasdaq 100 +0.39%, Dow +0.02%, Russell 2000 +0.30%). Primary catalysts today/week: Fed rate decision; Big Tech earnings after close (GOOG, MSFT, AMZN, META); Apple Q2-2026 earnings Thursday. Notable large-cap movers: NXPI +19% (Q1 earnings beat + strong outlook); HOOD −10.8% (Q1 miss, crypto revenue −47%); ENPH −7.2% (weak Q2 guidance). No penny stock ($0.50–$5.00) candidates surfaced with confirmed ≥5% premarket move.

**PDUFA check (Apr-29-26):** Sanofi (SNY) PDUFA for Tzield — large-cap, price disqualified. No penny stock PDUFA dates on Apr-29 confirmed.

**Dilution / SEC 8-K check:** No 8-K filings for prior tracked tickers (CDXS, IFRX, ABCL, ATNM, BTAI) found from Apr-28/29-26 searches.

**Notable status updates from prior scan entries (as of premarket Apr-29-26):**

- **CDXS:** Price now ~$1.82 (+4.6% on last session per search data) — significant decline from Apr-24 close range of ~$2.40–$2.62. PM move below 5% threshold; did not qualify for this scan. Earnings confirmed May-7-26 after close; 200-day MA cross from Apr-22 may have reversed given steep price decline. Monitor intraday for RVOL and MA position vs. prior scan baselines.
- **IFRX:** No new catalyst confirmed from Apr-28/29 searches. Earnings window May-6–11-26 approaching. Nasdaq deficiency cure deadline Sep-8-26 unchanged. RVOL ~2.3x was Apr-22 confirmed; re-verify intraday today.
- **ABCL:** No new data from searches. Earnings May-11-26 unchanged. RVOL unconfirmed above 2.0 premarket.
- **ATNM:** No update. RVOL ~0.25 last confirmed Apr-24; earnings May-8-26 unchanged.
- **BTAI:** No update. RVOL ~0.77 last confirmed Apr-24. PDUFA Nov-14-26 unchanged.

**Premarket scan conclusion:** Zero qualifying UP movers cleared all filters (API unavailable; manual web search found no penny stock ≥5% PM move in $0.50–$5.00 range with sufficient liquidity). No tickers starred (*) for Monday aggregation +2 conviction bonus.

---

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
| MDAI | ~$1.87 | ~0.09x | ~$120K est. | Y | BARDA $54.9M non-dilutive; FDA De Novo pending; earnings 2026-05-12–13 | None detected | Unknown | — | **FAIL — RVOL 0.09x < 1.5; dollar vol $120K < $500K; earnings not tonight/tomorrow** |
| BZAI | ~$2.19 | ~0.65x (10.44M vs avg 15.95M) | ~$22.9M | Y | Nokia APAC partnership; Indonesia MOU; NeoTensr $50M — all prior, no new catalyst tonight/tomorrow | None detected | Unknown | — | **FAIL — RVOL 0.65x < 1.5; no catalyst tonight/tomorrow confirmed** |
| OABI | ~$1.53 | ~0.78x (386K vs avg 494K) | ~$590K est. | Unknown (52W $1.22–$3.52; near lows) | OmniUltra platform Dec 2025; earnings 2026-05-07 | Unknown | Unknown | 2/5 | **FAIL — RVOL 0.78x < 1.5; earnings not until May 7** |
| RZLV | ~$2.58 | Unconfirmed | Unconfirmed | Unknown | 543% H2 2025 revenue growth (Apr 22); $360M FY 2026 guide | Unknown | Unknown | — | **FAIL — RVOL unconfirmed; discarded per rules** |
| RCAT | ~$11.80 | — | — | — | Drone/defense; Q4 FY2026 revenue surge 2,500%; maritime unmanned systems | — | — | — | **FAIL — above $5.00 ceiling** |
| LOGC | ~$8.50 | — | — | — | $907.5M US Salt acquisition Feb 2026; $2.9B NOLs | — | — | — | **FAIL — above $5.00 ceiling** |

**Summary (6 screened, 0 passed):** No PDUFA decisions confirmed for April 29 in penny range. Both MDAI and BZAI fail strict RVOL ≥ 1.5 and/or dollar vol ≥ $500K thresholds today; no new catalyst expected tonight/tomorrow. OABI borderline dollar vol but RVOL 0.78x and May 7 earnings too far out. RZLV RVOL unconfirmed. RCAT and LOGC above $5 ceiling. Watchlist set to empty.

### 2026-04-29 Afternoon Scan

| Ticker | Price | RVOL | Dollar Vol | Above SMA20 | Catalyst | Dilution | Short Float | Score | Result |
|--------|-------|------|-----------|-------------|---------|---------|------------|-------|--------|
| RZLV | ~$2.53 | ~0.82x (18M vs avg 22M) | ~$57M est. | Unknown (52W $1.90–$8.45; price ~$2.53 near low end) | 2025 blowout results + $360M FY2026 guide (announced Apr 22 — already priced in); no new catalyst tonight/tomorrow confirmed | Prior QII private placement at $5.40/share — dilution risk | Unknown | 2/5 | **FAIL — RVOL 0.82x < 1.5; catalyst already priced in (Apr 22); dilution risk from prior PP** |
| CDXS | ~$2.56–$2.65 | ~1.0x (1.51M vs ~1.5M avg) | ~$4M est. | Y (price risen from ~$1.08 in Mar to ~$2.65 Apr — strong uptrend) | Q1 2026 earnings May 7 after close (not tonight/tomorrow); $38M Merck licence prior catalyst | 18.71% share count increase YoY — moderate dilution | Unknown | 2/5 | **FAIL — RVOL ~1.0x < 1.5; catalyst (earnings) not until May 7; moderate dilution** |
| MNDR | ~$0.73 | Unknown | ~$187K est. (avg 256K shares × $0.73) | Unknown | $126M AI data center campus announcement (phased 60MW); prior catalyst Mar/Apr | Market cap only ~$3–4M; tiny float — HIGH DILUTION/LIQUIDITY RISK | Unknown | 1/5 | **FAIL — dollar vol ~$187K far below $500K threshold; micro-cap liquidity risk** |
| KOPN | ~$2.25 | ~0.87x (MSN confirms Apr 29 close ~$2.25, -2.63%) | Unknown | Unknown | Earnings May 12, 2026 — not tonight/tomorrow; defense microdisplays/optical | None noted | Unknown | 2/5 | **FAIL — no catalyst tonight/tomorrow; earnings May 12 too far out; RVOL below threshold** |
| AXSM | ~$189 | — | — | — | PDUFA Apr 30 for AXS-05 (Alzheimer's Agitation) — Priority Review | None noted | — | — | **FAIL — far above $5.00 ceiling (~$189)** |
| ASBP | ~$0.25 | High (WallStreetZen most-active Apr 28) | Unknown | Unknown | No confirmed positive catalyst found | Unknown — micro-cap | Unknown | 1/5 | **FAIL — price below $0.50 floor; no confirmed catalyst** |

| FDMT | ~$9.45 | — | — | — | PRISM 2-yr readout May 1 2026; avg analyst PT $31.25 | None noted | — | — | **FAIL — above $5.00 ceiling (~$9.45)** |
| LOGC | ~$8.50 | — | — | — | $2.7B NOL carryforwards; strategic alternatives; no near-term catalyst | None noted | — | — | **FAIL — above $5.00 ceiling (~$8.50); formerly WISH, ticker changed** |
| ASTC | ~$2.85–$3.10 | Unconfirmed (Apr 27: 107x; stale) | Unconfirmed | Y (historical) | No confirmed new catalyst Apr 29/30; Dec 2025 DHS $1B initiative already priced in; RSI ~85 overbought | $30M mixed shelf Jan 2026 (not drawn) | Unknown | 2/5 | **FAIL — no confirmed new catalyst today; RVOL unconfirmed; overbought RSI** |

**Summary (9 screened, 0 passed):** No PDUFA decisions on Apr 30 in penny range (AXSM at ~$189 is sole Apr 30 PDUFA — far above ceiling). No penny-range confirmed earnings beats after close tonight. RZLV meets price/dollar-vol but RVOL 0.82x and catalyst already priced in from Apr 22; prior PP dilution risk. CDXS in uptrend but RVOL ~1.0x and earnings not until May 7. MNDR dollar volume below $500K threshold. KOPN no near-term catalyst. ASBP below $0.50 floor. FDMT ($9.45) and LOGC ($8.50) above ceiling. ASTC no confirmed new catalyst and stale RVOL data. Macro note: Meta Q1 2026 earnings due after close tonight — watch penny-range AI/tech names in tomorrow's pre-market scan if Meta beats. **Watchlist set to empty.**

---

### 2026-04-30 Morning Scan

_Scan time: 10:15 AM EST | Criteria: price $0.50–$10.00, RVOL ≥ 1.5 confirmed intraday, dollar vol ≥ $500K, spread ≤ 3%, above 20-day MA, confirmed SEC 8-K catalyst_

| Ticker | Price | RVOL | Dollar Vol | Spread | Above SMA20 | Catalyst (SEC) | Dilution | Short Float | Tech Score | Conviction | Result |
|--------|-------|------|-----------|--------|-------------|----------------|---------|------------|-----------|-----------|--------|
| BZAI | ~$1.75 +41% | ~1.89x (est: 30.3M vs ~16M avg) | ~$53M | ~1.5% est. | **UNCONFIRMED** (3-day decline $2.25→~$1.24 before today's bounce; SMA20 borderline) | NeoTensr $50M (Apr 14); Datacomm MOU (Apr 21); Stockholder rights plan (Apr 22) — no new Apr 30 filing | $30M PP @$3.20 (above-mkt); 25–45% projected dilution; cash $45.8M, burn $16.5M/qtr → ~8mo runway | Unknown | 1–2/5 | 6–7 (tech 1–2 + 5 prior appearances) | **FAIL** — SMA20 unconfirmed; per rules "if unconfirmed, discard"; dilution 25–45% projected concerning |
| FATN | ~$2.38 +38% est. | ~70x (est: 4.55M vs ~65K avg) — April 30 data unconfirmed | ~$10.8M est. (April 30 unconfirmed; April 29 confirmed vol $351K < $500K) | Unknown | Uncertain (above SMA20 as of Apr 21; recent dip to ~$1.73 then bounce) | Apr 28: VeloCloud Replacement Program; Apr 29: NASA SEWP / Equalis expansion — both **press releases only**, NOT confirmed 8-K filings (last confirmed 8-K: Mar 25, 2026) | Minimal (~6.9% share count increase since IPO); $6.2M cash; positive adj. EBITDA $0.59M | 2.5% float; 152.6K shares short (+172% recent period) | 2–3/5 | 2–3 (no prior appearances) | **FAIL** — no confirmed April 8-K; April 29 dollar vol $351K < $500K threshold; April 30 RVOL/vol data unconfirmed |
| HWH | ~$1.76 +34% | Unknown | ~$2.4M est. (1.39M shares × $1.76) | Unknown | Unknown | No confirmed SEC 8-K catalyst found for April 2026 (lifestyle/marketplace business: Hapi Cafe, Hapi Travel, Hapi Wealth Builder) | Confirmed ~$1.76M public offering at $0.40/share (highly dilutive vs current price) | <10K shares short by Mar 13 (very low) | —/5 | — | **FAIL** — no confirmed SEC catalyst; recent dilutive offering at $0.40 |
| TURB | ~$1.96 +32% | ~18x est. (9.35M vs ~500K avg est.) | ~$18.3M | Unknown | Uncertain | Apr 28: 6-K — AI-driven energy storage deployed in international military ops; Apr 27: 6-K — EGM shareholders authorize board to raise capital / issue convertible securities (dilution signal); Apr 9: patent; Apr 20: Hithium partnership; Mar 30: 130–140% revenue growth 6-K | $100M F-3 shelf (Nov 2025); Apr 27 EGM authorized additional capital raises; Mar 2026 $3.25M registered direct offering @$3.25 ADS | 743.3K shares short; 1.0 DTC (~3.4% float) | 2–3/5 | 2–3 (no prior appearances) | **FAIL** — conviction < 4; Danelfin AI score 1/10 (Strong Sell); April 27 capital authorization is dilution signal; F-3 $100M shelf vs $21.6M market cap |
| ASTC | ~$3.46 +2.4% | ~1.4x est. (34.3K vs ~24.6K avg) | ~$118K | ~2% est. | Y (historical) | Q2 FY2026 earnings (Feb 13); DHS $1B initiative (Dec 2025) — no new April 2026 catalyst | $30M mixed shelf (not drawn) | Very low | —/5 | — | **FAIL** — dollar vol $118K far below $500K; RVOL barely above 1.0; no new catalyst |

**Screened out summary (5 tickers screened, 0 passed):** Macro context: Meta Q1 2026 beat (reported Apr 29 after close) — broad market positive tone but no penny-range derivative catalyst. BZAI (41%) has the largest move and best conviction score estimate (~6–7) but fails the SMA20 unconfirmed rule; heavy dilution overhang (25–45% projected); no new April 30 8-K. FATN (38%) has confirmed insider buying and minimal dilution but lacks a confirmed April 8-K and April 29 dollar vol was $351K (below $500K threshold). TURB (32%) has confirmed 6-K catalysts but conviction < 4 and massive dilution overhang ($100M F-3 shelf vs $21.6M mkt cap). HWH (34%) lacks any confirmed SEC catalyst. ASTC volume negligible ($118K). **No entries today.**

---

### 2026-04-30 Afternoon Scan

| Ticker | Price | RVOL | Dollar Vol | Above SMA20 | Catalyst | Dilution | Short Float | Score | Result |
|--------|-------|------|-----------|-------------|---------|---------|------------|-------|--------|
| BYND | $0.99 (+21.9%) | >1.5x est. (~35.87M avg vol; +22% close at HOD) | ~$30M+ est. | Y est. (price in $0.65–$0.80 range prior 20 days; $0.99 close likely above SMA20; at HOD) | Army plant-based rations inquiry (Apr 30 — Military Times; not 8-K); $23.5M pea protein supply deal (8-K confirmed); Nasdaq compliance cured (8-K); Q1 earnings May 6 AH (confirmed) | No new equity offering confirmed; COO Nelson resigning May 2026 (8-K) | 31.09% → SQUEEZE CANDIDATE | 3/5 | **PASS** — added to watchlist |
| GEVO | ~$1.65 | Unconfirmed | ~$5.4M avg/day | Unknown | DOE LPO withdrawal Apr 15 (negative 8-K); CEO consulting deal; Q1 earnings May 7 | None detected | Unknown | 1/5 | **FAIL** — negative prior catalyst (DOE withdrawal); no confirmed new positive catalyst today |
| OPAL | $2.17 | Unconfirmed | Unknown | Unknown | Q1 earnings May 7 — not tonight/tomorrow; momentum per screener (+14% past week) | Unknown | Unknown | 2/5 | **FAIL** — RVOL unconfirmed; no catalyst tonight/tomorrow; earnings May 7 too far |
| PLUG | ~$3.41 (Apr 29) | ~elevated Apr 29 | Unconfirmed Apr 30 | Unknown | Analyst PT hike Apr 29; Q1 earnings May 11 | None noted | Unknown | 2/5 | **FAIL** — Apr 30 data unconfirmed; earnings May 11 too far out; Apr 29 catalyst already priced in |
| CDXS | $2.86 (+3%) | ~0.37x (477K vs 1.31M avg) | ~$1.37M | Y (historical) | Q1 earnings May 7 — not tonight/tomorrow | None noted | Unknown | 2/5 | **FAIL** — RVOL 0.37x far below 1.5; no tonight/tomorrow catalyst |
| MGRT | ~$135 | — | — | — | Leadership overhaul Jan 2026; meme stock dynamics | Unknown | Unknown | — | **FAIL** — far above $10 ceiling; meme stock characteristics; no confirmed fundamental catalyst |

**Summary (6 screened, 1 passed):** BYND qualifies on strong-close criterion: +21.9% close at HOD with estimated RVOL >1.5, dollar vol ~$30M+, 31.09% short float (SQUEEZE CANDIDATE), confirmed Q1 earnings May 6 AH, $23.5M pea protein supply deal (8-K) and Nasdaq compliance cured (8-K). SMA20 estimated above given prior 20-day range ~$0.65–$0.80 vs $0.99 close; flagged as unconfirmed. No confirmed high dilution offering. GEVO rejected on negative DOE catalyst. OPAL/PLUG/CDXS fail RVOL or timing thresholds. MGRT far above ceiling.

---

### 2026-04-29 Morning Scan

_Scan time: 10:15 AM EST | Criteria: price $0.50–$10.00, RVOL ≥ 2.0 confirmed intraday, dollar vol ≥ $500K, spread ≤ 3%, above 20-day MA, confirmed SEC 8-K catalyst_

| Ticker | Price | RVOL | Dollar Vol | Spread | Above SMA20 | Catalyst (SEC) | Dilution | Short Float | Tech Score | Conviction | Result |
|--------|-------|------|-----------|--------|-------------|----------------|---------|------------|-----------|-----------|--------|
| ASTC | ~$2.85–$3.10 | Unconfirmed today (Apr 27: ~107x) | Unconfirmed | ~2% est. | Y (historical) | 8-K: Q2 FY2026 earnings Feb 13 (R&D −25%); DHS $1B initiative Dec 2025 — no new Apr 2026 8-K | $30M mixed shelf Jan 2026 (not drawn) | 960K short (+3,233% from Mar 15); 0.1 DTC | 3/5 | — | **FAIL — RVOL unconfirmed today; no new April 2026 catalyst; Apr 27 spike not sustained** |
| GEVO | ~$1.81–$1.89 | Unconfirmed | ~$5.4M avg/day | ~1.5% est. | Unknown | 8-K: DOE financing withdrawal Apr 16 (NEGATIVE); CEO consulting Apr 22 | None detected | Unknown | 1/5 | — | **FAIL — Negative DOE withdrawal catalyst; CEO transition; no confirmed positive 8-K** |
| CELZ | ~$2.28–$2.47 | 0.40x (40K vs 102K avg) | ~$95K est. | Unknown | Unknown | No confirmed April 2026 8-K | Unknown | Unknown | 1/5 | — | **FAIL — RVOL 0.40x < 2.0; dollar vol ~$95K far below $500K** |
| GCTS | ~$1.20–$1.37 | Unconfirmed today (Apr 6: ~1.25x) | Unconfirmed | Unknown | Unknown | No recent 8-K confirmed (5G/4G LTE semiconductor) | Unknown | Unknown | 2/5 | — | **FAIL — RVOL unconfirmed today; stale data from Apr 6** |
| IFRX | ~$1.69 | 0.73x (855K vs 1.17M avg) | ~$1.44M | Unknown | Y (Nasdaq compliance met) | 6-K: Nasdaq bid price compliance regained Apr 27 | Unknown | Unknown | 2/5 | — | **FAIL — RVOL 0.73x < 2.0; compliance regain is minor catalyst, not strong 8-K** |
| BZAI | ~$1.70–$1.90 | Unconfirmed | Unconfirmed | ~1.5% est. | Y | 8-K: NeoTensr $50M; Nokia AI — all prior; down −13.43% Apr 28; no new Apr 29 catalyst | None detected | Unknown | 2/5 | — | **FAIL — RVOL unconfirmed; price declining; no new catalyst** |
| MDAI | ~$1.96 | 0.93x (413K vs 444K avg) | ~$813K | ~2% est. | Y | BARDA $54.9M; FDA De Novo pending — all prior catalysts; Q1 earnings May 12 | None detected | Unknown | 3/5 | — | **FAIL — RVOL 0.93x < 2.0; no new catalyst today** |
| PACB | ~$1.52–$1.65 | Unconfirmed today (Apr 27: ~1.69x) | Unconfirmed | Unknown | Unknown | Trillion Gene Atlas (Basecamp Research, Mar 2026 — already priced in) | None noted | Unknown | 2/5 | — | **FAIL — RVOL unconfirmed today; catalyst already priced in from Mar 2026** |

**Screened out summary (8 tickers screened, 0 passed):** No tickers met the combined threshold of confirmed RVOL ≥ 2.0 + confirmed positive SEC 8-K catalyst. Market context: Big Tech Q1 earnings after close today (GOOG, MSFT, AMZN, META) creating risk-off tone in small/micro caps. ASTC Apr 27 RVOL spike (107x) was event-specific and not confirmed as repeating today. GEVO DOE withdrawal is a negative catalyst. CELZ dollar vol far below minimum. GCTS data stale. IFRX, BZAI, MDAI all sub-1.0x RVOL. PACB catalyst already priced in. **No entries today.**

---

### 2026-05-01 Pre-Market

_Scan time: ~9:00 AM EST | Criteria: price $0.50–$10.00, PM move ≥5% UP, prev dollar vol ≥$500K, spread ≤3%_

| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| — | — | — | — | — | — | — | — | — |

**Market context (pre-market ~9:00 AM EST):** Futures broadly positive: S&P 500 +0.36%, Nasdaq 100 +0.16%, Dow Jones +0.40%, Russell 2000 +0.18%. Large-cap movers: TEAM +23% (Q1 32% revenue beat — above $10 ceiling); RBLX −24.8% (lowered annual growth outlook — above $10 ceiling). CUE Biopharma surged +77.8% overnight (Apr 29→Apr 30) on $30M PIPE and Ascendant-221 Phase 2 anti-IgE antibody license (8-K filed Apr 30); however Apr 30 close was ~$14.74 and pre-market May 1 is ~$12.70 (−2.27%) — **price far above $10 ceiling; today a DOWN pre-market mover**.

**PDUFA check (May-1-26):** No PDUFA decisions confirmed in penny range ($0.50–$10.00) for today. FDMT (4D Molecular Therapeutics) released PRISM 2-yr Phase 1/2 wet AMD readout (positive long-term data, 94% fewer injections in Phase 2b subgroup); however FDMT pre-market ~$9.11 is DOWN −2.36% — **DOWN mover; positive data partially priced in from Nov 2025 interim readout**.

**Screened candidates (4 tickers examined, 0 passed all filters):**

| Ticker | Prev Close | PM Price | PM Move% | Direction | Spread | Above SMA20 | Catalyst | SEC Confirmed |
|--------|-----------|---------|---------|-----------|--------|-------------|----------|---------------|
| CUE | ~$8.51 est. (Apr 29 close) | ~$12.70 | N/A — surge was Apr 29→Apr 30 | DOWN (−2.27% from Apr 30 close $14.74) | Unknown | Unknown | $30M PIPE + Ascendant-221 anti-IgE Phase 2 license + new CEO | 8-K: PIPE + license (Apr 30) | **FAIL: Apr 30 close $14.74 — far above $10 ceiling; pre-market May 1 is a DOWN mover** |
| BYND | $0.9841 | ~$1.00 est. | +1.44% | UP | Low est. | Y est. | Q1 earnings May 6 AH; Army protein inquiry; Nasdaq compliance cured; Big Geyser Beyond Immerse deal | 8-K: pea protein supply deal + Nasdaq cure | **FAIL: PM move +1.44% — far below 5% threshold; remains on watchlist from Apr 30 afternoon scan** |
| FDMT | ~$9.45 est. | ~$9.11 | −2.36% | DOWN | Unknown | Unknown | PRISM 2-yr wet AMD readout (positive: 94% fewer injections in Phase 2b subgroup) — move DOWN (profit-taking; data partially priced in Nov 2025) | Data disclosed; no new 8-K confirmed | **FAIL: DOWN mover; catalyst partially priced in; price borderline near $10 ceiling** |
| CDXS | ~$2.86 | ~$2.24 | −6.67% | DOWN | Unknown | Y (historical) | Q1 2026 earnings May 7 AH — no new May 1 catalyst identified | None | **FAIL: DOWN mover; no catalyst; earnings not until May 7** |

**Pre-market scan conclusion:** Zero qualifying UP movers cleared all filters. CUE was the week's largest penny-adjacent biotech catalyst but closed at $14.74 (above $10 ceiling) and is a DOWN mover pre-market today. BYND +1.44% far below 5% threshold. FDMT released positive PRISM data but is a DOWN pre-market mover. CDXS down sharply with no catalyst. No new tickers receive +2 conviction bonus for the 10:15 AM morning execution scan.

**BYND carries forward** on WATCHLIST from Apr 30 afternoon scan (3/5 score; Q1 earnings May 6 AH; 31.09% short float SQUEEZE CANDIDATE).

---

### 2026-05-01 Morning Scan

_Scan time: 10:15 AM EST | Criteria: price $0.50–$10.00, RVOL ≥ 1.5 confirmed intraday, dollar vol ≥ $500K, spread ≤ 3%, above 20-day MA, confirmed SEC 8-K catalyst_

| Ticker | Price | RVOL | Dollar Vol | Spread | Above SMA20 | Catalyst (SEC) | Dilution | Short Float | Tech Score | Conviction | Result |
|--------|-------|------|-----------|--------|-------------|----------------|---------|------------|-----------|-----------|--------|
| BYND | $1.10 | ~0.51x (13.85M vs ~27M avg) | ~$15.2M | Low est. | Y est. | 8-K: $23.5M pea protein supply deal (Mar 28); Nasdaq compliance cured; COO resignation 8-K (Apr 20); Q1 earnings May 6 AH | HIGH DILUTION — ATM exhausted $151.7M; shares outstanding +496.1%; S-3 shelf 9.55M selling shares | 31.09% — SQUEEZE CANDIDATE; borrow fee 47.90%; DTC ~5.25 days | —/5 | — | **FAIL** — RVOL 0.51x < 1.5; HIGH DILUTION RISK (shares +496.1%); insider selling (CLO sold 29,978 shares Apr 20 via 10b5-1) |
| BBAI | ~$4.00 | ~1.5–1.8x est. (50–70M vs ~38M avg) | ~$200–280M est. | Unknown | Y (20.2% above SMA20 confirmed) | 8-K: Apr 21 authorized shares doubled 500M→1B (DILUTION signal); no positive catalyst 8-K in 2026; pre-earnings positioning only (Q1 May 5 AH) | Authorized shares doubled (500M→1B); balance sheet healthy ($611M equity); Ask Sage $250M acquisition Dec 31 | ~28.11% — SQUEEZE CANDIDATE | 1/5 | 4 | **FAIL** — no confirmed positive SEC 8-K catalyst; only 2026 8-K is dilution (authorized share doubling); all 4 insider transactions = selling; pre-earnings speculation only |
| BZAI | ~$1.90 | ~0.53x (Apr 30 data; May 1 unconfirmed) | N/A | ~1.5% est. | Y | 8-K: NeoTensr $50M; Nokia AI (prior Apr catalysts); no new May 2026 filing | $30M PP @$3.20 above-market; 25–45% projected dilution | Unknown | —/5 | — | **FAIL** — RVOL unconfirmed May 1; last confirmed data (Apr 30): 0.53x < 1.5 |
| MDAI | ~$2.09 | ~0.91x (327K vs 359K avg) | ~$683K | ~2% est. | Y | BARDA $54.9M (prior); FDA De Novo pending (prior); Q1 earnings May 12 — no new catalyst | None detected | Unknown | —/5 | — | **FAIL** — RVOL 0.91x < 1.5; no new catalyst today; Q1 earnings May 12 too far |
| PDYN | ~$5–6 est. | Unconfirmed | Unknown | Unknown | Unknown | AFRL HANGTIME contract (prior, already priced in); Q1 earnings May 13 | None noted | Unknown | —/5 | — | **FAIL** — RVOL unconfirmed; prior catalyst already priced in; earnings May 13 too far |

**Screened out summary (5 tickers screened, 0 passed):** No tickers met the combined threshold of confirmed RVOL ≥ 1.5 + confirmed positive SEC 8-K catalyst. Market context: May Day holiday in many global markets; U.S. markets open; macro broadly positive (S&P 500 +0.36% futures per pre-market). BYND (watchlist) failed RVOL 0.51x and carries HIGH DILUTION RISK (ATM exhausted; shares +496.1%). BBAI (+10% today, ~$4.00) is the day's most interesting candidate but lacks a confirmed positive 8-K — only 2026 8-K is dilution-negative (authorized share doubling Apr 21); all 4 insider transactions = selling. BZAI May 1 RVOL unconfirmed; Apr 30 data showed 0.53x. MDAI and PDYN both below RVOL threshold or unconfirmed. **No entries today.**

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
