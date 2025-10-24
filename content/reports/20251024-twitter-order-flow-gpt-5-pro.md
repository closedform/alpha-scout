20251024 Twitter Order Flow Sweep

Alpha Discovery Report (Equities Only)

Model Run
- Model: GPT-5 Pro
- Reasoning Time: 11m20s

⸻

Report Meta
- Source Searched: Twitter/X (selected threads via Thread Reader) + supporting public docs
- Query / Filters: equity alpha
- Scan Window: 2017-01-01 – 2025-12-31
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: 3:50 “Significant Imbalance” → drift into the NYSE close

Source(s):
- @NYSE Data Insights — “The NYSE Significant Imbalance” (Nov 4, 2024)
- BMLL — “Into the Close: U.S. Closing Auction Dynamics” (Jun 24, 2025)

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
NYSE publishes a “Significant Imbalance” flag at 3:50:00 PM that highlights outsized auction imbalances based on notional and 20‑day auction volume baselines. A positive (buy) flag statistically coincides with price drift into the close and larger auction slippage versus the 2‑minute pre‑close VWAP, especially for highly intern alized names. Trade the into‑close drift conditional on the flag and normalized imbalance magnitude.  ￼

Feature Transformations (bullet list):
- Binary SignificantImbFlag_350 ∈ {0,1} (3:50:00 PM publication)
- ImbZ = ImbalanceShares / avg20dAuctionVol (z‑score by symbol)
- Slippage2m = CloseAuctionPrice − VWAP[3:58–4:00]
- Drift = Price[4:00] − Price[3:50] (or last 10 minutes)
- Interaction: ImbZ × HighInternalization (TRF share filter)

Data Dependencies (concise list):
NYSE Closing Imbalance feed (or BMLL auction imbalance), top‑of‑book NBBO, TAQ prints, TRF share within 15m of close.

Universe & Filters:
US Large‑Cap; price > $5; ADV > $10M; primary‑listed NYSE; exclude halts.

Directionality / Construction Hints:
Long on SignificantImbFlag_350=Buy with ImbZ>τb; short on Sell flags with ImbZ<−τs; beta‑neutral; scale by |ImbZ|; exit on auction print or 4:00:00.

Strength & Actionability (qualitative only):
Strong – Exchange-documented flag, clear timestamp, straightforward transforms; liquid execution.

Keywords (comma-separated):
order-flow, MOC, auction, imbalance, intraday, slippage

Expected Horizon Notes:
Backtest 2023–2025 intraday; live monitor 6–8 weeks.

Citations:
- NYSE Significant Imbalance explainer.  ￼
- BMLL analysis of closing auctions and imbalance dynamics.  ￼

⸻

Alpha Idea #2: Imbalance acceleration from 3:50→3:55 (D‑quotes window) predicts last‑minute move

Source(s):
- DataBento Blog — “How NYSE’s Closing Imbalance Feed Moves Markets” (Apr 4, 2023)
- NYSE — “Closing Auction” overview

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Imbalance updates accelerate after 3:50 as offsetting D‑Orders (D‑quotes) appear, often causing directional bursts into the close. The rate of change of imbalance between 3:50 and ~3:55 (and to 3:59:50) is predictive of the final 5‑minute price path. Build a slope/acceleration measure and trade the sign.  ￼

Feature Transformations:
- dImb/dt over [3:50, 3:55], [3:55, 3:59:50]
- Accel = (dImb/dt)_late − (dImb/dt)_early
- ImbConv = Imbalance[3:59:50] − Imbalance[3:50] normalized by avg20dAuctionVol
- ΔMid = Mid[4:00] − Mid[3:50]

Data Dependencies:
Closing imbalance feed, NBBO mid, trades.

Universe & Filters:
NYSE‑listed >$5, ADV > $5M; exclude earnings days (optional).

Directionality / Construction Hints:
Follow the sign of Accel; close at auction or 4:00:00; add cap at extreme spreads.

Strength & Actionability:
Promising – Mechanism well‑documented; requires feed access but easy to compute.

Keywords:
order-flow, D-quotes, acceleration, imbalance, closing

Expected Horizon Notes:
Backtest 2019–2025; live run 1–2 rebalance cycles.

Citations:
- D‑quotes/imbalance impact explainer.  ￼
- NYSE auction process reference.  ￼

⸻

Alpha Idea #3: Highly internalized names → larger into‑close drift and slippage

Source(s):
- NYSE Data Insights — “Closing Auction: Internalization effect throughout imbalance period” (Nov 17, 2022)

Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: Intraday (1-6h) & Overnight
Signal Type: Microstructure/Order-Flow

Core Idea:
Symbols with high off‑exchange (TRF) share near the close show more price drift during the imbalance period and larger auction slippage, creating a tradable tilt when combined with imbalance direction. Filter names by recent TRF share and amplify the closing drift/auction slippage play.  ￼

Feature Transformations:
- TRF15 = TRFVol[3:45–4:00] / (AuctionVol + TRFVol[3:45–4:00])
- Interaction: Sign(Imbalance) × TRF15
- Slip2m as in Idea #1

Data Dependencies:
Imbalance feed, TRF prints, auction prints, NBBO.

Universe & Filters:
S&P 1500 constituents; exclude ADRs.

Directionality / Construction Hints:
Scale position by TRF15 deciles; consider overnight mean‑reversion of extreme slippage.

Strength & Actionability:
Strong – Exchange study; transparent transforms; robust liquidity.

Keywords:
internalization, MOC, imbalance, slippage, TRF

Expected Horizon Notes:
Backtest Mar–Sep 2022, then extend 2023–2025.

Citations:
- NYSE internalization effect and drift/slippage study.  ￼

⸻

Alpha Idea #4: Opening auction imbalance sign predicts first 5–15 minutes

Source(s):
- NYSE — “The Closing Auction” (opening auction rules included)
- NYSE TAQ Quick Reference — Order Imbalance messages (Opening/Closing)
- NYSE Arca Trading Info — opening imbalance schedule

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Opening imbalance messages (8:30–9:35 cadence) reveal demand/supply skew that tends to carry into the first minutes post‑open. Normalize imbalance by average opening auction volume and trade the first 5–15 minutes in the direction of the sign.  ￼

Feature Transformations:
- OpenImbZ = ImbShares / avg20dOpenAuctionVol
- GapAdj = (OpenPrice − pre‑mkt VWAP)
- Filter: |OpenImbZ| > τ and Spread <= k × tick

Data Dependencies:
Opening imbalance feed, auction print, pre‑market trades, NBBO.

Universe & Filters:
NYSE/Arca‑listed; price > $5; ADV > $5M.

Directionality / Construction Hints:
Directional scalp (5–15 min); fade when GapAdj is into the imbalance (exhaustion).

Strength & Actionability:
Promising – Clear timestamps and cadence; execution straightforward with L1/L2.

Keywords:
opening auction, imbalance, gap, intraday

Expected Horizon Notes:
Backtest 2018–2025 (intraday); forward monitor 4 weeks.

Citations:
- Imbalance timings and cadence.  ￼

⸻

Alpha Idea #5: Nasdaq NOIS snapshots → pre‑close drift predictor (Tape C)

Source(s):
- Nasdaq Net Order Imbalance Snapshot (NOIS) v2.2 — spec

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
NOIS provides net order imbalance snapshots for Nasdaq names. The normalized snapshot level and its change over the last 10 minutes before the close predict drift in the continuous book and the final cross price.  ￼

Feature Transformations:
- NOIS_Z = NOIS / avg20dCloseAuctionVol
- NOIS_d = NOIS[t] − NOIS[t−Δ]
- DriftClose = Price[4:00] − Price[3:50]

Data Dependencies:
NOIS feed, NBBO/trades.

Universe & Filters:
Nasdaq‑listed, price > $5, ADV > $10M.

Directionality / Construction Hints:
Trade the sign of NOIS_Z; weight by |NOIS_d|; exit at cross.

Strength & Actionability:
Promising – Well‑specified data product; consistent publication schedule.

Keywords:
NOIS, imbalance, Nasdaq, closing, drift

Expected Horizon Notes:
Backtest 2017–2025.

Citations:
- NOIS data product and message definitions.  ￼

⸻

Alpha Idea #6: Index‑level MOC notional imbalance → SPY/QQQ/DIA into‑close tilt

Source(s):
- FinancialJuice — MOC imbalance tweet (Dec 20, 2023)
- Traders Mastermind — “Market‑On‑Close (MOC) Order Flow” (2025)

Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY, QQQ, DIA)
Horizon: Intraday (1-6h)
Signal Type: Event-Driven / Microstructure/Order-Flow

Core Idea:
Aggregated notional MOC imbalances for major indices are broadcast widely and force ETF/futures hedging into the close. Build an index‑level imbalance composite and trade the last 10–15 minutes accordingly.  ￼

Feature Transformations:
- MOC_Index = Σ (Imb_i × weight_i) over index members (or vendor aggregate)
- MOC_Index_Z via 60‑day z‑score
- ΔIndexFutBasis as risk control

Data Dependencies:
Vendor MOC prints/estimates, ETF prints, index weights.

Universe & Filters:
SPY/QQQ/DIA; avoid expiry Fridays with large options flows (optional).

Directionality / Construction Hints:
Directional or pairs vs futures; exits at 4:00:00.

Strength & Actionability:
Promising – Public notional figures are common; ETFs are liquid.

Keywords:
MOC, ETF, imbalance, hedging

Expected Horizon Notes:
Backtest 2020–2025.

Citations:
- Example index MOC broadcast; general MOC overview.  ￼

⸻

Alpha Idea #7: Auction slippage mean‑reverts overnight

Source(s):
- NYSE Internalization/Slippage study (Nov 17, 2022)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Overnight
Signal Type: Mean-Reversion / Microstructure

Core Idea:
Extreme positive or negative closing auction slippage (vs last 2‑minute VWAP) often reflects flow imbalances that partially revert by next open. Build a cross‑sectional overnight mean‑reversion overlay keyed to |Slip2m|.  ￼

Feature Transformations:
- Slip2m deciles
- Winsorized Slip2m per sector; beta‑neutral overlay

Data Dependencies:
Auction print, pre‑close VWAP, next‑day open.

Universe & Filters:
S&P 1500; exclude earnings/pre‑announce.

Directionality / Construction Hints:
Long high negative slippage, short high positive slippage; close at next open.

Strength & Actionability:
Promising – Directly tied to observable closing mechanics.

Keywords:
auction, slippage, mean-reversion, overnight

Expected Horizon Notes:
Backtest 2018–2025 daily.

Citations:
- Drift/slippage patterns around close.  ￼

⸻

Alpha Idea #8: Integrated OFI (multi‑level) → short‑horizon price impact

Source(s):
- Cont, Kukanov & Stoikov — “The Price Impact of Order Book Events” (2010/2012)
- Xu, Gould, Howison — “Multi‑Level Order‑Flow Imbalance (MLOFI)” (2019/2020)
- Cont et al. — “Cross‑Impact of OFI in Equity Markets” (2021)

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Order‑flow imbalance (OFI) across multiple LOB levels has a near‑linear relation to short‑horizon returns, with slope inversely related to depth. Compute integrated multi‑level OFI and regress to near‑term price change; optionally include cross‑impact from sector leaders.  ￼

Feature Transformations:
- OFI_L1..Lk and OFI_Int = Σ w_l OFI_Ll
- DepthInv = 1 / Depth_L1 interaction
- Cross‑impact term: sector ETF OFI or peer leader OFI

Data Dependencies:
Full depth L2/L3, NBBO, trades.

Universe & Filters:
Top 500 by ADV; exclude large‑tick constraints if needed.

Directionality / Construction Hints:
Thresholded linear predictor; inventory and spread‑aware exits (<5–10 min).

Strength & Actionability:
Strong – Extensive literature; simple transforms; robust execution in liquid names.

Keywords:
OFI, microstructure, depth, cross-impact

Expected Horizon Notes:
Backtest 2017–2025 tick/L2.

Citations:
- OFI impact and multi‑level construction; cross‑impact evidence.  ￼

⸻

Alpha Idea #9: Queue imbalance / microprice → one‑tick‑ahead predictor

Source(s):
- Stoikov — “The Micro‑Price: A High‑Frequency Estimator of Future Prices” (2017)
- Gould & Bonart — “Queue Imbalance as a One‑Tick‑Ahead Price Predictor” (2015)
- Sasha Stoikov tweet (Jun 11, 2020) — microprice definition

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Microprice and best‑level queue imbalance predict the direction of the next mid‑price movement. Use imbalance‑adjusted mid (microprice) and a signed deviation from last trade to trade one‑tick‑ahead moves with tight exits.  ￼

Feature Transformations:
- I = Q_bid / (Q_bid + Q_ask)
- Micro = I*P_ask + (1−I)*P_bid
- ΔMicro = Micro − Mid ; trade sign(ΔMicro)

Data Dependencies:
Level‑1 sizes/prices, trades.

Universe & Filters:
Large‑tick, liquid names (AAPL, MSFT, etc.).

Directionality / Construction Hints:
Enter with sign(ΔMicro); exit on fill or next quote update; spread‑aware sizing.

Strength & Actionability:
Strong – Reproducible with L1; well‑studied.

Keywords:
microprice, queue-imbalance, one-tick, NBBO

Expected Horizon Notes:
Backtest tick 2019–2025.

Citations:
- Microprice and queue imbalance foundations.  ￼

⸻

Alpha Idea #10: NBBO rotation spike → short‑term “attention” momentum

Source(s):
- Proof Trading — Market Structure Primer §5: NBBO change clustering (Oct 1, 2022)
- (Context) Multiple Twitter reposts quoting “NBBO rotates 500% more…” snippets in active names.

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Event-Driven / Microstructure

Core Idea:
Bursts of NBBO updates (quote rotation) cluster during information arrival and tend to precede short‑term directional moves. Compute a rotation‑z‑score (recent NBBO changes vs 20‑day same‑time baseline) and trade in the direction of contemporaneous OFI.  ￼

Feature Transformations:
- Rot = #NBBO_changes[Δt] ; RotZ = zscore_by_timeofday(Rot)
- Interaction: RotZ × sign(OFI_L1)
- Filter by spread/tick and quote-to-trade (see Idea #11)

Data Dependencies:
SIP or direct feed NBBO, L1 sizes, trades.

Universe & Filters:
Mega‑caps and news‑sensitive names.

Directionality / Construction Hints:
Trigger when RotZ>2; hold 5–30 minutes; beta‑neutral basket.

Strength & Actionability:
Tentative – Needs careful debiasing for latency and feed artifacts.

Keywords:
NBBO, rotation, attention, OFI, intraday

Expected Horizon Notes:
Backtest 2021–2025; event windows only.

Citations:
- NBBO clustering and activity characterization.  ￼

⸻

Alpha Idea #11: Quote‑to‑trade ratio (QTR) filter → higher quality OFI signals

Source(s):
- Brugler et al. (2025) — “Differential access to dark markets…”, defines 60s quote‑to‑trade ratio

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Periods with low QTR indicate more genuine trade activity vs quote churn; OFI has higher predictive content when QTR is low. Use QTR as a regime filter to gate OFI entries.  ￼

Feature Transformations:
- QTR60 = NBBO_changes_60s / Trades_60s
- Trade OFI only if QTR60 < q_low percentile
- Optional: QTRZ by symbol/time‑of‑day

Data Dependencies:
NBBO updates, trades.

Universe & Filters:
Top 100 by ADV.

Directionality / Construction Hints:
Same as OFI (Idea #8), applied only in low‑QTR regimes.

Strength & Actionability:
Promising – Simple filter improving SNR of OFI.

Keywords:
QTR, NBBO, OFI, filter

Expected Horizon Notes:
Backtest 2019–2025.

Citations:
- QTR definition and context.  ￼

⸻

Alpha Idea #12: Odd‑lot dominance ratio → next‑day mean‑reversion tilt

Source(s):
- Schwarz et al. — “The Actual Retail Price of Equity Trades” (2022/2024)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Overnight
Signal Type: Microstructure / Mean‑Reversion

Core Idea:
Odd‑lot activity (not reflected in NBBO) proxies for certain retail/internalized flow conditions. Extreme odd‑lot share near the close correlates with closing dislocations that mean‑revert by next day’s open. Build an “odd‑lot dominance” score and run a cross‑sectional overnight reversal.  ￼

Feature Transformations:
- OddShare = OddLotVol / TotalVol (late day)
- Interact with Slip2m (Idea #7)
- Sector/size neutralization

Data Dependencies:
Trades with odd‑lot flags, auction print, next‑day open.

Universe & Filters:
S&P 500/400; exclude < $5.

Directionality / Construction Hints:
Long high OddShare + negative slippage; short mirror.

Strength & Actionability:
Tentative – Data availability varies; concept supported by execution‑quality literature.

Keywords:
odd-lots, internalization, NBBO, mean-reversion

Expected Horizon Notes:
Backtest 2020–2025.

Citations:
- Execution vs NBBO / odd‑lot context.  ￼

⸻

Alpha Idea #13: Iceberg detection via replenishment patterns → follow the hidden interest

Source(s):
- Exegy — “ML signals predicting NBBO movements / Liquidity Lamp” (2019–2021 series)
- Quant.SE — iceberg detection caveats (requires full order log)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Repeated small fills at the same price with near‑instantaneous displayed size refresh indicate hidden/iceberg interest. When iceberg events cluster on one side and microprice points that way, short‑horizon follow‑through improves.  ￼

Feature Transformations:
- IcebergHits/min (pattern of partial fills + immediate depth replenishment)
- IcebergBias = Hits_bid − Hits_ask
- ΔMicro from Idea #9

Data Dependencies:
Deep LOB (preferably L3), message/queue events.

Universe & Filters:
Top 200 by L2 message rate.

Directionality / Construction Hints:
Trade with IcebergBias sign; exit on queue depletion or price move × ticks.

Strength & Actionability:
Tentative – Requires granular feed and careful heuristics; potentially strong.

Keywords:
iceberg, hidden-liquidity, replenishment, microprice

Expected Horizon Notes:
Backtest 2021–2025.

Citations:
- Product use‑case and detection constraints.  ￼

⸻

Alpha Idea #14: Sector cross‑impact — leader OFI spills into peers

Source(s):
- Cont et al. — “Cross‑Impact of Order Flow Imbalance in Equity Markets” (2021)

Verification Status: Verified (direct link)
Equity Class: Sector-Specific (specify)
Horizon: Intraday (1-6h)
Signal Type: Cross-Sectional Composite / Microstructure

Core Idea:
OFI in large cap “leaders” propagates to related names via cross‑impact. Form sector buckets (e.g., semis) and trade lagged OFI signals from leaders into peers with brief holding windows.  ￼

Feature Transformations:
- LeaderOFI_Int (Idea #8)
- Peer regressions: Ret_peer[t+Δ] ← OFI_leader[t]
- Control: Market/sector ETF OFI

Data Dependencies:
L2/L3, taxonomy, trades.

Universe & Filters:
Sector groups; exclude illiquid peers.

Directionality / Construction Hints:
Cross‑sectional ranking; hedge to sector ETF.

Strength & Actionability:
Promising – Mechanism documented; straightforward bucket construction.

Keywords:
cross-impact, sector, OFI, propagation

Expected Horizon Notes:
Backtest 2019–2025.

Citations:
- Cross‑impact empirical study.  ￼

⸻

Alpha Idea #15: LULD re‑open auction imbalance → first 5–15 minute follow‑through

Source(s):
- Nasdaq — “All About LULDs” (Feb 10, 2022)
- SEC — Nasdaq rule filing on reopen collars (Nov 14, 2024 / Feb 4, 2025)

Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: Intraday (1-6h)
Signal Type: Event-Driven / Microstructure

Core Idea:
After LULD pauses, reopen auctions use collars and display imbalance; large signed reopen imbalance predicts initial post‑reopen direction. Trade the imbalance sign with strict halting/vol controls.  ￼

Feature Transformations:
- ReopenImbZ vs past 60 reopen auctions for the name
- CollarW as volatility proxy
- FollowThrough[5–15m]

Data Dependencies:
Reopen auction messages, NBBO/trades.

Universe & Filters:
US mid‑caps prone to LULD; exclude news halts (optional).

Directionality / Construction Hints:
Directional scalp; time‑based exit; spreads/ticks constraint.

Strength & Actionability:
Promising – Rules are public; transforms clear; execution risky but defined.

Keywords:
LULD, reopen, auction, imbalance, collars

Expected Horizon Notes:
Backtest 2020–2025 halts.

Citations:
- LULD mechanics; reopen collars.  ￼

⸻

Alpha Idea #16: Stacked footprint imbalances across levels → reversal zones

Source(s):
- Marketcalls — “Using Stacked Imbalances to Identify Key Market Reversals” (Oct 16, 2024)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Clusters (“stacks”) of aggressive buying/selling across consecutive price levels create transient support/resistance that often reverses when absorption appears. Detect stacked imbalances in equities L2 and fade on weakening delta.  ￼

Feature Transformations:
- StackLen (consecutive levels with imbalance > k)
- Absorb = rising passive volume against aggression
- Trigger: StackLen≥3 & delta_rollover

Data Dependencies:
Aggregated footprint from L2 trades, volumes by level.

Universe & Filters:
High‑ADV names; avoid news spikes.

Directionality / Construction Hints:
Fade stacks with absorption; tight stops beyond stack.

Strength & Actionability:
Tentative – Popular discretionary concept; codifiable with consistent rules.

Keywords:
footprint, stacked-imbalance, absorption, reversal

Expected Horizon Notes:
Backtest 2022–2025.

Citations:
- Tutorial and definitions.  ￼

⸻

Alpha Idea #17: Long‑memory in order‑flow signs → intraday momentum overlay

Source(s):
- Sato & Kanazawa — LMF quantitative test (2023)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow / Momentum

Core Idea:
Order‑flow sign exhibits long‑range autocorrelation due to metaorder splitting. Use rolling signed‑trade imbalances (volume‑weighted) to create a slow‑moving intraday momentum overlay that boosts OFI signals in persistent regimes.  ￼

Feature Transformations:
- SignImb = Σ sign(trade)*size over rolling window
- H_est (Hurst) as regime flag
- Interaction: OFI × SignImb

Data Dependencies:
Trade prints with aggressor side, L1.

Universe & Filters:
Top 500 by prints/day.

Directionality / Construction Hints:
Enter only when H_est>0.5 and SignImb concurs with OFI.

Strength & Actionability:
Promising – Well‑documented persistence; easy to compute.

Keywords:
long-memory, order-splitting, momentum, intraday

Expected Horizon Notes:
Backtest 2019–2025.

Citations:
- Empirical validation of long‑memory in order flow.  ￼

⸻

Alpha Idea #18: Fragmentation/venue‑routing context → OFI impact filter

Source(s):
- Mishra (2021) — Routing decisions survey
- Holden (2011) — NBBO calculation pitfalls

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Venue fragmentation and NBBO construction choices affect perceived impact of OFI. Use a fragmentation index (Herfindahl of venue shares) and discount OFI signals in highly fragmented periods.  ￼

Feature Transformations:
- FragIdx = Σ (venue_share^2) rolling 1h
- OFI_eff = OFI × f(FragIdx)
- Filter when SIP dislocation risk is high (direct vs SIP)

Data Dependencies:
Venue‑tagged trades, NBBO, (optionally) direct vs SIP.

Universe & Filters:
Top 300 by multi‑venue activity.

Directionality / Construction Hints:
Scale positions down as fragmentation rises; prefer leaders.

Strength & Actionability:
Tentative – Useful filter; requires venue‑level data.

Keywords:
fragmentation, routing, NBBO, OFI

Expected Horizon Notes:
Backtest 2018–2025.

Citations:
- Survey and NBBO pitfalls.  ￼

⸻

Alpha Idea #19: Intermarket Sweep Order (ISO) “sweep” burst → short‑term continuation

Source(s):
- Nasdaq — Routing/ISO overview
- Nasdaq — “How trades speed between venues” (ISO hump explanation)

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Clusters of rapid, cross‑venue prints consistent with ISO/sweep behavior often produce short‑lived momentum. Detect multi‑venue prints within tight time buckets and trade continuation, gated by spread and depth.  ￼

Feature Transformations:
- SweepBurst = (#prints ≥ N across ≥ M venues within ≤ Δt_ms)
- BurstDisplacement = (last_print − preburst_mid)/tick
- Filter by spread <= 2*ticks

Data Dependencies:
Millisecond timestamped prints w/ venue tags; NBBO.

Universe & Filters:
Liquid S&P 100 names.

Directionality / Construction Hints:
Enter with BurstDisplacement sign; exit on fade or k ticks.

Strength & Actionability:
Promising – Mechanistically grounded; requires precise tape.

Keywords:
ISO, sweep, venues, momentum

Expected Horizon Notes:
Backtest 2019–2025 millisecond tape.

Citations:
- ISO concept and inter‑venue timing patterns.  ￼

⸻

Alpha Idea #20: Russell reconstitution day — closing auction flow tilt in adds/deletes

Source(s):
- BMLL — U.S. closing auction dynamics and Russell reconstitution (Jun 24, 2025)

Verification Status: Verified (direct link)
Equity Class: US Small-Cap
Horizon: Intraday (<1h) & 1–3 Days
Signal Type: Event-Driven / Microstructure

Core Idea:
On Russell reconstitution, adds/deletes experience large closing auction imbalances and price dislocations. Trade into‑close direction with auction data and consider short‑term reversal next day on extreme slippage.  ￼

Feature Transformations:
- ReconstFlag (membership change)
- ImbZ at 3:50 and 3:59:50
- Slip2m and next‑day reversal

Data Dependencies:
Auction imbalance feed, index membership lists, auction prints.

Universe & Filters:
Russell 2000 candidates.

Directionality / Construction Hints:
Into‑close directional; overnight partial fade of extremes.

Strength & Actionability:
Strong – Well‑known flow event with clear mechanics and data.

Keywords:
reconstitution, MOC, imbalance, small-cap

Expected Horizon Notes:
Backtest 2018–2025 (June events).

Citations:
- Closing auction behavior around Russell rebalance.  ￼

⸻

Notes on Deduplication
- Auction‑based ideas differentiate by which auction (open vs close, LULD reopen) and by feature focus (flag presence vs acceleration vs internalization vs slippage).
- OFI/microprice/queue‑imbalance concepts are kept distinct by horizon and construction (one‑tick vs few minutes, integrated multi‑level OFI vs L1 queue, cross‑impact overlay).
- Filters (QTR, fragmentation) are separated as meta‑ideas that alter signal quality rather than redefine the same feature set.

⸻

JSON Export Schema (append after the markdown sections)

{
  "meta": {
    "source_searched": "Twitter/X (selected threads via Thread Reader) + supporting public docs",
    "query": "equity alpha",
    "scan_window": "2017-01-01 - 2025-12-31",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "3:50 “Significant Imbalance” → drift into the NYSE close",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "NYSE publishes a Significant Imbalance flag at 3:50:00 PM. A positive (buy) flag and large normalized imbalance tend to coincide with into-close drift and larger auction slippage; trade the direction, scaled by normalized imbalance and internalization.",
      "feature_transformations": [
        "SignificantImbFlag_350 ∈ {0,1}",
        "ImbZ = ImbalanceShares / avg20dAuctionVol",
        "Slippage2m = CloseAuctionPrice − VWAP[3:58–4:00]",
        "Drift = Price[4:00] − Price[3:50]",
        "Interaction: ImbZ × HighInternalization"
      ],
      "data_dependencies": [
        "NYSE Closing Imbalance feed or BMLL auction imbalance",
        "NBBO/TAQ",
        "TRF share near close"
      ],
      "universe_filters": "US Large‑Cap; price > $5; ADV > $10M; primary NYSE; exclude halts",
      "directionality": "Follow sign of flag; beta/sector neutral; exit at auction",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Exchange-documented flag; clear timestamps; highly liquid."
      },
      "keywords": ["order-flow", "MOC", "auction", "imbalance", "slippage", "intraday"],
      "expected_horizon_notes": "Backtest 2023–2025 intraday; live monitor 6–8 weeks.",
      "citations": [
        "https://www.nyse.com/data-insights/the-nyse-significant-imbalance-enhanced-trading-opportunities-at-the-nyse-closing-auction",
        "https://www.bmlltech.com/news/market-insight/into-the-close-unpacking-u-s-closing-auction-dynamics-and-the-impact-of-the-russell-reconstitution"
      ]
    },
    {
      "title": "Imbalance acceleration 3:50→3:55 (D‑quotes) predicts last‑minute move",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Imbalance updates accelerate post‑3:50 as D‑Orders interact; the slope/acceleration of imbalance between 3:50 and ~3:55 predicts final minutes’ price path.",
      "feature_transformations": [
        "dImb/dt over [3:50, 3:55] and [3:55, 3:59:50]",
        "Accel = (dImb/dt)_late − (dImb/dt)_early",
        "ImbConv normalized by avg20dAuctionVol",
        "ΔMid = Mid[4:00] − Mid[3:50]"
      ],
      "data_dependencies": ["Closing imbalance feed", "NBBO mid", "Trades"],
      "universe_filters": "NYSE‑listed >$5; ADV > $5M; exclude earnings days",
      "directionality": "Trade sign(Accel); exit on auction",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Mechanism and timing well-documented; requires feed access."
      },
      "keywords": ["order-flow", "D-quotes", "acceleration", "closing", "imbalance"],
      "expected_horizon_notes": "Backtest 2019–2025; forward 1–2 rebalance cycles.",
      "citations": [
        "https://databento.com/blog/how-nyse-closing-imbalance-feed-moves-markets",
        "https://www.nyse.com/auctions"
      ]
    },
    {
      "title": "Highly internalized names → larger into‑close drift and slippage",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "Intraday (1-6h), Overnight",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Stocks with high TRF share near the close show more drift and auction slippage; tilt closing trades by internalization and optionally fade the slippage overnight.",
      "feature_transformations": [
        "TRF15 = TRFVol[3:45–4:00]/(AuctionVol + TRFVol[3:45–4:00])",
        "Sign(Imbalance) × TRF15",
        "Slip2m vs 2‑minute VWAP"
      ],
      "data_dependencies": ["Imbalance feed", "TRF prints", "Auction print", "NBBO"],
      "universe_filters": "S&P1500; exclude ADRs",
      "directionality": "Scale closing direction by TRF15 decile; optional overnight fade of extremes",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Exchange study; transparent computation; liquid names."
      },
      "keywords": ["internalization", "MOC", "imbalance", "slippage", "TRF"],
      "expected_horizon_notes": "Backtest 2022–2025.",
      "citations": [
        "https://www.nyse.com/data-insights/closing-auction-internalization-effect-throughout-imbalance-period"
      ]
    },
    {
      "title": "Opening auction imbalance sign predicts first 5–15 minutes",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Opening imbalance (8:30–9:35 cadence) indicates immediate demand/supply skew; normalized imbalance sign predicts initial post‑open direction.",
      "feature_transformations": [
        "OpenImbZ = Imb/avg20dOpenAuctionVol",
        "GapAdj = (OpenPrice − pre‑market VWAP)",
        "Spread/tick and volatility filters"
      ],
      "data_dependencies": ["Opening imbalance feed", "Auction print", "Pre‑market trades"],
      "universe_filters": "NYSE/Arca; price > $5; ADV > $5M",
      "directionality": "Directional 5–15 min scalp; fade if large gap into imbalance",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear timestamps; liquid opening prints."
      },
      "keywords": ["opening", "imbalance", "gap", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2025.",
      "citations": [
        "https://www.nyse.com/auctions",
        "https://www.nyse.com/publicdocs/nyse/data/TAQ_NYSE_Order_Imbalance_QRC.pdf",
        "https://www.nyse.com/markets/nyse-arca/trading-info"
      ]
    },
    {
      "title": "Nasdaq NOIS snapshots → pre‑close drift predictor",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "NOIS net imbalance snapshots predict into‑close drift and final cross price; use normalized level and last‑10‑minute change.",
      "feature_transformations": [
        "NOIS_Z = NOIS/avg20dCloseAuctionVol",
        "NOIS_d = NOIS[t] − NOIS[t−Δ]",
        "DriftClose = Price[4:00] − Price[3:50]"
      ],
      "data_dependencies": ["Nasdaq NOIS", "NBBO/trades"],
      "universe_filters": "Nasdaq‑listed >$5, ADV >$10M",
      "directionality": "Trade sign(NOIS_Z); exit at cross",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Well‑specified feed; consistent cadence."
      },
      "keywords": ["NOIS", "imbalance", "Nasdaq", "closing"],
      "expected_horizon_notes": "Backtest 2017–2025.",
      "citations": [
        "https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NOIS_v2.2.pdf"
      ]
    },
    {
      "title": "Index‑level MOC notional imbalance → SPY/QQQ/DIA into‑close tilt",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (SPY/QQQ/DIA)",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Event-Driven",
      "core_idea": "Aggregated index MOC imbalances force ETF/futures hedges; trade index ETFs into the close using normalized notional imbalance.",
      "feature_transformations": [
        "MOC_Index = Σ(Imb_i × weight_i)",
        "MOC_Index_Z via 60‑day z‑score",
        "ΔIndexFutBasis risk check"
      ],
      "data_dependencies": ["Vendor/desk broadcasts", "Component imbalances", "ETF trades"],
      "universe_filters": "SPY, QQQ, DIA",
      "directionality": "Directional tilt; exit at 4:00",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Public broadcasts common; ETFs highly liquid."
      },
      "keywords": ["MOC", "ETF", "imbalance", "hedging"],
      "expected_horizon_notes": "Backtest 2020–2025.",
      "citations": [
        "https://twitter.com/financialjuice/status/1737554508575185293",
        "https://tradersmastermind.com/moc-order-flow/"
      ]
    },
    {
      "title": "Auction slippage mean‑reverts overnight",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Overnight",
      "signal_type": "Mean-Reversion",
      "core_idea": "Extreme closing auction slippage vs late VWAP often reverts by next open; run cross‑sectional overnight reversal keyed to |Slip2m|.",
      "feature_transformations": [
        "Slip2m deciles",
        "Sector/size neutralization",
        "Exclude earnings"
      ],
      "data_dependencies": ["Auction print", "2‑min VWAP", "Next open"],
      "universe_filters": "S&P1500; price > $5",
      "directionality": "Long negative slippage, short positive; exit at open",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Mechanism linked to well‑documented internalization effects."
      },
      "keywords": ["auction", "slippage", "mean-reversion", "overnight"],
      "expected_horizon_notes": "Backtest 2018–2025.",
      "citations": [
        "https://www.nyse.com/data-insights/closing-auction-internalization-effect-throughout-imbalance-period"
      ]
    },
    {
      "title": "Integrated multi‑level OFI → short‑horizon price impact",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Compute multi‑level OFI and regress to short‑horizon returns, with inverse‑depth scaling and optional sector cross‑impact.",
      "feature_transformations": [
        "OFI_L1..Lk; OFI_Int = Σ w_l OFI_Ll",
        "DepthInv = 1/Depth_L1",
        "Sector cross‑impact term"
      ],
      "data_dependencies": ["L2/L3 depth", "NBBO", "Trades"],
      "universe_filters": "Top 500 by ADV",
      "directionality": "Thresholded linear predictor; 5–10 min holds",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Extensive literature; robust transforms."
      },
      "keywords": ["OFI", "depth", "microstructure", "cross-impact"],
      "expected_horizon_notes": "Backtest 2017–2025 tick/L2.",
      "citations": [
        "https://arxiv.org/abs/1011.6402",
        "https://ora.ox.ac.uk/objects/uuid%3A9b7d0422-4ef1-48e7-a2d4-4eaa8a0a7ec1/files/m89dedb16194e627a2c92d14e3329bd48",
        "https://arxiv.org/abs/2112.13213"
      ]
    },
    {
      "title": "Queue imbalance / microprice → one‑tick‑ahead predictor",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Use microprice and best‑level queue imbalance to predict the next tick direction; trade sign(ΔMicro).",
      "feature_transformations": [
        "I = Qb/(Qb+Qa)",
        "Micro = I*Ask + (1−I)*Bid",
        "ΔMicro = Micro − Mid"
      ],
      "data_dependencies": ["L1 sizes/prices", "Trades"],
      "universe_filters": "Large‑tick mega‑caps",
      "directionality": "Enter with sign(ΔMicro); exit on quote update",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Simple and reproducible using L1."
      },
      "keywords": ["microprice", "queue-imbalance", "NBBO", "one-tick"],
      "expected_horizon_notes": "Backtest 2019–2025.",
      "citations": [
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2970694",
        "https://arxiv.org/pdf/1512.03492",
        "https://twitter.com/sashastoikov/status/1271072142063525889"
      ]
    },
    {
      "title": "NBBO rotation spike → short‑term “attention” momentum",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Event-Driven",
      "core_idea": "NBBO update bursts (rotation) cluster at information arrival; a high rotation z‑score combined with OFI predicts near‑term moves.",
      "feature_transformations": [
        "Rot = #NBBO_changes[Δt]; RotZ = zscore_by_timeofday(Rot)",
        "Interaction: RotZ × sign(OFI_L1)"
      ],
      "data_dependencies": ["NBBO", "Trades"],
      "universe_filters": "Mega‑caps, news‑sensitive names",
      "directionality": "Trigger when RotZ>2; hold 5–30 min",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Requires careful debiasing for feed artifacts."
      },
      "keywords": ["NBBO", "rotation", "attention", "OFI"],
      "expected_horizon_notes": "Backtest 2021–2025.",
      "citations": [
        "https://primer.prooftrading.com/assets/pdf/section_05_market-activity.pdf"
      ]
    },
    {
      "title": "Quote‑to‑trade ratio (QTR) filter → higher quality OFI signals",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Use 60s QTR to gate OFI entries; low QTR implies more informative trading activity.",
      "feature_transformations": [
        "QTR60 = NBBO_changes_60s / Trades_60s",
        "Trade OFI only if QTR60 < percentile threshold"
      ],
      "data_dependencies": ["NBBO changes", "Trades"],
      "universe_filters": "Top 100 by ADV",
      "directionality": "As in OFI, filtered by QTR",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Simple SNR filter supported by literature context."
      },
      "keywords": ["QTR", "NBBO", "OFI", "filter"],
      "expected_horizon_notes": "Backtest 2019–2025.",
      "citations": [
        "https://www.sciencedirect.com/science/article/pii/S0304405X25000947"
      ]
    },
    {
      "title": "Odd‑lot dominance ratio → next‑day mean‑reversion tilt",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Overnight",
      "signal_type": "Microstructure/Mean-Reversion",
      "core_idea": "Odd‑lot share late‑day proxies for internalized/retail conditions; extremes mean‑revert by next open.",
      "feature_transformations": [
        "OddShare = OddLotVol / TotalVol (late day)",
        "Interact with Slip2m deciles"
      ],
      "data_dependencies": ["Odd‑lot trade flags", "Auction print"],
      "universe_filters": "S&P 500/400; exclude <$5",
      "directionality": "Cross‑sectional LR/short overlay; exit at open",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Data availability varies; concept supported by execution quality studies."
      },
      "keywords": ["odd-lots", "internalization", "NBBO", "reversion"],
      "expected_horizon_notes": "Backtest 2020–2025.",
      "citations": [
        "https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13467"
      ]
    },
    {
      "title": "Iceberg detection via replenishment patterns → follow hidden interest",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Detect repeated partial fills with immediate depth refresh as iceberg proxies; trade with iceberg bias and microprice.",
      "feature_transformations": [
        "IcebergHits/min and IcebergBias",
        "ΔMicro as directional confirmation"
      ],
      "data_dependencies": ["L3/order messages", "L2 depth", "Trades"],
      "universe_filters": "Top 200 by L2 message rate",
      "directionality": "Trade with IcebergBias; exit on depth depletion",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Needs granular feeds; conceptually strong."
      },
      "keywords": ["iceberg", "hidden-liquidity", "replenishment", "microprice"],
      "expected_horizon_notes": "Backtest 2021–2025.",
      "citations": [
        "https://www.exegy.com/ml-copycat-investors-alpha-clones-part-1/",
        "https://quant.stackexchange.com/questions/64356/determine-market-and-ice-berg-order-types-from-live-trade-and-quote-data"
      ]
    },
    {
      "title": "Sector cross‑impact — leader OFI spills into peers",
      "verification_status": "Verified (direct link)",
      "equity_class": "Sector-Specific (specify)",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Leader OFI propagates to peers via cross‑impact; trade peer baskets on leader OFI with short holding windows.",
      "feature_transformations": [
        "LeaderOFI_Int",
        "Peer regression vs leader OFI",
        "Sector ETF control"
      ],
      "data_dependencies": ["L2 depth", "Trades", "Sector taxonomy"],
      "universe_filters": "Semis, mega‑cap tech, financials; liquid peers only",
      "directionality": "Cross‑sectional long/short; hedge to ETF",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Documented cross‑impact; scalable cross‑sectionally."
      },
      "keywords": ["cross-impact", "sector", "OFI"],
      "expected_horizon_notes": "Backtest 2019–2025.",
      "citations": [
        "https://arxiv.org/abs/2112.13213"
      ]
    },
    {
      "title": "LULD reopen auction imbalance → first 5–15 minute follow‑through",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Event-Driven",
      "core_idea": "Use signed reopen imbalance and collar width to predict post‑reopen direction.",
      "feature_transformations": [
        "ReopenImbZ vs history",
        "CollarW as volatility proxy"
      ],
      "data_dependencies": ["Reopen auction feed", "NBBO/trades"],
      "universe_filters": "Mid‑caps prone to LULD",
      "directionality": "Directional scalp; tight risk",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Published mechanisms and rule changes."
      },
      "keywords": ["LULD", "reopen", "auction", "imbalance"],
      "expected_horizon_notes": "Backtest 2020–2025.",
      "citations": [
        "https://www.nasdaq.com/articles/all-about-lulds",
        "https://www.sec.gov/files/rules/sro/nasdaq/2024/34-101620.pdf"
      ]
    },
    {
      "title": "Stacked footprint imbalances across levels → reversal zones",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Detect stacked (multi‑level) aggressive imbalances and fade when absorption appears.",
      "feature_transformations": [
        "StackLen (levels with imbalance>k)",
        "Absorb: rising passive volume against aggression"
      ],
      "data_dependencies": ["L2/L3 footprint", "Trades"],
      "universe_filters": "High‑ADV names; exclude news",
      "directionality": "Fade stacks with absorption; tight stops",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Popular concept; codifiable with clear rules."
      },
      "keywords": ["footprint", "stacked-imbalance", "absorption"],
      "expected_horizon_notes": "Backtest 2022–2025.",
      "citations": [
        "https://www.marketcalls.in/orderflow/using-stacked-imbalances-to-identify-key-market-reversals-orderflow-tutorial.html"
      ]
    },
    {
      "title": "Long‑memory in order‑flow signs → intraday momentum overlay",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Exploit persistent sign autocorrelation from metaorder splitting to gate/enhance OFI entries.",
      "feature_transformations": [
        "SignImb (volume‑weighted signed trades)",
        "Hurst‑based regime filter"
      ],
      "data_dependencies": ["Trades with aggressor side", "NBBO"],
      "universe_filters": "Top 500 by prints/day",
      "directionality": "Overlay on OFI; trade only in persistent regimes",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Empirical support; simple to compute."
      },
      "keywords": ["long-memory", "order-splitting", "momentum"],
      "expected_horizon_notes": "Backtest 2019–2025.",
      "citations": [
        "https://arxiv.org/abs/2301.13505"
      ]
    },
    {
      "title": "Fragmentation/venue‑routing context → OFI impact filter",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Compute a fragmentation index (venue Herfindahl) and down‑weight OFI in highly fragmented conditions.",
      "feature_transformations": [
        "FragIdx = Σ venue_share^2 (rolling)",
        "OFI_eff = OFI × f(FragIdx)"
      ],
      "data_dependencies": ["Venue‑tagged trades", "NBBO"],
      "universe_filters": "Top 300 by venue count",
      "directionality": "Scale down as fragmentation rises",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Filtering concept supported by routing literature."
      },
      "keywords": ["fragmentation", "routing", "NBBO", "OFI"],
      "expected_horizon_notes": "Backtest 2018–2025.",
      "citations": [
        "https://www.mdpi.com/1911-8074/14/11/556",
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1911491"
      ]
    },
    {
      "title": "Intermarket Sweep Order (ISO) bursts → short‑term continuation",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Detect rapid, multi‑venue print clusters consistent with ISO sweeps and trade continuation with spread/depth checks.",
      "feature_transformations": [
        "SweepBurst (#prints≥N across≥M venues within ≤Δt_ms)",
        "BurstDisplacement (ticks from mid)"
      ],
      "data_dependencies": ["Millisecond prints with venue tags", "NBBO"],
      "universe_filters": "S&P 100",
      "directionality": "Enter with displacement sign; quick exits",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Mechanistically grounded; requires precise tape."
      },
      "keywords": ["ISO", "sweep", "venues", "momentum"],
      "expected_horizon_notes": "Backtest 2019–2025.",
      "citations": [
        "https://www.nasdaqtrader.com/trader.aspx?id=routing",
        "https://www.nasdaq.com/articles/how-trades-speed-between-venues"
      ]
    },
    {
      "title": "Russell reconstitution day — closing auction tilt",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "Intraday (<1h), 1-3 Days",
      "signal_type": "Event-Driven",
      "core_idea": "Adds/deletes show large closing imbalances and slippage; trade into‑close direction and partial next‑day reversal on extremes.",
      "feature_transformations": [
        "ReconstFlag (index changes)",
        "ImbZ at 3:50, 3:59:50",
        "Slip2m and follow‑through"
      ],
      "data_dependencies": ["Auction imbalance", "Index membership files", "Auction print"],
      "universe_filters": "Russell 2000 candidates",
      "directionality": "Into‑close tilt; next‑day partial fade",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Well‑known flow event; rich public data."
      },
      "keywords": ["reconstitution", "MOC", "imbalance", "small-cap"],
      "expected_horizon_notes": "Backtest 2018–2025 (June).",
      "citations": [
        "https://www.bmlltech.com/news/market-insight/into-the-close-unpacking-u-s-closing-auction-dynamics-and-the-impact-of-the-russell-reconstitution"
      ]
    }
  ]
}