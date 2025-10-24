20251024 GitHub Quant Research Sweep

Alpha Discovery Report (Equities Only)

Model Run
- Model: GPT-5 Pro
- Reasoning Time: 11m43s

Instructions Compliance
- Task & Scope: Public, testable equity alphas and feature transforms only (single-name stocks, equity ETFs). No crypto/FX/futures-only.
- Source: GitHub-first sweep, with supporting repos/notebooks/papers where appropriate.
- Format: Concise, technical, de-duplicated; each idea includes direct sources, transforms, construction notes, and horizon guidance.

⸻

Report Meta
- Source Searched: GitHub
- Query / Filters: equity alpha research feature engineering orderbook fundamentals repo
- Scan Window: 2012-01-01 - 2025-10-24
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: LOB Microprice–Midprice Divergence (sub-minute drift)

Source(s): mansoor-mamnoon/ml-orderbook (microprice formula & L1/L2 features), nicolezattarin/LOB-feature-analysis, yhf2007/LimitOrderBook_NeuralNetwork (FI-2010/NASDAQ Nordic)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
When the microprice (best bid/ask weighted by queue sizes) deviates from the midquote, the imbalance reflects near-term pressure from the dominant side of the book. Positive microprice–mid spread indicates latent buy pressure and tends to resolve via upticks; negative signals the opposite. This is a liquidity-provision/consumption imbalance signal most effective in high-ADV names around stable spread regimes.

Feature Transformations (bullet list):
- Microprice = (ask₁·bidSize₁ + bid₁·askSize₁) / (bidSize₁ + askSize₁)
- Z-score of (microprice − midquote) over rolling 60–300 ticks (robust clip/median MAD)
- Top-of-book volume imbalance: (bidSize₁ − askSize₁) / (bidSize₁ + askSize₁) with EWMA(λ=0.1) smoothing

Data Dependencies (concise list):
NBBO L1 (bid/ask/size), L2 depth optional, trades/quotes (ITCH/PROPRIETARY), timestamps

Universe & Filters:
US Large-Cap; price > $5; ADV > $20M; spread ≤ 2 ticks; exclude halts/auctions; ignore first/last 5 min

Directionality / Construction Hints:
Cross-sectional ranking of z-scores; long top decile (positive), short bottom decile; beta- and industry-neutral; exit on mean-reversion to midquote or after 60–600s; hard cap on participation (e.g., ≤5 bps ADV)

Strength & Actionability (qualitative only):
Strong – Clear mechanics, public formulas, liquid universe, straightforward tick-level backtest.

Keywords (comma-separated):
microprice, order-book, imbalance, ITCH, intraday

Expected Horizon Notes:
Backtest 2018–2025 using full-tick (ITCH/Nasdaq Basic); live monitor 6 weeks for slippage fill-model calibration

Citations:
- Microprice/imbalance definition and code examples.  ￼
- LOB feature overview and definitions.  ￼
- FI-2010/NASDAQ Nordic LOB dataset usage.  ￼

⸻

Alpha Idea #2: Top-of-Book Queue Imbalance (directional lead)

Source(s): nicolezattarin/LOB-feature-analysis, alpacahq/example-hftish (imbalance-based micro alpha)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Short-horizon returns are positively related to the queue imbalance at the touch. A sustained skew (bidSize₁ » askSize₁ or vice versa) predicts the next few prints via queue priority and depletion dynamics.

Feature Transformations (bullet list):
- Queue imbalance ratio (QIR) = (∑ₗ bidSizeₗ − ∑ₗ askSizeₗ)/(∑ₗ bidSizeₗ + ∑ₗ askSizeₗ), levels l=1..5
- EWMA of QIR with decay ~2–5s; throttle when spread widens
- Microtrend filter: sign(Δmidquote over last 1–3s) to avoid fading momentum spikes

Data Dependencies:
NBBO + L2 book; trade prints; millisecond timestamps

Universe & Filters:
US tickers with spread=1 tick most of the day; ADV > $10M; exclude news halts

Directionality / Construction Hints:
Threshold entry (|QIR|>0.6) with tight time-stop (≤60s) or until QIR mean-reverts; neutralize beta intraday via index micro-hedge

Strength & Actionability:
Promising – Well-known mechanic; execution/latency modeling is the main friction.

Keywords:
queue-imbalance, microstructure, L1/L2, intraday

Expected Horizon Notes:
Intraday 2019–2025; need market-replay or ITCH simulator; 4–6 weeks live-paper validation

Citations:
- LOB features and imbalance definitions.  ￼
- Example imbalance micro alpha (Alpaca).  ￼

⸻

Alpha Idea #3: Order-Flow Imbalance (OFI) & Impact Micro Alpha

Source(s): shubhamcodez/Market-Impact-Model (OFI & impact), bbalouki/itch (Nasdaq ITCH 5.0 parser)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (<1h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Signed order-flow imbalance aggregated in volume time anticipates short-horizon price impact. Normalizing OFI by contemporaneous volatility and spread filters noise and stabilizes cross-sectional comparability.

Feature Transformations:
- OFI over ΔV volume buckets; sign via Lee-Ready or quote rule; z-score by rolling σ(OFI)
- Spread-normalized OFI: OFI / (spread ticks)
- Volume-time bars (e.g., 10k shares) to de-skew event intensity

Data Dependencies:
Full trades/quotes; ITCH or exchange feeds

Universe & Filters:
S&P 500 constituents; price > $10; ADV > $30M

Directionality / Construction Hints:
Enter with OFI z > +2 (long) or < −2 (short); time-stop 30–180s; cap participation; avoid earnings windows

Strength & Actionability:
Strong – Public parsers; portable transforms; easy to validate on liquid US names.

Keywords:
OFI, volume-bars, impact, intraday

Expected Horizon Notes:
ITCH-based backtest 2018–2025; run across rolling regimes; 1 month paper trade

Citations:
- OFI + impact modeling overview.  ￼
- ITCH parser for event reconstruction.  ￼

⸻

Alpha Idea #4: VPIN (Flow Toxicity) + Quote Imbalance Spike

Source(s): theopenstreet/VPIN_HFT  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1–6h)
Signal Type: Microstructure/Order-Flow

Core Idea:
Rising VPIN (volume-synchronized probability of informed trading) indicates toxic order flow and elevated likelihood of directional moves, especially when accompanied by quote imbalance. Combining VPIN with L1 imbalance creates a regime filter to trade only high-informational-flow intervals.

Feature Transformations:
- VPIN computed over volume buckets (e.g., 50k–200k shares)
- Quote imbalance EWMA (2–5min)
- Regime flag: VPIN percentile > 80% & |imbalance| > 0.4

Data Dependencies:
Trades (signed), quotes; volume-bucketed sampling

Universe & Filters:
Mega/large-cap with deep liquidity; exclude opening/closing auctions

Directionality / Construction Hints:
Directional bias follows side of net flow (buys> sells → long); scale down in wide-spread regimes

Strength & Actionability:
Promising – Public code; requires robust classification of trade sign and careful slippage modeling.

Keywords:
VPIN, toxicity, imbalance, intraday

Expected Horizon Notes:
Backtest 2017–2025; live shadow for 4 weeks

Citations:
- VPIN and quote imbalance as predictive signals.  ￼

⸻

Alpha Idea #5: NASDAQ Closing Auction Imbalance (Optiver TAC)

Source(s): liyiyan128/optiver-trading-at-the-close  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap, Equity ETFs (NASDAQ-listed)
Horizon: Intraday (1–6h)
Signal Type: Event-Driven / Microstructure

Core Idea:
Large MOC imbalance relative to typical auction volume predicts price pressure into the close and post-auction mean-reversion. Features engineered around imbalance scale, imbalance direction changes, and indicative match price drift capture flow from indexers and MOC order submission patterns.

Feature Transformations:
- Imbalance% = MOC_imbalance / median(auction_volume_lookback)
- Drift of indicative match price vs. intraday VWAP (ΔIMBPrice)
- “Imbalance flip” count in last 10 min; market beta hedge via synthetic index weights

Data Dependencies:
Official NASDAQ auction fields; L1 quotes; intraday trades

Universe & Filters:
NASDAQ 100 + liquid mid/large caps; ignore days with <p10 auction volume

Directionality / Construction Hints:
Trade with the imbalance into 15:59, unwind across the cross or fade in the first 5–15 min post-close; beta-neutral

Strength & Actionability:
Strong – Public competition dataset and many feature recipes; precise microstructure hooks.

Keywords:
MOC, auction, imbalance, close, intraday

Expected Horizon Notes:
Backtest 2020–2023 TAC; extend to live auctions 2024–2025; 6-week dry-run

Citations:
- TAC dataset, features (weighted WAP, synthetic index weights).  ￼

⸻

Alpha Idea #6: Stock–Synthetic Index Weight Mispricing at the Close

Source(s): liyiyan128/optiver-trading-at-the-close (reconstruct synthetic index weights)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1–6h)
Signal Type: Event-Driven / Relative Value

Core Idea:
Rebuild the synthetic index weights from intraday returns; exploit intraday deviations of single-name closing dynamics from the synthetic index path when MOC imbalances are large. Trade spread: single name vs. index basket into the cross.

Feature Transformations:
- Regress stock on synthetic index returns intraday to infer weight/residual
- Residual z-score in last 15 min; interaction with MOC imbalance sign
- Post-cross mean reversion of residual in first 5 min of aftermarket

Data Dependencies:
Intraday trades/quotes; auction data; index synthetic features

Universe & Filters:
NASDAQ 100; exclude earnings/rebalance days

Directionality / Construction Hints:
Long residual underperformers with same-sign imbalance; short residual outperformers; flatten on cross

Strength & Actionability:
Promising – Robust relative-value framing; needs tight execution controls.

Keywords:
close, synthetic-index, residual, auction

Expected Horizon Notes:
Same as #5; emphasize 2020–2025

Citations:
- Synthetic index weight reconstruction approach.  ￼

⸻

Alpha Idea #7: PEAD – Standardized Earnings Surprise Drift

Source(s): mcravi8/PEAD-mini-WRDS (IBES+CRSP), gen-li/Replicate_PEAD, tradermonty/earnings-trade-backtest  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-/Large-Cap
Horizon: 1–4 Weeks
Signal Type: Event-Driven / Momentum

Core Idea:
Cross-sectionally rank standardized earnings surprises (SUE) at announcement; drift persists post-print as sell-side/allocators update slowly. Combine SUE with abnormal announcement volume and news tone for stronger separation.

Feature Transformations:
- SUE = (EPS_actual − EPS_est) / σ(EPS surprise, 8q)
- Abnormal volume ratio event-day / 60D median
- Post-event suppression of names with guidance uncertainty (keyword counts)

Data Dependencies:
IBES estimates, CRSP prices, earnings calendars; optional news sentiment

Universe & Filters:
US stocks with analyst coverage > 3; price > $5; ADV > $5M

Directionality / Construction Hints:
Long top SUE decile; short bottom; industry-neutral; hold 10–20 trading days; staggered entries

Strength & Actionability:
Strong – Decades of literature; multiple public pipelines to reproduce.

Keywords:
earnings, SUE, event, drift

Expected Horizon Notes:
Backtest 2000–2025; live monitor 8 weeks around quarterly cycles

Citations:
- Minimal IBES/CRSP pipeline.  ￼
- Replication notebooks.  ￼
- Backtest scaffolding.  ￼

⸻

Alpha Idea #8: Analyst EPS Revisions Momentum (IBES)

Source(s): Feng-CityUHK/EquityCharacteristics (Compustat/CRSP/IBES toolkit)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: US Mid-/Large-Cap
Horizon: 1–6 Months
Signal Type: Fundamental / Momentum

Core Idea:
Aggregate 3M net EPS estimate revisions (upgrades − downgrades, value-weighted by analyst reputation or broker) and rank cross-sectionally. Positive net revisions anticipate favorable drift as institutions rebalance.

Feature Transformations:
- Revisions score = Δconsensus_EPS(3M) / |price|, winsorized
- Analyst “quality” weighting; sector-neutral z-scores
- Interaction term with prior 12–1 momentum to avoid crowded longs

Data Dependencies:
IBES summary history; CRSP prices; sector mappings

Universe & Filters:
US names with ≥5 analysts; market cap > $1B

Directionality / Construction Hints:
Monthly rebalance; top/bottom deciles; beta- and industry-neutral

Strength & Actionability:
Promising – Widely used; toolkit eases replication with WRDS.

Keywords:
analyst-revisions, fundamentals, cross-sectional

Expected Horizon Notes:
Backtest 2003–2025 monthly; 3 months live dry-run

Citations:
- Toolkit listing IBES/CRSP characteristics.  ￼

⸻

Alpha Idea #9: Earnings Call LM Lexicon Net Tone (post-call drift)

Source(s): personal-coding/Stock-Earnings-Call-Transcript-NLP (LM lexicon + backtests)  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-/Large-Cap
Horizon: 1–5 Days
Signal Type: Sentiment / Event-Driven

Core Idea:
Compute net positive tone using Loughran–McDonald dictionaries on call transcripts; neutralize by sector and historical tone. Elevated net tone post-call predicts short-horizon outperformance; negative tone the opposite.

Feature Transformations:
- Net tone = (pos − neg)/tokens; exclude stopwords; speaker-tag weighting (CEO/CFO)
- Surprise-adjusted tone: residual from regression on SUE and guidance mentions
- Volume filter: event abnormal volume > 1.5×

Data Dependencies:
Transcripts (SeekingAlpha/Motley Fool), LM lexicon, prices

Universe & Filters:
S&P 1500 with regular earnings calls; English transcripts

Directionality / Construction Hints:
Trade open+1 to +3 sessions; size by tone percentile; industry-neutral

Strength & Actionability:
Promising – Open repo with end‑to‑end scrape/score/backtest scaffolding.

Keywords:
earnings-call, LM-lexicon, sentiment, event

Expected Horizon Notes:
Backtest 2015–2025; 2 earnings seasons live

Citations:
- Project: transcript scraping, LM scoring, and backtesting.  ￼

⸻

Alpha Idea #10: FinBERT Q&A Negativity Differential

Source(s): ProsusAI/FinBERT, cdubiel08/Earnings-Calls-NLP (event windows)  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-/Large-Cap
Horizon: 1–5 Days
Signal Type: Sentiment / Event-Driven

Core Idea:
Compute FinBERT sentiment for Q&A vs. prepared remarks. A large Q&A negativity − prepared spread suggests unexpected concerns surfaced by analysts, predicting short-term underperformance.

Feature Transformations:
- Sent_QA − Sent_Prepared (z-scored within sector and Y/Y)
- Guidance-token detection (e.g., “guide”, “outlook”) as interaction term
- Abnormal return control on event day (CAR[−1,+1])

Data Dependencies:
Call transcripts; FinBERT; event windows

Universe & Filters:
S&P 500; exclude microcaps; English transcripts only

Directionality / Construction Hints:
Short high-spread negatives; long positives; close after 3–5 sessions

Strength & Actionability:
Promising – Clear NLP pipeline; easy to replicate with open models.

Keywords:
FinBERT, earnings-call, sentiment, event

Expected Horizon Notes:
Backtest 2018–2025; 2 seasons live

Citations:
- FinBERT model & docs.  ￼
- Event-return windows used in transcript studies.  ￼

⸻

Alpha Idea #11: Overnight News Sentiment Factor

Source(s): yukit-k/ai-for-trading (factor projects incl. Overnight Sentiment)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Overnight
Signal Type: Sentiment

Core Idea:
Aggregate prior-evening news sentiment into an overnight alpha vector predicting open-to-open returns. Use ticker-level rolling z-scores and sector neutralization to reduce attention/common-mode biases.

Feature Transformations:
- Headline/article sentiment EOD t; z-score by 60D; cap extreme counts
- Attention control: sqrt(news_count) scaling
- Sector/industry residualization

Data Dependencies:
News feed (headline/body); mapping; prices

Universe & Filters:
S&P 500; exclude earnings days

Directionality / Construction Hints:
Cross-sectional long–short; rebalance daily at close; hedge index futures

Strength & Actionability:
Tentative – Requires stable news feed; repo shows scaffolding to build factor.

Keywords:
overnight, news, sentiment, cross-sectional

Expected Horizon Notes:
Backtest 2015–2025; live for 6 weeks due to data latency considerations

Citations:
- Course repo with momentum/overnight factor templates.  ￼

⸻

Alpha Idea #12: One-Day Reversal (Volume-Conditioned)

Source(s): yukit-k/ai-for-trading (short-horizon factors)  ￼
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1–3 Days
Signal Type: Mean-Reversion

Core Idea:
Fade extreme 1D returns when accompanied by elevated volume and no event news, expecting liquidity demand to exhaust. Condition on spread and volatility to avoid trend breaks.

Feature Transformations:
- r₁D/ATR(20) and Vol_ratio = Vol/median(20)
- Filter out earnings/news days and >2σ beta moves
- Entry on next open; exit on VWAP cross or +2 days

Data Dependencies:
OHLCV; calendar/news flags

Universe & Filters:
S&P 1500; price>$5; ADV>$2M; exclude ADRs

Directionality / Construction Hints:
Long worst decile (oversold) and short best decile (overbought); sector-neutral

Strength & Actionability:
Promising – Simple, robust; many public baselines to reproduce.

Keywords:
mean-reversion, volume, short-term

Expected Horizon Notes:
Backtest 2005–2025; 4-week live trial

Citations:
- Factor templates and ranking schemes.  ￼

⸻

Alpha Idea #13: 52‑Week High Breakout (Trend Persistence)

Source(s): StevenDowney86/Public_Research_and_Backtests – “52 Week Break Out Trendfollowing”  ￼
Verification Status: Verified (direct link)
Equity Class: US Mid-/Large-Cap
Horizon: 1–4 Weeks
Signal Type: Momentum

Core Idea:
Names breaking 52‑week highs with confirming breadth/volume show continued demand as constraints/mandates chase leaders. Filter false breakouts with 20D pullback and low short interest.

Feature Transformations:
- Breakout flag: close > max(close,252) * (1+ε) with ε≈0.1%
- Confirmation: 10D up-day breadth > 60%; Vol_ratio > 1.5×
- False-breakout guard: max intra-20D drawdown < 5%

Data Dependencies:
OHLCV; short interest optional

Universe & Filters:
US ex‑microcaps; price>$5

Directionality / Construction Hints:
Enter on close or next open; trailing stop = ATR(14)×k; sector cap per bucket

Strength & Actionability:
Promising – Public notebook; clear, testable transforms.

Keywords:
momentum, breakout, 52-week-high

Expected Horizon Notes:
Backtest 2000–2025; 2 months live shadow

Citations:
- 52-week breakout notebooks.  ￼

⸻

Alpha Idea #14: Turn‑of‑the‑Month / Payday Seasonality (ETFs)

Source(s): paperswithbacktest/awesome-systematic-trading (seasonality entries & QC links)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Equity ETFs (SPY, QQQ, IWM)
Horizon: 1–5 Days
Signal Type: Seasonality/Calendar

Core Idea:
Equity index ETFs exhibit turn‑of‑the‑month and payday effects due to systematic flows (payroll/retirement contributions, rebalancing). Trade short windows around month‑end/start with tight risk controls.

Feature Transformations:
- Calendar dummy windows: D ∈ {−1..+3} around month‑end
- Interaction with realized vol regime (σ₁₀/σ₂₅₀)
- Filter FOMC days / major macro releases

Data Dependencies:
Daily ETF OHLCV; calendar

Universe & Filters:
SPY, QQQ, IWM, sector ETFs with high AUM

Directionality / Construction Hints:
Long at t=−1 to +3 trading days; flatten on VIX spike regimes

Strength & Actionability:
Tentative – Documented, but flow regimes vary; easy to test.

Keywords:
seasonality, ETF, flows, calendar

Expected Horizon Notes:
Backtest 1994–2025; forward test 2 months

Citations:
- Seasonality collection with links to research writeups.  ￼

⸻

Alpha Idea #15: Insider Cluster Buys (Form 4)

Source(s): StevenAdema/sec4-filings-scanner, form‑4 insider analysis gist (fork), Bellingcat/EDGAR CLI  ￼
Verification Status: Verified (direct link)
Equity Class: US Small-/Mid-/Large-Cap
Horizon: 1–4 Weeks
Signal Type: Event-Driven / Fundamental

Core Idea:
Clustered insider open‑market buys (multiple officers/directors within 30 days) scaled by float predict positive drift as signals align and liquidity is thin. Exclude 10b5‑1 plans and very small purchases.

Feature Transformations:
- Insider buy $sum / float mktcap (winsorized)
- Cluster count in 30D; role weights (CEO/CFO>director)
- Exclude option exercises & gifts; eliminate penny stocks

Data Dependencies:
SEC Form 4 (EDGAR), float, prices

Universe & Filters:
US equities price>$3; ADV>$1M

Directionality / Construction Hints:
Cross-sectional long rank on scaled cluster buys; 20 trading day hold; industry-neutral

Strength & Actionability:
Promising – Public scrapers; straightforward event logic; low turnover.

Keywords:
insiders, Form4, event, drift

Expected Horizon Notes:
Backtest 2012–2025; live 2 months

Citations:
- Scanner for Form 4 details.  ￼
- Tutorial/analysis notebook fork.  ￼
- EDGAR CLI for retrieval.  ￼

⸻

Alpha Idea #16: Short Interest / Days‑to‑Cover Shock

Source(s): asxshorts-examples (shorting dataset pipelines), jaycode/short_sale_volume (pipeline setup)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: Global Developed (adaptable to US via FINRA/Nasdaq)
Horizon: 1–4 Weeks
Signal Type: Event-Driven / Sentiment

Core Idea:
Spikes in days‑to‑cover (short interest / ADV) combined with rising borrow fees predict asymmetric moves: squeeze risk after positive catalysts; downside drift absent catalysts as constraints bind.

Feature Transformations:
- ΔDays‑to‑cover z-score (3M)
- Borrow fee percentile (if available)
- Catalyst guard: exclude imminent earnings/MA

Data Dependencies:
Short interest feeds (FINRA/ASX), volume, borrow fee; prices

Universe & Filters:
US/Global Developed; price>$5

Directionality / Construction Hints:
Two‑sided: long high DTC names on positive news surprise (squeeze), short otherwise; hold 5–20d

Strength & Actionability:
Tentative – Data quality key; examples show pipelines to adapt.

Keywords:
short-interest, DTC, borrow, squeeze

Expected Horizon Notes:
Backtest 2014–2025 monthly; monitor 6 weeks live

Citations:
- ASX shorts usage examples.  ￼
- Short sale volume pipeline.  ￼

⸻

Alpha Idea #17: Value Investors Club (VIC) Publication Attention Effect

Source(s): dschonholtz/ValueInvestorsClub (timing study)  ￼
Verification Status: Verified (direct link)
Equity Class: US Small-/Mid-/Large-Cap
Horizon: 1–4 Weeks
Signal Type: Event-Driven / Alternative Data

Core Idea:
VIC idea postings, especially contest winners/best ideas, generate attention and subsequent flow. Long (short) bias for long (short) theses immediately post-publication with time‑limited horizon.

Feature Transformations:
- Binary event = VIC post time; rank by “winner/score”
- Abnormal turnover and spread on T+1
- Sentiment extraction from thesis text (optional)

Data Dependencies:
VIC posts (scraped), prices/volume

Universe & Filters:
US liquid names; exclude micro illiquids

Directionality / Construction Hints:
Enter on post; hold 5–20 sessions; hedge beta; tight stop for shorts

Strength & Actionability:
Promising – Open analysis indicates concentrated alpha immediately post‑post.

Keywords:
attention, VIC, event, alternative-data

Expected Horizon Notes:
Backtest 2008–2024 posts; live 2 months

Citations:
- Empirical timing analysis around VIC posts.  ￼

⸻

Alpha Idea #18: Accruals Anomaly (Low Accruals → Higher Returns)

Source(s): paperswithbacktest/awesome-systematic-trading (Accrual Anomaly entry)  ￼
Verification Status: Partially Verified (secondary references)
Equity Class: US Mid-/Large-Cap
Horizon: 1–6 Months
Signal Type: Fundamental

Core Idea:
Rank working capital + depreciation accruals scaled by assets; lower accruals imply higher earnings quality and subsequent returns. Combine with profitability and investment for robustness.

Feature Transformations:
- Total accruals = (ΔCA − ΔCash − ΔCL + ΔSTD − Depreciation) / Total Assets
- Sector‑neutral z‑scores; winsorize 1/99
- Interaction with gross profitability (see #19)

Data Dependencies:
Compustat fundamentals; prices

Universe & Filters:
US ex‑financials/REITs; mcap > $1B

Directionality / Construction Hints:
Quarterly rebalance; long low‑accrual decile; short high‑accrual decile

Strength & Actionability:
Promising – Canonical accounting signal; straightforward implementation.

Keywords:
accruals, accounting, quality

Expected Horizon Notes:
Backtest 1990–2025 quarterly; 2 quarters live

Citations:
- Curated reference list with strategy pointers.  ￼

⸻

Alpha Idea #19: Gross Profitability & Quality Composite

Source(s): JerBouma/FinanceToolkit (ratios & fundamentals), ArturSepp/QuantInvestStrats (QIS notebooks/tools)  ￼
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1–6 Months
Signal Type: Fundamental / Cross-Sectional Composite

Core Idea:
Cross‑sectional quality sort combining gross profitability, leverage, and earnings stability captures persistent mispricing from constraints and mandates favoring “quality at reasonable price”.

Feature Transformations:
- GP/A, ROA, Net debt/EBITDA (winsorized), accrual quality
- Composite via rank average; sector‑neutral z-scores
- Optional macro regime filter via realized vol

Data Dependencies:
Financial statements; ratios; prices

Universe & Filters:
Large/mid caps; ex‑financials when leverage used

Directionality / Construction Hints:
Quarterly rebalance; long top‑quality; short bottom; beta‑neutral

Strength & Actionability:
Strong – Public toolkits expose all components; durable cross‑sectional edge.

Keywords:
quality, profitability, leverage, composite

Expected Horizon Notes:
Backtest 1990–2025; 2 quarters live

Citations:
- Open-source ratios and docs.  ￼
- QIS notebooks/utilities for factor analysis.  ￼

⸻

Alpha Idea #20: GTJA‑191 Technical Factor Ensemble (rank‑blend)

Source(s): shrektan/techfactor (GTJA‑191 alphas implemented), microsoft/qlib (factor libraries & data flow)  ￼
Verification Status: Verified (direct link)
Equity Class: Global Developed / Global Emerging
Horizon: 1–4 Weeks
Signal Type: Cross-Sectional Composite

Core Idea:
Blend a subset of GTJA‑191 price/volume nonlinear transforms (e.g., decaylinear, tsrank interactions of VWAP, intraday highs/lows, and volume) into a rank-composite. Enforce sector neutrality and turnover constraints.

Feature Transformations:
- Select ~20 orthogonal GTJA signals (low intra‑correlation)
- Rank‑average with volatility scaling; rebalance weekly
- Turnover penalty & neutralization to sector/beta

Data Dependencies:
OHLCV, intraday VWAP; corporate actions

Universe & Filters:
Top 1000 global developed names by ADV; price>$3

Directionality / Construction Hints:
Weekly cross‑sectional long–short; cap idiosyncratic risk per name

Strength & Actionability:
Strong – Public implementations; flexible ensemble design.

Keywords:
GTJA‑191, composite, technical, cross‑sectional

Expected Horizon Notes:
Backtest 2010–2025 weekly; 8 weeks live paper

Citations:
- Full set of GTJA‑191 implementations.  ￼
- Qlib pipeline for factor research/production.  ￼

⸻

Notes on Deduplication
- Auction/close variants (#5 vs #6): Kept both; one treats imbalance momentum into the cross; the other trades residual vs synthetic index.
- Earnings text (#9 vs #10): Distinct signals: dictionary net tone vs FinBERT Q&A differential.
- Microstructure (#1–#4): Each relies on different feature families—microprice divergence, queue imbalance, OFI, VPIN—to avoid overlap.
- Fundamentals (#18–#19) vs GTJA composite (#20): Accounting vs. price/volume composites; complementary.

⸻

JSON Export (structured payload)

{
  "meta": {
    "source_searched": "GitHub",
    "query": "equity alpha research feature engineering orderbook fundamentals repo",
    "scan_window": "2012-01-01 - 2025-10-24",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "LOB Microprice–Midprice Divergence (sub-minute drift)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Microprice (size-weighted best bid/ask) diverging from midquote reflects latent pressure from the dominant side of the book; the divergence tends to resolve via short-horizon price moves.",
      "feature_transformations": [
        "Microprice vs midquote difference; rolling z-score over 60–300 ticks",
        "Top-of-book volume imbalance with EWMA smoothing (λ≈0.1)",
        "Spread/volatility regime filter"
      ],
      "data_dependencies": ["NBBO L1", "optional L2 depth", "trades/quotes (ITCH)", "timestamps"],
      "universe_filters": "US large-cap; price > $5; ADV > $20M; spread ≤ 2 ticks; exclude halts and first/last 5 minutes",
      "directionality": "Cross-sectional rank; long positive z-scores, short negative; beta/industry neutral; exit on reversion or 60–600s time-stop",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Clear mechanism, public formulas, liquid universe and standard replay/backtest workflow"
      },
      "keywords": ["microprice", "order-book", "imbalance", "ITCH", "intraday"],
      "expected_horizon_notes": "Backtest 2018–2025 full-tick; 6 weeks live monitoring for execution/slippage calibration",
      "citations": [
        "https://github.com/mansoor-mamnoon/ml-orderbook",
        "https://github.com/nicolezattarin/LOB-feature-analysis",
        "https://github.com/yhf2007/LimitOrderBook_NeuralNetwork"
      ]
    },
    {
      "title": "Top-of-Book Queue Imbalance (directional lead)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Sustained queue imbalance at the touch anticipates near-term directional prints as one side of the book depletes faster.",
      "feature_transformations": [
        "Queue imbalance ratio across L1–L5; EWMA(2–5s)",
        "Microtrend filter using short midquote slope",
        "Spread-widening suppressor"
      ],
      "data_dependencies": ["NBBO", "L2 depth", "trade prints"],
      "universe_filters": "High-liquidity US names; spread=1 tick majority of day; ADV > $10M",
      "directionality": "Threshold entries (|QIR|>0.6), exit ≤60s or on reversion; beta-hedged intraday",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Well-documented imbalance mechanic; execution latency is primary friction"
      },
      "keywords": ["queue-imbalance", "microstructure", "L1/L2", "intraday"],
      "expected_horizon_notes": "Intraday 2019–2025; validate with market replay",
      "citations": [
        "https://github.com/nicolezattarin/LOB-feature-analysis",
        "https://github.com/alpacahq/example-hftish"
      ]
    },
    {
      "title": "Order-Flow Imbalance (OFI) & Impact Micro Alpha",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (<1h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Volume-time aggregated signed order-flow imbalance predicts short-horizon price impact; normalize by spread/volatility for cross-name comparability.",
      "feature_transformations": [
        "OFI over fixed volume buckets; rolling z-score",
        "Spread-normalized OFI = OFI / spread (ticks)",
        "Volume-time bars to stabilize event intensity"
      ],
      "data_dependencies": ["Trades", "Quotes", "ITCH or exchange feeds"],
      "universe_filters": "S&P 500; price> $10; ADV > $30M",
      "directionality": "Enter on OFI z>2 (long) or <−2 (short); time-stop 30–180s; avoid earnings windows",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Public parsers and clear transforms; robust on liquid names"
      },
      "keywords": ["OFI", "volume-bars", "impact", "intraday"],
      "expected_horizon_notes": "2018–2025 ITCH; 1-month paper trade",
      "citations": [
        "https://github.com/shubhamcodez/Market-Impact-Model",
        "https://github.com/bbalouki/itch"
      ]
    },
    {
      "title": "VPIN (Flow Toxicity) + Quote Imbalance Spike",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "High VPIN percentiles, especially with concurrent quote imbalance, flag informed-flow regimes and directional pressure.",
      "feature_transformations": [
        "VPIN in volume-time; 80th percentile regime flag",
        "EWMA quote imbalance (2–5 min)",
        "Conjunction rule: VPIN high & |imb|>0.4"
      ],
      "data_dependencies": ["Trades (signed)", "Quotes"],
      "universe_filters": "Mega/large caps; exclude auctions",
      "directionality": "Trade with net flow direction; scale down in wide spread regimes",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Open implementation; needs careful trade-sign logic"
      },
      "keywords": ["VPIN", "toxicity", "imbalance", "intraday"],
      "expected_horizon_notes": "2017–2025; 4-week shadow",
      "citations": ["https://github.com/theopenstreet/VPIN_HFT"]
    },
    {
      "title": "NASDAQ Closing Auction Imbalance (Optiver TAC)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Event-Driven",
      "core_idea": "Large market-on-close imbalance relative to typical auction volume drives predictable pressure into the cross and partial mean-reversion after.",
      "feature_transformations": [
        "Imbalance% vs median auction volume",
        "Indicative match price drift vs intraday VWAP",
        "Imbalance flip counts in last 10 minutes"
      ],
      "data_dependencies": ["NASDAQ auction fields", "L1 quotes", "intraday prints"],
      "universe_filters": "NASDAQ 100 + liquid mid/large caps; exclude thin auctions",
      "directionality": "Trade with imbalance into 15:59; fade partially post-cross; beta-hedged",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Public dataset and feature recipes enable precise replication"
      },
      "keywords": ["MOC", "auction", "imbalance", "close", "intraday"],
      "expected_horizon_notes": "2020–2023 dataset; extend to 2024–2025 live",
      "citations": [
        "https://github.com/liyiyan128/optiver-trading-at-the-close"
      ]
    },
    {
      "title": "Stock–Synthetic Index Residual Mispricing at the Close",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Event-Driven",
      "core_idea": "Reconstruct synthetic index weights intraday; trade single-name residual vs index into the cross when imbalance is large.",
      "feature_transformations": [
        "Intraday regression to infer stock weight in synthetic index",
        "Residual z-score in last 15 min",
        "Interaction with imbalance sign"
      ],
      "data_dependencies": ["Intraday returns", "auction data", "index synthetic"],
      "universe_filters": "NASDAQ 100; exclude rebalance/earnings",
      "directionality": "Long underperforming residuals (same-sign imbalance); short outperformers",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear RV construction; execution key"
      },
      "keywords": ["close", "residual", "synthetic-index", "auction"],
      "expected_horizon_notes": "Align with TAC sample; forward test 6 weeks",
      "citations": ["https://github.com/liyiyan128/optiver-trading-at-the-close"]
    },
    {
      "title": "Post‑Earnings Announcement Drift (SUE-ranked)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Cross-sectional ranking on standardized earnings surprises shows persistent post-event drift as investors update slowly.",
      "feature_transformations": [
        "SUE over 8 quarters",
        "Abnormal volume ratio on event day",
        "Guidance-uncertainty penalty"
      ],
      "data_dependencies": ["IBES estimates", "CRSP prices", "earnings calendar"],
      "universe_filters": "US names with >3 analysts; price>$5",
      "directionality": "Long top SUE decile; short bottom; hold 10–20 days; industry neutral",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Multiple public pipelines enable replication"
      },
      "keywords": ["earnings", "SUE", "event", "drift"],
      "expected_horizon_notes": "2000–2025; 8-week live monitor",
      "citations": [
        "https://github.com/mcravi8/PEAD-mini-WRDS",
        "https://github.com/gen-li/Replicate_PEAD",
        "https://github.com/tradermonty/earnings-trade-backtest"
      ]
    },
    {
      "title": "Analyst EPS Revisions Momentum (IBES)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "3‑month net EPS estimate revisions predict forward returns as allocators rebalance toward improving names.",
      "feature_transformations": [
        "ΔConsensus EPS(3M) scaled; analyst quality weights",
        "Sector-neutral z-scores",
        "Interaction with 12–1 momentum"
      ],
      "data_dependencies": ["IBES", "CRSP", "sector classification"],
      "universe_filters": "≥5 analysts; mcap > $1B",
      "directionality": "Monthly long–short; beta/industry neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Toolkit eases WRDS workflows; well-documented factor"
      },
      "keywords": ["analyst-revisions", "fundamental", "cross-sectional"],
      "expected_horizon_notes": "2003–2025 monthly; 3 months live",
      "citations": [
        "https://github.com/Feng-CityUHK/EquityCharacteristics"
      ]
    },
    {
      "title": "Earnings Call LM Lexicon Net Tone",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-5 Days",
      "signal_type": "Sentiment",
      "core_idea": "Net positive tone in call transcripts (LM dictionaries) predicts short-horizon drift; adjust for event severity and guidance mentions.",
      "feature_transformations": [
        "Net tone = (pos − neg)/tokens",
        "Speaker-weighted scoring (CEO/CFO emphasis)",
        "Event abnormal volume filter"
      ],
      "data_dependencies": ["Transcripts", "LM lexicon", "prices"],
      "universe_filters": "S&P 1500; English transcripts",
      "directionality": "Long high-tone; short low-tone; 1–3 day hold",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Open pipeline from scrape to backtest"
      },
      "keywords": ["earnings-call", "lexicon", "sentiment"],
      "expected_horizon_notes": "2015–2025; 2 seasons live",
      "citations": [
        "https://github.com/personal-coding/Stock-Earnings-Call-Transcript-Natural-Language-Processing"
      ]
    },
    {
      "title": "FinBERT Q&A Negativity Differential",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-5 Days",
      "signal_type": "Sentiment",
      "core_idea": "Q&A sentiment more negative than prepared remarks signals unexpected concerns; short-term underperformance ensues.",
      "feature_transformations": [
        "FinBERT sentiment for Q&A vs prepared",
        "Guidance keyword interaction",
        "CAR[−1,+1] control"
      ],
      "data_dependencies": ["Transcripts", "FinBERT", "prices"],
      "universe_filters": "S&P 500",
      "directionality": "Short large negative spread; long positive",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear, testable differential; public model"
      },
      "keywords": ["FinBERT", "earnings-call", "sentiment"],
      "expected_horizon_notes": "2018–2025; 2 seasons",
      "citations": [
        "https://github.com/ProsusAI/finBERT",
        "https://github.com/cdubiel08/Earnings-Calls-NLP"
      ]
    },
    {
      "title": "Overnight News Sentiment Factor",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Overnight",
      "signal_type": "Sentiment",
      "core_idea": "Aggregate prior-evening news sentiment into a cross-sectional alpha vector predicting open-to-open returns.",
      "feature_transformations": [
        "Headline/body sentiment z-scored by 60D",
        "Attention control via sqrt(news_count)",
        "Sector residualization"
      ],
      "data_dependencies": ["News feed", "prices"],
      "universe_filters": "S&P 500; exclude earnings",
      "directionality": "Daily long–short at close; hedge beta",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Data feed stability required; template exists"
      },
      "keywords": ["overnight", "news", "sentiment"],
      "expected_horizon_notes": "2015–2025; 6-week live",
      "citations": [
        "https://github.com/yukit-k/ai-for-trading"
      ]
    },
    {
      "title": "One-Day Reversal (Volume-Conditioned)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-3 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "Fade extreme 1D moves when volume is elevated and no event is present; mean-reversion in liquidity shocks.",
      "feature_transformations": [
        "r1D/ATR(20) and Vol_ratio vs 20D",
        "Exclude earnings/news days",
        "Exit on VWAP cross or 2 days"
      ],
      "data_dependencies": ["OHLCV", "news flags"],
      "universe_filters": "S&P 1500; ADV > $2M",
      "directionality": "Long worst decile; short best decile; sector-neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Robust baseline with public templates"
      },
      "keywords": ["mean-reversion", "volume", "short-term"],
      "expected_horizon_notes": "2005–2025; 4-week pilot",
      "citations": [
        "https://github.com/yukit-k/ai-for-trading"
      ]
    },
    {
      "title": "52‑Week High Breakout (Trend Persistence)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Momentum",
      "core_idea": "Names breaking 52‑week highs with confirming breadth/volume continue to attract flows; filter false breakouts.",
      "feature_transformations": [
        "Close > 252D max * (1+ε)",
        "Up-day breadth and volume confirmations",
        "False-breakout guard via recent drawdown"
      ],
      "data_dependencies": ["OHLCV"],
      "universe_filters": "US ex-microcaps; price>$5",
      "directionality": "Enter on breakout; ATR trailing stops; sector caps",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear transforms; open notebook"
      },
      "keywords": ["momentum", "breakout", "52-week-high"],
      "expected_horizon_notes": "2000–2025; 2 months",
      "citations": [
        "https://github.com/StevenDowney86/Public_Research_and_Backtests"
      ]
    },
    {
      "title": "Turn-of-the-Month / Payday Seasonality (ETFs)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (SPY/QQQ/IWM)",
      "horizon": "1-5 Days",
      "signal_type": "Seasonality/Calendar",
      "core_idea": "Index ETFs show month-end/start and payday flow patterns; exploit with short windows and risk filters.",
      "feature_transformations": [
        "Calendar dummy windows around month-end",
        "Volatility regime interaction",
        "Exclude macro/FOMC days"
      ],
      "data_dependencies": ["ETF OHLCV", "calendar"],
      "universe_filters": "High AUM ETFs",
      "directionality": "Long around turn; flatten in high VIX",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Effect size time-varying; trivial to test"
      },
      "keywords": ["seasonality", "ETF", "flows", "calendar"],
      "expected_horizon_notes": "1994–2025; 2 months",
      "citations": [
        "https://github.com/paperswithbacktest/awesome-systematic-trading"
      ]
    },
    {
      "title": "Insider Cluster Buys (Form 4)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Multiple insider open-market buys within 30 days scaled by float predict positive drift.",
      "feature_transformations": [
        "Scaled insider buy value / float cap",
        "Cluster count and role weights",
        "Exclude 10b5-1/option-related"
      ],
      "data_dependencies": ["SEC Form 4", "float", "prices"],
      "universe_filters": "US price>$3; ADV>$1M",
      "directionality": "Long high scaled cluster buys; 20D hold",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Open scrapers and filters available"
      },
      "keywords": ["insiders", "Form4", "event", "drift"],
      "expected_horizon_notes": "2012–2025; 2 months live",
      "citations": [
        "https://github.com/StevenAdema/sec4-filings-scanner",
        "https://gist.github.com/firmai/0e2bd233af4a0406a6b2fe4a4a4e1e8b",
        "https://github.com/bellingcat/EDGAR"
      ]
    },
    {
      "title": "Short Interest / Days-to-Cover Shock",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Global Developed",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Spikes in days-to-cover and borrow costs predict squeezes after positive catalysts and negative drift absent catalysts.",
      "feature_transformations": [
        "ΔDays-to-cover z-score (3M)",
        "Borrow fee percentile",
        "Catalyst filter (earnings/MA)"
      ],
      "data_dependencies": ["Short interest", "volume", "borrow fee", "prices"],
      "universe_filters": "Price>$5",
      "directionality": "Two-sided conditional on catalyst",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Data availability/quality dependent; examples exist"
      },
      "keywords": ["short-interest", "borrow", "squeeze"],
      "expected_horizon_notes": "2014–2025; 6 weeks",
      "citations": [
        "https://github.com/ay-mich/asxshorts-examples",
        "https://github.com/jaycode/short_sale_volume"
      ]
    },
    {
      "title": "Value Investors Club Publication Attention Effect",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Alternative Data",
      "core_idea": "VIC posts—especially winners—induce short-horizon attention flows; trade in thesis direction over limited windows.",
      "feature_transformations": [
        "Event time from post; winner flag",
        "Abnormal turnover on T+1",
        "Optional text sentiment of thesis"
      ],
      "data_dependencies": ["VIC posts", "prices/volume"],
      "universe_filters": "Liquid US names; exclude illiquid microcaps",
      "directionality": "Enter at publish; hold 5–20 sessions; hedge beta",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Open analysis suggests concentrated effect"
      },
      "keywords": ["attention", "VIC", "event"],
      "expected_horizon_notes": "2008–2024; 2 months",
      "citations": [
        "https://github.com/dschonholtz/ValueInvestorsClub"
      ]
    },
    {
      "title": "Accruals Anomaly (Low Accruals → Higher Returns)",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "Low total accruals scaled by assets signal higher earnings quality and subsequent returns; combine with profitability for robustness.",
      "feature_transformations": [
        "Total accruals formula (scaled)",
        "Sector-neutral ranks; winsorize outliers",
        "Composite with profitability and investment"
      ],
      "data_dependencies": ["Compustat", "prices"],
      "universe_filters": "Ex-financials/REITs; mcap>$1B",
      "directionality": "Quarterly long low-accruals; short high",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Canonical, simple to reproduce"
      },
      "keywords": ["accruals", "quality", "fundamental"],
      "expected_horizon_notes": "1990–2025; 2 quarters",
      "citations": [
        "https://github.com/paperswithbacktest/awesome-systematic-trading"
      ]
    },
    {
      "title": "Gross Profitability & Quality Composite",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-6 Months",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Blend gross profitability, leverage, and earnings stability into a sector-neutral composite; tilt toward high-quality names.",
      "feature_transformations": [
        "GP/A, ROA, leverage, accrual quality",
        "Rank-average; volatility scaling",
        "Turnover penalty"
      ],
      "data_dependencies": ["Financial statements", "ratios", "prices"],
      "universe_filters": "Mid/Large caps; ex-financials if leverage used",
      "directionality": "Quarterly long top-quality; short bottom",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Public toolkits and notebooks cover required metrics"
      },
      "keywords": ["quality", "profitability", "composite"],
      "expected_horizon_notes": "1990–2025; 2 quarters",
      "citations": [
        "https://github.com/JerBouma/FinanceToolkit",
        "https://github.com/ArturSepp/QuantInvestStrats"
      ]
    },
    {
      "title": "GTJA‑191 Technical Factor Ensemble",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-4 Weeks",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Rank-blend a diversified subset of GTJA‑191 technical alphas (VWAP/HL/volume nonlinears); sector-neutral with turnover controls.",
      "feature_transformations": [
        "Select ~20 low-correlation GTJA signals",
        "Rank-average with vol scaling",
        "Sector/beta neutralization; weekly rebalance"
      ],
      "data_dependencies": ["OHLCV", "VWAP", "corporate actions"],
      "universe_filters": "Top 1000 by ADV; price>$3",
      "directionality": "Weekly long–short composite",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Open implementations; flexible ensemble design"
      },
      "keywords": ["GTJA-191", "technical", "composite"],
      "expected_horizon_notes": "2010–2025; 8 weeks paper",
      "citations": [
        "https://github.com/shrektan/techfactor",
        "https://github.com/microsoft/qlib"
      ]
    }
  ]
}
