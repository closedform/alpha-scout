"""Extract JSON payloads from markdown reports and append to the index."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Set

from . import json_index

JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL | re.IGNORECASE)


def _fallback_json(markdown: str) -> str | None:
    """Attempt to extract a JSON object when no fenced block exists."""

    anchor = markdown.lower().rfind("json export schema")
    region = markdown[anchor:] if anchor != -1 else markdown

    idx = region.find("{")
    while idx != -1:
        depth = 0
        end = None
        for offset, char in enumerate(region[idx:], start=idx):
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = offset
                    break

        if end is not None:
            candidate = region[idx:end + 1].strip()
            if candidate:
                try:
                    json.loads(candidate)
                    return candidate
                except json.JSONDecodeError:
                    pass

        idx = region.find("{", idx + 1)

    return None


def find_json_block(markdown: str) -> str:
    matches = JSON_BLOCK.findall(markdown)
    if matches:
        return matches[-1]

    fallback = _fallback_json(markdown)
    if fallback is None:
        raise ValueError("No JSON block found in markdown report.")
    return fallback


def parse_report(markdown_path: Path) -> dict:
    text = markdown_path.read_text(encoding="utf-8")
    json_str = find_json_block(text)
    data = json.loads(json_str)
    if not isinstance(data, dict):
        raise ValueError("JSON block must decode to an object.")
    data["_report_path"] = str(markdown_path)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract JSON blocks from markdown reports and append to the alpha index."
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path("content/reports"),
        help="Directory containing markdown reports (default: content/reports).",
    )
    parser.add_argument(
        "--glob",
        type=str,
        default="*.md",
        help="Glob pattern used to select report files (default: *.md).",
    )
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("content/data/alpha-index.jsonl"),
        help="JSONL index path (default: content/data/alpha-index.jsonl).",
    )
    parser.add_argument(
        "--dump-json",
        type=Path,
        help="Optional directory to write extracted JSON payloads.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on first report that cannot be parsed (default: skip with warning).",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path("content/data/collect-log.txt"),
        help="Append warnings and extraction errors here (default: content/data/collect-log.txt).",
    )

    args = parser.parse_args()

    if not args.reports_dir.exists():
        parser.error(f"Reports directory not found: {args.reports_dir}")

    report_paths = list(args.reports_dir.glob(args.glob))
    if not report_paths:
        parser.error("No reports matched the specified pattern.")

    records: List[dict] = []
    processed_reports = 0
    dumped_reports = 0
    skipped: List[Path] = []
    log_entries: List[str] = []

    dump_dir = args.dump_json
    if dump_dir is not None:
        dump_dir.mkdir(parents=True, exist_ok=True)

    seen_hashes: Set[str] = set()

    index_path = args.index
    if index_path.is_file():
        with index_path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    existing = json.loads(line)
                    if isinstance(existing, dict) and "hash" in existing:
                        seen_hashes.add(existing["hash"])
                except json.JSONDecodeError:
                    continue

    for path in sorted(report_paths):
        try:
            report = parse_report(path)
            records.extend(json_index.iterate_records(report))
            processed_reports += 1
            if dump_dir is not None:
                dump_path = dump_dir / (path.stem + ".json")
                dump_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))
                dumped_reports += 1
        except Exception as exc:
            if args.strict:
                raise
            skipped.append(path)
            message = f"{datetime.utcnow().isoformat()}Z\t{path}\t{exc}"
            log_entries.append(message)
            print(f"Skipping {path}: {exc}")

    appended_count = 0
    if records:
        unique_records = json_index.filter_new_records(records, seen_hashes)
        if unique_records:
            json_index.append_records(args.index, unique_records)
            json_index.record_hashes(unique_records, seen_hashes)
            appended_count = len(unique_records)
        else:
            print("No new ideas to append (all hashes already present).")

    print(f"Processed {processed_reports} reports; appended {appended_count} ideas to {args.index}.")
    if dump_dir is not None:
        print(f"Wrote {dumped_reports} JSON files to {dump_dir}.")
    if skipped:
        print(f"Skipped {len(skipped)} reports.")

    if log_entries:
        log_path = args.log_file
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as log_file:
            for entry in log_entries:
                log_file.write(entry + "\n")
        print(f"Logged {len(log_entries)} issue(s) to {log_path}.")


if __name__ == "__main__":
    main()
