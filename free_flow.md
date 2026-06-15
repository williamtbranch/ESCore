# ESCore Free-Flow Story Workflow

This document describes the **free-flow** workflow: writing a natural-sounding
Spanish story that is **not** bound by the strict ESCore register, and gating it
by a target reading level (UL score), a source-relative length band, and a
final illustration-density packaging check.

Use **free-flow** when the goal is *natural prose at a controlled difficulty*
(e.g. a follow-up to `John_and_Alice`).

> **This file is self-contained — do not read other workflow docs for
> free-flow work.** A separate strict, whitelist-audited workflow exists (the
> `flow.md` / `ESCore.md` / `whitelist.txt` family), but those files are large
> and are **not relevant to free-flow**. Reading them only burns context. Ignore
> them unless the human explicitly asks for canonical ESCore-compliant text.

---

## 1. Philosophy

- **Natural language first.** Render scenes the way prose actually reads. Avoid
  NSM-style explications ("put food in their bodies", "be in another place").
  Meaning does not have to be made fully explicit — context plus repeated
  exposure over time teaches words. *"After Alice ate, she felt better."* is
  enough; we do not have to define *ate*.
- **Show, don't tell.** Low plot is fine. Scenery, two people, what they feel.
- **Text gates first, packaging gate last.** You are *not* bound by the strict
  ESCore register, its whitelist, or the audit (those belong to the separate
  strict workflow — no need to open those files). The whole Spanish language is
  available — but **rarer words cost more**, so there is a natural pull toward
  simple vocabulary.
- **UL score (info-only):** The UL score is computed and reported for the sister app's general-difficulty scale, but it is **not used as a gate** anymore.
- **i-score gate: iLevel ≤ 25.5 at coverage 0.85.** The i-score is the primary text gate. It measures the difficulty of the 85% comprehensible core, allowing the rarest 15% of the text to pass as an unpunished "+1" vocabulary tail.
- **Length gate: 85%–120% of source word count.** Compute
  `submission_words / source_words * 100`, ignoring full-line `%%META ... %%`
  marker lines in both files.
- **Illustration density gate (final packaging):** target about one
  illustration marker per 250 submission words. DRC reports required count and
  passes when marker count is within `± min(1, 15% of required)`.

---

## 2. File conventions (per story folder)

| File | Role |
|---|---|
| `story.md` | The **brief / intent**: requirements, target score, constraints. Authored by the human; do not overwrite it. |
| `story.txt` | The **Spanish story** that gets scored. Begins with the `%%META ... %%` header block (directives are stripped before scoring). |
| `story_en.md` | A **literal English translation** for human review. The human marks it up; edits flow back into `story.txt`. |
| `story.toml` | **Illustration prompt pack** keyed to `%%META illustration: <key>%%` markers in `story.txt` (scene prompts + style constraints). |
| `series_bible.md` *(recommended)* | Character/scene continuity bible so names, faces, wardrobe, locations, and visual style stay consistent across chapters/episodes. |

For chaptered works (e.g. novels), treat **each chapter as its own project folder** with this same file set.

Naming is standardized for DRC:

- Source must be named `source.txt`.
- Produced Spanish must be named `story.txt`.
- `chapter.txt` is deprecated for free-flow inputs.

For legacy texts copied from primitive viewers (hard-wrapped lines), normalize
`source.txt` before use:

- Double line breaks are paragraph boundaries and should remain paragraph breaks.
- Single line breaks inside paragraphs are line-wrap artifacts and should be removed.
- Use `normalize_source_linebreaks.py` (see §4) to do this safely.

---

## 2.1 Illustration tagging standard (required for final delivery)

All books and works in free-flow must include illustration metadata:

1. Insert inline markers in `story.txt` where scenes should be illustrated:
  `%%META illustration: <key>%%`
2. Define those keys in `story.toml` using the Nadie pattern:
  - one shared style/character section;
  - one `[[illustration]]` block per key with `key`, `scene`, and `prompt`.
3. Keep characters and environments visually consistent by maintaining a
  continuity bible (`series_bible.md` or chapter-local equivalent).

Use stable key naming (for example: `ch01_port_scene`, `ch01_arrival_night`) so
keys stay unique and easy to track across chapters.

---

## 3. The iteration loop

```
        ┌─────────────────────────────────────────────┐
        │ 1. Write / revise Spanish  → story.txt        │
        │ 2. Run DRC text gates (UL + word%)            │
        │ 3. Both in spec?  ── no ──► revise, go to 2   │
        │            │ yes                               │
        │ 4. Write literal English  → story_en.md       │
        │ 5. Human reviews & marks up story_en.md       │
        │ 6. Fold edits back into Spanish → story.txt   │
        │ 7. Re-score text gates (human edits can move) │
        │ 8. Add illustration markers as packaging step │
        │ 9. Run full DRC (incl. illustration density)  │
        │            └────────── repeat until approved  │
        └─────────────────────────────────────────────┘
```

1. **Write the Spanish** in `story.txt`. Keep the vocabulary common; lean on
   repetition. Rare descriptive words (colours, body parts, weather words,
   birds/leaves/clouds) spike the score fast — cut them first when over budget.
2. **Run DRC text gates** (see §4):
  - **i-score gate passes:** iLevel is ≤ 25.5 at coverage 0.85 (the poorest 15% is unpunished).
  - **Length gate passes:** word count must be **85%–120%** of source.
  If either check fails, revise and re-run.
3. **Write the literal English** in `story_en.md` only once the score passes.
4. **Human review.** The human edits `story_en.md` inline (often with `#edit -`
   / `#` comment lines explaining the change).
5. **Apply edits to the Spanish**, re-score (human edits can push the score back
   up — adjust as needed), then refresh `story_en.md` clean for the next round.
6. Once text is approved, add `%%META illustration: <key>%%` markers and
  matching `story.toml` keys.
7. Run final DRC and confirm the illustration-density gate passes.
8. Repeat until the human approves.

---

## 4. DRC tools — text gates + illustration density

Free-flow now uses three checks:

1. **i-score check** via `avd_ul_score.py` / `score_story.ps1` (uses `--coverage 0.85` and gates at `i-level <= 25.5`).
2. **Length check** via `word_count_ratio.py`.
3. **Illustration density check** from `story.txt` markers.

For normal iteration, use the master runner `drc_free_flow.ps1`, which runs all
checks and returns a combined pass/fail.

### Environment setup (run this first)

The DRC scripts will fail on a fresh shell until two things are set. Run these
once per PowerShell session **before** any DRC command:

```powershell
# 1) Allow the .ps1 scripts to run in this process only.
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

# 2) Point the scorer at a Python that has spaCy + es_core_news_lg +
#    snowballstemmer. score_story.ps1 hardcodes a WeaveLang venv at
#    E:\...\weavelang\.venv that does NOT exist on this machine; without this
#    override the DRC dies with "Python interpreter not found".
$env:ESCORE_PYTHON = Join-Path $PWD '.venv\Scripts\python.exe'
```

The workspace-local `.venv` already has the required packages. To confirm:

```powershell
& $env:ESCORE_PYTHON -c "import spacy, snowballstemmer, es_core_news_lg; print('deps OK')"
```

Notes:

- `drc_free_flow.ps1` has its own `py -3.13` fallback, but the inner
  `score_story.ps1` it calls does **not**, so `$env:ESCORE_PYTHON` is still
  required for the master runner to succeed.
- PowerShell may print a red `NativeCommandError` banner while piping Python
  output even on success; redirect to a file and `Get-Content` it if the table
  is hard to read.

### Master DRC (recommended)

```powershell
# Combined DRC: UL + word-count + illustration density (human-readable output)
.\drc_free_flow.ps1 `
  -StoryDir stories\Moby_Dick\chapters\Chapter_001_Loomings

# For Moby Dick chapters, apply the book-level domain lemma policy so core
# nautical terms are not penalized as rare:
.\drc_free_flow.ps1 `
  -StoryDir stories\Moby_Dick\chapters\Chapter_001_Loomings `
  -DomainLemmas stories\Moby_Dick\domain_lemmas.txt

# Machine-readable JSON for LLM/tooling loops
.\drc_free_flow.ps1 `
  -StoryDir stories\Moby_Dick\chapters\Chapter_001_Loomings `
  -Json
```

`drc_free_flow.ps1` gates by the **i-score** (using `--coverage 0.85` and gating at `i-level <= 25.5`). The UL score is computed and reported under the UL gate as info-only.

It also reports illustration density from `%%META illustration: <key>%%`
markers in `story.txt` using:

- target density: 1 illustration per 250 submission words;
- required count: `round(submission_words / 250)` (minimum 1);
- allowed deviation: `± min(1 illustration, 15% of required)`.

To keep illustrations as a final packaging step, this gate is **deferred**
until UL and length both pass. DRC still reports required/actual counts during
drafting so you can plan scene breaks early.

### Source normalization helper (`normalize_source_linebreaks.py`)

Use this helper when `source.txt` contains hard wraps from old viewers.

```powershell
# Normalize one source file in place
python .\normalize_source_linebreaks.py `
  stories\Moby_Dick\chapters\Chapter_001_Loomings\source.txt

# Normalize all chapter source.txt files under a root
python .\normalize_source_linebreaks.py `
  stories\Moby_Dick\chapters --recursive
```

Normalization rule:

- Keep paragraph breaks (`\n\n`) as paragraph breaks.
- Replace single intra-paragraph line breaks with spaces.

### Length-only check (`word_count_ratio.py`)

```powershell
# Human-readable output
python .\word_count_ratio.py `
  stories\John_and_Alice2\story.txt `
  stories\John_and_Alice\story.txt

# JSON + custom band
python .\word_count_ratio.py `
  stories\John_and_Alice2\story.txt `
  stories\John_and_Alice\story.txt `
  --min-percent 85 --max-percent 120 --json
```

The word counter ignores any full-line `%%META ... %%` directives in both
submission and source before counting.

### UL-only check (`avd_ul_score.py` / `score_story.ps1`)

A standalone, fast scorer that reproduces WeaveLang's `measure_user_score`
math **without** launching the WeaveLang app (no risk to its project state).

### Run it

```powershell
# Wrapper (recommended) — table output:
.\score_story.ps1 stories\John_and_Alice2\story.txt

# Show the rarest contributing lemmas (spot mis-lemmatized words / stray names):
.\score_story.ps1 stories\John_and_Alice2\story.txt -ShowRare 12

# Apply a BOOK-level domain lemma policy (example: Moby Dick maritime terms):
.\score_story.ps1 stories\Moby_Dick\chapters\Chapter_001_Loomings\story.txt `
  -DomainLemmas stories\Moby_Dick\domain_lemmas.txt

# No args = score every top-level Spanish story.txt under stories\ (skips *_en).
.\score_story.ps1
```

The scorer needs spaCy + `es_core_news_lg` + `snowballstemmer`. By default it
uses WeaveLang's venv interpreter; override with `$env:ESCORE_PYTHON`.

### Reading the output

```
Story       Tokens   InList     p85     p95      AVD   UL(x)    UL
------------------------------------------------------------------
story.txt      385      385     180     340   234.00    22.7  UL23
```

- **Tokens** — scored tokens (proper nouns and header directives excluded).
- **InList** — tokens found in the frequency list (the rest are treated as rare).
- **p85 / p95** — the 85th and 95th percentile token ranks. These are the
  **actionable diagnostics**: `p95` is the rank of your rare tail (the spike
  words), `p85` is the baseline vocabulary level. AVD and UL are flattened
  blends, so when iterating to lower difficulty, **watch `p95` drop** — it
  responds directly to swapping out rare words. A `p95` near 20000 means heavy
  rare-tail spikes; a `p95` in the low thousands or below is clean.
- **AVD** — tail-weighted average difficulty `(p85 + 2·p95)/3`.
- **UL(x)** — exact user level; **UL** — rounded. For workflow decisions, use
  the rounded-down integer UL (floor of UL(x)) and gate on UL 20–23.
  Example: UL(x) 23.7 => UL23 (pass); UL(x) 24.0 => UL24 (fail).

The master `drc_free_flow.ps1` also prints a `vocab:` line with `AVD / p85 / p95`
under the UL gate, so you get the same diagnostics in the combined DRC.

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
- a **mis-lemmatized / mis-ranked legitimate word form** (enclitics,
  conjugations, imperative forms, etc.) → fix the scorer logic and/or add a
  targeted exceptions/overrides entry;

Do **not** rewrite natural Spanish prose just to satisfy scorer bugs. Fix the
tooling first, then re-score.

those are the words to fix or simplify next.

### Lowering the UL score (word-choice strategy)

Getting the UL into band is usually the most iteration-heavy part of the loop.
The good news is the math tells you exactly where to spend effort.

**Only the rarest tokens matter.** UL is driven by
`AVD = (p85 + 2·p95)/3` — the 85th and 95th percentiles of token rank. In plain
terms, **only the rarest ~15% of your tokens move the score.** Everything below
the p85 mark is effectively free. So you do not need simpler prose everywhere —
you need to kill the handful of rank spikes.

**The substitution loop (do this every iteration):**

1. Run `-ShowRare 12` to list the current spike words (the offenders).
2. For each one, ask: can a more common word carry the same meaning?
3. Reach for replacements from the **top-500 lemma anchor**:
   `assets/es_freq_top500.txt` (lemma + rank, generated from the top-10k list).
   These are the cheapest words in Spanish; building prose from them keeps the
   tail light.
4. Re-score. Repeat until floor(UL(x)) is in band.

**Rank-cliff heuristic** (where words sit in the difficulty distribution):

| Band | Rank | Guidance |
|---|---|---|
| Free | ≤ ~1000 | Use freely; these never reach p85. The top-500 anchor lives here. |
| Cheap | ~1000–3000 | Normal prose vocabulary; fine to use. |
| Costly | ~3000–10000 | Use sparingly and only when needed. |
| Rare | > 10000 | Treated as rank **20000** by the scorer. These are the p95 spikes — cut first. |

Rare descriptive words spike the tail fastest: **colours, body parts, weather
words, specific birds/leaves/clouds, ornate verbs.** When over budget, simplify
those before touching plain narrative verbs and nouns.

> Use the top-500 anchor as a *deterministic tie-breaker*, not a straitjacket.
> When unsure whether (say) *embarcación* or *barco* is cheaper, the lower rank
> wins. Do not flatten natural prose just to stay inside the top 500 — only the
> rare tail is taxed.

### Optional: book-level domain lemma policy

For long, domain-heavy works (for example, nautical vocabulary in *Moby Dick*),
you may use a **book-level domain lemma policy** file (for example
`stories/Moby_Dick/domain_lemmas.txt`) with `-DomainLemmas`.

- Scope should be **book-level**, not per chapter.
- Keep the list short: only core repeated terms students will learn by context.
- Policy lowers difficulty conservatively (`effective_rank = min(raw, policy)`),
  it does not hide words entirely.
- Continue to review `-ShowRare`: non-domain rare words should still be
  simplified in prose.

---

## 5. Quick checklist

- [ ] `story.txt` written in natural, simple Spanish (no NSM explications).
- [ ] Ran `drc_free_flow.ps1` against source and story candidate.
- [ ] **i-score gate passes:** iLevel is ≤ 25.5 at coverage 0.85 (so the rarest 15% is unpunished).
- [ ] **UL score is noted:** Reported for the sister app (info-only).
- [ ] When over budget, ran `-ShowRare` and swapped spike words using the
  `assets/es_freq_top500.txt` anchor (see word-choice strategy in §4).
- [ ] **Length gate passes:** word count is 85%–120% of source.
- [ ] `-ShowRare` list contains only legitimate Spanish words.
- [ ] Illustration markers are added only after text gates pass.
- [ ] `story.txt` includes `%%META illustration: <key>%%` tags at scene breaks.
- [ ] Matching `story.toml` exists with prompts for each illustration key.
- [ ] **Illustration density gate passes:** marker count is within
  `± min(1, 15% of required)` around DRC-required count.
- [ ] `story_en.md` literal English produced for review.
- [ ] Human edits folded back into Spanish and **re-scored**.
- [ ] Approved → done.
