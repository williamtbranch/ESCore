#!/usr/bin/env python3
"""Split Moby Dick full text into per-chapter subfolders.

Input:
  English_source.txt in the same directory.

Output:
    chapters/Chapter_001_Loomings/source.txt
    chapters/Chapter_002_The_Carpet_Bag/source.txt
  ...
"""

from __future__ import annotations

import re
from pathlib import Path

SOURCE_FILE = "English_source.txt"
OUTPUT_DIR = "chapters"

# Matches: CHAPTER 1. Loomings.
CHAPTER_RE = re.compile(r"^CHAPTER\s+(\d+)\.\s*(.+?)\s*$")


def slugify(title: str) -> str:
    slug = title.strip().rstrip(".")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "Untitled"


def split_chapters(source_path: Path, output_root: Path) -> int:
    lines = source_path.read_text(encoding="utf-8-sig").splitlines()

    chapters: list[tuple[int, str, int]] = []
    for idx, line in enumerate(lines):
        match = CHAPTER_RE.match(line.strip())
        if match:
            number = int(match.group(1))
            title = match.group(2)
            chapters.append((number, title, idx))

    if not chapters:
        raise ValueError("No chapter headings found.")

    output_root.mkdir(parents=True, exist_ok=True)

    for i, (num, title, start_idx) in enumerate(chapters):
        end_idx = chapters[i + 1][2] if i + 1 < len(chapters) else len(lines)
        chunk = lines[start_idx:end_idx]

        folder_name = f"Chapter_{num:03d}_{slugify(title)}"
        chapter_dir = output_root / folder_name
        chapter_dir.mkdir(parents=True, exist_ok=True)

        chapter_text = "\n".join(chunk).rstrip() + "\n"
        (chapter_dir / "source.txt").write_text(chapter_text, encoding="utf-8")

    return len(chapters)


def main() -> int:
    base = Path(__file__).resolve().parent
    source_path = base / SOURCE_FILE
    output_root = base / OUTPUT_DIR

    if not source_path.exists():
        raise FileNotFoundError(f"Missing source file: {source_path}")

    count = split_chapters(source_path, output_root)
    print(f"Wrote {count} chapter folders under: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
