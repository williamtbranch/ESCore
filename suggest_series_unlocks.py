#!/usr/bin/env python3
"""Suggest the next vocabulary unlocks for an episodic ESCore series.

The script reads a lemmatized frequency list and filters out words already
covered by the global whitelist, proper-noun whitelist, or the series-local
whitelist in a story directory. The result is a short ranked candidate list to
help choose the next words to unlock.

This is advisory, not automatic. Final selection should balance:
  1. story-driven needs,
  2. high-frequency beginner usefulness,
  3. contextual learnability inside the episode.
"""

from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path


def strip_accents(text: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn"
    )


def load_token_set(path: Path) -> set[str]:
    values: set[str] = set()
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        token = raw.strip()
        if not token or token.startswith("#"):
            continue
        values.add(token.lower())
    return values


def load_frequency_rows(path: Path) -> list[tuple[str, int, int]]:
    rows: list[tuple[str, int, int]] = []
    for index, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines()):
        line = raw.strip()
        if not line:
            continue
        parts = line.split()
        if index == 0 and parts[:3] == ["lemma", "rank", "occurrences"]:
            continue
        if len(parts) < 3:
            continue
        lemma, rank_text, occ_text = parts[0], parts[1], parts[2]
        try:
            rows.append((lemma.lower(), int(rank_text), int(occ_text)))
        except ValueError:
            continue
    return rows


def build_known_norms(paths: list[Path]) -> set[str]:
    known: set[str] = set()
    for path in paths:
        for token in load_token_set(path):
            known.add(strip_accents(token))
    return known


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Suggest the next series unlock words.")
    parser.add_argument("--story-dir", required=True,
                        help="Series/story directory containing whitelist.txt")
    parser.add_argument("--count", type=int, default=10,
                        help="Number of candidates to print")
    parser.add_argument("--frequency-list", default="assets/frequency_list.txt")
    parser.add_argument("--global-whitelist", default="whitelist.txt")
    parser.add_argument("--pn-whitelist", default="PN_whitelist.txt")
    parser.add_argument("--story-whitelist-name", default="whitelist.txt")
    args = parser.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    base = Path.cwd()
    story_dir = base / args.story_dir
    if not story_dir.exists() or not story_dir.is_dir():
        raise FileNotFoundError(f"Story directory not found: {story_dir}")

    frequency_path = base / args.frequency_list
    story_whitelist = story_dir / args.story_whitelist_name
    known_norms = build_known_norms([
        base / args.global_whitelist,
        base / args.pn_whitelist,
        story_whitelist,
    ])

    candidates: list[tuple[str, int, int]] = []
    for lemma, rank, occurrences in load_frequency_rows(frequency_path):
        if strip_accents(lemma) in known_norms:
            continue
        candidates.append((lemma, rank, occurrences))
        if len(candidates) >= args.count:
            break

    print(f"Series directory: {args.story_dir}")
    print(f"Story whitelist: {story_whitelist.relative_to(base)}")
    print(f"Candidates requested: {args.count}")
    print()
    print("Next unlock candidates (frequency-ranked, not yet whitelisted):")
    for lemma, rank, occurrences in candidates:
        print(f"  {rank:>5}  {lemma:<20} {occurrences}")

    if not candidates:
        print("  none")

    print()
    print("Selection rule:")
    print("  Choose a mix of story-needed words and high-frequency words the")
    print("  episode can teach clearly in context. After unlocking, add them")
    print("  to the series whitelist and log them in series_vocabulary.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())