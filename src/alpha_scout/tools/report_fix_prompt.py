"""Generate a repair prompt for fixing a malformed alpha discovery report."""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent

DEFAULT_TEMPLATE = Path("content/prompts/alpha-discovery-report.md")


def build_prompt(report_text: str, template_text: str, error: str) -> str:
    return dedent(
        f"""
        ### Repair Task
        A previously generated alpha discovery report failed JSON validation when running `collect-json`.
        Fix the report so that the JSON payload at the end is valid, follows the schema, and remains consistent with the narrative sections.
        Preserve all substantive content; correct only the formatting and structure needed for a clean ingest.

        **Observed error:** {error}

        --- Canonical Template ---
        ~~~markdown
        {template_text.strip()}
        ~~~

        --- Report Requiring Fix ---
        ~~~markdown
        {report_text.strip()}
        ~~~

        Return only the corrected report in markdown, preserving the JSON block at the end.
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an instruction prompt to repair an alpha discovery report."
    )
    parser.add_argument(
        "--report",
        type=Path,
        required=True,
        help="Path to the markdown report that needs fixing.",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help="Prompt template to embed for reference (default: content/prompts/alpha-discovery-report.md).",
    )
    parser.add_argument(
        "--error",
        default="JSON parsing failed during collect-json.",
        help="Optional error message to include in the prompt.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the prompt to this file instead of stdout.",
    )

    args = parser.parse_args()

    if not args.report.is_file():
        parser.error(f"Report not found: {args.report}")
    if not args.template.is_file():
        parser.error(f"Template not found: {args.template}")

    report_text = args.report.read_text(encoding="utf-8")
    template_text = args.template.read_text(encoding="utf-8")

    prompt = build_prompt(report_text, template_text, args.error)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(prompt, encoding="utf-8")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
