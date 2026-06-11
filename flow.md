# ESCore Story Production Flow

This document describes the end-to-end workflow for turning an English draft into a fully ESCore-compliant Spanish story, ready for TTS, illustration, and YouTube production. Future agents working on a new story in this repository should follow this flow.

---

## 0. Prerequisites — Read Before Writing

Before generating or modifying any story text, an agent **must** read:

1. **`ESCore.md`** — the canonical definition of the ESCore register. It defines:
   - The semantic primes and approved vocabulary.
   - Grammatical constraints (present indicative only; no past, subjunctive, conditional, morphological future, passive, progressive).
   - Approved constructions (e.g. infinitives after modals, the colon-want construction `Quiero esto: tú + indicative`, *hace que* + indicative as the subjunctive workaround).
   - Banned words and the reasons for the bans.
2. **`whitelist.txt`** — the master list of every word approved for ESCore core. If a word is not here and not in `PN_whitelist.txt` and not in the story's local whitelist, it fails the audit.
3. **`PN_whitelist.txt`** — approved proper nouns (character names, faction names).
4. **`layer1.txt`** — words that have been explicitly *excluded* from ESCore core, documented with the reasoning and the workarounds. Read this to understand what *not* to reach for.
5. **`proposed_additions.md`** — running record of vocabulary debates, decisions, and pending proposals.

You cannot write ESCore-compliant prose without first internalizing the contents of `ESCore.md` and `whitelist.txt`. Do not skip this step.

---

## 0.5 Anchor Tier vs. Story Tier — The +1 Philosophy

ESCore has two registers, and stories use the second. Read `ESCore.md` §22.7–22.11 for the full treatment; the operational summary:

- **Anchor tier (strict ESCore):** prime + support vocabulary only, present indicative, no subjunctive. This is for an LLM interlocutor and the explication loop.
- **Story tier (ESCore+1):** the core is the **anchor the story revolves around, not the fence that bounds it.** The semantic spine — load-bearing meanings, connective tissue, repeated frame sentences — must be core. On top of that spine, a *budgeted* layer of out-of-core but high-transparency vocabulary is allowed. This is Krashen's *i+1*: mostly-known input with a thin margin of new, which is the mechanism that advances a reader from ultra-basic toward simple Spanish.

**Do not bend over backwards with strained explications for words knowable from context.** A five-clause prime paraphrase of a word the reader could glean from the next sentence makes the prose worse, not purer.

### The three buckets of "out of core"

When the audit flags out-of-core words, sort each into a bucket (proper nouns are a free fourth category):

| Bucket | What it is | Policy |
|---|---|---|
| **A — Inflectional** | Past/perfect/frozen-subjunctive form of a verb whose lemma IS in core (*hizo, era, vino, sepas*) | Allowed in narrative (see below) |
| **B — Transparent concrete** | Ultra-high-frequency concrete noun outside core only because it isn't a *prime* (*agua, niño, noche, fuego*) | Freely allowed within budget |
| **C — New lexeme** | Genuinely new content verb/abstract (*escuchar, caminar, sostener, sentimiento*) | Rationed; **must** go in the local whitelist |

Measure **Bucket C**, not the flat audit percentage. A flat audit can read ~28% out-of-core while genuine new lexemes (C) are ~1 in 25–30 tokens. Rough budget: **about 1 new Bucket-C lexeme per 25–30 tokens**, by judgment.

### The contextual-learnability test (the *Lingua Latina* principle)

Before admitting any new (Bucket B/C) word, confirm the reader has a path to acquire it from the text itself — the standard set by Ørberg's *Lingua Latina per se Illustrata*:

1. Bucket A or B? Usually self-evident — admit it.
2. Bucket C? It must be **constrained by its neighbours** — a nearby sentence that says what one *does* with it, what it *is like*, or what *happens* to it. *"Jim toma una manzana"* teaches nothing; *"Jim toma una manzana. Piensa en comerla. Tiene hambre."* teaches *manzana*.
3. Prefer words **echoed across the scene** (anchored by repetition) over one-off words (a vocabulary tax).
4. For video, illustration can disambiguate — but don't rely on it for words that must also work audio-only.

A new word with no acquisition path is a defect, even if it is "simple." Be as cognisant of every new word as Ørberg was: know exactly *how* the reader is meant to learn it.

### Frozen frames allowed in the story tier

- **Narrative past** for legends/recounted stories (*había una mujer… vino un hombre*) — Bucket A, recognised not decoded. Keep the framing sentences in present tense to anchor the listener.
- **Fixed-frame subjunctive**, holistically processed: *quiero que + [subj.]*, *hace/hizo que + [subj.]*, *antes de que + [subj.]*, *hasta que + [subj.]*. Canonical *Quiero que sepas* is preferred over the strict-core *Quiero esto: tú sabes…* in story prose.

These remain **out of the anchor tier** — only authored story content uses them.

---

## 1. Project Layout

Each story lives in its own directory under `stories/`:

```
stories/
  My_Story_Name/
    story.md          # English source draft (optional, for translation work)
    story.txt         # The canonical ESCore Spanish text (audited)
    whitelist.txt     # Local whitelist — words approved for THIS story only
```

  Every story text file must begin with metadata lines in this form:

  ```text
  %%META source_language: es%%
  %%META target_language: es%%
  %%META simple_mode: on%%
  %%META source_is_basic: on%%
  ```

  These metadata lines belong at the top of every story and are part of the
  standard story wrapper, not the prose itself. The audit script must ignore
  them completely.

The story-local `whitelist.txt` is the new convention. It holds vocabulary that:

- Is *not* general enough to belong in the global `whitelist.txt`.
- Is required by this specific story (e.g. domain-specific nouns: *comida*, *mesa*, *agua* — words that only matter because the story happens in a particular setting).

Story-local words are merged into the audit pool at scan time without polluting the global core.

---

## 2. The Writing Loop

Work one chapter (or one scene) at a time. For each chapter:

### 2a. Draft
Write the Spanish prose in ESCore register, drawing only on:
- The global `whitelist.txt`.
- The local `whitelist.txt` for the current story.
- The `PN_whitelist.txt` for character/faction names.

When tempted to reach for a word that isn't approved, choose one of:
- **Rewrite** using approved primes (e.g. *casa* → *un lugar para vivir*).
- **Propose** the word for inclusion (see step 3).
- **Add it locally** if it is story-specific and unambiguously simple (see step 4).

### 2b. Audit
Run the compliance scanner against the file:

```powershell
python audit_escore_compliance.py `
  --target "stories\My_Story_Name\story.txt" `
  --local-whitelist "stories\My_Story_Name\whitelist.txt"
```

The auditor reports the flat out-of-core figure **and** the A/B/C bucket
breakdown (§0.5, ESCore.md 22.8). It classifies each unknown automatically:
Bucket A = non-present forms of core verbs, Bucket B = transparent concrete
nouns (`bucket_b_transparent.txt`), Bucket C = genuinely new lexemes. A clean
anchor-tier chapter shows flat `0`; a story-tier chapter is judged on its
**Bucket-C** figure, not the flat number.

> The legacy PowerShell scanner (`audit_escore_compliance.ps1`) still works but
> only reports the flat out-of-core number — it cannot lemmatise, so it cannot
> separate the buckets. Prefer the Python tool.

### 2c. Fix or Promote
For every unknown token, sort it into a bucket (§0.5) and decide:
- **Bucket A (inflected core verb)** — allowed in narrative; leave it, or rewrite only if the story is anchor-tier.
- **Bucket B/C, fails contextual-learnability** — rewrite the sentence, or add a neighbouring sentence that teaches the word.
- **Bucket B/C, passes contextual-learnability** — promote to the **local whitelist** (Bucket C must always be tracked there).
- **Genuinely fundamental, cross-story** — propose for the core whitelist (see step 3).

Re-run the audit after every change. The target is not flat zero out-of-core; it is **zero un-budgeted, un-learnable Bucket-C words.**

---

## 3. Proposing Vocabulary for the Global Core

If a word seems to belong in `whitelist.txt` (i.e. it would be useful across many stories, and it represents a near-primitive concept):

1. Add an entry to `proposed_additions.md` with:
   - The word.
   - The semantic gap it fills.
   - Why no existing prime or combination covers it.
   - The proposed approval scope (single form, full paradigm, etc.).
2. **Stop and ask the user.** Do not add to `whitelist.txt` autonomously. The global core is a deliberate, slow-moving artifact.
3. On approval: add the word (and any required inflected forms) to `whitelist.txt`. If the user denies it, move the entry to `layer1.txt` with the workaround documented.

Words that have been added this way include: `hacia`, `vida`, `muerte`.
Words denied and pushed to layer 1 include: `miedo`, `volver`.

---

## 4. Local Whitelist Conventions

The story-local `whitelist.txt` is for words that:

- Are tied to a specific setting or scene (food, places, props).
- Would clutter the global core if added everywhere.
- Are still simple, concrete nouns or basic verbs — not abstract concepts. Abstract vocabulary still requires a global-core conversation.

Examples of good local-whitelist entries: *comida*, *mesa*, *sentar*, *sentarse* (if the story is about a meal); *árbol*, *río* (if the story is set in a specific landscape).

Examples of words that should **not** go in the local whitelist: emotional or abstract terms (*tristeza*, *esperanza*), grammatical extensions (new tenses, new moods), or words that simply rephrase a primitive (*comenzar* when *empezar* is already approved — or vice versa).

When in doubt, ask the user before adding to the local whitelist.

### 4.5 New-Words Logging (Per Episode)

To support gradual vocabulary growth across episodes, every story should keep a
running log of words first introduced locally.

Use this policy:

1. Keep the story-local `whitelist.txt` as the source of truth for currently
  approved local words.
2. After each episode audit pass, append a short changelog entry in
  `proposed_additions.md` under a heading like
  `## New Words Log — Story_Name Episode_N`.
3. For each new local word added in that episode, record:
  - The word.
  - Bucket (B or C).
  - One-line contextual-learnability note (how the reader can infer it).
  - Keep or promote recommendation.
4. Promotion rule of thumb: if a local word appears in 2 to 3 stories and is
  clearly high-frequency beginner vocabulary, propose it for global
  `whitelist.txt` using the step 3 process above.
5. If a word is intentionally story-only, keep it local and mark it as
  "local-only" in the log entry.

This keeps the core deliberate while still letting episode-by-episode writing
expand the beginner vocabulary in a traceable way.

### 4.6 Episodic Series Vocabulary Growth

For an episodic story folder (for example `stories/Nadie_Lo_Vio_Morir/` with
`episode_0001.txt`, `episode_0002.txt`, etc.), treat the folder-local
`whitelist.txt` as the **active series whitelist**.

Use this workflow:

1. Keep a `series_vocabulary.md` file inside the series folder.
2. When an episode unlocks a new local word, do two things at the same time:
  - add the word to the folder-local `whitelist.txt`
  - add a row to `series_vocabulary.md` with episode number, word, why it was
    unlocked, and a reuse window
3. Reuse rule of thumb: every unlocked word should be used intentionally in the
  next 2 to 3 episodes unless it is clearly one-off or purely structural.
4. Use `assets/frequency_list.txt` to guide selection, but do not let the list
  override the needs of the story. A good unlock set is a balance of:
  - words the current episode genuinely needs
  - words near the top of the frequency list
  - words the episode can teach clearly in context
5. Use the helper script to propose candidates:

```powershell
python suggest_series_unlocks.py --story-dir "stories\My_Story_Name" --count 10
```

The helper output is advisory only. Human editorial judgment decides what to
unlock.

---

## 5. Editorial Passes (Before Production)

Once all chapters audit clean, do at least one editorial pass before TTS/illustration/YouTube. Past passes have included:

- **Naming variety** — avoid mechanical repetition of faction or character labels; introduce synonyms (e.g. *la gente mala* → *los Granken* → *los malos*).
- **Heart moments** — identify scenes where the ESCore register can carry emotional weight (death, reunion, arrival). Convert internal narration into spoken dialogue when communion among characters is more powerful than a narrator's reflection.
- **Format normalization** — for TTS, remove markdown (`##` headers become plain text); standardize punctuation (use `—` em-dash consistently, not `--`); use `«»` for dialogue quotes throughout.

After each editorial pass, re-run the audit.

---

## 6. Heart-Things Principle

NSM (and ESCore by extension) is poor for technical or scientific content but exceptional for moral, emotional, and relational content — the same territory that wisdom literature and scripture occupy. When inserting dialogue at climactic moments:

- Prefer primitive constructions over clever phrasing. *No sé. Nadie sabe.* lands harder than any rephrased equivalent.
- Use the colon-want construction for directed desires: *Quiero esto: ella vive.*
- Let characters speak the philosophy; let the narrator stay silent.
- Distribute the closing beats across multiple characters when a moment is communal.

---

## 7. Production Handoff

When the story is audited clean and editorial passes are complete:

1. Confirm the file uses plain text (no markdown headers) for TTS.
2. Confirm em-dashes (`—`) are used consistently, not double-hyphens.
3. Confirm dialogue uses `«»` consistently.
4. The story is now ready for TTS, illustration, and video assembly.

---

## Quick Reference — Audit Command

```powershell
# Audit a single story with its local whitelist (Bucket A/B/C aware)
python audit_escore_compliance.py `
  --target "stories\My_Story_Name\story.txt" `
  --local-whitelist "stories\My_Story_Name\whitelist.txt"

# Approve new proper nouns into PN_whitelist.txt
python audit_escore_compliance.py --approve-pn name1 name2
```

Required outcome for an anchor-tier chapter: `Out-of-core (flat): 0`.
For a story-tier chapter: every Bucket-C word is budgeted and passes the
contextual-learnability test (§0.5).
