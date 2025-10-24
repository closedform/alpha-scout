# alpha-scout

Collecting alpha from online sources.

## License
- Code (`/src` and subfolders): licensed under Apache License 2.0 (see `LICENSE-CODE`). You must retain copyright notices and the `NOTICE` file and include prominent notices in any files you modify.
- Content (`/content`, including alpha write-ups, schemas, and docs): licensed under CC BY 4.0 (see `LICENSE-CONTENT`). You must provide attribution and indicate if changes were made to the content.

No crypto content is included or licensed here.

## Structure
- `config/`: reusable run configurations (`.env` style) such as `twitter-scan.env`, `kaggle-optiver.env`, `twitter-alpha-hunters.env`, `reddit-algotrading.env`, `github-research.env`, and `arxiv-cross-sectional.env`.
- `content/prompts/`: canonical templates.
- `content/prompt-requests/`: generated prompts to feed into LLMs.
- `content/reports/`: completed write-ups returned by the models.
- `data/`: optional structured indices (JSONL/CSV) for cataloging alphas.
- `src/alpha_scout/`: lightweight helpers (Apache-licensed code).

## Prompts
- Use `content/prompts/alpha-discovery-report.md` as the standard template for equity alpha discovery runs.
- Store generated prompt requests under `content/prompt-requests/` (the helper in `src/alpha_scout/tools/` creates this automatically).

## Reports
- Archive completed alpha discovery results under `content/reports/`. Keep LLM-ready prompt requests separate in `content/prompt-requests/` so it is clear what still needs to be executed.

## Using the Alpha Discovery Prompt
- Launch a web-enabled LLM such as GPT-4.1 with browsing or Gemini Advanced and open a fresh chat.
- Paste the full template from `content/prompts/alpha-discovery-report.md`.
- Fill the braces before submitting, e.g. `LIMIT=5`, `SOURCE_NAME=Twitter`, `QUERY_TEXT="equity alpha order flow"`, `START_DATE=2024-07-01`, `END_DATE=2024-07-31`.
- Add any platform-specific instructions (e.g. “Use the builtin browser to search Twitter with this query; only read posts from @somehandle”) so the model knows how to scope its crawl.
- Remind the model that each idea must include a `Keywords (comma-separated)` line and an `Expected Horizon Notes` line so you can tag and size backtests quickly.
- Ask the model to append the structured JSON block at the end of the report (following the template’s schema) so downstream tooling can ingest results automatically.

### Scoping Best Practices
- Specify a single platform plus filters: “Search Reddit r/algotrading between 2024-08-01 and 2024-08-31; ignore duplicate cross-posts.”
- Provide keyword and account whitelists/blacklists to keep the run focused.
- Cap `LIMIT` to a workable number (3–5) so the model spends more effort vetting each idea.
- Remind the model to document ignored candidates (“Log discarded ideas in a scratchpad”) when you need transparency.
- When you already have raw links, feed them in via a quick bulleted list and ask the model to synthesize rather than re-searching the web.

### Automating Prompt Runs
- Store reusable run parameters under `config/` (see `config/twitter-scan.env` for an example).
- Use `uv run generate-prompt config/twitter-scan.env` to emit a dated prompt request. `uv` reads `pyproject.toml`, builds an isolated environment, and exposes the `generate-prompt` console script.
- The generated markdown lands in `content/prompt-requests/` by default and starts with `### YYYYMMDD <Config Title>` for quick cataloging.
- Override filenames with `OUTPUT_BASENAME` in the config or supply an explicit output path as a second argument: `uv run generate-prompt config/twitter-scan.env tmp/my-run.md`.
- Each uppercase key in the config replaces a matching `{KEY}` token in the template; placeholders with no config value are left untouched so you can fill them manually before sharing with an LLM.
- Rotate through the provided configs for broader coverage, e.g. `uv run generate-prompt config/kaggle-optiver.env`, `uv run generate-prompt config/twitter-alpha-hunters.env`, `uv run generate-prompt config/reddit-algotrading.env`, `uv run generate-prompt config/github-research.env`, or `uv run generate-prompt config/arxiv-cross-sectional.env`.
- When a report is complete, run `uv run collect-json --reports-dir content/reports --index data/alpha-index.jsonl` to extract the embedded JSON blocks and append the ideas to the lightweight search index. Add `--dump-json data/json` if you also want individual `.json` snapshots.
- If you already have a standalone JSON file from an LLM, skip the markdown step and call `uv run append-index path/to/report.json --index data/alpha-index.jsonl`.
- The indexer computes a SHA-256 hash of each idea’s payload; re-running the command skips ideas already archived so duplicates are not appended.

### Cataloging & Search
- Drop structured metadata (JSONL or CSV) into `data/` so you can index alphas without a heavyweight database. A simple schema—`{"date": "...", "title": "...", "keywords": [...], "source": "...", "report_path": "..."}`—is enough for filtering.
- The keyword and expected horizon notes in each report let you group alphas by theme and testing timeline (e.g., order-flow, earnings drift, sentiment; 3y intraday backtest).
- Consider running a periodic script that parses `content/reports/` and appends entries to `data/alpha-index.jsonl`.
- The JSON index includes a stable hash identifier (`hash`) for each idea so you can detect repeats or reference the original record succinctly.
- If you outgrow flat files, the same records can be loaded into SQLite or DuckDB with minimal changes.

### Compliance & Ethics
- This repository can hold prompt templates, generated prompt requests, and any downstream reports you commit. Review everything before sharing to ensure it is appropriate for external distribution.
- If you are affiliated with a regulated firm (e.g. hedge fund, broker-dealer), confirm with your compliance team before sending non-public or client-related information to external services. Some firms require pre-cleared tooling or VPN routing, even on personal time.
- Avoid copying material that is proprietary or under NDA into third-party models; stick to publicly available sources.
- Nothing here is legal advice—follow your employer and regulator policies first.
