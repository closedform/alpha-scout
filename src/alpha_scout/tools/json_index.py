"""Utilities for appending structured alpha ideas into a JSONL index."""

from __future__ import annotations

import argparse
import json
import hashlib
from pathlib import Path
from typing import Any, Dict, Iterable, List


def _normalize_string(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False)


def _ensure_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str):
        return [value]
    return [json.dumps(value, ensure_ascii=False)]


def load_report(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("JSON report must be an object.")
    if "ideas" not in data:
        raise ValueError("JSON report missing 'ideas' key.")
    return data


def iterate_records(report: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    meta = report.get("meta", {})
    for idea in report.get("ideas", []):
        record = {
            "title": _normalize_string(idea.get("title")),
            "date": _normalize_string(meta.get("report_date")),
            "source_searched": _normalize_string(meta.get("source_searched")),
            "query": _normalize_string(meta.get("query")),
            "equity_class": _normalize_string(idea.get("equity_class")),
            "horizon": _normalize_string(idea.get("horizon")),
            "signal_type": _normalize_string(idea.get("signal_type")),
            "keywords": _ensure_list(idea.get("keywords")),
            "expected_horizon_notes": _normalize_string(idea.get("expected_horizon_notes")),
            "strength_rating": _normalize_string(
                idea.get("strength_actionability", {}).get("rating")
                if isinstance(idea.get("strength_actionability"), dict)
                else idea.get("strength_actionability")
            ),
            "report_path": _normalize_string(report.get("_report_path", "")),
            "citations": _ensure_list(idea.get("citations")),
        }
        yield record


def hash_record(record: Dict[str, Any]) -> str:
    payload = json.dumps(record, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def filter_new_records(
    records: Iterable[Dict[str, Any]],
    existing_hashes: Iterable[str],
) -> List[Dict[str, Any]]:
    seen = set(existing_hashes)
    filtered: List[Dict[str, Any]] = []
    for record in records:
        record_hash = record.get("hash") or hash_record(record)
        if record_hash in seen:
            continue
        record = dict(record)
        record["hash"] = record_hash
        filtered.append(record)
        seen.add(record_hash)
    return filtered


def append_records(index_path: Path, records: Iterable[Dict[str, Any]]) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with index_path.open("a", encoding="utf-8") as f:
        for record in records:
            if "hash" not in record:
                record = dict(record)
                record["hash"] = hash_record(record)
            json.dump(record, f, ensure_ascii=False)
            f.write("\n")


def record_hashes(records: Iterable[Dict[str, Any]], sink: set[str]) -> None:
    for record in records:
        if "hash" in record:
            sink.add(record["hash"])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Append JSON report ideas into a JSONL index file."
    )
    parser.add_argument(
        "json_report",
        type=Path,
        help="Path to the structured JSON report (as produced by the prompt template).",
    )
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("data/alpha-index.jsonl"),
        help="Path to the JSONL index file (default: data/alpha-index.jsonl).",
    )
    parser.add_argument(
        "--report-path",
        type=str,
        default="",
        help="Optional relative path to store in each record for traceability.",
    )

    args = parser.parse_args()

    if not args.json_report.is_file():
        parser.error(f"JSON report not found: {args.json_report}")

    report = load_report(args.json_report)
    if args.report_path:
        report["_report_path"] = args.report_path

    records = list(iterate_records(report))
    if not records:
        parser.error("No ideas found in report.")

    append_records(args.index, records)
    print(f"Appended {len(records)} ideas to {args.index}")


if __name__ == "__main__":
    main()
