20251024 Twitter Alpha Hunters Deep Dive

Alpha Discovery Report (Equities Only)

Model Run
- Model: GPT-5 Pro
- Reasoning Time: 12m54s

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
- Source Searched: Twitter/X (https://x.com)
- Query / Filters: equity alpha signal feature engineering backtest order flow -crypto
- Scan Window: 2017-01-01 - 2025-10-24
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: SPY Opening-Range / Intraday Momentum from AAD(OPEN) Breakout

Source(s): @ConcretumR tweet (May 2024), Paper PDF (Barbon et al., 2025), Article + code, Follow‑up code note incl. gap‑revert filter, Community implementation (QuantConnect)   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY)
Horizon: Intraday (1-6h)
Signal Type: Momentum

Core Idea (2-4 sentences):
Define an adaptive intraday breakout threshold using the trailing average absolute deviation from the open (AAD(OPEN), e.g., 14 sessions). Enter with the first 5–15m range expansion exceeding a multiple of AAD(OPEN), optionally filtered by pre-open gap context. The strategy exploits intraday persistence and liquidity herding around the open.

Feature Transformations (bullet list):
- AAD(OPEN,14) = mean(|price_t − open|) over last 14 sessions; trigger if |price−open| > k·AAD
- 5–15m Opening Range Breakout with volume confirmation vs. 20‑day intraday volume baseline
- Gap-reversion veto: fade filter if pre‑open gap z‑score < −1 reverts within first 30m (disable pro‑trend entries)

Data Dependencies (concise list):
1‑min/5‑min OHLCV, pre‑market prints/indications, opening range bars

Universe & Filters:
SPY only; trade during regular hours; skip major halts; avoid high‑impact scheduled data drops within first 10 minutes

Directionality / Construction Hints:
Long/short breakouts; flat by session close; stop = trailing multiple of AAD; avoid overlapping positions; no overnight

Strength & Actionability (qualitative only):
Strong – Full public paper + implementation notes and multiple replications; simple inputs and abundant liquidity on SPY.

Keywords (comma-separated):
intraday, opening-range, momentum, SPY, adaptive-threshold, gap

Expected Horizon Notes:
Backtest 2018–2025 on 1‑min; walk‑forward by year; live shadow trade 6 weeks

Citations:
- ConcretumR tweet announcing code release and model scope
- Paper (Barbon, Zarattini et al.) detailing methodology and robustness
- Concretum Group how‑to posts (+ gap reversion)
- QuantConnect community implementation and notes

⸻

Alpha Idea #2: Night‑vs‑Day Drift—Long Overnight / Manage Intraday

Source(s): Sentiment/overnight drift tweet example, “SPY returns: Overnight vs Intraday” tweet, NY Fed staff report on overnight drift in equity futures, JOIM: Overnight drift—drivers & retail activity, AdvisorPerspectives summary   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY; extend to QQQ/IWM)
Horizon: Overnight
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Systematically hold index ETFs only from close→next open and minimize intraday exposure. The edge is attributed to liquidity provision and risk‑transfer dynamics during off‑hours and European open. Add cross‑sectional overlays to select constituents with persistent positive overnight profiles.

Feature Transformations (bullet list):
- Overnight return z‑score vs. 60‑day ATR to size exposure
- Intraday volume‑shape feature (U‑shape vs. L‑shape) as an overnight signal enhancer
- Calendar controls (pre‑FOMC, earnings weeks) as regime dummies

Data Dependencies (concise list):
Daily OHLCV; intraday volume curves for shape classification

Universe & Filters:
SPY/QQQ/IWM; optionally S&P‑500 constituents with ADV > $10M

Directionality / Construction Hints:
Hold long overnight; neutralize market beta intraday (e.g., futures hedge); cut if overnight gap exceeds k·ATR

Strength & Actionability (qualitative only):
Promising – Strong descriptive evidence and macro microstructure rationale; requires careful intraday hedging.

Keywords (comma-separated):
overnight, seasonality, ETF, volume-shape

Expected Horizon Notes:
Backtest 1993–2025 daily; add 2–5y intraday for shape features; 8 weeks live monitor

Citations:
- Tweets visualizing night vs day split
- NY Fed & JOIM research on overnight drift

⸻

Alpha Idea #3: Post‑Earnings Announcement Drift (PEAD) with Surprise Normalization

Source(s): PEAD explainer tweet, PEAD thread, Earnings Whispers note   ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-Cap, US Large-Cap
Horizon: 1-4 Weeks
Signal Type: Event-Driven

Core Idea (2-4 sentences):
Go long firms with large positive standardized earnings surprises and high post‑print volume; short large negative surprise names. Drift persists due to under‑reaction and slow information diffusion, strongest where coverage is thin and frictions are higher.

Feature Transformations (bullet list):
- SUE = (EPS_actual − EPS_est) / σ(estimate errors, 8q)
- Drift filter: post‑earnings day return > 1.5·industry σ and abnormal volume > 2× 60‑day median
- Industry‑neutral rank; exclude guidance confounders on the same day

Data Dependencies (concise list):
I/B/E/S or equivalent, OHLCV, corporate actions, earnings calendar

Universe & Filters:
US stocks price > $3; ADV > $2M; exclude ADRs

Directionality / Construction Hints:
Cross‑sectional long‑short on SUE ranks; hold 10–20 trading days; beta/industry neutral

Strength & Actionability (qualitative only):
Strong – Decades of literature plus continuous practitioner threads; straightforward to implement.

Keywords (comma-separated):
earnings, drift, event, SUE, cross‑sectional

Expected Horizon Notes:
Backtest 2005–2025; quarterly rolling; 2 earnings seasons live

Citations:
- Multiple PEAD tweet threads and practitioner notes

⸻

Alpha Idea #4: FOMC “Fed Day” Effect—Buy Day‑Before, Exit After Announcement

Source(s): QuantInsti tweet referencing Fed‑day backtest, Quantra glossary – Fed Day effect (rules), Quantra overview page   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY; sector ETFs for tilt)
Horizon: 1-3 Days
Signal Type: Event-Driven / Seasonality

Core Idea (2-4 sentences):
Enter SPY 1 day before the scheduled FOMC decision and exit near the post‑announcement close. Tendency for positive return around policy announcements aligns with “don’t fight the Fed” and reduced uncertainty premia.

Feature Transformations (bullet list):
- Calendar join: map FOMC decision dates to trading sessions
- Optional trend filter (SPY > SMA(100))
- Sector tilt: overweight high beta (e.g., XLK/XLY) on high‑probability “pause/cut” regimes

Data Dependencies (concise list):
Daily OHLCV; FOMC calendar; sector ETF data

Universe & Filters:
SPY base; liquid sector ETFs; avoid days with unscheduled Fed events

Directionality / Construction Hints:
Long‑only; full exit EOD; maximum 8–10 events/year reduces turnover

Strength & Actionability (qualitative only):
Promising – Clear rules and accessible calendars; infrequent trades reduce frictions.

Keywords (comma-separated):
FOMC, event, seasonality, ETF

Expected Horizon Notes:
Backtest 1993–2025; event‑study framework; 6 months live observation

Citations:
- QuantInsti/Quantra links with explicit rule set

⸻

Alpha Idea #5: Turn‑of‑the‑Month (ToM) Effect in ETFs and Sectors

Source(s): CXO Advisory ToM tweet/post, Quantra course page listing ToM strategy, @quantpedia ToM mention   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (broad + sectors)
Horizon: 1-5 Days
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Equity returns concentrate near month‑end and early next month. Exploit via ToM windows on SPY/sector ETFs, optionally trend‑filtered or volatility‑scaled.

Feature Transformations (bullet list):
- ToM dummy: trade sessions D−1…D+3 around last trading day
- Volatility targeting via 20‑day realized vol
- Sector momentum overlay: long sectors with positive 63‑day relative strength entering ToM

Data Dependencies (concise list):
Daily OHLCV; trading‑calendar metadata

Universe & Filters:
SPY + liquid sector ETFs; exclude rebalance/holiday distortions where needed

Directionality / Construction Hints:
Long‑only; equal weight across ETFs or tilt by prior momentum; exit after D+3

Strength & Actionability (qualitative only):
Promising – Widely documented effect; ETF implementation is straightforward.

Keywords (comma-separated):
seasonality, ToM, ETF, sectors

Expected Horizon Notes:
Backtest 1993–2025; include sector ETFs since 1998+; 3 ToM cycles live

Citations:
- CXO, Quantra/QuantInsti, Quantpedia references

⸻

Alpha Idea #6: Post‑Lunch Positive Shift (“Lunch Effect”) Intraday Mean Reversion

Source(s): Quantpedia: Lunch Effect in U.S. Indexes   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY/QQQ)
Horizon: Intraday (<1h)
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
Index returns show a distinct positive drift immediately after lunch. Fade midday weakness into the 13:00–13:30 ET window and exit by 14:30–15:00 ET.

Feature Transformations (bullet list):
- Intraday return z‑score over last 20 sessions at minute‑bucket level
- VWAP deviation at 13:00 ET as entry qualifier
- Exclude days with FOMC/major macro at 14:00 ET

Data Dependencies (concise list):
1‑min OHLCV; sessionized time features

Universe & Filters:
SPY/QQQ; avoid early close days

Directionality / Construction Hints:
Long‑bias mean‑reversion; risk via ATR‑scaled stops

Strength & Actionability (qualitative only):
Tentative – Effect is subtle; requires careful slippage modeling.

Keywords (comma-separated):
intraday, seasonality, mean‑reversion

Expected Horizon Notes:
Backtest 2018–2025 minute bars; 4 weeks live

Citations:
- Quantpedia strategy note

⸻

Alpha Idea #7: Overnight Gap Fade in First 30 Minutes

Source(s): Concretum Group note—gap typically reverts in first 30m   ￼
Verification Status: Verified (direct link)
Equity Class: Equity ETFs (SPY)
Horizon: Intraday (<1h)
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Large pre‑open gaps in SPY revert partially during the first 30m as liquidity is restored and overnight imbalances clear. Fade extreme gaps relative to ATR with VWAP magnet as target.

Feature Transformations (bullet list):
- Gap% / ATR(20) z‑score threshold
- Opening auction to first‑print slippage proxy
- VWAP deviation as exit/partial target

Data Dependencies (concise list):
Pre‑market prints; 1‑min OHLCV; VWAP

Universe & Filters:
SPY; exclude macro event days; skip if opening range immediately expands > k·ATR

Directionality / Construction Hints:
Contrarian entry on extreme gaps; hard stop at opening range extremes

Strength & Actionability (qualitative only):
Promising – Simple, liquid, repeatedly observed on public datasets.

Keywords (comma-separated):
gap, mean‑reversion, intraday, VWAP

Expected Horizon Notes:
Backtest 2018–2025; 1‑min bars; 6 weeks live

Citations:
- Concretum Group applied note

⸻

Alpha Idea #8: Analyst EPS Revision Momentum → Short‑Horizon Stock Returns

Source(s): B. Caughran (ex‑DE Shaw/Citadel) on EPS revisions driving returns   ￼
Verification Status: Partially Verified (secondary references)
Equity Class: US Large-Cap, US Mid-Cap
Horizon: 1-4 Weeks
Signal Type: Fundamental

Core Idea (2-4 sentences):
Stocks with accelerating positive EPS revisions (FY1/FY2) tend to outperform over the next few weeks as consensus catches up and PMs rebalance. Negative revision streaks underperform.

Feature Transformations (bullet list):
- Net revisions count and magnitude (ΔCons_FY1, ΔFY2) over past 20 trading days
- Revision‑surprise rank normalized by industry
- Combine with drift filter post‑print days

Data Dependencies (concise list):
Consensus estimates history (I/B/E/S/Refinitiv), OHLCV

Universe & Filters:
S&P 1500; price > $5; ADV > $5M

Directionality / Construction Hints:
Cross‑sectional long‑short; beta/industry neutral; weekly rebalance

Strength & Actionability (qualitative only):
Strong – Well‑known sell‑side signal; operationally clean with consensus feeds.

Keywords (comma-separated):
revisions, fundamentals, cross‑sectional

Expected Horizon Notes:
Backtest 2010–2025; rolling 4‑week live

Citations:
- Practitioner thread highlighting deterministic linkage

⸻

Alpha Idea #9: Insider Buying Clusters—Executive‑Cohort Credibility Filter

Source(s): “When Are Insider Purchases Credible?” (Beneish & Markarian, 2023), “Information Content of Insider Trades—Whose Trades Matter and When?”, Insider transaction abnormal returns (various)   ￼
Verification Status: Verified (direct link)
Equity Class: US Small-Cap, US Mid-Cap
Horizon: 1-6 Months
Signal Type: Fundamental / Event-Driven

Core Idea (2-4 sentences):
Concentrated insider purchase clusters by multiple executives, with higher personal wealth risk borne by insiders, predict positive abnormal returns. Filter out noisy single trades and overweight “credible” clusters.

Feature Transformations (bullet list):
- Cluster intensity: count of unique insiders + $volume over 30d window
- Credibility score: Δinsider delta/vega exposure post‑purchase (proxy by option holdings)
- Exclude heavy options market activity pre‑trade (dampener per recent SSRN evidence)

Data Dependencies (concise list):
Form 4/5 filings, insider positions/options, OHLCV, option volume

Universe & Filters:
US listed; price > $3; ADV > $1M; exclude microcaps with illiquid filings

Directionality / Construction Hints:
Long‑only baskets; 3–6m hold; sector‑neutral

Strength & Actionability (qualitative only):
Promising – Strong academic backing; requires data plumbing for filings.

Keywords (comma-separated):
insiders, clusters, fundamentals, event

Expected Horizon Notes:
Backtest 2005–2025; monitor continuously; 3 months live

Citations:
- SSRN papers on credibility and cluster effects

⸻

Alpha Idea #10: 52‑Week‑High Proximity (PTH) as Momentum Proxy

Source(s): George & Hwang (2004) paper PDF, SSRN page, Tweet noting 52‑week effect usage   ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap, US Mid-Cap
Horizon: 1-6 Months
Signal Type: Momentum

Core Idea (2-4 sentences):
Nearness to 52‑week high explains a large share of momentum profits and improves upon past‑return ranks. Buy names near highs, sell those far from highs, industry‑neutral.

Feature Transformations (bullet list):
- PTH = price / 52‑week high; rank‑invert for longs
- Combine with 6‑12m momentum for composite score
- Volatility cap via 60‑day σ

Data Dependencies (concise list):
Daily OHLCV; corporate actions

Universe & Filters:
S&P 1500; price > $5; ADV > $5M

Directionality / Construction Hints:
Cross‑sectional long‑short; monthly rebalance; sector‑neutral

Strength & Actionability (qualitative only):
Strong – Robust across markets with simple data.

Keywords (comma-separated):
momentum, 52‑week, cross‑sectional

Expected Horizon Notes:
Backtest 1995–2025; monthly; 8 weeks live

Citations:
- Foundational paper + supportive tweet

⸻

Alpha Idea #11: Options‑Expiration (OPEX) Week Monday Bias

Source(s): The Robust Trader account noting OPEX Monday rule   ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY)
Horizon: 1-3 Days
Signal Type: Seasonality/Calendar

Core Idea (2-4 sentences):
During OPEX week, Monday sessions following a 5‑day high close show a positive bias in SPY due to dealer positioning and gamma decay. Trade only when prior‑week momentum set‑up exists.

Feature Transformations (bullet list):
- OPEX calendar flag (3rd Friday) → Monday filter
- Prior 5‑day breakout condition at Friday close
- Optional VIX regime filter (VIX < 20)

Data Dependencies (concise list):
Daily OHLCV; options expiration calendar; VIX

Universe & Filters:
SPY only; avoid FOMC‑adjacent OPEX weeks

Directionality / Construction Hints:
Long Monday open→close or Fri close→Mon close

Strength & Actionability (qualitative only):
Tentative – Requires careful regime conditioning; sparse events.

Keywords (comma-separated):
OPEX, seasonality, ETF

Expected Horizon Notes:
Backtest 2005–2025; event‑study; 3 months live

Citations:
- Practitioner source flagging the rule of thumb

⸻

Alpha Idea #12: Intraday Volume‑Shape Predicts Overnight Returns

Source(s): SSRN: Overnight Returns and the Timing of Trading Volume (Perreten, 2024)   ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Overnight
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
U‑shaped intraday activity (high open + high close volume) forecasts stronger next‑overnight returns than L‑shaped activity. Cross‑sectionally rank stocks by intraday volume‑shape metrics and allocate overnight.

Feature Transformations (bullet list):
- Volume‑shape index = (vol_open + vol_close) / total intraday volume
- Interaction with prior overnight momentum for composite score
- Liquidity floor (ADV, spread) constraints

Data Dependencies (concise list):
1‑min volume bars; daily returns

Universe & Filters:
S&P 500; ADV > $10M; spread < 20 bps

Directionality / Construction Hints:
Rank‑long top decile, short bottom decile overnight; beta‑neutral

Strength & Actionability (qualitative only):
Promising – Fresh academic evidence; implementable with standard intraday feeds.

Keywords (comma-separated):
overnight, microstructure, volume‑shape, cross‑sectional

Expected Horizon Notes:
Backtest 2008–2025; 6 weeks live

Citations:
- SSRN paper with construction details

⸻

Notes on Deduplication
- ORB/AAD(OPEN) and gap‑fade are related to opening dynamics but use distinct entry logic; kept separate.
- PEAD and EPS‑revision momentum overlap on earnings information; PEAD uses realized surprise, Revisions use forward estimate changes; both retained with clear distinctions.
- Night‑vs‑Day and Volume‑shape overnight signals differ: one is allocation timing, the other is cross‑sectional stock selection.

⸻

JSON Export Schema (append after the markdown sections)

{
  "meta": {
    "source_searched": "Twitter/X (https://x.com)",
    "query": "equity alpha signal feature engineering backtest order flow -crypto",
    "scan_window": "2017-01-01 - 2025-10-24",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "SPY Opening-Range / Intraday Momentum from AAD(OPEN) Breakout",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY)",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Momentum",
      "core_idea": "Adaptive intraday breakout on SPY using trailing AAD(OPEN) to set expansion thresholds; optionally condition on pre-open gap context to avoid fades. Captures early-session persistence and liquidity herding.",
      "feature_transformations": [
        "AAD(OPEN,14) trigger: |price−open| > k·AAD",
        "5–15m Opening Range Breakout with volume confirmation vs 20-day baseline",
        "Gap-reversion veto when pre-open gap z-score < -1 reverts within 30m"
      ],
      "data_dependencies": ["1-min/5-min OHLCV", "pre-market prints/indications"],
      "universe_filters": "SPY only; regular hours; skip macro minutes",
      "directionality": "Long/short breakouts; flat by close; ATR/AAD stops",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Paper + code + replications; liquid and simple to execute."
      },
      "keywords": ["intraday", "opening-range", "momentum", "SPY", "adaptive-threshold", "gap"],
      "expected_horizon_notes": "Backtest 2018–2025 1-min; walk-forward by year; 6 weeks live shadow",
      "citations": [
        "https://x.com/ConcretumR/status/1799083286175641781",
        "https://www.alexandria.unisg.ch/bitstreams/a99aba00-f967-49b3-aceb-f544dc386e0b/download",
        "https://concretumgroup.com/python-backtesting-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/",
        "https://concretumgroup.com/backtesting-7-years-of-free-data-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/",
        "https://www.quantconnect.com/forum/discussion/17091/beat-the-market-an-effective-intraday-momentum-strategy-for-s-amp-p500-etf-spy/"
      ]
    },
    {
      "title": "Night-vs-Day Drift—Long Overnight / Manage Intraday",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY; extend QQQ/IWM)",
      "horizon": "Overnight",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Hold index ETFs only from close to next open; avoid intraday exposure. Overnight drift aligns with liquidity provision dynamics and European hours; enhance with cross-sectional features to select stocks with persistent positive overnight profiles.",
      "feature_transformations": [
        "Overnight return z-score vs 60-day ATR",
        "Intraday volume-shape feature (U vs L) as enhancer",
        "Calendar regime dummies (pre-FOMC, earnings weeks)"
      ],
      "data_dependencies": ["Daily OHLCV", "Intraday volume curves"],
      "universe_filters": "SPY/QQQ/IWM; S&P 500 constituents ADV > $10M for cross-section",
      "directionality": "Long overnight; optional intraday beta-hedge; gap-based risk cuts",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Strong descriptive studies; implementable with standard data; hedge design matters."
      },
      "keywords": ["overnight", "seasonality", "ETF", "volume-shape"],
      "expected_horizon_notes": "Backtest 1993–2025 daily + 2–5y intraday for shape; 8 weeks live",
      "citations": [
        "https://x.com/ftr_investors/status/1905922267843871124",
        "https://x.com/SJosephBurns/status/1061620773939494912",
        "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf",
        "https://www.joim.com/wp-content/uploads/emember/downloads/P0753.pdf",
        "https://www.advisorperspectives.com/articles/2022/06/24/night-moves-is-the-overnight-drift-the-grandmother-of-all-market-anomalies"
      ]
    },
    {
      "title": "PEAD with Standardized Surprise & Volume Confirmation",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Long high SUE winners with abnormal post-print volume; short negative surprises. Drift persists due to under-reaction and attention limits.",
      "feature_transformations": [
        "SUE normalized by historical analyst error volatility (8q)",
        "Abnormal volume > 2× 60-day median as confirmation",
        "Industry-neutral rank; exclude same-day guidance confounders"
      ],
      "data_dependencies": ["I/B/E/S or equivalent", "OHLCV"],
      "universe_filters": "US stocks price > $3; ADV > $2M; exclude ADRs",
      "directionality": "Cross-sectional long-short; 10–20 trading day holds",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Deep literature + repeated practitioner guidance; clear data needs."
      },
      "keywords": ["earnings", "drift", "event", "SUE", "cross-sectional"],
      "expected_horizon_notes": "Backtest 2005–2025; 2 seasons live",
      "citations": [
        "https://x.com/sai_shankarg/status/1980630043165683977",
        "https://x.com/NSuresh_ECW/status/1944885606338978066",
        "https://x.com/eWhispers/status/1970476319424049531"
      ]
    },
    {
      "title": "FOMC Day Effect—Buy Day-Before, Exit Announcement Close",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY)",
      "horizon": "1-3 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Systematically own SPY into scheduled FOMC decisions and exit same day after the statement. Reduced uncertainty and accommodative bias support short-window returns.",
      "feature_transformations": [
        "Calendar join to FOMC dates",
        "Trend filter (SMA(100) > 0)",
        "Sector tilt overlay in high-probability pause/cut regimes"
      ],
      "data_dependencies": ["Daily OHLCV", "FOMC calendar"],
      "universe_filters": "SPY + liquid sectors",
      "directionality": "Long-only; event-limited exposure",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Simple, low-trade-frequency seasonality with public calendars."
      },
      "keywords": ["FOMC", "event", "seasonality", "ETF"],
      "expected_horizon_notes": "Backtest 1993–2025 event-study; 6 months live",
      "citations": [
        "https://x.com/QuantInsti/status/1937465741361520893",
        "https://quantra.quantinsti.com/glossary/Is-There-an-Opportunity-to-Trade-Around-FED-Meetings",
        "https://quantra.quantinsti.com/glossary/Fed-day-effect"
      ]
    },
    {
      "title": "Turn-of-the-Month (ToM) Effect for SPY and Sector ETFs",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY + Sectors)",
      "horizon": "1-5 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Allocate into month-end and early next month sessions where equity returns cluster. Use trend and vol targeting for robustness.",
      "feature_transformations": [
        "ToM dummy D-1…D+3",
        "Vol targeting by 20d realized vol",
        "Sector momentum overlay (63d)"
      ],
      "data_dependencies": ["Daily OHLCV", "Trading calendar"],
      "universe_filters": "SPY + sectors; liquid ETFs only",
      "directionality": "Long-only; exit after D+3",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Well-documented; ETF implementation is operationally simple."
      },
      "keywords": ["seasonality", "ToM", "ETF", "sectors"],
      "expected_horizon_notes": "Backtest 1993–2025; 3 ToM cycles live",
      "citations": [
        "https://x.com/CXOAdvisory/status/1977676698390073702",
        "https://quantra.quantinsti.com/course/event-driven-trading-strategies",
        "https://x.com/quantpedia/status/1980186994098544679"
      ]
    },
    {
      "title": "Post-Lunch Positive Shift Intraday Mean Reversion",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY/QQQ)",
      "horizon": "Intraday (<1h)",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Exploit the positive post-lunch drift by buying into midday weakness and exiting into early afternoon.",
      "feature_transformations": [
        "Minute-bucket z-scores vs 20-session history",
        "VWAP deviation at 13:00 ET as qualifier",
        "Macro-event exclusion filter"
      ],
      "data_dependencies": ["1-min OHLCV"],
      "universe_filters": "SPY/QQQ; avoid early-close days",
      "directionality": "Long bias; ATR-scaled stops",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Effect size modest; slippage control critical."
      },
      "keywords": ["intraday", "seasonality", "mean-reversion"],
      "expected_horizon_notes": "Backtest 2018–2025 minute bars; 4 weeks live",
      "citations": ["https://quantpedia.com/lunch-effect-in-the-u-s-stock-market-indices/"]
    },
    {
      "title": "Overnight Gap Fade in First 30 Minutes",
      "verification_status": "Verified (direct link)",
      "equity_class": "Equity ETFs (SPY)",
      "horizon": "Intraday (<1h)",
      "signal_type": "Mean-Reversion",
      "core_idea": "Fade extreme pre-open gaps that partially revert as liquidity normalizes during the first 30 minutes.",
      "feature_transformations": [
        "Gap% / ATR(20) threshold",
        "Opening-range extreme as stop",
        "VWAP magnet exit"
      ],
      "data_dependencies": ["Pre-market prints", "1-min OHLCV", "VWAP"],
      "universe_filters": "SPY; skip macro days",
      "directionality": "Contrarian; flat by 10:00 ET",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Simple, frequent set-ups; well-documented behavior."
      },
      "keywords": ["gap", "mean-reversion", "intraday", "VWAP"],
      "expected_horizon_notes": "Backtest 2018–2025 1-min; 6 weeks live",
      "citations": [
        "https://concretumgroup.com/backtesting-7-years-of-free-data-beat-the-market-an-effective-intraday-momentum-strategy-for-the-sp500-etf-spy/"
      ]
    },
    {
      "title": "Analyst EPS Revision Momentum (Short-Horizon)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Fundamental",
      "core_idea": "Accelerating positive FY1/FY2 EPS revisions predict near-term outperformance; negative streaks underperform.",
      "feature_transformations": [
        "Net revisions count & magnitude in trailing 20d",
        "Industry-neutral z-scores of Δconsensus",
        "Combine with post-earnings drift filter"
      ],
      "data_dependencies": ["Estimates history (I/B/E/S/Refinitiv)", "OHLCV"],
      "universe_filters": "S&P 1500; price > $5; ADV > $5M",
      "directionality": "Cross-sectional long-short; weekly rebalance",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Broad practitioner use; clean data plumbing."
      },
      "keywords": ["revisions", "fundamentals", "cross-sectional"],
      "expected_horizon_notes": "Backtest 2010–2025; 4-week live",
      "citations": ["https://x.com/FundamentEdge/status/1700232675477618707"]
    },
    {
      "title": "Insider Buying Clusters with Credibility Screen",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "Multiple-executive purchase clusters where insiders increase personal wealth exposure predict positive abnormal returns; avoid noisy single trades.",
      "feature_transformations": [
        "Cluster intensity: unique insiders + $volume over 30 days",
        "Credibility proxy via insider delta/vega change",
        "Options-flow pre-trade dampener"
      ],
      "data_dependencies": ["SEC Forms 4/5", "Insider holdings/options", "OHLCV", "Options volume"],
      "universe_filters": "US listed; price > $3; ADV > $1M",
      "directionality": "Long-only baskets; 3–6m hold; sector neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Robust academic backing; requires filings pipeline."
      },
      "keywords": ["insiders", "clusters", "event", "fundamentals"],
      "expected_horizon_notes": "Backtest 2005–2025; 3 months live",
      "citations": [
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3478344",
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3077389",
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=677442"
      ]
    },
    {
      "title": "52-Week-High Proximity (PTH) Momentum",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Momentum",
      "core_idea": "Nearness to 52-week high dominates traditional momentum for forecasting returns; buy near highs, sell far-from-highs.",
      "feature_transformations": [
        "PTH = price / 52-week high; long highest ranks",
        "Composite with 12-1 momentum",
        "Volatility cap via 60d sigma"
      ],
      "data_dependencies": ["Daily OHLCV"],
      "universe_filters": "S&P 1500; price > $5; ADV > $5M",
      "directionality": "Cross-sectional long-short; monthly rebalance",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Extensively replicated; trivial data requirements."
      },
      "keywords": ["momentum", "52-week", "cross-sectional"],
      "expected_horizon_notes": "Backtest 1995–2025; 8 weeks live",
      "citations": [
        "https://www.bauer.uh.edu/tgeorge/papers/gh4-paper.pdf",
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1104491",
        "https://x.com/alojoh/status/1979743876408647988"
      ]
    },
    {
      "title": "OPEX Week Monday Bias with Prior 5‑Day High",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (SPY)",
      "horizon": "1-3 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "During options-expiration week, Monday after a 5-day high close tends to lean positive due to dealer gamma dynamics.",
      "feature_transformations": [
        "OPEX calendar flag",
        "Prior 5-day breakout condition",
        "VIX regime filter"
      ],
      "data_dependencies": ["Daily OHLCV", "OPEX calendar", "VIX"],
      "universe_filters": "SPY",
      "directionality": "Long Monday; or Fri close→Mon close",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Sparse but tradable; needs robust event controls."
      },
      "keywords": ["OPEX", "seasonality", "ETF"],
      "expected_horizon_notes": "Backtest 2005–2025; 3 months live",
      "citations": [
        "https://x.com/robusttrader"
      ]
    },
    {
      "title": "Intraday Volume-Shape → Overnight Cross-Section",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Overnight",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Stocks with U-shaped intraday volume profiles deliver higher subsequent overnight returns than L-shaped profiles; build an overnight long-short on shape ranks.",
      "feature_transformations": [
        "Volume-shape index = (vol_open + vol_close) / intraday total",
        "Interaction with prior overnight momentum",
        "Liquidity floor (ADV, spread)"
      ],
      "data_dependencies": ["1-min volume bars", "Daily returns"],
      "universe_filters": "S&P 500; ADV > $10M; spread < 20 bps",
      "directionality": "Rank-long top decile, short bottom decile; beta-neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "New evidence; implementable with standard intraday feeds."
      },
      "keywords": ["overnight", "microstructure", "volume-shape", "cross-sectional"],
      "expected_horizon_notes": "Backtest 2008–2025; 6 weeks live",
      "citations": [
        "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5004991"
      ]
    }
  ]
}