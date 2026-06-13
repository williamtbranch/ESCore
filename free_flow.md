# ESCore Free-Flow Story Workflow

This document describes the **free-flow** workflow: writing a natural-sounding
Spanish story that is **not** bound by the strict ESCore register, and gating it
only by a target reading level (UL score). It is the counterpart to
[`flow.md`](flow.md), which covers the strict, whitelist-audited ESCore flow.

Use **free-flow** when the goal is *natural prose at a controlled difficulty*
(e.g. a follow-up to `John_and_Alice`). Use the strict `flow.md` when the goal is
canonical ESCore-compliant text.

---

## 1. Philosophy

- **Natural language first.** Render scenes the way prose actually reads. Avoid
  NSM-style explications ("put food in their bodies", "be in another place").
  Meaning does not have to be made fully explicit — context plus repeated
  exposure over time teaches words. *"After Alice ate, she felt better."* is
  enough; we do not have to define *ate*.
- **Show, don't tell.** Low plot is fine. Scenery, two people, what they feel.
- **The score is the only hard gate.** You are *not* bound by `ESCore.md`,
  `whitelist.txt`, or the audit. The whole Spanish language is available — but
  **rarer words cost more**, so there is a natural pull toward simple vocabulary.
- **Target: UL 20–24 after rounding down** (e.g. 24.6 is fine). `John_and_Alice`
  is ~UL21; `John_and_Alice2` lands at UL23.

---

## 2. File conventions (per story folder)

| File | Role |
|---|---|
| `story.md` | The **brief / intent**: requirements, target score, constraints. Authored by the human; do not overwrite it. |
| `story.txt` | The **Spanish story** that gets scored. Begins with the `%%META ... %%` header block (directives are stripped before scoring). |
| `story_en.md` | A **literal English translation** for human review. The human marks it up; edits flow back into `story.txt`. |

---

## 3. The iteration loop

```
        ┌─────────────────────────────────────────────┐
        │ 1. Write / revise Spanish  → story.txt       │
        │ 2. Score it (avd_ul_score) → UL              │
        │ 3. UL in 20–24?  ── no ──► simplify, go to 2 │
        │            │ yes                              │
        │ 4. Write literal English  → story_en.md      │
        │ 5. Human reviews & marks up story_en.md      │
        │ 6. Fold edits back into Spanish → story.txt  │
        │ 7. Re-score (human edits can move the score) │
        │            └────────── repeat until approved │
        └─────────────────────────────────────────────┘
```

1. **Write the Spanish** in `story.txt`. Keep the vocabulary common; lean on
   repetition. Rare descriptive words (colours, body parts, weather words,
   birds/leaves/clouds) spike the score fast — cut them first when over budget.
2. **Score it** (see §4). If above UL24, simplify and re-score.
3. **Write the literal English** in `story_en.md` only once the score passes.
4. **Human review.** The human edits `story_en.md` inline (often with `#edit -`
   / `#` comment lines explaining the change).
5. **Apply edits to the Spanish**, re-score (human edits can push the score back
   up — adjust as needed), then refresh `story_en.md` clean for the next round.
6. Repeat until the human approves.

---

## 4. Scoring — `avd_ul_score.py` / `score_story.ps1`

A standalone, fast scorer that reproduces WeaveLang's `measure_user_score`
math **without** launching the WeaveLang app (no risk to its project state).

### Run it

```powershell
# Wrapper (recommended) — table output:
.\score_story.ps1 stories\John_and_Alice2\story.txt

# Show the rarest contributing lemmas (spot mis-lemmatized words / stray names):
.\score_story.ps1 stories\John_and_Alice2\story.txt -ShowRare 12

# No args = score every top-level Spanish story.txt under stories\ (skips *_en).
.\score_story.ps1
```

The scorer needs spaCy + `es_core_news_lg` + `snowballstemmer`. By default it
uses WeaveLang's venv interpreter; override with `$env:ESCORE_PYTHON`.

### Reading the output

```
Story       Tokens   InList      AVD   UL(x)    UL
--------------------------------------------------
story.txt      385      385   234.00    22.7  UL23
```

- **Tokens** — scored tokens (proper nouns and header directives excluded).
- **InList** — tokens found in the frequency list (the rest are treated as rare).
- **AVD** — tail-weighted average difficulty `(p85 + 2·p95)/3`.
- **UL(x)** — exact user level; **UL** — rounded. The gate is on UL 20–24.

### How it works (and why it is fast)

- Uses a **trimmed top-10k frequency list** (`assets/es_freq_top10k.txt`,
  generated from WeaveLang's 3.48M-line master) so startup only stems 10k
  lemmas, not millions → near-instant instead of a long wait.
- Any lemma **not** in the top-10k list is assigned **rank 20000** (rare). This
  is deliberately conservative: a rare word cannot sneak through by being
  silently dropped.
- **Proper nouns** (spaCy `PROPN`, e.g. *John*, *Alice*) are **excluded** so
  names never inflate difficulty.
- `%%META ... %%` header directives are **stripped** before tokenizing (so
  words like *on*, *meta*, *es* in the header never count as prose).
- A `LEMMA_OVERRIDES` table in `avd_ul_score.py` corrects known spaCy
  mis-lemmatizations; grow it as `--show-rare` surfaces bad cases.

> **Note — intentional divergence from exact WeaveLang parity.** The trimmed
> list, the 20000 sentinel, and the proper-noun/header exclusions make this a
> fast *pre-screen*, not a 1:1 replica. For simple-register stories (target
> UL ≤ 24) the number does not move versus parity — real words never reach the
> p95 mark above rank 10k. For an exact parity check, point `--freq-list` at the
> full master list:
> `assets\frequency_lists\es_master_frequency_list.txt` in the WeaveLang repo.

### Using `--show-rare` during iteration

After each score, run `-ShowRare 10` and scan the list. Every entry should be a
real, correctly-lemmatized Spanish word. If you see:

- an **English/junk token** (`on`, `meta`) → a directive or stray text leaked in;
- a **proper noun** → confirm it should be excluded (add to handling if needed);
- a **mis-lemmatized word** → add a fix to `LEMMA_OVERRIDES`;

those are the words to fix or simplify next.

---

## 5. Quick checklist

- [ ] `story.txt` written in natural, simple Spanish (no NSM explications).
- [ ] Scored with `score_story.ps1`; **UL 20–24**.
- [ ] `-ShowRare` list contains only legitimate Spanish words.
- [ ] `story_en.md` literal English produced for review.
- [ ] Human edits folded back into Spanish and **re-scored**.
- [ ] Approved → done.
