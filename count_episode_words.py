"""
count_episode_words.py  —  report token count and estimated duration for each episode.

Calibration: Episode 1 = 1,771 tokens = 15 min  →  ~118 tokens / minute.

Usage:
    python count_episode_words.py                          # scan all stories
    python count_episode_words.py --story Nadie_Lo_Vio_Morir
    python count_episode_words.py --tokens-per-min 110     # override calibration
"""

import argparse
import re
from pathlib import Path

# ── calibration ──────────────────────────────────────────────────────────────
DEFAULT_TOKENS_PER_MIN = 118   # from Episode 1: 1,771 tokens = 15 min

TARGET_LOW  = 1_771            # Episode 1 length (lower bound)
TARGET_HIGH = round(TARGET_LOW * 1.30)   # +30 %  → 2,302


def count_tokens(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    # strip %%META lines if present
    text = re.sub(r"^[ \t]*%%META.*$", "", text, flags=re.MULTILINE)
    return len(re.findall(r"\b\w+\b", text))


def fmt_dur(tokens: int, tpm: float) -> str:
    mins = tokens / tpm
    m = int(mins)
    s = round((mins - m) * 60)
    return f"{m}m {s:02d}s"


def status(tokens: int) -> str:
    if tokens < TARGET_LOW:
        pct = round((TARGET_LOW - tokens) / TARGET_LOW * 100)
        return f"SHORT  ({pct}% below target floor)"
    elif tokens > TARGET_HIGH:
        pct = round((tokens - TARGET_HIGH) / TARGET_HIGH * 100)
        return f"LONG   ({pct}% above target ceiling)"
    else:
        return "OK     (within target range)"


def main():
    parser = argparse.ArgumentParser(description="Count tokens per episode and estimate duration.")
    parser.add_argument("--story", default=None, help="Limit to one story folder name.")
    parser.add_argument("--tokens-per-min", type=float, default=DEFAULT_TOKENS_PER_MIN,
                        metavar="N", help=f"Narration rate (default {DEFAULT_TOKENS_PER_MIN}).")
    args = parser.parse_args()

    tpm  = args.tokens_per_min
    root = Path(__file__).parent / "stories"

    if args.story:
        dirs = [root / args.story]
    else:
        dirs = sorted(d for d in root.iterdir() if d.is_dir())

    print(f"\n{'Story':<28} {'Episode':<30} {'Tokens':>7}  {'Est. Time':>9}  Status")
    print("-" * 90)

    for story_dir in dirs:
        episodes = sorted(story_dir.glob("episode_*.txt"))
        if not episodes:
            continue
        for ep in episodes:
            tokens = count_tokens(ep)
            print(f"{story_dir.name:<28} {ep.name:<30} {tokens:>7}  {fmt_dur(tokens, tpm):>9}  {status(tokens)}")

    print()
    print(f"Target range: {TARGET_LOW:,} – {TARGET_HIGH:,} tokens  "
          f"({fmt_dur(TARGET_LOW, tpm)} – {fmt_dur(TARGET_HIGH, tpm)} at {tpm:.0f} tok/min)")
    print()


if __name__ == "__main__":
    main()
