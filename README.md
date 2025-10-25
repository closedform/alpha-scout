# alpha-scout

Collecting alpha from online sources.

Lean tooling for drafting LLM prompts, capturing structured reports, and cataloging equity alpha ideas. Extend it with new templates in `content/prompts/`, configs in `config/`, or processing helpers in `src/alpha_scout/tools/`.

## Basic Usage
```bash
# 1) Generate a prompt from a config
uv run generate-prompt config/twitter-scan.env

# 2) Paste the markdown file from content/prompt-requests/ into an LLM
#    (fill placeholders, remind the model to include keywords, horizon notes, JSON)

# 3) Save the response under content/reports/<date>-<slug>.md

# 4) Ingest the ideas into the index
uv run collect-json --reports-dir content/reports --index content/data/alpha-index.jsonl

# Optional: ingest a standalone JSON file
uv run append-index results/report.json --index content/data/alpha-index.jsonl
```

## Directory Layout
- `config/` – ENV parameter sets for different searches.
- `content/prompts/` – reusable prompt templates (markdown).
- `content/prompt-requests/` – generated prompts ready to paste into an LLM.
- `content/reports/` – completed write-ups (markdown + JSON block).
- `data/` – lightweight indexes such as `alpha-index.jsonl`.
- `src/alpha_scout/` – CLI helpers (`generate-prompt`, `collect-json`, `append-index`).

## Prompt & Scoping Tips
- Run one surface at a time and spell out filters (date range, handles, keywords).
- Keep `LIMIT` to what you intend to review unless you want a deep sweep.
- Ask the model for a brief "discarded ideas" log when transparency matters.
- Provide curated links when you only need synthesis rather than exploration.

## Cataloging & Search
- `collect-json` extracts the fenced JSON payload and appends SHA-256 deduped ideas to `content/data/alpha-index.jsonl`.
- Keywords and expected-horizon notes make it easy to group alphas by theme and testing effort.
- Stick with flat files for quick filtering; move to SQLite/DuckDB if you need heavier analytics.

## Compliance & Ethics
- Do not send proprietary or client data to external LLMs without approval.
- Templates and tools are generic; review every report before sharing.
- Nothing here is legal advice—follow employer and regulator policies first.

## Troubleshooting
- Review `content/data/collect-log.txt` after running `uv run collect-json` to see any reports that could not be ingested.
- If a report needs repair, generate a fix-it prompt with `uv run --module alpha_scout.tools.report_fix_prompt --report <path/to/report.md> --error "<collect-json message>"` and feed it to an LLM to regenerate clean markdown and JSON.

## License
- Code (`/src` and subfolders): Apache License 2.0 (`LICENSE-CODE`).
- Content (`/content`): CC BY 4.0 (`LICENSE-CONTENT`).

No crypto content is included or licensed here.

