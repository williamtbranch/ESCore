# Chapter 001 — Loomings (project brief)

This chapter follows the root `free_flow.md` workflow.

## Goals

- Produce natural, idiomatic Spanish prose at graded-reader level UL20-UL23.
- Preserve the core movement of Chapter 1 (Ishmael's state of mind, pull toward
  the sea, and choice to go as sailor, not passenger).
- Keep rhythm readable and literary, without NSM-style over-explaining.

## Source and constraints

- Canonical chapter source is `source.txt` in this folder (do not modify).
- `story.txt` is the scored Spanish draft.
- `story_en.md` is literal English for review and markup.
- `story.toml` defines prompts for every `%%META illustration: <key>%%` marker.

## Illustration requirements

- Keep character and world continuity aligned with `stories/Moby_Dick/series_bible.md`.
- Use stable chapter-scene keys (prefix `ch01_`).
- Every illustration marker in `story.txt` must have a matching key in `story.toml`.

## Scoring policy

If legitimate Spanish forms (enclitics/conjugations) are mis-ranked, fix the
scorer/overrides; do not rewrite natural prose just to bypass scorer bugs.