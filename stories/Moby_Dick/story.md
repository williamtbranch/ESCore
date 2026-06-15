# Moby Dick book brief

This book follows the root `free_flow.md` workflow.

## Goals

- Produce natural, idiomatic Spanish prose at graded-reader level UL20-UL23.
- Preserve the core movement of each chapter while keeping the prose readable
	and literary.
- Keep the work consistent across chapters with shared character, scene, and
	visual continuity.

## Chapter selection

- The chapter being worked on will be indicated by the user.
- If the user does not specify a chapter, ask which chapter to work on before
	starting.

## Project structure

- Each chapter is its own project folder.
- Canonical chapter source is `source.txt` in that folder.
- `story.txt` is the scored Spanish draft.
- `story_en.md` is literal English for review and markup.
- `story.toml` defines prompts for every `%%META illustration: <key>%%` marker.

## Illustration requirements

- All chapter folders must use illustration markers and a matching TOML file.
- Use stable chapter-scene keys with a chapter prefix.
- Keep character and world continuity aligned with the book-level
	`series_bible.md`.
- Keep a shared scene/character bible current as the book grows.

## Scoring policy

- Follow the root `free_flow.md` scoring and packaging rules.
- If legitimate Spanish forms are mis-ranked because of enclitics or
	conjugations, fix the scorer or its exceptions/overrides.
- Do not rewrite natural prose just to work around scorer bugs.