20251024 Kaggle Optiver Deep Dive

Alpha Discovery Report (Equities Only)
Model Run
- Model: GPT-5 Pro
- Reasoning Time: 12m20s


Instructions (Follow Exactly)
- Task: Search the specified source for publicly shared, actionable equity alphas and feature transformations (no crypto). Extract ideas that include concrete, testable features.
- Scope: Equities only (single-name stocks and equity ETFs). Exclude crypto, digital assets, FX-only, and pure futures-only content.
- Deliverable: Produce up to 100 distinct ideas using the exact schema below, in order, one after another. Use concise, technical prose.
- Sources: Provide direct links for each idea (tweet, notebook, paper, repo). If multiple posts in a thread support the same idea, include all links.
- Style: No emojis. No questions. No disclaimers. No performance estimates (Sharpe, t-stat, returns). No code unless quoted from a cited source.
- Deduplication: Merge near-duplicates; keep the most complete citation set.
- Assessment: Provide a qualitative “Strength & Actionability” judgment (e.g., Strong / Promising / Tentative) with a one-line rationale.
- Keywords: Add a concise, comma-separated tag list for each idea (e.g., order-flow, intraday, imbalance).
- Expected Horizon Notes: Mention how far back to backtest / monitor (e.g., 3y historical intraday data, rolling live for 6 weeks).
- Output Format: After the markdown sections, append a fenced json block containing the structured payload described under JSON Export Schema.

⸻

Report Meta
- Source Searched: Kaggle Optiver competitions (Optiver Realized Volatility Prediction; Optiver – Trading at the Close), plus linked GitHub/Medium/X writeups
- Query / Filters: Optiver competition equities order book alpha feature engineering
- Scan Window: 2015-01-01 - 2025-10-24
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: Market Urgency (Spread × Liquidity Imbalance)

Source(s):
- liyiyan128/optiver-trading-at-the-close – feature notes + formulae (2024)  ￼
- Kaggle discussion highlights (market_urgency, imb* family) (2023–2024)  ￼
- Intro to TATC auction fields (near/far, imbalance, reference price) (2023)  ￼

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Closing-auction pressure is captured by the interaction of spread and liquidity imbalance. Define liquidity imbalance = (bid_size − ask_size)/(bid_size + ask_size). The market_urgency feature = spread × liquidity imbalance proxies the instantaneous price pressure toward the cross, predicting sign and magnitude of the next-minute reference price move into the close.  ￼

Feature Transformations (bullet list):
- LiquidityImbalance = (bid_size − ask_size)/(bid_size + ask_size)
- MarketUrgency = (ask_price − bid_price) × LiquidityImbalance
- Rolling z-score of MarketUrgency over last 20–60s per stock (groupby stock_id, seconds_in_bucket)

Data Dependencies (concise list):
Auction NOII-like fields: bid/ask price & size, reference price, seconds_in_bucket.  ￼

Universe & Filters:
US Large-Cap; price > $5; ADV > $10M; primary-listing on Nasdaq.

Directionality / Construction Hints:
Rank long the top decile of MarketUrgency; short bottom decile; beta-neutral vs synthetic index; hold to the cross or 30–60s after cross for exit.

Strength & Actionability (qualitative only):
Strong – widely shared by top kernels; simple to compute from standard auction feeds; clear mechanism.  ￼

Keywords (comma-separated):
order-flow, imbalance, auction, microstructure, intraday

Expected Horizon Notes:
Backtest 2023–2025 TATC-like intraday auction snapshots; live monitor 6–8 weeks around close.

Citations:
- Market-urgency definitions and examples.  ￼
- Public discussions referencing imb* / urgency families.  ￼
- TATC intro explaining imbalance/near/far/reference price.  ￼

⸻

Alpha Idea #2: Mid–Microprice Divergence (microprice “pull”)

Source(s):
- liyiyan128/optiver-trading-at-the-close – market_urgency_v2 (mid − microprice) (2024)  ￼
- Microprice definition / intuition (Quant.SE) (2020)  ￼

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
The microprice (size-weighted mid) indicates which side is more likely to be hit next. The gap Mid − Microprice forecasts the one-minute drift in the reference price: if microprice > mid, expect uptick pressure and vice versa.  ￼

Feature Transformations (bullet list):
- Microprice = (ask_price×bid_size + bid_price×ask_size)/(bid_size + ask_size)
- Divergence = ((ask_price + bid_price)/2) − Microprice
- EWM( Divergence, span=10s ) and sign(ΔDivergence)

Data Dependencies (concise list):
Best bid/ask price & size; seconds_in_bucket.

Universe & Filters:
US Large-/Mid-Cap; exclude halted names.

Directionality / Construction Hints:
Cross-sectional rank by Divergence; long negative Divergence (microprice above mid), short positive; sector/beta-neutral; exit at cross.

Strength & Actionability:
Strong – classic LOB predictor; explicitly codified in shared repos.  ￼

Keywords:
microprice, imbalance, auction, intraday

Expected Horizon Notes:
Backtest 2019–2025 where NOII-equivalent exists; live A/B 4–6 weeks.

Citations:
- Repo with market_urgency_v2 definition.  ￼
- Microprice rationale.  ￼

⸻

Alpha Idea #3: Doublet / Triplet Imbalance Ratios

Source(s):
- liyiyan128/optiver-trading-at-the-close – doublet & triplet imbalance definitions (2024)  ￼
- Kaggle threads mentioning imb1, imb2, and imbalance families (2023)  ￼

Verification Status: Verified (direct link)
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Pairwise and triplet ratios compress price/size fields into directional “pressure” scalars. They decorrelate raw fields and improved leaderboard scores across multiple public writeups.  ￼

Feature Transformations:
- Doublet: (x − y)/(x + y) for {x,y} in {bid_size, ask_size, near_px, far_px, reference_px}
- Triplet: (max − mid)/(mid − min) row-wise across {near, far, reference}
- Rolling mean, Δ, and Δ² of these ratios over 10–60s

Data Dependencies:
Auction book (near/far/reference), sizes, counts.  ￼

Universe & Filters:
US Large-/Mid; ADV > $5M.

Directionality / Construction Hints:
Rank by sign and magnitude; ensemble multiple ratios; industry/beta-neutral.

Strength & Actionability:
Strong – heavily reused public feature family; easy to port.  ￼

Keywords:
imbalance, ratios, auction, intraday

Expected Horizon Notes:
Backtest 2023–2025; live shadow-trade 1 month.

Citations:
- Doublet/triplet notes and interpretation.  ￼
- imb1/imb2 mentions.  ￼

⸻

Alpha Idea #4: Imbalance Momentum (d/dt of Imbalance vs Matched)

Source(s):
- “Imbalance Momentum” and related features listed by participants (2024)  ￼

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Momentum, Microstructure/Order-Flow

Core Idea:
First and second differences of auction imbalance, scaled by matched size, capture accelerations in order arrival and predict the next 30–60s change in reference price.  ￼

Feature Transformations:
- ImbMomentum = Δ(imbalance) / max(matched_size, ε)
- ImbAccel = Δ²(imbalance) / matched_size
- EWM( ImbMomentum, span=15s )

Data Dependencies:
imbalance, matched_size, reference price.  ￼

Universe & Filters:
US Large-/Mid-Cap; exclude thinly traded auction names.

Directionality / Construction Hints:
Go with the sign of ImbMomentum; truncate when spread widens unexpectedly; exit at cross.

Strength & Actionability:
Promising – repeatedly cited; robust mechanism; must tune scaling by stock liquidity.  ￼

Keywords:
imbalance, momentum, auction

Expected Horizon Notes:
Backtest two auction seasons (2023–2024); live 6 weeks.

Citations:
- Feature lists including “Imbalance Momentum.”  ￼

⸻

Alpha Idea #5: Depth Pressure using Near/Far Differentials

Source(s):
- Participant lists: Depth Pressure, Spread-Depth Ratio (2024)  ￼
- Imbalance-focused kernels and threads (2023–2024)  ￼

Verification Status: Partially Verified (secondary references)
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Combine side depth and the gap between far and near indicative prices to estimate cross-direction pressure. When buy depth exceeds sell depth and far > near, the indicative clearing price skews upward, forecasting a positive next-minute move.  ￼

Feature Transformations:
- DepthDiff = bid_size − ask_size
- NearFarSkew = far_price − near_price
- DepthPressure = DepthDiff × NearFarSkew; z-score by stock

Data Dependencies:
near_price, far_price, bid/ask sizes.  ￼

Universe & Filters:
US Large-/Mid; price > $5.

Directionality / Construction Hints:
Rank by DepthPressure; neutralize sector; stop if spread widens > 2× median.

Strength & Actionability:
Promising – clear intuition; needs venue/stock-specific tuning.  ￼

Keywords:
near-far, depth, auction

Expected Horizon Notes:
Backtest 2023–2025; online monitor for 1 month.

Citations:
- Depth/Spread-depth examples.  ￼
- Near/Far definitions and usage context.  ￼

⸻

Alpha Idea #6: Matched vs. Unmatched Flow Ratio

Source(s):
- TATC dataset description (NOII-like fields) (2023)  ￼
- Introductory notebook (auction mechanics) (2023)  ￼

Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
The ratio paired_shares / (paired_shares + imbalance_shares) measures how close the auction is to clearing at the current indicated price; a rising ratio predicts convergence of reference price toward near/far with the sign guided by net imbalance.  ￼

Feature Transformations:
- PairingRate = paired/(paired + |imb|)
- ΔPairingRate, and ΔPairingRate × sign(imbalance)
- Time-weighted average over 10–30s

Data Dependencies:
paired_shares, imbalance_shares, near/far/reference.  ￼

Universe & Filters:
US Large-Cap; ADV > $15M.

Directionality / Construction Hints:
Trade in the sign of imbalance when PairingRate accelerates; cap risk by spread.

Strength & Actionability:
Promising – simple and robust across names with active auctions.

Keywords:
auction, paired, imbalance

Expected Horizon Notes:
Backtest 2y TATC-like; live 4 weeks.

Citations:
- Dataset fields and definitions.  ￼
- Auction mechanics/context.  ￼

⸻

Alpha Idea #7: Reference-Price Slope vs. Imbalance Divergence

Source(s):
- UT Austin Medium writeup (competition overview & feature intuition) (2023)  ￼
- TATC dataset context (2023)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Momentum

Core Idea:
When the reference price drifts against the change in imbalance (e.g., reference up while imbalance turns net sell), subsequent re-alignment often occurs within the next minute. Use the sign disagreement as an entry filter.  ￼

Feature Transformations:
- RefSlope = Δ(reference_price)
- ImbSlope = Δ(imbalance) normalized by depth
- DivergenceSignal = −sign(RefSlope × ImbSlope)

Data Dependencies:
reference_price, imbalance, sizes.

Universe & Filters:
US Large-/Mid-Cap; exclude extreme spread events.

Directionality / Construction Hints:
Enter with DivergenceSignal; exit on sign agreement or at cross.

Strength & Actionability:
Tentative – intuitive; requires careful slippage modeling.

Keywords:
auction, divergence, momentum

Expected Horizon Notes:
Backtest 2023–2025; paper trade 1 month.

Citations:
- Overview and rationale.  ￼
- Data fields.  ￼

⸻

Alpha Idea #8: Synthetic Index Residual (β-neutral auction drift)

Source(s):
- Synthetic index weights & features (repo notes) (2024)  ￼
- Feature lists including “Weighted WAP / Index Ratio” (2024)  ￼

Verification Status: Verified
Equity Class: Equity ETFs (QQQ) + Constituents; Sector-Specific (Tech)
Horizon: Intraday (<1h)
Signal Type: Cross-Sectional Composite

Core Idea:
Reconstruct synthetic index weights via regression and form residual reference price per stock vs index. Residual momentum and residual imbalance pressure predict relative moves into the cross, supporting pairs vs. index baskets.  ￼

Feature Transformations:
- β_i from rolling intraday regressions vs synthetic index
- ResidRef = ΔRef_i − β_i ΔRef_index
- ResidImb = Imb_i − β_i Imb_index; rank ResidRef × sign(ResidImb)

Data Dependencies:
reference_price, imbalance; index proxy (synthetic/index-constructed).  ￼

Universe & Filters:
Nasdaq 100 constituents; ETFs: QQQ.

Directionality / Construction Hints:
Long residual winners with positive ResidImb; short residual losers; market-neutral.

Strength & Actionability:
Strong – well-documented in community repos; straightforward basket construction.  ￼

Keywords:
index, residual, pairs, auction

Expected Horizon Notes:
Backtest 2023–2025; live 6 weeks.

Citations:
- Synthetic index reconstruction + features.  ￼
- Weighted WAP/index feature mentions.  ￼

⸻

Alpha Idea #9: Sector-Time Grouped Context Features

Source(s):
- Participant summary: grouped features by sector and time instant (2024)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Cross-Sectional Composite

Core Idea:
Sector-level aggregates of imbalance and reference price movement enhance signal stability by removing idiosyncratic noise. Normalize stock features by concurrent sector averages.  ￼

Feature Transformations:
- SectorImbZ = (Imb_i − mean_sector_imb)/std_sector_imb
- SectorRelRef = ΔRef_i − mean_sector_ΔRef
- Feature ratios to sector medians

Data Dependencies:
auction features + sector mapping.

Universe & Filters:
US Large-/Mid-Cap in GICS sectors.

Directionality / Construction Hints:
Rank by sector-relative signals; sector-neutral portfolio.

Strength & Actionability:
Promising – repeatedly cited by participants; low complexity.  ￼

Keywords:
sector, normalization, auction

Expected Horizon Notes:
Backtest 2y; live 1 month.

Citations:
- Sector/time grouping mention.  ￼

⸻

Alpha Idea #10: Time-to-Cross Urgency (seconds remaining)

Source(s):
- NOII description (update cadence, fields) (investopedia) (n/a)  ￼
- Optiver competition page/blog context (2023)  ￼

Verification Status: Partially Verified
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Auction update frequency and informational granularity intensify closer to the cross. Weight pressure features by a convex function of time_remaining (e.g., 1/√t) to emphasize late-arriving, higher-impact signals.  ￼

Feature Transformations:
- UrgencyWeight = 1/√(seconds_to_close + 1)
- WeightedImb = Imbalance × UrgencyWeight
- LateSurge = ΔImbalance over last 20s × UrgencyWeight

Data Dependencies:
imbalance, seconds_in_bucket / time remaining.

Universe & Filters:
US Large-/Mid-Cap; active NOII.

Directionality / Construction Hints:
Use weighted ranks; cap exposure in final 5s.

Strength & Actionability:
Promising – aligns with NOII microstructure; simple to add.  ￼

Keywords:
NOII, timing, auction

Expected Horizon Notes:
Backtest 2023–2025; live 4 weeks.

Citations:
- NOII cadence/fields.  ￼
- Competition context.  ￼

⸻

Alpha Idea #11: Spread–Depth Ratio

Source(s):
- Participant lists include “Spread Depth Ratio” among useful features (2024)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Mean-Reversion, Microstructure

Core Idea:
Very wide spreads relative to depth often revert as liquidity providers step in before the cross; extremely tight spreads with thin depth can flip quickly. Normalize spread by total top-of-book depth.  ￼

Feature Transformations:
- SDR = (ask − bid)/(bid_size + ask_size)
- SDR z-score and ΔSDR over 10–30s
- Interaction: SDR × sign(imbalance)

Data Dependencies:
Top-of-book spread and sizes.

Universe & Filters:
US Large-/Mid-Cap.

Directionality / Construction Hints:
Lean against extreme SDR tails; exit on normalization.

Strength & Actionability:
Tentative – requires careful liquidity filters; mixed views in discussions.  ￼

Keywords:
spread, depth, mean-revert

Expected Horizon Notes:
Backtest 2y; live 1 month.

Citations:
- Feature family mention.  ￼

⸻

Alpha Idea #12: Far–Near Asymmetry Trigger

Source(s):
- Auction walkthrough (near vs far, unmatched shares) (2023)  ￼

Verification Status: Verified
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Event-Driven

Core Idea:
A widening far − near spread flags tension about the clearing price; sharp changes in this differential predict next update direction. Combine with imbalance sign.  ￼

Feature Transformations:
- FNDelta = far − near
- ΔFNDelta and sign(ΔFNDelta) × sign(imb)
- Volatility-adjusted FNDelta (divide by recent ref-price std)

Data Dependencies:
near, far, imbalance, reference.

Universe & Filters:
US Large-Cap; Nasdaq listings.

Directionality / Construction Hints:
Follow sign of FNDelta acceleration; stop on spread blowout.

Strength & Actionability:
Promising – direct from auction fields; low compute.  ￼

Keywords:
near, far, event, auction

Expected Horizon Notes:
Backtest 2023–2025; live 4 weeks.

Citations:
- Near/far mechanics.  ￼

⸻

Alpha Idea #13: Matched-Size Slope (Fill Momentum)

Source(s):
- UT Austin Medium (notes on predictive gaps/time ahead) (2023)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Momentum

Core Idea:
Rising matched size per second (derivative of paired_shares) indicates increasing certainty of the clearing price and tends to align with subsequent reference-price increments in the direction of net imbalance.  ￼

Feature Transformations:
- FillSlope = Δ(paired_shares)/Δt
- FillAccel = Δ²(paired_shares)
- FillSlope × sign(imbalance)

Data Dependencies:
paired_shares, imbalance.

Universe & Filters:
US Large-/Mid-Cap; active auctions.

Directionality / Construction Hints:
Trade with FillSlope × sign(imbalance); exit at cross.

Strength & Actionability:
Tentative – needs stable paired_shares estimates.

Keywords:
paired, slope, momentum

Expected Horizon Notes:
Backtest 2y; live 1 month.

Citations:
- Competition timing and feature challenges.  ￼

⸻

Alpha Idea #14: Cross-Day z-Score of Market Urgency

Source(s):
- Thread referencing cross-day indicators, ts_zscore(market_urgency) (2023–2024)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (<1h)
Signal Type: Cross-Sectional Composite

Core Idea:
Standardize today’s urgency by its same-stock distribution over prior sessions to reduce regime drift; extreme positive z-scores predict stronger directional closes.  ￼

Feature Transformations:
- ZUrgency_t = (Urgency_t − μ_Urgency_pastN)/σ_Urgency_pastN
- Bucket by minutes-to-close

Data Dependencies:
auction features; historical.

Universe & Filters:
US Large-/Mid-Cap; 60+ prior sessions.

Directionality / Construction Hints:
Rank by ZUrgency; industry/beta-neutral.

Strength & Actionability:
Promising – common normalization; robust in practice.  ￼

Keywords:
z-score, normalization, auction

Expected Horizon Notes:
Backtest 6–12 months; live 4 weeks.

Citations:
- Cross-day indicator mention.  ￼

⸻

Alpha Idea #15: Auction Price Convergence Rate

Source(s):
- Intro notebook explaining auction convergence mechanics (near/far/reference) (2023)  ￼

Verification Status: Verified
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Momentum

Core Idea:
Measure how quickly reference price approaches near/far over rolling windows; faster convergence rates predict continuation in the same sign on the next update.  ￼

Feature Transformations:
- DistToNear = |reference − near|; DistToFar = |reference − far|
- Convergence = −Δ(DistToNearest) / Δt
- EWM of Convergence × sign(imbalance)

Data Dependencies:
near, far, reference, imbalance.

Universe & Filters:
US Large-Cap.

Directionality / Construction Hints:
Trade with sign of Convergence; cut risk if Dist widens.

Strength & Actionability:
Promising – directly tied to auction microstructure.  ￼

Keywords:
convergence, auction, momentum

Expected Horizon Notes:
Backtest 2y; live 1 month.

Citations:
- Near/far/reference definitions.  ￼

⸻

Alpha Idea #16: Weighted WAP / Index Ratio & Difference

Source(s):
- Participant list of features: Weighted WAP; WAP Index Ratio/Diff (2024)  ￼
- Synthetic index construction notes (2024)  ￼

Verification Status: Verified
Equity Class: Equity ETFs (QQQ) + Constituents
Horizon: Intraday (<1h)
Signal Type: Cross-Sectional Composite

Core Idea:
Re-weight WAP by inferred index betas and use WAP_i/WAP_index and WAP_i − β_i·WAP_index as residual features to detect relative dislocations into the close.  ￼

Feature Transformations:
- WAPRatio, WAPDiff; rolling z-scores
- Interaction with sign(imbalance)

Data Dependencies:
WAP/reference, index proxy.

Universe & Filters:
Nasdaq 100 constituents; QQQ.

Directionality / Construction Hints:
Pairs vs index; close-only execution.

Strength & Actionability:
Promising – simple residual framework.  ￼

Keywords:
WAP, index, residual

Expected Horizon Notes:
Backtest 2y; live 1 month.

Citations:
- Feature list with Weighted WAP / ratios.  ￼
- Index weighting notes.  ￼

⸻

Alpha Idea #17: OFI (Order Flow Imbalance) at BBO

Source(s):
- OFI tutorial + formulas (blog) (2022)  ￼
- ORVP EDA mentions price/size imbalance families (2021)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (1–6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Compute OFI from changes in best bid/ask prices and sizes between book events; aggregate to 10–60s bars. OFI predicts short-horizon returns; apply during regular session and around close.  ￼

Feature Transformations:
- OFI_t = ΔBidSize·1{ΔBid≥0} − ΔAskSize·1{ΔAsk≤0} + …
- Bar-aggregated OFI, EWM(OFI), OFI/Depth

Data Dependencies:
level-1 NBBO book updates; trade prints.

Universe & Filters:
US Large-/Mid-Cap; high-ADV.

Directionality / Construction Hints:
Trade with OFI sign; neutralize by beta; strict slippage haircuts.

Strength & Actionability:
Strong – canonical HFT signal; widely reproduced.  ￼

Keywords:
OFI, microstructure, intraday

Expected Horizon Notes:
Backtest 2018–2025 intraday NBBO; live 6 weeks.

Citations:
- OFI derivation and examples.  ￼
- ORVP EDA imbalance emphasis.  ￼

⸻

Alpha Idea #18: Microprice Trend (Regular Session)

Source(s):
- Microprice explanation (2020)  ￼
- ORVP EDA links to microstructure features (2021)  ￼

Verification Status: Partially Verified
Equity Class: US Large-/Mid-Cap
Horizon: Intraday (1–6h)
Signal Type: Momentum

Core Idea:
In continuous trading, ΔMicroprice leads ΔMid by a few updates; short-horizon returns align with ΔMicroprice sign, especially in low-spread names.  ￼

Feature Transformations:
- Microprice as in Idea #2; compute Δ and EWM slope
- Microprice−Mid divergence decay rate

Data Dependencies:
NBBO book L1 sizes & prices.

Universe & Filters:
US Large-/Mid-Cap; spread ≤ 2 ticks.

Directionality / Construction Hints:
Trade with Microprice slope; fade when divergence snaps.

Strength & Actionability:
Promising – established heuristic; liquidity dependent.  ￼

Keywords:
microprice, momentum, intraday

Expected Horizon Notes:
Backtest 2018–2025; live 6 weeks.

Citations:
- Microprice definition.  ￼
- ORVP microstructure context.  ￼

⸻

Alpha Idea #19: Volatility Ratio (Target / RealizedVol of log_return1)

Source(s):
- “Public 39th solution – vol_ratio” (2021)  ￼
- ORVP competition page (2021)  ￼

Verification Status: Verified
Equity Class: Global Developed
Horizon: 1–5 Days (risk carry)
Signal Type: Mean-Reversion

Core Idea:
Compute vol_ratio = next-interval realized vol proxy divided by realized_vol(log_return1). Extreme ratios flag over/under-shooting volatility that tends to mean-revert in subsequent intervals/days.  ￼

Feature Transformations:
- RealizedVol of WAP returns (ORVP recipe)
- vol_ratio, z-scored by stock/day
- Cross-sectional rank for next-day vol change

Data Dependencies:
10-second bar WAP; intraday book/trade.

Universe & Filters:
Developed-market equities; ADV > $5M.

Directionality / Construction Hints:
Short vol_ratio >> 0 tails (mean-reversion); long small tails; apply via straddle hedges or risk targets.

Strength & Actionability:
Promising – directly from shared solution; needs robust microstructure noise filters.  ￼

Keywords:
realized vol, mean-revert, intraday

Expected Horizon Notes:
Backtest 2018–2024; monitor 8 weeks.

Citations:
- Feature description (public 39th).  ￼
- ORVP context.  ￼

⸻

Alpha Idea #20: All-Levels WAP & Liquidity Curvature

Source(s):
- “15th Place, Interesting Features – extensions of WAP to all book orders; liquidity measures” (2021)  ￼
- ORVP writeups noting last trade vs book dislocation (2021)  ￼

Verification Status: Verified
Equity Class: Global Developed
Horizon: Intraday (1–6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Extend WAP beyond top-of-book by depth-weighting across multiple levels; compute curvature (slope changes of price vs cumulative depth). Curvature interacts with return dislocation to forecast short-horizon reversal/continuation.  ￼

Feature Transformations:
- Multi-level WAP_k; differences WAP_1−WAP_k
- Curvature = Δ(Price_vs_Depth slope) across levels
- Dislocation = last_trade − WAP_1; interact with curvature

Data Dependencies:
LOB L1–L10; trades.

Universe & Filters:
US Large-/Mid-Cap; high-ADV.

Directionality / Construction Hints:
Fade dislocations when curvature signals replenishment; follow when curvature steepens with thin opposite depth.

Strength & Actionability:
Strong – documented in public writeups; portable to equities with L2 feeds.  ￼

Keywords:
WAP, depth, curvature, dislocation

Expected Horizon Notes:
Backtest 2018–2025; live 6 weeks.

Citations:
- All-level WAP and liquidity features.  ￼
- Dislocation examples.  ￼

⸻

Notes on Deduplication
- Ideas #1, #2, #3, #4, #11, #12, #14, #15 all use imbalance/auction fields but differ in transform (interaction vs divergence vs cross-day z-score vs convergence). Kept as separate due to distinct constructions and trade rules.
- ORVP-related (#17–#20) are regular-session microstructure features distinct from auction-only signals (#1–#16).
- Where multiple posts described the same transform family (e.g., imb*), citations were consolidated to the most informative kernels/threads/repos.

⸻

JSON Export Schema (append after the markdown sections)

{
  "meta": {
    "source_searched": "Kaggle Optiver competitions (Optiver Realized Volatility Prediction; Optiver – Trading at the Close), plus linked GitHub/Medium/X writeups",
    "query": "Optiver competition equities order book alpha feature engineering",
    "scan_window": "2015-01-01 - 2025-10-24",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "Market Urgency (Spread × Liquidity Imbalance)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Closing-auction pressure is captured by the interaction of spread and liquidity imbalance; MarketUrgency = (ask−bid) × (bid_size−ask_size)/(bid_size+ask_size) forecasts the next-minute reference price move.",
      "feature_transformations": [
        "LiquidityImbalance = (bid_size − ask_size)/(bid_size + ask_size)",
        "MarketUrgency = (ask_price − bid_price) × LiquidityImbalance",
        "Rolling z-score of MarketUrgency over 20–60s per stock"
      ],
      "data_dependencies": ["NOII-like auction fields: bid/ask price & size, reference price", "seconds_in_bucket"],
      "universe_filters": "US Large-Cap; price > $5; ADV > $10M; Nasdaq primary",
      "directionality": "Rank long high MarketUrgency, short low; beta-neutral vs synthetic index; hold to cross or +30–60s",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Widely shared feature with clear mechanism; low implementation friction"
      },
      "keywords": ["order-flow", "imbalance", "auction", "microstructure", "intraday"],
      "expected_horizon_notes": "Backtest 2023–2025 TATC-like snapshots; live monitor 6–8 weeks.",
      "citations": [
        "https://github.com/liyiyan128/optiver-trading-at-the-close",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/462743",
        "https://www.kaggle.com/code/tomforbes/optiver-trading-at-the-close-introduction"
      ]
    },
    {
      "title": "Mid–Microprice Divergence (microprice “pull”)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "The size-weighted mid (microprice) indicates which side is likely to be hit; Mid − Microprice predicts near-term drift in the auction reference price.",
      "feature_transformations": [
        "Microprice = (ask×bid_size + bid×ask_size)/(bid_size+ask_size)",
        "Divergence = Mid − Microprice",
        "EWM(Divergence, span=10s) and sign(ΔDivergence)"
      ],
      "data_dependencies": ["Best bid/ask price & size", "seconds_in_bucket"],
      "universe_filters": "US Large-/Mid-Cap; exclude halted names",
      "directionality": "Long negative Divergence (microprice above mid), short positive; sector/beta-neutral; exit at cross",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Classic LOB predictor; explicitly codified in shared repos"
      },
      "keywords": ["microprice", "imbalance", "auction", "intraday"],
      "expected_horizon_notes": "Backtest 2019–2025; live A/B 4–6 weeks.",
      "citations": [
        "https://github.com/liyiyan128/optiver-trading-at-the-close",
        "https://quant.stackexchange.com/questions/50651/how-to-understand-micro-price-aka-weighted-mid-price"
      ]
    },
    {
      "title": "Doublet / Triplet Imbalance Ratios",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Pairwise (x−y)/(x+y) and triplet (max−mid)/(mid−min) ratios across price/size fields compress auction state into directionally informative scalars used by many top solutions.",
      "feature_transformations": [
        "Doublet ratios over {bid_size, ask_size, near_px, far_px, reference_px}",
        "Triplet ratios row-wise across {near, far, reference}",
        "Rolling mean and differences over 10–60s"
      ],
      "data_dependencies": ["near/far/reference", "sizes, counts"],
      "universe_filters": "US Large-/Mid; ADV > $5M",
      "directionality": "Ensemble ranks of ratios; beta/industry neutralization",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Heavily reused public feature family; easy to port"
      },
      "keywords": ["imbalance", "ratios", "auction", "intraday"],
      "expected_horizon_notes": "Backtest 2023–2025; live 1 month.",
      "citations": [
        "https://github.com/liyiyan128/optiver-trading-at-the-close",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/450626"
      ]
    },
    {
      "title": "Imbalance Momentum (d/dt of Imbalance vs Matched)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Momentum",
      "core_idea": "First/second differences of auction imbalance scaled by matched size indicate accelerating order arrival and predict next 30–60s changes in reference price.",
      "feature_transformations": [
        "ImbMomentum = Δ(imbalance)/max(matched_size, ε)",
        "ImbAccel = Δ²(imbalance)/matched_size",
        "EWM(ImbMomentum, span=15s)"
      ],
      "data_dependencies": ["imbalance", "matched_size", "reference price"],
      "universe_filters": "US Large-/Mid-Cap; exclude thin auction names",
      "directionality": "Trade with sign of ImbMomentum; truncate on spread spikes",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Repeatedly cited by participants; mechanism clear"
      },
      "keywords": ["imbalance", "momentum", "auction"],
      "expected_horizon_notes": "Backtest 2023–2024; live 6 weeks.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/485967",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/486666"
      ]
    },
    {
      "title": "Depth Pressure using Near/Far Differentials",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Combine side depth and far−near gap to estimate cross-direction pressure; positive depth with far>near skew implies upward pressure into the cross.",
      "feature_transformations": [
        "DepthDiff = bid_size − ask_size",
        "NearFarSkew = far − near",
        "DepthPressure = DepthDiff × NearFarSkew; z-score by stock"
      ],
      "data_dependencies": ["near_price", "far_price", "bid/ask sizes"],
      "universe_filters": "US Large-/Mid; price > $5",
      "directionality": "Rank by DepthPressure; stop if spread widens >2× median",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Intuitive combination; requires tuning by venue"
      },
      "keywords": ["near-far", "depth", "auction"],
      "expected_horizon_notes": "Backtest 2023–2025; live 1 month.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/485967",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/462743"
      ]
    },
    {
      "title": "Matched vs. Unmatched Flow Ratio",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "PairingRate = paired/(paired+|imb|) tracks closeness to clearing; rising PairingRate aligned with imbalance sign predicts direction of next reference-price step.",
      "feature_transformations": [
        "PairingRate level and Δ",
        "ΔPairingRate × sign(imbalance)",
        "Time-weighted average over last 10–30s"
      ],
      "data_dependencies": ["paired_shares", "imbalance_shares", "near/far/reference"],
      "universe_filters": "US Large-Cap; ADV > $15M",
      "directionality": "Trade in sign of imbalance when PairingRate accelerates",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Directly from NOII-like fields; simple"
      },
      "keywords": ["auction", "paired", "imbalance"],
      "expected_horizon_notes": "Backtest 2y; live 4 weeks.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/data",
        "https://www.kaggle.com/code/tomforbes/optiver-trading-at-the-close-introduction"
      ]
    },
    {
      "title": "Reference-Price Slope vs. Imbalance Divergence",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Momentum",
      "core_idea": "Sign disagreement between Δreference and Δimbalance flags likely re-alignment within ~60s; use as a filter or standalone signal.",
      "feature_transformations": [
        "RefSlope = Δ(reference)",
        "ImbSlope = Δ(imbalance)/depth",
        "DivergenceSignal = −sign(RefSlope × ImbSlope)"
      ],
      "data_dependencies": ["reference", "imbalance", "sizes"],
      "universe_filters": "US Large-/Mid-Cap",
      "directionality": "Enter with DivergenceSignal; exit on sign agreement or cross",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Intuitive but sensitive to noise"
      },
      "keywords": ["auction", "divergence", "momentum"],
      "expected_horizon_notes": "Backtest 2023–2025; paper trade 1 month.",
      "citations": [
        "https://medium.com/@joehbridges/gauging-the-market-optivers-trading-at-the-close-kaggle-competition-27b73f7789c0",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/data"
      ]
    },
    {
      "title": "Synthetic Index Residual (β-neutral auction drift)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (QQQ)",
      "horizon": "Intraday (<1h)",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Reconstruct synthetic index weights; form ResidRef and ResidImb vs index to forecast relative moves into the cross (pairs vs QQQ).",
      "feature_transformations": [
        "β_i via intraday regression vs synthetic index",
        "ResidRef = ΔRef_i − β_i ΔRef_index",
        "ResidImb = Imb_i − β_i Imb_index"
      ],
      "data_dependencies": ["reference, imbalance", "index proxy / synthetic index"],
      "universe_filters": "Nasdaq-100 constituents; QQQ",
      "directionality": "Long residual winners with positive ResidImb; short residual losers; market-neutral",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Well-documented repo approach; straightforward baskets"
      },
      "keywords": ["index", "residual", "pairs", "auction"],
      "expected_horizon_notes": "Backtest 2023–2025; live 6 weeks.",
      "citations": [
        "https://github.com/liyiyan128/optiver-trading-at-the-close",
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/485967"
      ]
    },
    {
      "title": "Sector-Time Grouped Context Features",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Normalize stock-level auction features by concurrent sector statistics to reduce idiosyncratic noise and improve cross-sectional rank stability.",
      "feature_transformations": [
        "SectorImbZ",
        "SectorRelRef",
        "Ratios to sector medians"
      ],
      "data_dependencies": ["auction features", "sector mapping"],
      "universe_filters": "US Large-/Mid-Cap; GICS sectoring",
      "directionality": "Rank by sector-relative metrics; sector-neutral portfolio",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Cited by participants; low complexity"
      },
      "keywords": ["sector", "normalization", "auction"],
      "expected_horizon_notes": "Backtest 2y; live 1 month.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/487276"
      ]
    },
    {
      "title": "Time-to-Cross Urgency (seconds remaining)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Weight pressure features by a convex function of time remaining to emphasize higher-signal late updates from NOII.",
      "feature_transformations": [
        "UrgencyWeight = 1/√(seconds_to_close+1)",
        "WeightedImb = Imbalance × UrgencyWeight",
        "LateSurge = ΔImbalance last 20s × UrgencyWeight"
      ],
      "data_dependencies": ["imbalance, seconds_in_bucket (time remaining)"],
      "universe_filters": "US Large-/Mid-Cap",
      "directionality": "Use weighted ranks; cap exposure in last 5s",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Aligned with NOII mechanics; easy to add"
      },
      "keywords": ["NOII", "timing", "auction"],
      "expected_horizon_notes": "Backtest 2023–2025; live 4 weeks.",
      "citations": [
        "https://www.investopedia.com/terms/n/net-order-imbalance-indicator-noii.asp",
        "https://optiver.com/kaggle-and-optiver-predicting-nasdaqs-closing-cross-auction-movements/"
      ]
    },
    {
      "title": "Spread–Depth Ratio",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Mean-Reversion",
      "core_idea": "Normalize spread by top-of-book depth; extreme SDR tends to revert pre-cross as liquidity replenishes.",
      "feature_transformations": [
        "SDR = (ask − bid)/(bid_size + ask_size)",
        "SDR z-score and ΔSDR",
        "SDR × sign(imbalance)"
      ],
      "data_dependencies": ["spread", "sizes"],
      "universe_filters": "US Large-/Mid-Cap",
      "directionality": "Fade extreme SDR; exit on normalization",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Feature mentioned in posts; mixed empirical results"
      },
      "keywords": ["spread", "depth", "mean-revert"],
      "expected_horizon_notes": "Backtest 2y; live 1 month.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/485967"
      ]
    },
    {
      "title": "Far–Near Asymmetry Trigger",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Event-Driven",
      "core_idea": "Widening far−near reflects uncertainty about clearing price; sharp changes predict next update direction when combined with imbalance sign.",
      "feature_transformations": [
        "FNDelta = far − near",
        "ΔFNDelta and sign(ΔFNDelta) × sign(imb)",
        "Volatility-adjusted FNDelta"
      ],
      "data_dependencies": ["near, far, imbalance, reference"],
      "universe_filters": "US Large-Cap",
      "directionality": "Follow sign of ΔFNDelta; risk cap on spread blowout",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Direct from auction fields; low compute"
      },
      "keywords": ["near", "far", "auction", "event"],
      "expected_horizon_notes": "Backtest 2y; live 4 weeks.",
      "citations": [
        "https://www.kaggle.com/code/tomforbes/optiver-trading-at-the-close-introduction"
      ]
    },
    {
      "title": "Matched-Size Slope (Fill Momentum)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Momentum",
      "core_idea": "Rising paired_shares per second indicates increasing certainty of clearing price; tends to align with subsequent reference-price moves.",
      "feature_transformations": [
        "FillSlope = Δ(paired_shares)/Δt",
        "FillAccel = Δ²(paired_shares)",
        "FillSlope × sign(imbalance)"
      ],
      "data_dependencies": ["paired_shares", "imbalance"],
      "universe_filters": "US Large-/Mid-Cap",
      "directionality": "Trade with FillSlope × sign(imbalance); exit at cross",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Needs stable paired_shares estimates"
      },
      "keywords": ["paired", "slope", "auction"],
      "expected_horizon_notes": "Backtest 2y; live 1 month.",
      "citations": [
        "https://medium.com/@joehbridges/gauging-the-market-optivers-trading-at-the-close-kaggle-competition-27b73f7789c0"
      ]
    },
    {
      "title": "Cross-Day z-Score of Market Urgency",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Normalize today’s urgency by historical distribution to reduce regime drift; extreme positive z-scores predict stronger directional closes.",
      "feature_transformations": [
        "ZUrgency_t = (Urgency_t − μ_pastN)/σ_pastN",
        "Bucket by minutes-to-close"
      ],
      "data_dependencies": ["auction features", "history"],
      "universe_filters": "US Large-/Mid-Cap; 60+ prior sessions",
      "directionality": "Rank by ZUrgency; industry/beta-neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Common normalization; robust in practice"
      },
      "keywords": ["z-score", "normalization", "auction"],
      "expected_horizon_notes": "Backtest 6–12 months; live 4 weeks.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/462664"
      ]
    },
    {
      "title": "Auction Price Convergence Rate",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Momentum",
      "core_idea": "Faster convergence of reference to near/far predicts continuation on the next update; use convergence velocity as the signal.",
      "feature_transformations": [
        "DistToNear = |reference − near|; DistToFar = |reference − far|",
        "Convergence = −Δ(DistToNearest)/Δt",
        "EWM(Convergence) × sign(imbalance)"
      ],
      "data_dependencies": ["near", "far", "reference", "imbalance"],
      "universe_filters": "US Large-Cap",
      "directionality": "Trade with sign of Convergence; cut on widening distance",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Directly tied to auction mechanics"
      },
      "keywords": ["convergence", "auction", "momentum"],
      "expected_horizon_notes": "Backtest 2y; live 1 month.",
      "citations": [
        "https://www.kaggle.com/code/tomforbes/optiver-trading-at-the-close-introduction"
      ]
    },
    {
      "title": "Weighted WAP / Index Ratio & Difference",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (QQQ)",
      "horizon": "Intraday (<1h)",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Use Weighted WAP vs index (ratio/difference) to detect residual dislocations into the close and trade pairs vs QQQ.",
      "feature_transformations": [
        "WAPRatio = WAP_i/WAP_index; WAPDiff = WAP_i − β_i·WAP_index",
        "Rolling z-scores; interact with imbalance"
      ],
      "data_dependencies": ["WAP/reference", "index proxy / synthetic"],
      "universe_filters": "Nasdaq 100 constituents; QQQ",
      "directionality": "Residual long/short; market-neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Simple residual framework; cited by participants"
      },
      "keywords": ["WAP", "index", "residual"],
      "expected_horizon_notes": "Backtest 2y; live 1 month.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/485967",
        "https://github.com/liyiyan128/optiver-trading-at-the-close"
      ]
    },
    {
      "title": "OFI (Order Flow Imbalance) at BBO",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "OFI from changes in best bid/ask prices and sizes aggregated to 10–60s bars predicts short-horizon returns in continuous trading and around the close.",
      "feature_transformations": [
        "OFI_t from ΔBid/Ask size/price events",
        "Bar-aggregated OFI, EWM(OFI), OFI/Depth"
      ],
      "data_dependencies": ["NBBO L1 book updates", "trade prints"],
      "universe_filters": "US Large-/Mid-Cap; high-ADV",
      "directionality": "Trade with OFI sign; beta-neutral; slippage haircuts",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Canonical signal; widely reproduced"
      },
      "keywords": ["OFI", "microstructure", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2025; live 6 weeks.",
      "citations": [
        "https://dm13450.github.io/2022/02/02/Order-Flow-Imbalance.html",
        "https://www.kaggle.com/code/gunesevitan/optiver-realized-volatility-prediction-eda"
      ]
    },
    {
      "title": "Microprice Trend (Regular Session)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-/Mid-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Momentum",
      "core_idea": "ΔMicroprice tends to lead ΔMid; short-horizon returns align with the microprice slope, especially in tight-spread names.",
      "feature_transformations": [
        "Microprice; Δ and EWM slope",
        "Microprice−Mid divergence decay rate"
      ],
      "data_dependencies": ["NBBO L1 price & size"],
      "universe_filters": "US Large-/Mid-Cap; spread ≤ 2 ticks",
      "directionality": "Trade with Microprice slope; fade on quick snap",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Established heuristic; liquidity dependent"
      },
      "keywords": ["microprice", "momentum", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2025; live 6 weeks.",
      "citations": [
        "https://quant.stackexchange.com/questions/50651/how-to-understand-micro-price-aka-weighted-mid-price",
        "https://www.kaggle.com/code/gunesevitan/optiver-realized-volatility-prediction-eda"
      ]
    },
    {
      "title": "Volatility Ratio (Target / RealizedVol of log_return1)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-5 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "vol_ratio = next-interval vol proxy / realized_vol(log_return1); extremes flag over/under-shooting volatility that mean-reverts in subsequent intervals/days.",
      "feature_transformations": [
        "Realized vol of WAP returns (ORVP method)",
        "vol_ratio and z-score by stock/day"
      ],
      "data_dependencies": ["WAP 10s bars", "book/trade"],
      "universe_filters": "Developed-market equities; ADV > $5M",
      "directionality": "Short vol_ratio tails; long small tails; risk via position sizing",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Directly from public solution; portable"
      },
      "keywords": ["realized vol", "mean-revert", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2024; monitor 8 weeks.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/discussion/275973",
        "https://www.kaggle.com/competitions/optiver-realized-volatility-prediction"
      ]
    },
    {
      "title": "All-Levels WAP & Liquidity Curvature",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Depth-weighted WAP across multiple levels and curvature (slope changes of price vs cumulative depth) interact with dislocation to forecast reversal/continuation.",
      "feature_transformations": [
        "WAP_k across depth; WAP_1−WAP_k",
        "Curvature = Δ(Price_vs_Depth slope)",
        "Dislocation = last_trade − WAP_1; interact with curvature"
      ],
      "data_dependencies": ["LOB L1–L10", "trades"],
      "universe_filters": "US Large-/Mid-Cap; high-ADV",
      "directionality": "Fade dislocations when curvature signals replenishment; follow when curvature steepens",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Documented in public writeups; easy to port with L2"
      },
      "keywords": ["WAP", "depth", "curvature", "dislocation"],
      "expected_horizon_notes": "Backtest 2018–2025; live 6 weeks.",
      "citations": [
        "https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/writeups/jacoby-jaeger-15th-place-interesting-features-no-p",
        "https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/writeups/fritz-cremer-public-37th-solution"
      ]
    }
  ]
}