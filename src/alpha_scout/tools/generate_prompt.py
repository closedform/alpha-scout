"""Generate a filled-in alpha discovery prompt from a config file.

Run via uv:

    uv run generate-prompt config/twitter-scan.env
"""
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Mapping


CONFIG_DEFAULT_TEMPLATE = Path("content/prompts/alpha-discovery-report.md")
CONFIG_DEFAULT_OUTPUT_DIR = Path("content/prompt-requests")


@dataclass
class PromptConfig:
    raw: Dict[str, str]
    template_path: Path
    output_dir: Path
    config_title: str
    output_basename: str | None = None


def parse_env_file(path: Path) -> Dict[str, str]:
    """Parse a simple KEY=VALUE env file."""
    variables: Dict[str, str] = {}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            continue

        if value and value[0] in {'"', "'"} and value[-1:] == value[0]:
            value = value[1:-1]

        variables[key] = value

    return variables


def build_config(env_path: Path) -> PromptConfig:
    env = parse_env_file(env_path)

    template_path = Path(env.get("PROMPT_TEMPLATE", CONFIG_DEFAULT_TEMPLATE))
    output_dir = Path(env.get("OUTPUT_DIR", CONFIG_DEFAULT_OUTPUT_DIR))
    config_title = env.get("CONFIG_TITLE", env_path.stem)
    output_basename = env.get("OUTPUT_BASENAME")

    return PromptConfig(
        raw=env,
        template_path=template_path,
        output_dir=output_dir,
        config_title=config_title,
        output_basename=output_basename,
    )


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "prompt"


def resolve_output_path(
    cfg: PromptConfig, override: Path | None, datestamp: str
) -> Path:
    if override is not None:
        return override

    if cfg.output_basename:
        basename = cfg.output_basename
    else:
        basename = slugify(cfg.config_title)

    return cfg.output_dir / f"{datestamp}-{basename}.md"


def fill_template(
    template_path: Path,
    header_line: str,
    variables: Mapping[str, str],
) -> tuple[str, Iterable[str]]:
    pattern = re.compile(r"\{([A-Za-z0-9_]+)\}")
    missing: set[str] = set()

    template_text = template_path.read_text()

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key in variables:
            return variables[key]
        missing.add(key)
        return match.group(0)

    body = pattern.sub(replace, template_text)
    return f"{header_line}\n\n{body}", sorted(missing)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a dated alpha discovery prompt from a config file."
    )
    parser.add_argument(
        "config_path",
        type=Path,
        help="Path to the KEY=VALUE env config (e.g., config/twitter-scan.env)",
    )
    parser.add_argument(
        "output_path",
        type=Path,
        nargs="?",
        help="Optional explicit path for the generated markdown.",
    )

    args = parser.parse_args()

    if not args.config_path.is_file():
        parser.error(f"Config file not found: {args.config_path}")

    cfg = build_config(args.config_path)

    if not cfg.template_path.is_file():
        parser.error(f"Prompt template not found: {cfg.template_path}")

    today = datetime.now().strftime("%Y%m%d")
    output_path = resolve_output_path(cfg, args.output_path, today)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    header = f"### {today} {cfg.config_title}"
    merged_vars = {**os.environ, **cfg.raw}
    filled, missing = fill_template(cfg.template_path, header, merged_vars)

    output_path.write_text(filled)

    print(f"Wrote prompt to {output_path}")
    if missing:
        print(
            "Warning: no value provided for "
            + ", ".join(missing)
            + " (placeholders left in template)",
            file=os.sys.stderr,
        )


if __name__ == "__main__":
    main()
