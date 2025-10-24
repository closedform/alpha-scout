20251024 Reddit Quant Alphas Sweep

Alpha Discovery Report (Equities Only)

Model Run
- Model: GPT-5 Pro
- Reasoning Time: 13m05s

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
- Source Searched: Reddit (r/algotrading, r/quantfinance)
- Query / Filters: r/algotrading OR r/quantfinance OR “quant equity alpha” “feature transform” OR “signal design”
- Scan Window: 2014-01-01 - 2025-10-24
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: Opening‑5m Relative-Volume Breakout (Top‑20, ATR Stop)

Source(s): u/— (r/algotrading): “Has anyone reviewed this paper on an opening breakout strategy?” (2024)  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: Intraday (1-6h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Screen the broad US universe at the open for abnormal 5‑min relative volume (first 5‑minute bar vs. a rolling average of the first 5‑minute bar over the prior ~14 sessions). Trade in the direction of the opening 5‑min bar (breakout/continuation), apply ATR-based stop, and close by session end to avoid overnight risk. Rank by relative-volume magnitude and take the top K (e.g., 20) names.  ￼

Feature Transformations (bullet list):
- 5‑min opening relative volume = vol_{9:30–9:35} / mean(vol_{9:30–9:35} past 14 days)
- Direction filter = sign(close_{9:35} − open_{9:30})
- Stop distance = x·ATR(14) on 1‑min or 5‑min bars; end‑of‑day forced exit

Data Dependencies (concise list):
Intraday OHLCV (1–5m), ATR, corporate actions for price adjust, opening print timestamps

Universe & Filters:
US-listed equities, price > $5, ADV > $3M, exclude ADRs; remove halts & news‑halted names

Directionality / Construction Hints:
Cross-sectional long/short basket by rank; scale position by relative-volume z‑score; beta- and industry‑neutralize; noon cut-off to reduce afternoon noise

Strength & Actionability (qualitative only):
Promising – Clear, testable setup with explicit filters and exits; liquidity/frictions manageable on mid/large caps.

Keywords (comma-separated):
opening, relative-volume, breakout, ATR, intraday

Expected Horizon Notes:
Backtest 2018–2025 intraday; dry-run live for 6 weeks; stress 2020–2022 open volatility regimes

Citations:
- https://www.reddit.com/r/algotrading/comments/1dhs545/has_anyone_reviewed_this_paper_on_an_opening/

⸻

Alpha Idea #2: Opening Range Breakout (ORB‑15)

Source(s): u/Russ_CW (r/algotrading): “Backtest Results for the Opening Range Breakout Strategy” (2025‑03)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h)
Signal Type: Momentum

Core Idea (2-4 sentences):
Define the opening range using the 9:30–9:45 candle. Enter on a close above/below the range before noon with stop at the opposite side and fixed 1.5:1 R multiple target; exit intraday. ORB concentrates on the morning trend impulse while avoiding afternoon mean reversion.  ￼

Feature Transformations (bullet list):
- Opening range = [High, Low] of 9:30–9:45
- Breakout confirmation = bar close beyond range with subsequent entry
- Time filter: entries only 9:45–12:00; TP = 1.5·risk

Data Dependencies (concise list):
Intraday OHLCV (15m/5m), corporate actions, trading calendar

Universe & Filters:
SPX constituents; price > $10; ADV > $10M; exclude earnings days and halts

Directionality / Construction Hints:
Directional per breakout; limit K simultaneous names; sector caps; optional ADX(14) > threshold prefilter

Strength & Actionability (qualitative only):
Promising – Transparent logic, simple implementation; slippage manageable on SPX names.

Keywords (comma-separated):
opening, breakout, trend, intraday, ORB

Expected Horizon Notes:
Backtest 2015–2025; out‑of‑sample 2023–2025; live paper 4 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/1j9pxsr/backtest_results_for_the_opening_range_breakout/

⸻

Alpha Idea #3: IBS + Lower‑Band Mean Reversion (Daily)

Source(s): u/ucals (r/algotrading): “A Mean Reversion Strategy with 2.11 Sharpe” (2024)  ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY, QQQ)
Horizon: 1-5 Days
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Daily mean‑reversion using IBS = (Close−Low)/(High−Low) combined with a volatility‑scaled lower band (rolling high − 2.5×avg intraday range). Go long when close < lower band and IBS < 0.3, exit when close > prior day high. This captures short‑term overextensions within index ETFs.  ￼

Feature Transformations (bullet list):
- IBS = (C−L)/(H−L)
- Range proxy = mean(High−Low, lookback 25)
- Lower band = High_{10} − 2.5×range proxy
- Exit: Close > High_{yday}

Data Dependencies (concise list):
Daily OHLC, corporate actions

Universe & Filters:
SPY/QQQ (optional: top N large-caps by ADV as cross‑sectional variant)

Directionality / Construction Hints:
Long‑only; scale by z‑score of IBS; optional VIX regime filter

Strength & Actionability (qualitative only):
Strong – Explicit rules, minimal data requirements, widely testable on liquid ETFs.

Keywords (comma-separated):
IBS, mean‑reversion, volatility‑band, ETF, daily

Expected Horizon Notes:
Backtest 2005–2025; walk‑forward 2015–2025

Citations:
- https://www.reddit.com/r/algotrading/comments/1cwsco8/a_mean_reversion_strategy_with_211_sharpe/

⸻

Alpha Idea #4: “Close‑Near‑Low” Next‑Day Bounce

Source(s): u/Russ_CW (r/algotrading): “Backtesting a ‘Close near Low’ Strategy” (2021)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Overnight
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Compute the position of close within day range. If close percentile ≤ 20% of the day’s range (bottom quintile), buy at MOC, sell next day close (or open as a variant) to exploit rebound tendency. Edge is stronger on liquid, index‑like names.  ￼

Feature Transformations (bullet list):
- RangePctClose = (Close−Low)/(High−Low)
- Threshold: RangePctClose ≤ 0.2
- Optional filter: prior day negative O–C return; exit at next D1 close

Data Dependencies (concise list):
Daily OHLC; auction access (MOC/MOO optional)

Universe & Filters:
SPX names, price > $5, ADV > $5M; exclude earnings day−1 and day0

Directionality / Construction Hints:
Long‑only; beta‑neutral overlay with index future/ETF; cap per‑name risk

Strength & Actionability (qualitative only):
Promising – Simple, testable, and compatible with auction order workflow.

Keywords (comma-separated):
mean‑reversion, range‑position, overnight, auction

Expected Horizon Notes:
Backtest 2010–2025; live monitor 8 weeks for slippage vs. backtest

Citations:
- https://www.reddit.com/r/algotrading/comments/ni1zuj/backtesting_a_close_near_low_strategy/

⸻

Alpha Idea #5: Connors RSI(2) Mean‑Reversion (with MA Filter)

Source(s): r/algotrading: “Backtest Results for Connors RSI2” (2024)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-3 Days
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Classic daily mean‑reversion: enter long when RSI(2) < 5 and price above a long‑term MA filter; exit via RSI(2) rebound or cross above previous day high. Apply cross‑sectional selection among liquid US equities.  ￼

Feature Transformations (bullet list):
- RSI(2) threshold (e.g., <5)
- Trend safety filter: price > SMA(200)
- Exit on RSI(2) > 65 or Close > High_{yday}

Data Dependencies (concise list):
Daily OHLC; RSI; moving averages

Universe & Filters:
SPX/NDX components; price > $5; ADV > $5M

Directionality / Construction Hints:
Cross‑sectional long ranking by RSI(2) ascending; equal‑risk sizing; beta‑neutral portfolio

Strength & Actionability (qualitative only):
Promising – Well‑documented, straightforward rules enable robust out‑of‑sample tests.

Keywords (comma-separated):
RSI2, mean‑reversion, filter, cross‑sectional

Expected Horizon Notes:
Backtest 2000–2025; regime‑slice 2007–2009 and 2020

Citations:
- https://www.reddit.com/r/algotrading/comments/1b6ow5k/backtest_results_for_connors_rsi2/

⸻

Alpha Idea #6: Close→Open (Overnight Drift) Capture

Source(s): r/algotrading: “Buying close selling open – backtesting” (2018) ; r/algotrading: “Buying on Open and Selling on Close vs Opposite (SPY)” (2021)  ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY, QQQ)
Horizon: Overnight
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Exploit the structural overnight return premium by buying at close (MOC) and selling at next open (MOO). Enhance with filters (e.g., prior intraday return negative, exclude earnings days, VIX regime).  ￼

Feature Transformations (bullet list):
- Overnight return RO = log(Open_{t+1}/Close_t)
- Filter: intraday return RI < 0 to avoid chasing trend
- Regime filter via VIX percentile

Data Dependencies (concise list):
Daily OHLC (composite vs primary open distinctions), auction order support (MOC/MOO)

Universe & Filters:
SPY/QQQ (expand to liquid sector ETFs)

Directionality / Construction Hints:
Long‑only; full overlap allowed; cap exposure near macro events

Strength & Actionability (qualitative only):
Promising – Widely observed phenomenon; implementation hinges on auctions and slippage control.

Keywords (comma-separated):
overnight, drift, MOC, MOO, ETF

Expected Horizon Notes:
Backtest 1993–2025; walk-forward 2018–2025; live shadow 4 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/bc898w/buying_close_selling_open_backtesting/
- https://www.reddit.com/r/algotrading/comments/o5hpr5/buying_on_open_and_selling_on_close_vs_opposite/

⸻

Alpha Idea #7: Regime‑Based Overnight Mean‑Reversion on Leveraged Equity ETFs

Source(s): u/ChristianZahl (r/algotrading): “Built a Regime‑Based Overnight Mean Reversion Model – 10.19.25” (2025‑10‑19)  ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (leveraged, e.g., TQQQ, SOXL, SPXL)
Horizon: Overnight
Signal Type: Cross-Sectional Composite

Core Idea (2-4 sentences):
Classify market into regimes (strong/weak bull, bear, sideways, unpredictable) using index MAs + VIX. Within each regime, select leveraged equity ETFs with large intraday overreactions and historically positive overnight reversion propensity; buy near 15:50 ET and exit at open.  ￼

Feature Transformations (bullet list):
- Regime features: SPX MA stack, VIX level/vol-of-vol
- Intraday shock = |RI_t| vs rolling distribution
- Per‑ticker Bayesian overnight-direction probability by regime

Data Dependencies (concise list):
Daily OHLC for ETFs; VIX; regime classifiers; ETF lists

Universe & Filters:
US leveraged equity ETFs; exclude low ADV; avoid earnings for single‑name leveraged ETNs

Directionality / Construction Hints:
Long or short per reversion expectation; cap leverage; pre‑open exit via MOO

Strength & Actionability (qualitative only):
Promising – Clear rules and scheduling; capacity ok across large leveraged ETFs; regime logic explicit.

Keywords (comma-separated):
overnight, regime, leveraged‑ETFs, mean‑reversion

Expected Horizon Notes:
Backtest 2015–2025; forward test 8 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/1ob5xao/built_a_regimebased_overnight_mean_reversion/

⸻

Alpha Idea #8: Post‑Earnings Surprise Long Basket (15‑Day Hold)

Source(s): u/InvestorsEdgeAlgos (r/algotrading): “Do the rewards outweigh the risks with this earnings surprise strategy?” (2018)  ￼
Verification Status: Verified (direct link)
Equity Class: US Small-Cap
Horizon: 1-4 Weeks
Signal Type: Event-Driven

Core Idea (2-4 sentences):
Each day, form a basket from yesterday’s reporters with EPS ≥ +15% vs consensus and positive 2‑week price momentum; hold 15 trading days; rebalance daily, max 10 names. This captures PEAD in smaller names with sufficient surprise magnitude.  ￼

Feature Transformations (bullet list):
- Earnings surprise % = (Actual−Est)/|Est|
- Momentum filter = 10‑day return > 0
- Sector‑neutral rank by z‑scored surprise magnitude

Data Dependencies (concise list):
Structured earnings (actual, estimate), earnings calendar, daily OHLC

Universe & Filters:
US stocks/ADRs; mkt cap > $50M; price > $3; liquidity > $1M ADV

Directionality / Construction Hints:
Long‑only; equal risk sizing; optional stop on large negative guidance headlines

Strength & Actionability (qualitative only):
Strong – Concrete rules with hold time; clear data fields; easy to replicate.

Keywords (comma-separated):
earnings, PEAD, small‑cap, event‑driven, momentum‑filter

Expected Horizon Notes:
Backtest 2010–2025; earnings season stratified; live dry‑run 1 season

Citations:
- https://www.reddit.com/r/algotrading/comments/9cm4d0/do_the_rewards_outweigh_the_risks_with_this/

⸻

Alpha Idea #9: 3σ Intraday Drop → Multihorizon Rebound

Source(s): r/algotrading: “Developing a method / backtest on Mean Reversion in US stocks” (2023)  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: 1-3 Days
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Trigger on intraday move ≤ −3σ relative to 20‑day volatility; long into the close or at next open. Test multi‑horizon exits (1D, 1W, 1M) and size by shock magnitude.  ￼

Feature Transformations (bullet list):
- Shock = (Close−Open)/σ_{20, intraday}
- Regime filter via VIX percentile; exclude earnings
- Exit ladder at D+1/D+5/D+21

Data Dependencies (concise list):
Intraday OHLCV, realized intraday σ, earnings calendar

Universe & Filters:
Price > $5; ADV > $2M; exclude trading halts

Directionality / Construction Hints:
Long‑biased; risk parity by ATR; beta‑hedge with index future

Strength & Actionability (qualitative only):
Tentative – Clear trigger; needs robust execution/overnight gap handling.

Keywords (comma-separated):
intraday, mean‑reversion, shock, volatility

Expected Horizon Notes:
Backtest 2018–2025 intraday; simulate auction entries

Citations:
- https://www.reddit.com/r/algotrading/comments/13myyoq/developing_a_method_backtest_on_mean_reversion_in/

⸻

Alpha Idea #10: Two‑Bar HH/LL Reversal (Daily Break of Inside Weak Bar)

Source(s): r/algotrading: “Backtest Results for a Simple Reversal Strategy” (2024)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: 1-5 Days
Signal Type: Momentum (counter-trend trigger → reversal)

Core Idea (2-4 sentences):
Identify days with Lower Low AND Lower High vs. prior day, then enter on next‑day break above that bar’s high (mirror for shorts). This setup frames short‑term exhaustion and subsequent reversal.  ￼

Feature Transformations (bullet list):
- Weak bar flag: LL & LH vs yday
- Trigger: next‑day intraday High > weak bar High
- Exit: R multiple or close>prior swing high

Data Dependencies (concise list):
Daily OHLC (optional: 30‑min for intraday triggers)

Universe & Filters:
SPX names; earnings blackout; min $5 price, ADV > $3M

Directionality / Construction Hints:
Long/short per trigger; equal‑risk sizing; optional ATR stop

Strength & Actionability (qualitative only):
Tentative – Rules are simple; requires robust filter set to avoid chop.

Keywords (comma-separated):
reversal, HH/LL, trigger, daily

Expected Horizon Notes:
Backtest 2005–2025; monitor live 6 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/1f8v70e/backtest_results_for_a_simple_reversal_strategy/

⸻

Alpha Idea #11: Turn‑of‑Month (ToM) Equity Bias

Source(s): r/algotrading: “Would it make sense to first test an underlying market dynamic… (ToM)” (2023) ; r/algotrading: “A list of 26 stock market anomalies and investing ideas” (2018)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY, IWM)
Horizon: 1-5 Days
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Go long from last trading day (LTD) through first 3 trading days (TD+3) of the next month to capture month‑end/start flows. Avoid overlapping large macro/earnings clusters.  ￼

Feature Transformations (bullet list):
- Calendar flag: [LTD, TD+3] inclusive
- Filter: VIX > 90th pctile → reduce size
- Exit on TD+3 close or trailing stop

Data Dependencies (concise list):
Trading calendar, daily OHLC, VIX

Universe & Filters:
SPY/QQQ/IWM; optional sector ETFs

Directionality / Construction Hints:
Long‑only; no overlap with earnings super‑weeks; cap size ahead of FOMC

Strength & Actionability (qualitative only):
Tentative – Well‑known anomaly; needs slippage/decay check post‑2015.

Keywords (comma-separated):
seasonality, turn‑of‑month, ETF

Expected Horizon Notes:
Backtest 1993–2025; rolling live 2 months

Citations:
- https://www.reddit.com/r/algotrading/comments/1550ofu/would_it_make_sense_to_first_test_an_underlying/
- https://www.reddit.com/r/algotrading/comments/8lezo0/a_list_of_26_stock_market_anomalies_and_investing/

⸻

Alpha Idea #12: OPEX (Monthly Options Expiry) Flow Skew

Source(s): r/algotrading: “Consistent mid‑month dip … because of options expiration” (2021)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY/QQQ)
Horizon: 1-3 Days
Signal Type: Event-Driven

Core Idea (2-4 sentences):
Exploit dealer‑hedging flows into monthly OPEX by positioning short ahead of OPEX when delta‑hedging unwinds (or long post‑OPEX for vol reset). Apply strict windows (e.g., TD−3→TD0).  ￼

Feature Transformations (bullet list):
- Window flag = days −3 to 0 around monthly OPEX
- Vanna/Charm proxy via IV/term‑structure shifts
- Volatility filter to avoid macro event overlap

Data Dependencies (concise list):
Options calendar; ETF OHLC; IV summary (optional)

Universe & Filters:
SPY/QQQ; avoid earnings clusters for mega‑caps

Directionality / Construction Hints:
Directional; reduce exposure when IV bid is rising into OPEX

Strength & Actionability (qualitative only):
Tentative – Mechanism plausible; must validate with IV/flow proxies.

Keywords (comma-separated):
OPEX, dealer‑hedging, seasonality, ETF

Expected Horizon Notes:
Backtest 2016–2025; monitor 3 months live

Citations:
- https://www.reddit.com/r/algotrading/comments/pa4xmz/does_anyone_know_why_this_consistent_midmonth_dip/

⸻

Alpha Idea #13: Institutional Rebalance Front‑Run (60/40 & Index)

Source(s): r/quantfinance: “Can you front‑run institutional rebalancing?” (2024) ; r/algotrading: “ETF Holdings Project” (2021) – comments on index rebalancing edge  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (specify), Sector-Specific (index adds/deletes)
Horizon: 1-4 Weeks
Signal Type: Event-Driven

Core Idea (2-4 sentences):
Pre‑position in names forecast to be added/removed during index rebalances (e.g., S&P/Russell) and in 60/40 month‑end flows. Trade windows and sizing rules depend on published methodologies and preview lists.  ￼

Feature Transformations (bullet list):
- Add/Delete likelihood from rules (mkt‑cap rank, liquidity, profitability screens)
- Flow proxy = ETF creations/redemptions; ADV multiples
- Entry N days pre‑announce; exit around effective date

Data Dependencies (concise list):
Constituent files; reconstitution calendars; ETF flow/holdings

Universe & Filters:
Targeted indices (SPX, R2000) and impacted constituents

Directionality / Construction Hints:
Long adds, short deletes; sector‑neutral; cap crowding names

Strength & Actionability (qualitative only):
Promising – Process‑driven; needs calendar discipline and borrow/liquidity for deletes.

Keywords (comma-separated):
index‑rebal, flows, event‑driven, ETF

Expected Horizon Notes:
Backtest 2014–2025 on announced rebalances; paper trade next two cycles

Citations:
- https://www.reddit.com/r/quantfinance/comments/1ly08hm/can_you_frontrun_institutional_rebalancing_yes_it/
- https://www.reddit.com/r/algotrading/comments/s1hcp2/etf_holdings_project/

⸻

Alpha Idea #14: L1/L2 Order‑Book Imbalance → Short‑Horizon Reversion

Source(s): u/PianoWithMe (r/algotrading): “Features other than TA indicators that are useful?” (2023) ; r/algotrading: “Order flow analysis. Orderbook imbalance.” (2018)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Use queue/volume imbalance, microprice, cancel/add rates across top‑of‑book (and a few levels) to detect temporary dislocations; fade toward mid. Execution uses passive/pegged orders and queue estimates to minimize impact.  ￼

Feature Transformations (bullet list):
- Imbalance = (ΣBidQty−ΣAskQty)/(ΣBidQty+ΣAskQty), top N levels
- Microprice deviation = |Micro−Mid| normalized by spread
- Cancel/Add ratio, time‑since‑last‑fill, queue‑position estimates

Data Dependencies (concise list):
NBBO + depth (L2), prints, venue flags

Universe & Filters:
High‑ADV names (SPY, AAPL, MSFT, NVDA); spread ≤ 2 ticks

Directionality / Construction Hints:
Reversion to mid; size vs. expected time‑to‑fill; avoid news bursts

Strength & Actionability (qualitative only):
Tentative – Requires L2 and careful microstructure modeling; feasible on liquid US names.

Keywords (comma-separated):
order‑flow, microprice, imbalance, intraday

Expected Horizon Notes:
Backtest 2022–2025 L1/L2; live paper 4 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/13lkikt/features_other_than_ta_indicators_that_are_useful/
- https://www.reddit.com/r/algotrading/comments/80jl3n/order_flow_analysis_orderbook_imbalance_volume/

⸻

Alpha Idea #15: Day‑of‑Week (DoW) Bias Overlay

Source(s): r/algotrading: “Does anyone use a day‑of‑week filter?” (2025) ; r/algotrading: “How much merit do you give ‘day of week’ optimization” (2023)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY/QQQ)
Horizon: 1-3 Days
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Overlay a DoW filter onto existing signals (e.g., avoid Monday shorts; favor Friday→Monday overnight longs) consistent with observed drift differences by weekday. Apply only as a filter, not standalone predictor.  ￼

Feature Transformations (bullet list):
- DoW one‑hot; interaction terms with signal strength
- Rolling DoW edge stability test
- Exposure haircut on unfavorable DoW

Data Dependencies (concise list):
Calendar, daily OHLC

Universe & Filters:
SPY/QQQ; extend to high‑liquidity single names

Directionality / Construction Hints:
Use as gating/weighting factor; never override risk limits

Strength & Actionability (qualitative only):
Tentative – Seasonality exists but is weak; best as modulator.

Keywords (comma-separated):
seasonality, weekday, overlay, filter

Expected Horizon Notes:
Backtest 1993–2025; live 6 weeks as overlay

Citations:
- https://www.reddit.com/r/algotrading/comments/1ml7caa/does_anyone_use_a_dayofweek_filter/
- https://www.reddit.com/r/algotrading/comments/18k28e0/how_much_merit_do_you_give_day_of_week/

⸻

Alpha Idea #16: ML Target Re‑specification (Open→Open) to Avoid Close Data Leakage

Source(s): r/algotrading: “ML Target and Strategy: Close‑to‑Close vs. Open‑…” (2024)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-3 Days
Signal Type: Cross-Sectional Composite

Core Idea (2-4 sentences):
When training ML on daily bars, predict Open→Open returns to avoid EOD volume finalization leakage. Pair with robust feature set (lagged returns, volatility, breadth) and execute with EOD signals routed to MOC/MOO for clean fill logic.  ￼

Feature Transformations (bullet list):
- Target: r_{t+1}^{OO} = log(Open_{t+1}/Open_t)
- Leakage‑safe features available by ~15:50 ET
- Per‑sector standardization; cross‑sectional rank transform

Data Dependencies (concise list):
Daily OHLCV with timestamped EOD data availability; calendar

Universe & Filters:
Top 1000 US by ADV; price > $5

Directionality / Construction Hints:
Long/short by rank; beta/sector neutral; rebalance daily

Strength & Actionability (qualitative only):
Promising – Practical fix for leakage; requires disciplined feature timing.

Keywords (comma-separated):
ML, leakage, OO‑return, MOC/MOO

Expected Horizon Notes:
Backtest 2015–2025; live shadow 6 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/1ejy68l/ml_target_and_strategy_closetoclose_vs/

⸻

Alpha Idea #17: Breadth‑Thrust Overlay (Zweig‑Style) for Equity ETF Timing

Source(s): u/iggy555 & thread (r/algotrading): breadth metrics mentioned incl. Zweig thrust (2023)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY, IWM)
Horizon: 1-4 Weeks
Signal Type: Cross-Sectional Composite

Core Idea (2-4 sentences):
Use a breadth‑thrust trigger (e.g., % advancing issues thrusting above threshold in a short window) as an overlay to activate/deactivate risk in momentum or reversion systems on SPY/IWM. The thrust marks breadth regime shifts.  ￼

Feature Transformations (bullet list):
- Breadth ratio thrust (adv/dec) over 10 days
- Confirm with %>SMA(50) constituents
- Exposure step‑up post‑thrust; decay if thrust fails

Data Dependencies (concise list):
Advance/decline data; % above MA; ETF OHLC

Universe & Filters:
SPY/IWM; optional sector ETFs

Directionality / Construction Hints:
Overlay only; combine with core alpha (e.g., IBS or momentum)

Strength & Actionability (qualitative only):
Tentative – Overlay improves regime timing; needs robust source for breadth data.

Keywords (comma-separated):
breadth, regime, overlay, ETF

Expected Horizon Notes:
Backtest 2005–2025; live overlay 8 weeks

Citations:
- https://www.reddit.com/r/algotrading/comments/13lkikt/features_other_than_ta_indicators_that_are_useful/

⸻

Notes on Deduplication
- ORB‑15 (Idea #2) and Opening‑5m Relative‑Volume Breakout (Idea #1) are related; kept both due to distinct entry logic (range‑based vs. relative volume + ATR).
- IBS lower‑band (Idea #3) vs. Close‑near‑Low (Idea #4): both capture reversion, but IBS adds volatility‑band confirmation; retained both.
- Overnight drift capture (Idea #6) vs. Regime‑based overnight MR (Idea #7): same horizon, different selection/regime process; both included.
- Microstructure imbalance (Idea #14) is a short‑horizon L1/L2 variant and is not a duplicate of ORB or reversion systems.

⸻

JSON Export Schema (append after the markdown sections)

{
  "meta": {
    "source_searched": "Reddit (r/algotrading, r/quantfinance)",
    "query": "r/algotrading OR r/quantfinance OR “quant equity alpha” “feature transform” OR “signal design”",
    "scan_window": "2014-01-01 - 2025-10-24",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "Opening-5m Relative-Volume Breakout (Top-20, ATR Stop)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Screen first 5-minute bar relative volume versus prior 14 sessions, trade in bar direction with ATR stop, end-of-day exit. Rank and take top K names to concentrate exposure.",
      "feature_transformations": [
        "RelVol_5m = vol_9:30–9:35 / mean(vol_9:30–9:35, 14d)",
        "Direction = sign(close_9:35 − open_9:30)",
        "Stop = x·ATR(14); EOD forced exit"
      ],
      "data_dependencies": ["Intraday OHLCV (1–5m)", "ATR", "Auction timestamps"],
      "universe_filters": "US stocks; price > $5; ADV > $3M; exclude ADRs/halts",
      "directionality": "Long/short per breakout; cross-sectional; beta/industry neutralization",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear triggers and exits; ample liquidity open-to-midday."
      },
      "keywords": ["opening", "relative-volume", "breakout", "ATR", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2025 intraday; 6-week live paper",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1dhs545/has_anyone_reviewed_this_paper_on_an_opening/"]
    },
    {
      "title": "Opening Range Breakout (ORB-15)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Momentum",
      "core_idea": "Define 9:30–9:45 range; enter on close beyond range before noon; stop at opposite range; fixed R-multiple target.",
      "feature_transformations": [
        "OpeningRange = [High, Low] of 9:30–9:45",
        "Breakout confirmation = bar close beyond range",
        "Time filter 9:45–12:00; TP=1.5·risk"
      ],
      "data_dependencies": ["Intraday OHLCV (15m/5m)"],
      "universe_filters": "SPX; price > $10; ADV > $10M; exclude earnings/halts",
      "directionality": "Directional per breakout; K positions; optional ADX trend filter",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Simple, liquid, and widely testable."
      },
      "keywords": ["opening", "breakout", "trend", "intraday", "ORB"],
      "expected_horizon_notes": "Backtest 2015–2025; 4-week live dry-run",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1j9pxsr/backtest_results_for_the_opening_range_breakout/"]
    },
    {
      "title": "IBS + Lower-Band Mean Reversion (Daily)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "1-5 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "Long when IBS < 0.3 and close under a volatility-scaled lower band; exit once close > prior day high.",
      "feature_transformations": [
        "IBS = (C−L)/(H−L)",
        "Range proxy = mean(H−L, 25d)",
        "LowerBand = High_10 − 2.5×RangeProxy"
      ],
      "data_dependencies": ["Daily OHLC"],
      "universe_filters": "SPY/QQQ; or top N large-caps by ADV",
      "directionality": "Long-only; scale by IBS z-score; optional VIX filter",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Explicit rules; minimal data footprint."
      },
      "keywords": ["IBS", "mean-reversion", "volatility-band", "ETF", "daily"],
      "expected_horizon_notes": "Backtest 2005–2025; walk-forward 2015–2025",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1cwsco8/a_mean_reversion_strategy_with_211_sharpe/"]
    },
    {
      "title": "Close-Near-Low Next-Day Bounce",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Overnight",
      "signal_type": "Mean-Reversion",
      "core_idea": "If close is within bottom 20% of the day’s range, buy at the close and exit next session (open or close).",
      "feature_transformations": [
        "RangePctClose = (C−L)/(H−L) ≤ 0.2",
        "Optional prior-day negative intraday return filter",
        "Exit at D+1 close"
      ],
      "data_dependencies": ["Daily OHLC", "Auction access"],
      "universe_filters": "SPX; price > $5; ADV > $5M; earnings blackout",
      "directionality": "Long-only; beta-hedged",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Very simple trigger; auction-compatible."
      },
      "keywords": ["mean-reversion", "range-position", "overnight", "auction"],
      "expected_horizon_notes": "Backtest 2010–2025; live 8 weeks",
      "citations": ["https://www.reddit.com/r/algotrading/comments/ni1zuj/backtesting_a_close_near_low_strategy/"]
    },
    {
      "title": "Connors RSI(2) with Trend Filter",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-3 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "Enter long when RSI(2) < 5 with price above SMA(200); exit when RSI recovers or price exceeds yday high.",
      "feature_transformations": [
        "RSI(2) < 5",
        "SMA(200) filter",
        "Exit RSI(2) > 65 or C > H_yday"
      ],
      "data_dependencies": ["Daily OHLC", "RSI", "SMAs"],
      "universe_filters": "SPX/NDX; price > $5; ADV > $5M",
      "directionality": "Cross-sectional long ranking by RSI(2)",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Standardized and reproducible rules."
      },
      "keywords": ["RSI2", "mean-reversion", "filter", "cross-sectional"],
      "expected_horizon_notes": "Backtest 2000–2025",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1b6ow5k/backtest_results_for_connors_rsi2/"]
    },
    {
      "title": "Close→Open Overnight Drift Capture",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "Overnight",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Exploit structural overnight premium by buying at close (MOC) and selling next open (MOO), filtered by prior intraday return and VIX regime.",
      "feature_transformations": [
        "Overnight RO = log(O_{t+1}/C_t)",
        "Filter RI < 0",
        "VIX percentile gating"
      ],
      "data_dependencies": ["Daily OHLC", "Auction support"],
      "universe_filters": "SPY/QQQ; extend to sector ETFs",
      "directionality": "Long-only; risk caps near macro events",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Widely observed; execution-critical but feasible."
      },
      "keywords": ["overnight", "drift", "MOC", "MOO", "ETF"],
      "expected_horizon_notes": "Backtest 1993–2025; live 4 weeks",
      "citations": [
        "https://www.reddit.com/r/algotrading/comments/bc898w/buying_close_selling_open_backtesting/",
        "https://www.reddit.com/r/algotrading/comments/o5hpr5/buying_on_open_and_selling_on_close_vs_opposite/"
      ]
    },
    {
      "title": "Regime-Based Overnight Mean-Reversion (Leveraged ETFs)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "Overnight",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Use MA/VIX regime classification and historical overnight response by ticker/regime to buy leveraged ETFs near close and exit at open.",
      "feature_transformations": [
        "Regime via SPX MAs + VIX",
        "Intraday shock magnitude rank",
        "Bayesian overnight probability per ticker & regime"
      ],
      "data_dependencies": ["Daily OHLC", "VIX", "ETF lists"],
      "universe_filters": "US leveraged equity ETFs; ADV filter",
      "directionality": "Long/short per reversion expectation",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Explicit workflow; adequate capacity."
      },
      "keywords": ["overnight", "regime", "leveraged-ETFs", "mean-reversion"],
      "expected_horizon_notes": "Backtest 2015–2025; 8-week forward test",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1ob5xao/built_a_regimebased_overnight_mean_reversion/"]
    },
    {
      "title": "Post-Earnings Surprise Long Basket (15-Day Hold)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Daily rebalance into prior-day reporters with EPS ≥ +15% vs consensus and positive 10-day momentum; hold 15 trading days.",
      "feature_transformations": [
        "Surprise % = (Actual−Est)/|Est|",
        "Momentum = 10d return > 0",
        "Sector-neutral z-score rank"
      ],
      "data_dependencies": ["Earnings actual/estimate", "Calendar", "Daily OHLC"],
      "universe_filters": "US stocks/ADRs; cap > $50M; price > $3; ADV > $1M",
      "directionality": "Long-only; cap 10 names",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Concrete rule set and hold window."
      },
      "keywords": ["earnings", "PEAD", "small-cap", "event-driven", "momentum-filter"],
      "expected_horizon_notes": "Backtest 2010–2025; live one season",
      "citations": ["https://www.reddit.com/r/algotrading/comments/9cm4d0/do_the_rewards_outweigh_the_risks_with_this/"]
    },
    {
      "title": "3σ Intraday Drop → Multihorizon Rebound",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-3 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "Trigger on ≤ −3σ intraday move vs 20-day intraday σ; long into close or next open; ladder exits at D+1/D+5/D+21.",
      "feature_transformations": [
        "Shock = (C−O)/σ_{20,intraday}",
        "VIX regime filter",
        "Exit ladder across horizons"
      ],
      "data_dependencies": ["Intraday OHLCV", "Realized σ", "Earnings calendar"],
      "universe_filters": "Price > $5; ADV > $2M",
      "directionality": "Long-biased; beta hedge",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Clear trigger; execution/overnight controls needed."
      },
      "keywords": ["intraday", "mean-reversion", "shock", "volatility"],
      "expected_horizon_notes": "Backtest 2018–2025 intraday",
      "citations": ["https://www.reddit.com/r/algotrading/comments/13myyoq/developing_a_method_backtest_on_mean_reversion_in/"]
    },
    {
      "title": "Two-Bar HH/LL Reversal (Daily Trigger)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "1-5 Days",
      "signal_type": "Momentum",
      "core_idea": "Flag day with both LL and LH vs prior day; enter next day on break above that bar’s high (mirror short).",
      "feature_transformations": [
        "Weak bar detection (LL & LH)",
        "Trigger = High_t+1 > High_t",
        "Exit by R multiple"
      ],
      "data_dependencies": ["Daily OHLC"],
      "universe_filters": "SPX; earnings blackout",
      "directionality": "Long/short per trigger",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Simple rules; requires filters to avoid noise."
      },
      "keywords": ["reversal", "HH/LL", "trigger", "daily"],
      "expected_horizon_notes": "Backtest 2005–2025",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1f8v70e/backtest_results_for_a_simple_reversal_strategy/"]
    },
    {
      "title": "Turn-of-Month (ToM) Equity Bias",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "1-5 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Long LTD→TD+3 each month to capture start/end month flows; avoid macro/earnings clusters.",
      "feature_transformations": [
        "Calendar window [LTD, TD+3]",
        "VIX percentile gating",
        "Trailing stop on fail"
      ],
      "data_dependencies": ["Trading calendar", "Daily OHLC", "VIX"],
      "universe_filters": "SPY, IWM",
      "directionality": "Long-only; position caps",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Known anomaly; must confirm persistence post-2015."
      },
      "keywords": ["seasonality", "turn-of-month", "ETF"],
      "expected_horizon_notes": "Backtest 1993–2025",
      "citations": [
        "https://www.reddit.com/r/algotrading/comments/1550ofu/would_it_make_sense_to_first_test_an_underlying/",
        "https://www.reddit.com/r/algotrading/comments/8lezo0/a_list_of_26_stock_market_anomalies_and_investing/"
      ]
    },
    {
      "title": "OPEX Flow Skew (Monthly Expiry)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "1-3 Days",
      "signal_type": "Event-Driven",
      "core_idea": "Exploit dealer hedging unwinds around monthly OPEX via short pre-OPEX or long post-OPEX resets within a tight window.",
      "feature_transformations": [
        "Window TD−3→TD0",
        "IV/term-structure shift proxy",
        "Macro overlap filter"
      ],
      "data_dependencies": ["Options calendar", "ETF OHLC", "IV summary"],
      "universe_filters": "SPY/QQQ",
      "directionality": "Directional; size via IV regime",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Mechanism plausible; requires IV proxies for gating."
      },
      "keywords": ["OPEX", "dealer-hedging", "seasonality", "ETF"],
      "expected_horizon_notes": "Backtest 2016–2025; live 3 months",
      "citations": ["https://www.reddit.com/r/algotrading/comments/pa4xmz/does_anyone_know_why_this_consistent_midmonth_dip/"]
    },
    {
      "title": "Institutional Rebalance Front-Run (60/40 & Index Rebalances)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Sector-Specific (specify)",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Pre-position for index adds/deletes and 60/40 rebalancing flows based on rule-based previews and historical flow windows.",
      "feature_transformations": [
        "Add/Delete probability from index rules",
        "ETF flow/creation-redemption proxies",
        "Event window entry/exit offsets"
      ],
      "data_dependencies": ["Index methodology & calendars", "ETF holdings/flows"],
      "universe_filters": "Target indices and impacted constituents",
      "directionality": "Long adds, short deletes; sector neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Process-driven with public calendars."
      },
      "keywords": ["index-rebal", "flows", "event-driven", "ETF"],
      "expected_horizon_notes": "Backtest 2014–2025",
      "citations": [
        "https://www.reddit.com/r/quantfinance/comments/1ly08hm/can_you_frontrun_institutional_rebalancing_yes_it/",
        "https://www.reddit.com/r/algotrading/comments/s1hcp2/etf_holdings_project/"
      ]
    },
    {
      "title": "L1/L2 Order-Book Imbalance Reversion",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Fade microprice deviations when book imbalance and cancel/add ratios indicate short-lived pressure.",
      "feature_transformations": [
        "Imbalance=(ΣBid−ΣAsk)/(ΣBid+ΣAsk)",
        "Microprice vs mid deviation (spread-normalized)",
        "Cancel/Add ratio; time-since-last-fill"
      ],
      "data_dependencies": ["NBBO + depth", "Prints"],
      "universe_filters": "High-ADV names; tight spreads",
      "directionality": "Reversion to mid; passive exec preferred",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Data intensive but feasible on liquid names."
      },
      "keywords": ["order-flow", "microprice", "imbalance", "intraday"],
      "expected_horizon_notes": "Backtest 2022–2025",
      "citations": [
        "https://www.reddit.com/r/algotrading/comments/13lkikt/features_other_than_ta_indicators_that_are_useful/",
        "https://www.reddit.com/r/algotrading/comments/80jl3n/order_flow_analysis_orderbook_imbalance_volume/"
      ]
    },
    {
      "title": "Day-of-Week (DoW) Bias Overlay",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "1-3 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Use weekday dummy variables as gating/weighting on existing signals, e.g., favor Friday→Monday overnights.",
      "feature_transformations": [
        "DoW one-hot + interaction with signal strength",
        "Rolling stability test",
        "Exposure haircut on unfavorable DoW"
      ],
      "data_dependencies": ["Calendar", "Daily OHLC"],
      "universe_filters": "SPY/QQQ and mega-cap single names",
      "directionality": "Overlay only",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Seasonality is weak; best as a modulator."
      },
      "keywords": ["seasonality", "weekday", "overlay", "filter"],
      "expected_horizon_notes": "Backtest 1993–2025; 6-week live overlay",
      "citations": [
        "https://www.reddit.com/r/algotrading/comments/1ml7caa/does_anyone_use_a_dayofweek_filter/",
        "https://www.reddit.com/r/algotrading/comments/18k28e0/how_much_merit_do_you_give_day_of_week/"
      ]
    },
    {
      "title": "ML Target Respec: Open→Open to Avoid EOD Leakage",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-3 Days",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Predict open→open returns with features available by ~15:50 ET, routing entries via MOC to avoid volume-finalization leakage.",
      "feature_transformations": [
        "Target r^{OO} instead of close→close",
        "Leakage-safe features & timestamps",
        "Sector-standardization and rank"
      ],
      "data_dependencies": ["Daily OHLCV with timestamps"],
      "universe_filters": "Top 1000 by ADV",
      "directionality": "Rank long/short; sector/beta neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Practical engineering fix improving live fidelity."
      },
      "keywords": ["ML", "leakage", "OO-return", "MOC/MOO"],
      "expected_horizon_notes": "Backtest 2015–2025; 6-week shadow",
      "citations": ["https://www.reddit.com/r/algotrading/comments/1ejy68l/ml_target_and_strategy_closetoclose_vs/"]
    },
    {
      "title": "Breadth-Thrust Overlay (Zweig-Style)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (specify)",
      "horizon": "1-4 Weeks",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Deploy a breadth-thrust signal to gate exposure in momentum/reversion ETF strategies.",
      "feature_transformations": [
        "Adv/Dec thrust over 10 days",
        "% constituents > SMA(50)",
        "Exposure step-up/decay logic"
      ],
      "data_dependencies": ["Breadth data", "ETF OHLC"],
      "universe_filters": "SPY/IWM; sector ETFs",
      "directionality": "Overlay only",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Useful for regime timing; data source needed."
      },
      "keywords": ["breadth", "regime", "overlay", "ETF"],
      "expected_horizon_notes": "Backtest 2005–2025; 8-week live overlay",
      "citations": ["https://www.reddit.com/r/algotrading/comments/13lkikt/features_other_than_ta_indicators_that_are_useful/"]
    }
  ]
}