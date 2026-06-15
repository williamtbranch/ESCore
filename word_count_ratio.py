#!/usr/bin/env python3
"""
word_count_ratio.py - Compare submission word count against source length.

Design rule:
  pass when submission_words / source_words is within [min_percent, max_percent].

The counter ignores full-line %%META directives in both files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

META_LINE_RE = re.compile(r"^\s*%%META\b.*$", re.IGNORECASE)
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’-][A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)


def strip_meta_lines(text: str) -> str:
    lines = text.splitlines()
    kept = [line for line in lines if not META_LINE_RE.match(line)]
    return "\n".join(kept)


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def build_result(
    submission_path: Path,
    source_path: Path,
    min_percent: float,
    max_percent: float,
) -> dict:
    submission_text = strip_meta_lines(read_text(submission_path))
    source_text = strip_meta_lines(read_text(source_path))

    submission_words = count_words(submission_text)
    source_words = count_words(source_text)

    if source_words <= 0:
        raise ValueError(f"Source has zero countable words after META stripping: {source_path}")

    pct = (submission_words / source_words) * 100.0
    passed = min_percent <= pct <= max_percent

    return {
        "submission": str(submission_path),
        "source": str(source_path),
        "submission_words": submission_words,
        "source_words": source_words,
        "percent_of_source": round(pct, 2),
        "min_percent": min_percent,
        "max_percent": max_percent,
        "pass": passed,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Measure submission word-count as a percentage of source, "
            "ignoring full-line %%META directives."
        )
    )
    parser.add_argument("submission", type=Path, help="Submission text file.")
    parser.add_argument("source", type=Path, help="Source/original text file.")
    parser.add_argument(
        "--min-percent",
        type=float,
        default=85.0,
        help="Minimum allowed percentage of source words (default: 85).",
    )
    parser.add_argument(
        "--max-percent",
        type=float,
        default=120.0,
        help="Maximum allowed percentage of source words (default: 120).",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args(argv)

    if not args.submission.is_file():
        print(f"ERROR: submission not found: {args.submission}", file=sys.stderr)
        return 1
    if not args.source.is_file():
        print(f"ERROR: source not found: {args.source}", file=sys.stderr)
        return 1
    if args.min_percent < 0 or args.max_percent < 0:
        print("ERROR: min/max percent must be non-negative.", file=sys.stderr)
        return 1
    if args.min_percent > args.max_percent:
        print("ERROR: min-percent cannot exceed max-percent.", file=sys.stderr)
        return 1

    try:
        result = build_result(args.submission, args.source, args.min_percent, args.max_percent)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["pass"] else "FAIL"
        print(f"Submission:    {result['submission']}")
        print(f"Source:        {result['source']}")
        print(f"Words:         {result['submission_words']} / {result['source_words']}")
        print(f"Percent:       {result['percent_of_source']:.2f}%")
        print(f"Allowed range: {result['min_percent']:.1f}% - {result['max_percent']:.1f}%")
        print(f"Result:        {status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
