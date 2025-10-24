# Alpha Discovery Report (Equities Only)

## Instructions (Follow Exactly)
- Task: Search the specified source for **publicly shared, actionable equity alphas** and **feature transformations** (no crypto). Extract ideas that include concrete, testable features.
- Scope: Equities only (single-name stocks and equity ETFs). Exclude crypto, digital assets, FX-only, and pure futures-only content.
- Deliverable: Produce **up to {LIMIT} distinct ideas** using the exact schema below, in order, one after another. Use concise, technical prose.
- Sources: Provide direct links for each idea (tweet, notebook, paper, repo). If multiple posts in a thread support the same idea, include all links.
- Style: No emojis. No questions. No disclaimers. No performance estimates (Sharpe, t-stat, returns). No code unless quoted from a cited source.
- Deduplication: Merge near-duplicates; keep the most complete citation set.
- Assessment: Provide a **qualitative** “Strength & Actionability” judgment (e.g., Strong / Promising / Tentative) with a one-line rationale.

## Controlled Vocabulary
- **Equity Class:** One of {US Large-Cap, US Mid-Cap, US Small-Cap, US Micro-Cap, Global Developed, Global Emerging, Sector-Specific (specify), Equity ETFs (specify)}.
- **Horizon:** One of {Intraday (<1h), Intraday (1–6h), Overnight, 1–3 Days, 1–5 Days, 1–4 Weeks, 1–6 Months, >6 Months}.
- **Signal Type:** One of {Momentum, Mean-Reversion, Event-Driven, Sentiment, Microstructure/Order-Flow, Fundamental, Cross-Sectional Composite, Alternative Data, Seasonality/Calendar}.
- **Verification Status:** One of {Verified (direct link), Partially Verified (secondary references), Unverified (no direct link)}.

## Citations Guidance
- **Twitter/X:** Include handle, status URL(s), and post date(s).
- **Kaggle/GitHub:** Include notebook/repo URL, author, and file path if relevant.
- **Papers:** Include title, authors, venue/arXiv ID/DOI, section or page reference if possible.

---

# Report Meta
- **Source Searched:** {SOURCE_NAME or URL}
- **Query / Filters:** {QUERY_TEXT}
- **Scan Window:** {START_DATE} – {END_DATE}
- **Exclusions Applied:** Crypto and digital assets
- **Date of Report:** {YYYY-MM-DD}

---

## Alpha Idea #1: <short descriptive title>

**Source(s):** <markdown link(s) with author/handle and date>  
**Verification Status:** <Verified | Partially Verified | Unverified>  
**Equity Class:** <from controlled vocabulary>  
**Horizon:** <from controlled vocabulary>  
**Signal Type:** <from controlled vocabulary>  

**Core Idea (2–4 sentences):**  
<Explain the mechanism and intuition succinctly, focusing on why the signal should exist in equities.>

**Feature Transformations (bullet list):**  
- <Specific transform 1 (e.g., rolling z-score of overnight gap / ATR(20))>  
- <Specific transform 2 (e.g., EMA(5) – EMA(20) of quote imbalance)>  
- <Specific transform 3 (e.g., rank-normalized surprise earnings magnitude with industry-neutralization)>

**Data Dependencies (concise list):**  
<e.g., OHLCV, pre/post-market volume, NBBO/LOB fields, fundamentals (specify), news/sentiment feed (specify)>

**Universe & Filters:**  
<e.g., US Small-Cap; price > $3; ADV > $1M; exclude ADRs/OTC; sector include/exclude if applicable>

**Directionality / Construction Hints:**  
<Long or Short bias; cross-sectional ranking vs. threshold; neutralization (e.g., beta/industry); holding and exit cues>

**Strength & Actionability (qualitative only):**  
<Strong | Promising | Tentative> — <one-line justification focusing on originality, clarity, testability, frictions/liquidity>

**Citations:**  
- <link 1 with short description>  
- <link 2 with short description>

---

## Alpha Idea #2: <short descriptive title>

**Source(s):** <markdown link(s) with author/handle and date>  
**Verification Status:** <Verified | Partially Verified | Unverified>  
**Equity Class:** <from controlled vocabulary>  
**Horizon:** <from controlled vocabulary>  
**Signal Type:** <from controlled vocabulary>  

**Core Idea (2–4 sentences):**  
<…>

**Feature Transformations (bullet list):**  
- <…>  
- <…>

**Data Dependencies (concise list):**  
<…>

**Universe & Filters:**  
<…>

**Directionality / Construction Hints:**  
<…>

**Strength & Actionability (qualitative only):**  
<…>

**Citations:**  
- <…>

---

## Alpha Idea #3: <short descriptive title>

**Source(s):** <…>  
**Verification Status:** <…>  
**Equity Class:** <…>  
**Horizon:** <…>  
**Signal Type:** <…>  

**Core Idea (2–4 sentences):**  
<…>

**Feature Transformations (bullet list):**  
- <…>

**Data Dependencies (concise list):**  
<…>

**Universe & Filters:**  
<…>

**Directionality / Construction Hints:**  
<…>

**Strength & Actionability (qualitative only):**  
<…>

**Citations:**  
- <…>

---

## Notes on Deduplication
- If multiple sources present the same idea, consolidate under a single “Alpha Idea” and list all supporting links.  
- If sources present meaningful variants (different features/horizons/universes), keep separate entries and clarify distinctions in “Core Idea” and “Feature Transformations”.
