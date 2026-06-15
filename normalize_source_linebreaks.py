#!/usr/bin/env python3
"""
normalize_source_linebreaks.py

Normalize hard-wrapped source text files:
- paragraph breaks (blank lines) are preserved
- single line breaks inside paragraphs are replaced with spaces

By default, updates files in place.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.strip("\n")

    # Split paragraphs on one or more blank lines.
    paragraphs = re.split(r"\n\s*\n+", text)
    normalized_paragraphs: list[str] = []

    for p in paragraphs:
        # Collapse intra-paragraph hard wraps to single spaces.
        p = re.sub(r"\s*\n\s*", " ", p)
        p = re.sub(r"[ \t]+", " ", p).strip()
        if p:
            normalized_paragraphs.append(p)

    if not normalized_paragraphs:
        return ""

    return "\n\n".join(normalized_paragraphs) + "\n"


def collect_targets(path: Path, recursive: bool) -> list[Path]:
    if path.is_file():
        return [path]
    if not path.is_dir():
        return []

    pattern = "**/source.txt" if recursive else "source.txt"
    return sorted(p for p in path.glob(pattern) if p.is_file())


def process_file(path: Path, dry_run: bool) -> tuple[bool, int, int]:
    original = path.read_text(encoding="utf-8-sig")
    normalized = normalize_text(original)

    changed = normalized != original
    if changed and not dry_run:
        path.write_text(normalized, encoding="utf-8", newline="\n")

    return changed, len(original), len(normalized)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Normalize hard-wrapped source text: keep paragraph breaks, remove single line wraps."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="One or more source.txt files or directories.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="If a path is a directory, recurse and process all source.txt files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing files.",
    )
    args = parser.parse_args(argv)

    targets: list[Path] = []
    for path in args.paths:
        found = collect_targets(path, recursive=args.recursive)
        if not found:
            print(f"WARN: no target source.txt found for: {path}", file=sys.stderr)
            continue
        targets.extend(found)

    # De-duplicate while preserving stable sorted order.
    targets = sorted(set(targets))

    if not targets:
        print("ERROR: no source.txt files to process.", file=sys.stderr)
        return 1

    changed_count = 0
    for target in targets:
        changed, old_len, new_len = process_file(target, dry_run=args.dry_run)
        status = "CHANGED" if changed else "OK"
        print(f"{status}: {target} ({old_len} -> {new_len} chars)")
        if changed:
            changed_count += 1

    print(f"Processed: {len(targets)} file(s); changed: {changed_count}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
