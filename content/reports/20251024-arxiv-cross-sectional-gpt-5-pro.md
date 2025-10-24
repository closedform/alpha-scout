20251024 arXiv & SSRN Cross-Sectional Alpha Review

Alpha Discovery Report (Equities Only)

Model Run
- Model: GPT-5 Pro
- Reasoning Time: 17m00s

Instructions Followed
- Sources scanned: arXiv and SSRN (papers, working papers).
- Scope: single-name equities and equity ETFs only (no crypto/FX-only/futures-only).
- Output: concrete, testable signal ideas with direct links and feature transforms.
- Deduplicated: near-duplicates merged; variants kept only when horizon/features meaningfully differ.
- Judgments: qualitative only; no performance estimates.

⸻

Report Meta
- Source Searched: arXiv (https://arxiv.org) and SSRN (https://ssrn.com)
- Query / Filters: cross-sectional equity anomaly feature engineering factor discovery SSRN
- Scan Window: 2005-01-01 - 2025-10-24
- Exclusions Applied: Crypto and digital assets
- Date of Report: 2025-10-24

⸻

Alpha Idea #1: Intraday vs. Overnight Mispricing Split

Source(s): Bogousslavsky (2020/2021) “The Cross-Section of Intraday and Overnight Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: Intraday (1-6h) and Overnight
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Arbitrage capital is constrained overnight (margin, borrow fees), so mispricing strategies earn during the day and fade into the close; overnight risk premia differ from intraday premia cross-sectionally. Build separate daytime and overnight legs for the same characteristic and exploit their predictable divergence. This clarifies why many anomalies weaken near the close and re-emerge overnight. See the cited paper for construction details and cross-sectional patterns.  ￼

Feature Transformations (bullet list):
- For a characteristic X (e.g., value, mispricing composite), compute day return and overnight return legs separately; rank-normalize both cross-sectionally each day.
- Intraday-minus-Overnight spread: z(X){\text{day}} - z(X){\text{overnight}}.
- Systematic-variance split: estimate rolling CAPM beta separately for intraday vs. overnight windows; use ratio \sigma^2_{\text{overnight}}/\sigma^2_{\text{day}} as a conditioning feature.

Data Dependencies (concise list):
OHLCV with open/close stamps, intraday bars, borrow/fee calendar (for interpretation), market beta estimates.

Universe & Filters:
US top 1000 by ADV; price > $3; ADV > $5M; exclude ADRs/OTC.

Directionality / Construction Hints:
Cross-sectional ranks; neutralize by industry and beta; long positive intraday leg where overnight drag is highest; flatten into close and re-enter on open.

Strength & Actionability (qualitative only):
Promising – Clear, testable split using standard data; turnover management required around open/close.

Keywords (comma-separated):
overnight, intraday, mispricing, day–night split, beta

Expected Horizon Notes:
Backtest 2010–2025 with minute bars; live monitor 6 weeks around opens/closes.

Citations:
- Bogousslavsky, “The Cross-Section of Intraday and Overnight Returns.” https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2869624

⸻

Alpha Idea #2: Single-Stock VRP Adjusted for Turnover Shocks

Source(s): Eksi & Roy (2025) “Stock Return Predictability of Realized–Implied Volatility Spread and Abnormal Turnover” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-6 Months
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
The single-stock variance risk premium (VRP = realized − implied vol) predicts returns, but the signal is contaminated when realized vol is temporarily elevated by turnover shocks. Mean-reversion-correct realized vol before differencing with implied vol, or downweight observations with abnormal turnover, to restore predictability cross-sectionally.  ￼

Feature Transformations (bullet list):
- RVol* = realized vol with exponential mean-reversion correction to a 60d median.
- VRP* = \( \text{RVol\*} - \text{IVol}_{30d} \) from ATM options.
- Turnover shock filter: indicator \mathbb{1}(\text{Turnover} > \mu+2\sigma); set VRP* = NaN or shrink by factor in these states.

Data Dependencies (concise list):
Daily realized vol from intraday bars; option IV (30D ATM); daily turnover.

Universe & Filters:
US optionable names; price > $5; ADV > $10M.

Directionality / Construction Hints:
Cross-sectional rank long high VRP*, short low; beta/industry neutral; monthly rebalance.

Strength & Actionability (qualitative only):
Promising – Well-specified fix to a known options–equity link; needs options data but fully replicable.

Keywords (comma-separated):
VRP, implied vol, realized vol, turnover, options

Expected Horizon Notes:
Backtest 2012–2025; monthly refresh; live 8 weeks pilot.

Citations:
- Eksi & Roy (2025). https://ssrn.com/abstract=5234112

⸻

Alpha Idea #3: Weekly Realized Skewness as Cross-Sectional Predictor

Source(s): Amaya, Christoffersen, Jacobs & Vasquez (2015) “Does Realized Skewness Predict the Cross-Section of Equity Returns?” (SSRN/JFE)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-5 Days
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Stocks with high recent realized skewness underperform in the following week; realized kurtosis shows weaker positive relation. Compute realized higher moments from intraday returns and sort cross-sectionally each week.  ￼

Feature Transformations (bullet list):
- Realized skewness (weekly) from 5-min returns; winsorize extremes.
- Skew z-score cross-sectionally; optional sector-neutral z.
- Composite skew–kurtosis score: -z(\text{skew}) + 0.25\,z(\text{kurt}).

Data Dependencies (concise list):
Intraday bars, corporate action adjustments.

Universe & Filters:
Top 1500 by ADV; price > $3.

Directionality / Construction Hints:
Rank long lowest-skew quintile, short highest; weekly rebalance; beta/industry neutral.

Strength & Actionability (qualitative only):
Strong – Clear recipe, high-frequency data available, short holding period manageable.

Keywords (comma-separated):
realized skewness, intraday, weekly, higher moments

Expected Horizon Notes:
Backtest 2012–2025; weekly recompute; 8-week live shadow.

Citations:
- Amaya et al. (2015). https://ssrn.com/abstract=1898735

⸻

Alpha Idea #4: Downside Semivariance Ratio (RDRS) for Drawdown Aversion

Source(s): Thomas (2024/2025) “New Measures for Forecasting Downside Risk” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1-6 Months
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Downside risk dominates investor preferences; ratio of downside realized semivariance to total realized variance (RDRS) forecasts adverse outcomes and supports a cross-sectional tilt toward lower RDRS names. Use high-frequency semivariances to build a risk-aware stock selector.  ￼

Feature Transformations (bullet list):
- RDRS(60d) = \text{RSV}^{-}/(\text{RSV}^{-}+\text{RSV}^{+}) using 5–15m bars.
- Trend-adjusted RDRS: de-mean by sector-time average; z-score.
- Optional downside beta overlay vs. market drawdowns.

Data Dependencies (concise list):
Intraday returns, market index returns.

Universe & Filters:
Developed large/mid caps; price > $5; ADV > $5M.

Directionality / Construction Hints:
Rank long low RDRS, short high; rebalance monthly; neutralize by country/sector.

Strength & Actionability (qualitative only):
Promising – Technically precise and robust concept; HF data needed.

Keywords (comma-separated):
downside risk, semivariance, intraday, drawdown

Expected Horizon Notes:
Backtest 2015–2025; monthly rebalance; 12-week live trial.

Citations:
- Thomas (2024/2025). https://ssrn.com/abstract=4867217

⸻

Alpha Idea #5: Expected Growth (q5) as a Cross-Sectional Factor

Source(s): Hou, Mo, Xue & Zhang (2020) “An Augmented q-Factor Model with Expected Growth” (SSRN); Hou et al. (2018) “q5” (NBER/SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: >6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
Cross-sectional expected investment growth, forecast from firm fundamentals (q, OCF, ΔROE), earns a persistent premium not subsumed by common factor models. Construct an Expected Growth score and tilt long-high vs. short-low.  ￼

Feature Transformations (bullet list):
- Cross-sectional ML/regression forecast of next-12m Δ(Investment/Assets) using: log Tobin’s q, OCF/Assets, ΔROE, accruals.
- EG score = model prediction percentile; industry-neutral z-score.
- Combine with profitability and investment for a q5 composite.

Data Dependencies (concise list):
Quarterly fundamentals (Compustat/XBRL), market cap, prices.

Universe & Filters:
Developed markets; exclude financials/REITs; price > $5.

Directionality / Construction Hints:
Annual/semiannual rebalance; risk/beta neutral; capacity-friendly.

Strength & Actionability (qualitative only):
Strong – Clear recipe from peer-reviewed literature; uses widely available fundamentals.

Keywords (comma-separated):
expected growth, investment, profitability, q-factor

Expected Horizon Notes:
Backtest 2005–2025; semiannual refresh; 6–12m holds.

Citations:
- Hou et al. (2020). https://ssrn.com/abstract=3525435
- Hou et al. (2018). https://ssrn.com/abstract=3191167

⸻

Alpha Idea #6: Quality-Minus-Junk (QMJ) Composite

Source(s): Asness, Frazzini & Pedersen (2019/2017) “Quality Minus Junk” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: >6 Months
Signal Type: Cross-Sectional Composite

Core Idea (2-4 sentences):
Quality firms (safe, profitable, growing, well governed) command only modestly higher prices; long-high-quality minus short-low-quality earns a premium globally. Build a multi-pillar score from profitability, growth, safety, and payout.  ￼

Feature Transformations (bullet list):
- Profitability: Gross profits-to-assets; ROA; margins.
- Growth: ΔGP/Assets, ΔROA.
- Safety: low leverage, earnings volatility, beta.
- Payout: net issuance (negative is higher quality).
- Rank-average pillars into QMJ score; industry-neutral.

Data Dependencies (concise list):
Quarterly/annual fundamentals; price/beta; share issuance.

Universe & Filters:
Global ex-fin/REIT; market cap > $500M; ADV > $2M.

Directionality / Construction Hints:
Rebalance quarterly; long top decile QMJ, short bottom; beta neutral.

Strength & Actionability (qualitative only):
Strong – Widely replicated; straightforward construction.

Keywords (comma-separated):
quality, profitability, safety, payout, composite

Expected Horizon Notes:
Backtest 2005–2025; quarterly refresh; run live 3 months.

Citations:
- Asness et al. (2019/2017). https://ssrn.com/abstract=2312432

⸻

Alpha Idea #7: Gross Profitability (GP/A)

Source(s): Novy-Marx (2013/2010) “Good Growth and the Gross Profitability Premium” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: >6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
Gross profits scaled by assets predict the cross-section of returns, often subsuming many earnings-based anomalies. Prefer GP/A over bottom-line metrics to avoid accounting noise.  ￼

Feature Transformations (bullet list):
- GP/A with seasonal lag; winsorize by industry.
- GP/A trend: Δ(GP/A) over 4Q.
- Combine with investment (asset growth) for quality-growth balance.

Data Dependencies (concise list):
Fundamentals (rev, COGS, assets).

Universe & Filters:
Ex-fin/REIT; cap > $300M; ADV > $1M.

Directionality / Construction Hints:
Rank long high GP/A; neutralize by industry; quarterly rebal.

Strength & Actionability (qualitative only):
Strong – Simple and robust across regions.

Keywords (comma-separated):
profitability, fundamentals, quality

Expected Horizon Notes:
Backtest 2005–2025; quarterly updates.

Citations:
- Novy-Marx. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1598056

⸻

Alpha Idea #8: Asset Growth / Investment-to-Assets (Inv/A)

Source(s): Hou, Xue & Zhang stream (digesting anomalies, q-factors)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: >6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
Higher recent asset growth (investment) predicts lower future returns cross-sectionally, consistent with investment-based asset pricing. Use balance-sheet growth as a parsimonious negative signal.  ￼

Feature Transformations (bullet list):
- Inv/A = (Total assets_t − Total assets_{t−1}) / assets_{t−1}.
- Net issuance overlay to avoid dilution traps.
- Sector-relative z-score; combine with profitability.

Data Dependencies (concise list):
Quarterly fundamentals, shares outstanding.

Universe & Filters:
Ex-fin; cap > $300M.

Directionality / Construction Hints:
Short high Inv/A; long low; quarterly rebalance.

Strength & Actionability (qualitative only):
Strong – Long-horizon, capacity-friendly.

Keywords (comma-separated):
investment, asset growth, fundamentals

Expected Horizon Notes:
Backtest 2005–2025; semiannual holds.

Citations:
- Hou et al. “Digesting Anomalies.” https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2508322

⸻

Alpha Idea #9: Equity Loan Fee / Borrow Cost Tilt

Source(s): Engelberg et al. (2024) “The Loan Fee Anomaly” (SSRN); Hendrix & Crabb (2020) “Borrowing Fees and Expected Stock Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1-4 Weeks
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
High stock-loan fees embed contemporaneous shorting demand and predict underperformance over short horizons; persistence of high fees is itself informative. Use fee level and change to rank cross-sectionally and time entries.  ￼

Feature Transformations (bullet list):
- Fee level z(7d) and ΔFee(7d); composite score z+\frac{1}{2}\Delta z.
- DTC-adjusted: interact with days-to-cover to proxy “squeeze” risk.
- Tradeability filter: exclude fee > 500 bps annualized for cost control.

Data Dependencies (concise list):
Securities lending fees, short interest, turnover.

Universe & Filters:
Cap > $1B; lendable; ADV > $5M.

Directionality / Construction Hints:
Short high-fee, long low-fee; weekly rebalance; tight borrow management.

Strength & Actionability (qualitative only):
Strong – Direct microstructure price-of-arbitrage signal with short horizon.

Keywords (comma-separated):
shorting, loan fee, borrow, microstructure

Expected Horizon Notes:
Backtest 2012–2025 where fee data available; weekly.

Citations:
- Engelberg et al. (2024). https://papers.ssrn.com/sol3/Delivery.cfm/3707166.pdf?abstractid=3707166
- Hendrix & Crabb (2020). https://ssrn.com/abstract=3726227

⸻

Alpha Idea #10: Days-to-Cover (DTC) Short Interest

Source(s): Hong et al. (2015) “Days to Cover and Stock Returns” (NBER/SSRN)
Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: 1-4 Weeks
Signal Type: Microstructure/Order-Flow

Core Idea (2-4 sentences):
Days-to-cover (short interest scaled by turnover) better captures marginal cost of shorting than raw short interest and predicts poor future returns for high-DTC names. Combine with liquidity to isolate costly-to-arbitrage stocks.  ￼

Feature Transformations (bullet list):
- DTC = shares short / ADV(30d); z-score sector-neutral.
- Interaction: DTC × Amihud to isolate illiquid squeezes.
- Change in DTC over 1–2 weeks as entry timing.

Data Dependencies (concise list):
Short interest, daily volume, price.

Universe & Filters:
US 1,000–3,000 by cap; exclude microcaps < $300M.

Directionality / Construction Hints:
Short high-DTC quintile vs. long low; weekly rebalance.

Strength & Actionability (qualitative only):
Strong – Public, simple construction, consistent interpretation.

Keywords (comma-separated):
short interest, days-to-cover, liquidity

Expected Horizon Notes:
Backtest 2006–2025; 1–4w holds.

Citations:
- Hong et al. (2015). https://ssrn.com/abstract=2607356

⸻

Alpha Idea #11: MAX / β–MAX (Lottery Preference Control)

Source(s): Bali et al. (2009/2010) “Maxing Out” (NBER/SSRN); Ince & Ozsoylev (2024/2025) “Re-examination of the MAX Anomaly” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Small-Cap
Horizon: 1-4 Weeks
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Stocks with extreme single-day winners in the last month (MAX) subsequently underperform; adjusting MAX for market beta (β–MAX) improves signal purity. Target “lottery-like” names while controlling for market jumps.  ￼

Feature Transformations (bullet list):
- MAX(1m): max daily return over past 21 trading days.
- β–MAX: residual of MAX after regressing on market MAX (or divide by recent beta).
- Persistence flag if prior months also exhibit elevated MAX.

Data Dependencies (concise list):
Daily returns, market returns, rolling beta.

Universe & Filters:
US small/micro-cap; price > $3; ADV > $1M.

Directionality / Construction Hints:
Short top decile β–MAX; long bottom; weekly rebalance; borrow-aware.

Strength & Actionability (qualitative only):
Promising – Well-known effect with modern refinement; watch costs in small caps.

Keywords (comma-separated):
lottery, MAX, skewness, mean-reversion

Expected Horizon Notes:
Backtest 2007–2025; 1–4w holds.

Citations:
- Bali et al. (2009/2010). https://papers.ssrn.com/sol3/Delivery.cfm/nber_w14804.pdf?abstractid=1366204
- Ince & Ozsoylev (2024/2025). https://ssrn.com/abstract=5030210

⸻

Alpha Idea #12: Idiosyncratic Volatility (IVOL) Tilt (Post-2000 Behavior)

Source(s): Detzel et al. (2019) “The Cross-Section of Volatility and Expected Returns: Then and Now” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
High-IVOL stocks underperform low-IVOL peers; post-2000 strength varies by listing venue (e.g., NASDAQ). Use residual variance from factor model as IVOL and tilt against it cross-sectionally.  ￼

Feature Transformations (bullet list):
- IVOL(6m) from daily residuals of FF6 or q5.
- Stability filter: exclude beta/IVOL unstable names.
- Combine with short interest to separate “lottery vs. distress.”

Data Dependencies (concise list):
Daily returns, factor returns.

Universe & Filters:
US large/mid; price > $5.

Directionality / Construction Hints:
Long low-IVOL; short high; monthly rebalance.

Strength & Actionability (qualitative only):
Tentative – Time-variation and model dependency; use as a risk-control tilt.

Keywords (comma-separated):
idiosyncratic volatility, residual risk

Expected Horizon Notes:
Backtest 2005–2025; quarterly robustness checks.

Citations:
- Detzel et al. (2019). https://ssrn.com/abstract=3455609

⸻

Alpha Idea #13: Betting Against Beta (BAB) / Low-Risk Anomaly

Source(s): Frazzini & Pedersen (2010) “Betting Against Beta” (NBER/SSRN); Baker, Bradley & Wurgler (2010) “Benchmarks as Limits to Arbitrage” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1-6 Months
Signal Type: Cross-Sectional Composite

Core Idea (2-4 sentences):
Delegated constraints and leverage limits lead to overpricing of high-beta names and underpricing of low-beta names; a beta-neutral long-low-beta/short-high-beta strategy harvests the spread. Use ex-ante beta estimates and scale legs to equalize risk.  ￼

Feature Transformations (bullet list):
- Beta(2y/5y) shrinkage estimate; sector-adjusted.
- BAB portfolio weights proportional to 1/β (long) and −β (short).
- Optional stochastic-dominance filter to improve leg quality.

Data Dependencies (concise list):
Daily returns, market index, industry map.

Universe & Filters:
Global large/mid; exclude penny/illiquid.

Directionality / Construction Hints:
Monthly rebalance; target beta neutrality each side; country/industry neutral.

Strength & Actionability (qualitative only):
Strong – Decade-spanning literature; scalable implementation.

Keywords (comma-separated):
beta, low-risk, constraints, leverage

Expected Horizon Notes:
Backtest 2005–2025; monthly.

Citations:
- Frazzini & Pedersen (2010). https://papers.ssrn.com/sol3/Delivery.cfm/nber_w16601.pdf?abstractid=1723048
- Baker et al. (2010). https://ssrn.com/abstract=1585031

⸻

Alpha Idea #14: Analyst Target-Price Implied Return (TPIR) Bias-Adjusted

Source(s): Dechow & You (2019/2020) “Understanding Determinants of Analyst Target Price Forecasts” (SSRN); Bali et al. (2014) “Analyst Price Target Expected Returns and Option Implied Volatility” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-4 Weeks
Signal Type: Event-Driven

Core Idea (2-4 sentences):
Raw target-price implied returns mix true information with systematic optimism and model errors; de-bias TPIR using controls for beta/IVOL and forecast errors to recover a predictive cross-sectional signal.  ￼

Feature Transformations (bullet list):
- TPIR = (Target − Price)/Price; winsorize.
- Bias model: regress TPIR on β, IVOL, earnings forecast errors; take residual TPIR_adj.
- Change in TPIR around revisions as an event kicker.

Data Dependencies (concise list):
IBES/Refinitiv target prices & EPS forecasts; prices; betas.

Universe & Filters:
US large; analyst coverage ≥3.

Directionality / Construction Hints:
Rank-long high TPIR_adj; short low; 1–4w holds post-revision.

Strength & Actionability (qualitative only):
Promising – Clear de-biasing improves signal quality; requires analyst data.

Keywords (comma-separated):
analysts, target price, revisions, bias

Expected Horizon Notes:
Backtest 2010–2025; event windows 1–20d.

Citations:
- Dechow & You (2019/2020). https://ssrn.com/abstract=2412813
- Bali et al. (2014). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2516937

⸻

Alpha Idea #15: Analyst EPS Forecast Skewness

Source(s): Bhojraj et al. (2015) “Analyst Forecast Skewness and Cross Section Stock Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-4 Weeks
Signal Type: Sentiment

Core Idea (2-4 sentences):
Skewness of analyst EPS forecasts (disagreement asymmetry) predicts the cross-section of returns; highly positively skewed forecasts tend to precede underperformance. Construct a skewness metric from analyst EPS estimates distribution.  ￼

Feature Transformations (bullet list):
- Forecast skewness from current-fiscal EPS estimates; winsorize.
- Dispersion control: include STD to separate mere disagreement from skew.
- Change in skewness around guidance.

Data Dependencies (concise list):
Analyst estimate distributions; prices.

Universe & Filters:
Coverage ≥5 analysts; price > $5.

Directionality / Construction Hints:
Short high-skew names; long low/negative skew; weekly rebalance.

Strength & Actionability (qualitative only):
Promising – Parsimonious, data widely available.

Keywords (comma-separated):
analyst skewness, sentiment, disagreement

Expected Horizon Notes:
Backtest 2010–2025; 1–4w holds.

Citations:
- Bhojraj et al. (2015). (see link above)

⸻

Alpha Idea #16: Conference Call Tone × Credibility

Source(s): Price et al. (2012) “Earnings Conference Calls and Stock Returns” (SSRN); Hennig et al. (2023) “Investor Reactions to Tone and Credibility” (SSRN/JEDC)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-5 Days
Signal Type: Sentiment

Core Idea (2-4 sentences):
Conference-call linguistic tone predicts abnormal returns, but the reaction is moderated by perceived speaker/message credibility; tone signals are stronger when credibility cues are high. Build tone scores using finance-specific lexicons and modulate by credibility proxies.  ￼

Feature Transformations (bullet list):
- Tone from Loughran–McDonald dictionary on transcript Q&A and prepared remarks.
- Credibility proxy: manager Big-5 inferred features; structured speech markers.
- Tone_cred = Tone × Credibility; event-day rank.

Data Dependencies (concise list):
Call transcripts; LM dictionary; NLP pipeline.

Universe & Filters:
US S&P 1500 with regular calls.

Directionality / Construction Hints:
Event-driven; long positive Tone_cred, short negative; exits after 1–5 days.

Strength & Actionability (qualitative only):
Promising – Clear enhancements beyond raw tone; event windows tight.

Keywords (comma-separated):
earnings calls, tone, NLP, credibility, event

Expected Horizon Notes:
Backtest 2012–2025; event study framework.

Citations:
- Price et al. (2012). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1625863
- Hennig et al. (2023). (see link above)

⸻

Alpha Idea #17: 10‑K Text (LM Negativity/Uncertainty) Tilt

Source(s): Loughran & McDonald (2010/2011) “When is a Liability not a Liability?” (SSRN/JoF)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-6 Months
Signal Type: Sentiment

Core Idea (2-4 sentences):
Finance-specific negative and uncertainty word lists better capture tone in filings; more negative/uncertain 10‑K language predicts higher volatility and weaker post-filing returns. Build annual filing-tone factors with sector relative scoring.  ￼

Feature Transformations (bullet list):
- LM Negative/Uncertainty counts per 10‑K; normalize by length.
- Sectional weighting (MD&A overweight).
- Change vs. prior filing as the main predictor.

Data Dependencies (concise list):
EDGAR 10‑Ks, LM dictionary, filing dates.

Universe & Filters:
US large/mid; annual updates.

Directionality / Construction Hints:
Short high-negative movers; long improvements; rebalance annually after filing.

Strength & Actionability (qualitative only):
Strong – Replicable NLP with public data; low turnover.

Keywords (comma-separated):
10‑K, LM dictionary, sentiment, filings

Expected Horizon Notes:
Backtest 2006–2025; 6–12m hold post-filing.

Citations:
- Loughran & McDonald. https://ssrn.com/abstract=1331573

⸻

Alpha Idea #18: Employee (Glassdoor) Sentiment Factor

Source(s): Edmans (2012) “The Link Between Job Satisfaction and Firm Value” (SSRN); Becker, McGurk & Cardazzi (2024/2025) “Employee Sentiment and Stock Returns Through Textual Analysis” (SSRN); Chen & Zhou (2023) “BERT Employee Sentiment and Stock Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: >6 Months
Signal Type: Alternative Data

Core Idea (2-4 sentences):
Employee reviews capture internal culture and operational health; improvements in employee sentiment, especially text-derived sentiment beyond raw star ratings, forecast cross-sectional returns. Focus on current-employee reviews and early-review signals.  ￼

Feature Transformations (bullet list):
- Text sentiment (BERT/LM) on Glassdoor reviews (current employees).
- ΔSentiment(6m) and early-review weight.
- Headquarters-proximity weight to amplify local information.

Data Dependencies (concise list):
Glassdoor reviews (text + meta), ticker mapping.

Universe & Filters:
US & Europe large/mid with ≥50 reviews/yr.

Directionality / Construction Hints:
Long improving sentiment; short deteriorating; annual/quarterly rebalance.

Strength & Actionability (qualitative only):
Promising – Alternative data alpha with demonstrated links; coverage varies.

Keywords (comma-separated):
employee sentiment, Glassdoor, text, culture

Expected Horizon Notes:
Backtest 2014–2025; quarterly updates.

Citations:
- Edmans (2012). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2054066
- Becker et al. (2024/2025). https://ssrn.com/abstract=5135457
- Chen & Zhou (2023). (see link above)

⸻

Alpha Idea #19: Product-Market Links & Scope Similarity Spillovers

Source(s): Cohen & Frazzini (2008/2016 SSRN page) “Economic Links and Predictable Returns”; Jin et al. (2024) “Scope Similarity and Cross-Firm Return Predictability” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1-3 Days
Signal Type: Momentum

Core Idea (2-4 sentences):
News or returns of economically linked firms (customers/suppliers or scope-similar peers) diffuse with a lag; customer returns lead supplier returns, and scope-similar firms show lead–lag. Use text-based or disclosed-link networks to propagate shocks cross-sectionally.  ￼

Feature Transformations (bullet list):
- Build peer set via 10‑K text similarity (Hoberg–Phillips) or principal customers.
- Peer momentum: value-weighted peer return over t−1 to t−2 days.
- Visibility filter: amplify when focal firm is less visible (lower coverage).

Data Dependencies (concise list):
Hoberg–Phillips text data or Compustat Segments; daily returns.

Universe & Filters:
US + Developed; cap > $1B.

Directionality / Construction Hints:
Long firms with positive peer shocks; short negative; hold 1–3 days; industry neutral.

Strength & Actionability (qualitative only):
Strong – Robust cross-firm diffusion with multiple constructions.

Keywords (comma-separated):
customer–supplier, text similarity, lead–lag, spillover

Expected Horizon Notes:
Backtest 2005–2025; daily reformation.

Citations:
- Cohen & Frazzini. https://ssrn.com/abstract=2758776
- Jin et al. (2024). https://ssrn.com/abstract=5016418

⸻

Alpha Idea #20: News-Link Momentum

Source(s): Chen & Wang (2024) “News Links and Predictable Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Emerging (applicable broadly)
Horizon: 1-3 Days
Signal Type: Momentum

Core Idea (2-4 sentences):
Firms co-mentioned in news exhibit attention-linked lead–lag in returns; lagging co-mentioned firms underreact. Construct news-implied links and trade the spillover.  ￼

Feature Transformations (bullet list):
- Co-mention graph from financial news; edges weighted by recent joint mentions.
- News-link momentum: leader’s 1–3d return projected to followers.
- Underreaction filter: trade when follower’s move < threshold.

Data Dependencies (concise list):
News feed (Dow Jones/Reuters), ticker NLP.

Universe & Filters:
Coverage-rich listings; cap > $1B.

Directionality / Construction Hints:
Long predicted followers; short negative spillovers; exit in 2–3 days.

Strength & Actionability (qualitative only):
Promising – Requires robust news NLP; short holding period helps costs.

Keywords (comma-separated):
news, co-mention, attention, lead–lag

Expected Horizon Notes:
Backtest 2014–2025; rolling 30–90d link windows.

Citations:
- Chen & Wang (2024). https://ssrn.com/abstract=4766194

⸻

Alpha Idea #21: ETF Flow/Creation–Redemption Pressure on Constituents

Source(s): Ben-David et al. (2014) “Do ETFs Increase Volatility?” (NBER/SSRN); Reconciling the ETF–Vol Debate (2024) survey
Verification Status: Partially Verified (secondary synthesis + core paper)
Equity Class: Equity ETFs (broad beta, sector/industry); US Large-Cap constituents
Horizon: 1-3 Days
Signal Type: Event-Driven

Core Idea (2-4 sentences):
ETF creations/redemptions transmit non-fundamental demand to underlying baskets, creating short-horizon predictable pressure and elevated commonality. Trade constituent reversion following outsized primary-market flow shocks.  ￼

Feature Transformations (bullet list):
- Primary activity proxy: ETF shares outstanding Δ(1–3d); scaled by float.
- Constituent pressure: allocate flow to members by index weight.
- Reversal score: constituent return deviation vs. peer non-ETF names.

Data Dependencies (concise list):
ETF shares outstanding, constituent weights, price/volume.

Universe & Filters:
US ETFs (SPY/sector ETFs); S&P 1500 constituents.

Directionality / Construction Hints:
Mean-revert: short flow-pushed up constituents, long dragged-down; exit T+1/T+2.

Strength & Actionability (qualitative only):
Tentative – Data availability on creations/redemptions varies; promising around extreme flows.

Keywords (comma-separated):
ETF flows, creations/redemptions, pressure, reversal

Expected Horizon Notes:
Backtest 2012–2025; event windows ±3d.

Citations:
- Ben-David et al. (2014). (see link above)
- Reconciling ETF–Vol Debate (2024). (see link above)

⸻

Alpha Idea #22: Passive ETF Ownership → Stronger Short-Term Reversals

Source(s): Passive Investing and Market Quality (2024) (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Large-Cap
Horizon: 1-3 Days
Signal Type: Mean-Reversion

Core Idea (2-4 sentences):
Stocks with higher passive ETF ownership exhibit stronger short-term return reversals due to mechanical flows and reduced information production. Condition reversal strategies on passive-ownership percentiles.  ￼

Feature Transformations (bullet list):
- Passive ownership % (ETF shares/float).
- Reversal: prior 1–2d return sign; interact with ownership decile.
- Liquidity control using Amihud.

Data Dependencies (concise list):
ETF ownership datasets, prices, floats.

Universe & Filters:
US large/mid; price > $5.

Directionality / Construction Hints:
Apply larger weights to high-passive names in standard reversal; hold 1–2 days.

Strength & Actionability (qualitative only):
Promising – Enhances a classic effect with a structural conditioning variable.

Keywords (comma-separated):
passive ownership, reversal, ETF

Expected Horizon Notes:
Backtest 2012–2025; daily rebalance.

Citations:
- Passive Ownership & Market Quality (2024). (see link above)

⸻

Alpha Idea #23: Customer-Industry Leads Supplier-Industry (Global)

Source(s): Wu & Birge (2014/2015) “Supply Chain Network Structure and Firm Returns” (SSRN)
Verification Status: Verified (direct link)
Equity Class: Global Developed
Horizon: 1-4 Weeks
Signal Type: Momentum

Core Idea (2-4 sentences):
At the industry level and internationally, customer industries’ returns lead suppliers’. Tilt supplier baskets by lagged customer-industry performance, focusing on smaller and relationship-intensive suppliers.  ￼

Feature Transformations (bullet list):
- Map GICS industries to customer–supplier pairs.
- Customer lead: last 4 weeks’ return of customer industry vs. market.
- Supplier tilt strength weighted by relationship-specificity proxy.

Data Dependencies (concise list):
Industry returns; input–output or customer mapping.

Universe & Filters:
Developed markets; exclude tiny industries.

Directionality / Construction Hints:
Overweight suppliers to strong customers; underweight to weak; 2–4w hold.

Strength & Actionability (qualitative only):
Promising – Industry-level reduces noise; readily tradable via baskets.

Keywords (comma-separated):
supply chain, industry momentum, lead–lag

Expected Horizon Notes:
Backtest 2005–2025; weekly rebalance.

Citations:
- Wu & Birge (2014/2015). (see link above)

⸻

Alpha Idea #24: Amihud Down‑Day Illiquidity Premium

Source(s): Acharya & Pedersen lineage; re-exam: “An Analysis of the Amihud Illiquidity Premium” (2012) (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Small-Cap
Horizon: 1-6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
Decompose Amihud’s illiquidity into up-day and down-day components; down-day impact commands the cross-sectional premium. Prefer stocks with lower down-day impact conditional on total turnover.  ￼

Feature Transformations (bullet list):
- Amihud− = mean(|ret|/vol) on negative-return days.
- Amihud split ratio: Amihud− / Amihud (total).
- Sector-neutral z; interact with size.

Data Dependencies (concise list):
Daily prices, volumes.

Universe & Filters:
US small/mid; price > $3.

Directionality / Construction Hints:
Long low Amihud−; short high; monthly rebalance.

Strength & Actionability (qualitative only):
Promising – Simple daily data; robust to construction variants.

Keywords (comma-separated):
illiquidity, Amihud, downside, microstructure

Expected Horizon Notes:
Backtest 2005–2025; monthly.

Citations:
- “Analysis of the Amihud Illiquidity Premium” (2012). (see link above)

⸻

Alpha Idea #25: Local Downside Beta Premium

Source(s): Li & Niu (2025) “The Local Downside Risk Premium” (SSRN)
Verification Status: Verified (direct link)
Equity Class: US Mid-Cap
Horizon: 1-6 Months
Signal Type: Fundamental

Core Idea (2-4 sentences):
Stocks more sensitive to local market downturns (local downside beta) earn higher average returns; the effect is distinct from standard risk measures. Estimate downside beta to the stock’s local market and tilt accordingly.  ￼

Feature Transformations (bullet list):
- Local downside beta: regression of returns on local index when local market < 0.
- Local bias proxy: interaction with HQ region investor base intensity.
- Cross-sectional z by region/sector.

Data Dependencies (concise list):
Stock returns, local index returns, headquarters location.

Universe & Filters:
US & multi-region listings; cap > $1B.

Directionality / Construction Hints:
Long high local-downside-beta names (risk-compensated); hedge market beta.

Strength & Actionability (qualitative only):
Tentative – Newer evidence; ensure orthogonalization to standard factors.

Keywords (comma-separated):
downside beta, local bias, risk premium

Expected Horizon Notes:
Backtest 2008–2025; quarterly refresh.

Citations:
- Li & Niu (2025). https://ssrn.com/abstract=5019010

⸻

Notes on Deduplication
- MAX vs β–MAX: consolidated under one idea with the β-adjusted variant retained for actionability.
- Employee sentiment: multiple sources (Edmans; Becker et al.; Chen & Zhou) merged; we emphasize text-based improvements.
- Product-market links: customer–supplier and scope similarity combined but kept two entries where horizons differ (firm-level 1–3d spillovers vs. industry/basket 2–4w).
- ETF impacts: flows/creation–redemption pressure and passive-ownership-conditioned reversal kept as two separate event vs. conditioning effects.

⸻

JSON Export Schema (append after the markdown sections)

{
  "meta": {
    "source_searched": "arXiv (https://arxiv.org) and SSRN (https://ssrn.com)",
    "query": "cross-sectional equity anomaly feature engineering factor discovery SSRN",
    "scan_window": "2005-01-01 - 2025-10-24",
    "exclusions": ["Crypto and digital assets"],
    "report_date": "2025-10-24"
  },
  "ideas": [
    {
      "title": "Intraday vs. Overnight Mispricing Split",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "Intraday (1-6h)",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Separate intraday and overnight legs for the same characteristic; arbitrage frictions overnight cause predictable day–night divergence across stocks.",
      "feature_transformations": [
        "Compute day vs. overnight returns for characteristic-ranked legs; rank-normalize each daily",
        "Intraday-minus-Overnight spread: z(X)_day − z(X)_overnight",
        "Systematic-variance split: ratio of overnight to intraday beta-variance as a conditioner"
      ],
      "data_dependencies": ["OHLCV with opens/closes", "intraday bars", "market beta estimates"],
      "universe_filters": "US top 1000 by ADV; price > $3; ADV > $5M; exclude ADRs/OTC",
      "directionality": "Cross-sectional ranks; long intraday leg where overnight drag is highest; industry/beta neutral; close before EOD, re-enter on open",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear split, standard data, well-documented cross-sectional patterns"
      },
      "keywords": ["overnight", "intraday", "mispricing", "beta"],
      "expected_horizon_notes": "Backtest 2010–2025 minute bars; monitor 6 weeks live",
      "citations": ["https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2869624"]
    },
    {
      "title": "Single-Stock VRP Adjusted for Turnover Shocks",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Use realized–implied volatility spread as a cross-sectional predictor but correct realized vol for turnover-induced mean reversion to restore signal power.",
      "feature_transformations": [
        "RVol* = realized vol mean-reversion corrected to a 60d median",
        "VRP* = RVol* − 30D ATM implied vol",
        "Turnover shock filter: shrink or drop observations with abnormal turnover"
      ],
      "data_dependencies": ["Intraday realized vol", "Option IV (30D ATM)", "Daily turnover"],
      "universe_filters": "US optionable names; price > $5; ADV > $10M",
      "directionality": "Rank long high VRP*; short low; monthly rebalance; beta/industry neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Practical improvement on a known options–equity bridge"
      },
      "keywords": ["VRP", "implied vol", "realized vol", "turnover"],
      "expected_horizon_notes": "Backtest 2012–2025; monthly refresh; 8-week live",
      "citations": ["https://ssrn.com/abstract=5234112"]
    },
    {
      "title": "Weekly Realized Skewness Predictor",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-5 Days",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Higher recent realized skewness forecasts underperformance next week; use intraday-derived higher moments cross-sectionally.",
      "feature_transformations": [
        "Weekly realized skewness from 5m returns; winsorize extremes",
        "Sector-neutral z-score",
        "Skew–kurtosis composite: −z(skew) + 0.25*z(kurt)"
      ],
      "data_dependencies": ["Intraday bars", "Corporate action adjustments"],
      "universe_filters": "Top 1500 by ADV; price > $3",
      "directionality": "Long lowest-skew quintile; short highest; weekly rebalance",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Replicable with standard HF data; well-documented"
      },
      "keywords": ["realized skewness", "intraday", "weekly", "higher moments"],
      "expected_horizon_notes": "Backtest 2012–2025; 8-week pilot",
      "citations": ["https://ssrn.com/abstract=1898735"]
    },
    {
      "title": "Downside Semivariance Ratio (RDRS) Tilt",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-6 Months",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "Use the ratio of downside semivariance to total variance to identify stocks with unfavorable downside risk; tilt toward low-RDRS names.",
      "feature_transformations": [
        "RDRS(60d) = RSV− / (RSV− + RSV+)",
        "Sector-time demeaning and z-scoring",
        "Overlay with downside beta to market drawdowns"
      ],
      "data_dependencies": ["Intraday returns", "Market index"],
      "universe_filters": "Developed large/mid; price > $5; ADV > $5M",
      "directionality": "Long low RDRS, short high; monthly rebalance; sector/country neutral",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Technically sound, intuitive, needs HF data"
      },
      "keywords": ["downside risk", "semivariance", "intraday", "drawdown"],
      "expected_horizon_notes": "Backtest 2015–2025; monthly updates; 12-week live",
      "citations": ["https://ssrn.com/abstract=4867217"]
    },
    {
      "title": "Expected Growth (q5) Factor",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": ">6 Months",
      "signal_type": "Fundamental",
      "core_idea": "Forecast expected investment growth from fundamentals and sort cross-sectionally; long high expected growth, short low.",
      "feature_transformations": [
        "Cross-sectional forecast of Δ(Investment/Assets) using q, OCF/Assets, ΔROE",
        "Expected Growth percentile (industry-neutral)",
        "Combine with profitability and investment into a q5 composite"
      ],
      "data_dependencies": ["Quarterly fundamentals", "Prices"],
      "universe_filters": "Developed markets; ex-fin/REIT; price > $5",
      "directionality": "Semiannual rebalance; beta/industry neutral",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Peer-reviewed model; widely accessible inputs"
      },
      "keywords": ["expected growth", "investment", "profitability", "q-factor"],
      "expected_horizon_notes": "Backtest 2005–2025; 6–12m holds",
      "citations": ["https://ssrn.com/abstract=3525435", "https://ssrn.com/abstract=3191167"]
    },
    {
      "title": "Quality-Minus-Junk Composite",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": ">6 Months",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Multi-pillar quality (profitability, growth, safety, payout) predicts cross-sectional returns; long high-quality vs. short junk.",
      "feature_transformations": [
        "Profitability (GP/A, ROA), Growth (ΔROA, ΔGP/A), Safety (low leverage/vol/beta), Payout (net issuance)",
        "Rank-average pillars into QMJ",
        "Industry-neutral scoring"
      ],
      "data_dependencies": ["Fundamentals", "Prices", "Shares outstanding"],
      "universe_filters": "Global ex-fin/REIT; cap > $500M; ADV > $2M",
      "directionality": "Quarterly rebalance; beta neutral",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Extensively replicated; straightforward"
      },
      "keywords": ["quality", "profitability", "safety", "payout"],
      "expected_horizon_notes": "Backtest 2005–2025; quarterly",
      "citations": ["https://ssrn.com/abstract=2312432"]
    },
    {
      "title": "Asset Growth / Investment-to-Assets",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": ">6 Months",
      "signal_type": "Fundamental",
      "core_idea": "High recent asset growth predicts lower future returns; use Inv/A and combine with profitability to improve efficacy.",
      "feature_transformations": [
        "Inv/A = (Assets_t − Assets_{t−1})/Assets_{t−1}",
        "Overlay net issuance",
        "Sector-relative z-scoring"
      ],
      "data_dependencies": ["Quarterly fundamentals", "Shares"],
      "universe_filters": "Ex-fin; cap > $300M",
      "directionality": "Short high Inv/A; long low; quarterly rebalance",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Simple, capacity friendly, robust"
      },
      "keywords": ["investment", "asset growth", "fundamentals"],
      "expected_horizon_notes": "Backtest 2005–2025; semiannual holds",
      "citations": ["https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2508322"]
    },
    {
      "title": "Equity Loan Fee / Borrow Cost Tilt",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-4 Weeks",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "High loan fees signal contemporaneous short demand and predict short-horizon underperformance; sort by fee level and change.",
      "feature_transformations": [
        "Fee level z(7d) and ΔFee(7d) composite",
        "Interact with DTC and Amihud for squeeze risk",
        "Exclude extreme-fee tails for cost control"
      ],
      "data_dependencies": ["Securities lending fees", "Short interest", "Turnover"],
      "universe_filters": "Cap > $1B; lendable; ADV > $5M",
      "directionality": "Short high-fee; long low-fee; weekly rebalance",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Direct microstructure signal with short horizon"
      },
      "keywords": ["shorting", "loan fee", "borrow", "microstructure"],
      "expected_horizon_notes": "Backtest 2012–2025; weekly",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/3707166.pdf?abstractid=3707166", "https://ssrn.com/abstract=3726227"]
    },
    {
      "title": "Days-to-Cover Short Interest",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Microstructure/Order-Flow",
      "core_idea": "DTC = short interest / ADV is a better marginal shorting-cost proxy than raw SI; high-DTC names underperform.",
      "feature_transformations": [
        "Compute DTC and sector-neutral z",
        "DTC × Amihud interaction",
        "ΔDTC timing overlay"
      ],
      "data_dependencies": ["Short interest", "ADV", "Prices"],
      "universe_filters": "US 1,000–3,000 by cap; exclude < $300M",
      "directionality": "Short high-DTC; long low; weekly",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Simple, public, robust interpretation"
      },
      "keywords": ["short interest", "days-to-cover", "liquidity"],
      "expected_horizon_notes": "Backtest 2006–2025; 1–4w holds",
      "citations": ["https://ssrn.com/abstract=2607356"]
    },
    {
      "title": "MAX / β–MAX Lottery Control",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Mean-Reversion",
      "core_idea": "Extreme prior single-day winners (MAX) underperform; β-adjusted MAX refines the signal by controlling for market spikes.",
      "feature_transformations": [
        "MAX(1m) = max daily return over 21d",
        "β–MAX (residualized/divided by beta)",
        "Persistence flag from prior months"
      ],
      "data_dependencies": ["Daily returns", "Market returns", "Rolling beta"],
      "universe_filters": "Small/micro; price > $3; ADV > $1M",
      "directionality": "Short top decile β–MAX; long bottom; weekly",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Known effect with improved specification"
      },
      "keywords": ["lottery", "MAX", "skewness", "reversal"],
      "expected_horizon_notes": "Backtest 2007–2025; 1–4w holds",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/nber_w14804.pdf?abstractid=1366204", "https://ssrn.com/abstract=5030210"]
    },
    {
      "title": "Idiosyncratic Volatility Tilt",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "High-IVOL names underperform; use model-residual variance to sort; strength varies across venues.",
      "feature_transformations": [
        "IVOL(6m) from daily residuals of FF6 or q5",
        "Stability filter for betas/IVOL",
        "Combine with short-interest information"
      ],
      "data_dependencies": ["Daily returns", "Factor returns"],
      "universe_filters": "US large/mid; price > $5",
      "directionality": "Long low-IVOL; short high; monthly",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Time-varying strength; useful as risk tilt"
      },
      "keywords": ["idiosyncratic volatility", "residual risk"],
      "expected_horizon_notes": "Backtest 2005–2025; quarterly checks",
      "citations": ["https://ssrn.com/abstract=3455609"]
    },
    {
      "title": "Betting Against Beta (Low-Risk)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-6 Months",
      "signal_type": "Cross-Sectional Composite",
      "core_idea": "Constraints cause high-beta overpricing and low-beta underpricing; build a beta-neutral long-low/short-high portfolio.",
      "feature_transformations": [
        "Shrinkage beta estimates from 2–5y daily returns",
        "Risk-scaled leg weights (∝ 1/β and −β)",
        "Optional stochastic-dominance filter"
      ],
      "data_dependencies": ["Daily returns", "Index returns"],
      "universe_filters": "Global large/mid; liquid",
      "directionality": "Monthly rebalance; beta, sector, country neutral",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Deep literature, scalable"
      },
      "keywords": ["beta", "low-risk", "constraints", "leverage"],
      "expected_horizon_notes": "Backtest 2005–2025; monthly",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/nber_w16601.pdf?abstractid=1723048", "https://ssrn.com/abstract=1585031"]
    },
    {
      "title": "Analyst Target-Price Implied Return (Bias-Adjusted)",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Event-Driven",
      "core_idea": "Debias TPIR for optimism and risk misestimation using IVOL/beta and forecast errors; residual TPIR predicts returns.",
      "feature_transformations": [
        "TPIR = (Target − Price)/Price",
        "Bias model residual TPIR_adj (controls: β, IVOL, EPS errors)",
        "ΔTPIR around revisions as event kicker"
      ],
      "data_dependencies": ["IBES targets & EPS", "Prices", "Betas"],
      "universe_filters": "US large; coverage ≥3 analysts",
      "directionality": "Rank long high TPIR_adj; short low; 1–4w holds",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Cleaner information extraction from targets"
      },
      "keywords": ["analysts", "target price", "revisions", "bias"],
      "expected_horizon_notes": "Backtest 2010–2025; 1–20d windows",
      "citations": ["https://ssrn.com/abstract=2412813", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2516937"]
    },
    {
      "title": "Analyst Forecast Skewness",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-4 Weeks",
      "signal_type": "Sentiment",
      "core_idea": "Asymmetric EPS forecast distributions (skewness) predict cross-sectional returns; positive skew often precedes underperformance.",
      "feature_transformations": [
        "Estimate skewness of current-fiscal EPS estimates",
        "Control for dispersion (STD)",
        "Change in skewness around guidance"
      ],
      "data_dependencies": ["Analyst estimate distributions", "Prices"],
      "universe_filters": "Coverage ≥5; price > $5",
      "directionality": "Short high-skew; long low/negative; weekly",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Low-dimensional, widely available data"
      },
      "keywords": ["analyst skewness", "sentiment", "disagreement"],
      "expected_horizon_notes": "Backtest 2010–2025; weekly",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2602731_code1745712.pdf?abstractid=2602731"]
    },
    {
      "title": "Conference Call Tone × Credibility",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-5 Days",
      "signal_type": "Sentiment",
      "core_idea": "Tone predicts event-window returns but depends on speaker/message credibility; use a tone×credibility interaction for selection.",
      "feature_transformations": [
        "LM-based tone on transcripts (Q&A, prepared)",
        "Credibility proxy from linguistic markers and manager traits",
        "Tone_cred = Tone × Credibility"
      ],
      "data_dependencies": ["Call transcripts", "LM dictionary", "NLP pipeline"],
      "universe_filters": "S&P 1500 with regular calls",
      "directionality": "Long positive Tone_cred; short negative; 1–5d exits",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Enhancement over raw tone; tight horizons"
      },
      "keywords": ["earnings calls", "tone", "NLP", "credibility", "event"],
      "expected_horizon_notes": "Backtest 2012–2025; event framework",
      "citations": ["https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1625863", "https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4520536_code3532039.pdf?abstractid=4520536"]
    },
    {
      "title": "10‑K Text Negativity/Uncertainty Tilt",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Sentiment",
      "core_idea": "Finance-specific negative/uncertainty lexicons applied to 10‑Ks predict weaker post-filing returns; trade changes in tone.",
      "feature_transformations": [
        "LM Negative/Uncertainty normalized by length",
        "MD&A weighting",
        "ΔTone vs. prior filing"
      ],
      "data_dependencies": ["EDGAR 10‑Ks", "LM dictionary"],
      "universe_filters": "US large/mid; annual",
      "directionality": "Short increased negativity; long improvements",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Public data, robust construction, low turnover"
      },
      "keywords": ["10‑K", "LM dictionary", "sentiment", "filings"],
      "expected_horizon_notes": "Backtest 2006–2025; 6–12m hold",
      "citations": ["https://ssrn.com/abstract=1331573"]
    },
    {
      "title": "Employee (Glassdoor) Sentiment Factor",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": ">6 Months",
      "signal_type": "Alternative Data",
      "core_idea": "Improvements in employee sentiment, especially text-based beyond stars, forecast returns; emphasize current-employee reviews and early reviewers.",
      "feature_transformations": [
        "BERT/LM sentiment on reviews",
        "ΔSentiment(6m) with early review weighting",
        "HQ proximity weight"
      ],
      "data_dependencies": ["Glassdoor reviews (text+meta)", "Ticker mapping"],
      "universe_filters": "Large/mid with ≥50 reviews/yr",
      "directionality": "Long improving; short deteriorating; quarterly/annual",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Multiple corroborating studies; coverage variance"
      },
      "keywords": ["employee sentiment", "Glassdoor", "text", "culture"],
      "expected_horizon_notes": "Backtest 2014–2025; quarterly",
      "citations": ["https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2054066", "https://ssrn.com/abstract=5135457", "https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4631233_code3973152.pdf?abstractid=4631233"]
    },
    {
      "title": "Product-Market Links & Scope Similarity Spillovers",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-3 Days",
      "signal_type": "Momentum",
      "core_idea": "Returns and news of economically linked firms (customers/suppliers/scope-similar) diffuse with a lag; propagate shocks to peers.",
      "feature_transformations": [
        "Peer set via 10‑K text similarity or customer mapping",
        "Peer momentum over prior 1–2d",
        "Visibility filter to focus on underreaction"
      ],
      "data_dependencies": ["Hoberg–Phillips text or Compustat Segments", "Daily returns"],
      "universe_filters": "US + Developed; cap > $1B",
      "directionality": "Long positive-spillover peers; short negative; 1–3d hold",
      "strength_actionability": {
        "rating": "Strong",
        "rationale": "Robust effect with multiple datasets"
      },
      "keywords": ["customer–supplier", "text similarity", "lead–lag", "spillover"],
      "expected_horizon_notes": "Backtest 2005–2025; daily",
      "citations": ["https://ssrn.com/abstract=2758776", "https://ssrn.com/abstract=5016418"]
    },
    {
      "title": "News-Link Momentum",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Emerging",
      "horizon": "1-3 Days",
      "signal_type": "Momentum",
      "core_idea": "Co-mentioned firms in news show lead–lag; trade underreacting followers after leader moves.",
      "feature_transformations": [
        "Co-mention graph from financial news",
        "Leader’s 1–3d return projected to followers",
        "Underreaction threshold for entry"
      ],
      "data_dependencies": ["News feed (Reuters/Dow Jones)", "Ticker NLP"],
      "universe_filters": "Coverage-rich listings; cap > $1B",
      "directionality": "Long predicted followers; short negative spillovers",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Clear construction; short holding period"
      },
      "keywords": ["news", "co-mention", "attention", "lead–lag"],
      "expected_horizon_notes": "Backtest 2014–2025; 30–90d link windows",
      "citations": ["https://ssrn.com/abstract=4766194"]
    },
    {
      "title": "ETF Flow Pressure on Constituents",
      "verification_status": "Partially Verified (secondary references)",
      "equity_class": "Equity ETFs (US broad and sector) and their constituents",
      "horizon": "1-3 Days",
      "signal_type": "Event-Driven",
      "core_idea": "Large ETF creations/redemptions transmit temporary price pressure to constituents; mean-reversion follows extreme primary activity.",
      "feature_transformations": [
        "ΔShares Outstanding (1–3d) as primary activity proxy",
        "Allocate flow to constituents by index weights",
        "Constituent pressure vs. non-ETF peers to form a reversal score"
      ],
      "data_dependencies": ["ETF shares outstanding", "Constituent weights", "Prices"],
      "universe_filters": "US ETFs (e.g., SPY, sector ETFs) and S&P 1500 constituents",
      "directionality": "Short flow-pushed up constituents; long dragged down; T+1–T+2 exit",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Promising around extremes; data access varies"
      },
      "keywords": ["ETF flows", "creations/redemptions", "pressure", "reversal"],
      "expected_horizon_notes": "Backtest 2012–2025; ±3d event windows",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/nber_w20071.pdf?abstractid=2430066", "https://papers.ssrn.com/sol3/Delivery.cfm/4804048.pdf?abstractid=4804048"]
    },
    {
      "title": "Passive Ownership–Conditioned Reversal",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Large-Cap",
      "horizon": "1-3 Days",
      "signal_type": "Mean-Reversion",
      "core_idea": "Short-term reversal is stronger among stocks with higher passive ETF ownership; condition reversal weights on passive share.",
      "feature_transformations": [
        "Passive ownership % from ETF ownership data",
        "Reversal based on prior 1–2d returns",
        "Amihud control to avoid liquidity traps"
      ],
      "data_dependencies": ["ETF ownership data", "Prices", "Floats"],
      "universe_filters": "US large/mid; price > $5",
      "directionality": "Overweight reversal in high-passive names; 1–2d holds",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Structural conditioning boosts a classic signal"
      },
      "keywords": ["passive ownership", "reversal", "ETF"],
      "expected_horizon_notes": "Backtest 2012–2025; daily",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/4567751.pdf?abstractid=4567751"]
    },
    {
      "title": "Industry-Level Customer→Supplier Momentum (Global)",
      "verification_status": "Verified (direct link)",
      "equity_class": "Global Developed",
      "horizon": "1-4 Weeks",
      "signal_type": "Momentum",
      "core_idea": "Customer industries’ recent returns lead supplier industries; trade supplier baskets accordingly, focusing on smaller, relationship-intensive suppliers.",
      "feature_transformations": [
        "Map GICS industries to customer–supplier",
        "Customer 4w return vs. market",
        "Relationship-specificity weighting"
      ],
      "data_dependencies": ["Industry returns", "Input–output links"],
      "universe_filters": "Developed markets; liquid industries",
      "directionality": "Tilt supplier baskets with 2–4w holds",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Tradable via baskets/ETFs"
      },
      "keywords": ["supply chain", "industry momentum", "lead–lag"],
      "expected_horizon_notes": "Backtest 2005–2025",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2686904_code2034340.pdf?abstractid=2385217"]
    },
    {
      "title": "Amihud Down-Day Illiquidity Premium",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Small-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "Down-day Amihud component commands the cross-sectional premium; prefer names with lower down-day price impact.",
      "feature_transformations": [
        "Amihud− (negative-return days)",
        "Amihud−/Amihud split ratio",
        "Size-conditioned scoring"
      ],
      "data_dependencies": ["Daily prices", "Volumes"],
      "universe_filters": "US small/mid; price > $3",
      "directionality": "Long low Amihud−; short high; monthly",
      "strength_actionability": {
        "rating": "Promising",
        "rationale": "Daily data; intuitive downside focus"
      },
      "keywords": ["illiquidity", "Amihud", "downside", "microstructure"],
      "expected_horizon_notes": "Backtest 2005–2025; monthly",
      "citations": ["https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2034037_code2026.pdf?abstractid=1859632"]
    },
    {
      "title": "Local Downside Beta Premium",
      "verification_status": "Verified (direct link)",
      "equity_class": "US Mid-Cap",
      "horizon": "1-6 Months",
      "signal_type": "Fundamental",
      "core_idea": "Stocks with higher sensitivity to local-market downturns earn higher returns; estimate local downside beta and tilt.",
      "feature_transformations": [
        "Local downside beta to regional index (returns < 0)",
        "Interaction with local investor presence",
        "Region/sector-neutral z"
      ],
      "data_dependencies": ["Stock returns", "Local index returns", "HQ location"],
      "universe_filters": "US & multi-region listings; cap > $1B",
      "directionality": "Long high local-downside-beta names; hedge market beta",
      "strength_actionability": {
        "rating": "Tentative",
        "rationale": "Newer result; ensure orthogonality to standard factors"
      },
      "keywords": ["downside beta", "local bias", "risk premium"],
      "expected_horizon_notes": "Backtest 2008–2025; quarterly",
      "citations": ["https://ssrn.com/abstract=5019010"]
    }
  ]
}