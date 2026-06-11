# NSM-Spanish: A Grammar of the Semantic Core

*A controlled grammar of the subset of Spanish needed to use the Natural Semantic Metalanguage primes and their immediate function-word support. This is deliberately a subset of full Spanish grammar — but, as noted throughout, not a small one, because the prime inventory forces most high-frequency irregular verbs into scope.*

---

## Front Matter

### Preface — What This Book Is and Is Not
- This is a grammar of a **controlled subset**, not of Spanish as a whole.
- Design premise: NSM primes are universal meanings with language-specific *exponents*; the Spanish exponents can be taught L1-first because they cross-transfer 1:1. Everything built *on top of* the primes does not.
- Scope boundary: present-active register, infinitives admitted only under modal/auxiliary verbs, periphrastic "going-to" for futurity. Past and subjunctive deliberately excluded from the core (flagged where the reader will eventually need them).
- Honest caveat: the verb inventory cannot be shrunk below the primes, so the irregular core is unavoidable. We manage difficulty by constraining *what is done* with these verbs, not which verbs appear.
- Relationship to the companion materials: the semantic-core stories (unglossed) and the explication ramp. This book is the grammatical scaffolding under both.

### How to Use This Book
- For the solo learner vs. for the content author (LLM-prompt designer).
- The "closed set" principle: learn the irregular core as one bounded thing, up front, rather than meeting irregulars piecemeal.
- Notation conventions used throughout (prime exponents in **bold**, function words marked, ungrammatical examples marked with ✗).

---

## Part I — The Inventory

### Chapter 1 — The Semantic Primes and Their Spanish Exponents
- The full prime list grouped by category, each with its Spanish exponent and any allolexy (contextual variant forms).
  - Substantives: *yo, tú, alguien, algo, gente, cuerpo*
  - Relational substantives: *parte, tipo/clase*
  - Determiners: *este, el mismo, otro*
  - Quantifiers: *uno, dos, mucho, poco, algo de, todo*
  - Evaluators: *bueno, malo*
  - Descriptors: *grande, pequeño*
  - Mental predicates: *pensar, saber, querer, sentir, ver, oír*
  - Speech: *decir, palabra, verdad*
  - Actions/events/movement: *hacer, pasar, moverse*
  - Existence/possession: *haber/hay, ser/estar, tener (mío)*
  - Life and death: *vivir, morir*
  - Time: *cuándo/tiempo, ahora, antes, después, mucho tiempo, poco tiempo, por un tiempo, momento*
  - Space: *dónde/lugar, aquí, arriba, abajo, lejos, cerca, lado, dentro, tocar*
  - Logical concepts: *no, quizá, poder, porque, si*
  - Intensifier/augmentor: *muy, más*
  - Similarity: *como*
- **Allolexy note** — where one prime surfaces as more than one Spanish word (the ser/estar split of BE is the headline case; treated fully in Ch. 9).
- Exponents that are *also* high-frequency function words elsewhere — disambiguation up front.

### Chapter 2 — The Function-Word Support Layer
- The non-prime words that the grammar of the core makes unavoidable.
- Articles: *el, la, los, las, un, una* — including the lemma-merging convention (el/la = one lemma).
- Prepositions in core use: *a, de, en, con, para, por, sin, sobre.*
- Coordinators: *y, o, pero.*
- Why these aren't primes but can't be avoided; the principled boundary of "necessary support vocabulary."
- A note for the author: these inflate token counts but sit shallow in the frequency list, so they pull the AVD percentile cuts *down* — relevant to level targeting.

---

## Part II — The Noun System

### Chapter 3 — Gender
- Masculine/feminine as a property of every noun.
- Default patterns (-o / -a) and the high-frequency exceptions present in the core (*parte* fem., *cuerpo* masc., etc.).
- Why this matters before adjectives and articles are introduced.

### Chapter 4 — Number
- Singular/plural formation (-s, -es).
- Plural of the prime-relevant nouns.

### Chapter 5 — Articles and Agreement
- Definite vs. indefinite.
- Full four-way agreement (gender × number).
- When the article is required and when it is dropped (e.g., *en poco tiempo* without article — a pattern the learner will hit immediately).

### Chapter 6 — Adjective Agreement and Position
- Agreement in gender and number with the noun.
- **Default post-nominal position** (*cosas buenas*, not *buenas cosas*) — flagged as a frequent L1-interference error.
- The *bueno/malo* (adjective) vs. *bien/mal* (adverb) distinction, since both primes BUENO/MALO and their adverbial uses appear constantly.

### Chapter 7 — Pronouns
- Subject pronouns: *yo, tú, él, ella, nosotros, ellos, ellas* — and the fact that they're usually **droppable** because the verb encodes person.
- The *mi* (my) vs. *mí* (me) accent distinction — flagged as a recurring beginner error.
- Possessives in core use: *mi, tu, su, mío.*
- Forward-reference to object and reflexive pronouns (Ch. 11), which need the verb system first.

---

## Part III — The Verb System (The Core's Real Weight)

### Chapter 8 — Why the Verb Core Is Large
- The frequency–irregularity correlation: the most-used meanings resist regularization, and the primes *are* the most-used meanings.
- Consequence: the semantic floor sits on a substantial grammatical core. This chapter is the book's central honest disclosure.
- The design response: restrict the **conjugation surface**, not the verb set.

### Chapter 9 — *Ser* and *Estar* (the BE allolexy)
- The single most important distinction in the core.
- *Ser*: identity, what something fundamentally is (*es una parte*, *son las palabras*).
- *Estar*: location and condition/state (*está cerca*, *está mal*).
- Full present-tense conjugation of both.
- Decision procedure / flowchart for the learner.
- Why NSM treats these as exponents of one prime but Spanish grammar forces the split.

### Chapter 10 — The Present Tense (Active)
- Regular -ar / -er / -ir conjugation paradigms.
- The present as the workhorse — including its legitimate use for **narrative past** ("I go outside, something bad happens, I fall"), which lets the core avoid past tense entirely.
- Person/number endings drilled as the thing that makes subject pronouns optional.

### Chapter 11 — Reflexive Verbs
- Why the core leans heavily on these: body, movement, and internal states.
- *moverse* (*me muevo*), *caerse* (*me caigo*), *sentirse* (*se siente*), *llamarse.*
- Reflexive pronoun placement (*me, te, se, nos*) — pre-verbal in finite forms, attached to infinitives.
- The "something happens to me/it" pattern (*le pasa algo*) as a core idiom.

### Chapter 12 — The Irregular Core, as a Closed Set
- Taught together, deliberately, so they stop ambushing the reader.
- Present-tense paradigms for: *tener, ir, hacer, decir, ver, saber, querer, poder, oír, venir, dar.*
- Grouped by irregularity type (stem-changing, yo-irregular, fully irregular) so the patterns are learnable rather than memorized one by one.
- *hay* (existential HABER) as its own special case.

### Chapter 13 — Modal / Auxiliary Verbs and the Infinitive
- The one sanctioned use of the infinitive in the core.
- *poder + inf.* (*puedo decir*), *querer + inf.* (*quiero hablar*), *deber + inf.* (*no debo moverme*).
- Negation placement with modals (*no debo* before the verb).
- Pronoun attachment to the dependent infinitive (*quiero moverme*, *puedo decirlo*).

### Chapter 14 — Periphrastic Future ("Going-To")
- *ir a + infinitive* as the core's only future (*se va a sentir mejor*).
- Why this replaces the morphological future tense entirely in the controlled register.
- Conjugating *ir* + *a* + infinitive across persons.

---

## Part IV — The Sentence

### Chapter 15 — Negation
- *no* before the verb; placement with reflexives and modals.
- *nada, nadie, nunca* and the double-negative pattern.

### Chapter 16 — Questions
- Intonation questions vs. interrogative words.
- The accented interrogatives: *qué, quién, cuándo, dónde, cómo, por qué* — and their unaccented relative/conjunction twins (*que, porque, cuando, donde, como*).
- "What are the words?" type structures (*¿qué son las palabras?*) — a pattern the learner reaches for early and gets wrong.

### Chapter 17 — Basic Clause Combination
- Coordination with *y, o, pero.*
- Causal *porque* (because + clause) vs. *por esto / por eso* (because of this).
- Conditional *si* (in present-only form — the simple "si X, Y" that stays inside the register).
- *como* for similarity/comparison.

### Chapter 18 — Prepositional Patterns That Trip Learners
- *a* with motion and with personal direct objects ("a personal" — *María ve a Pedro*).
- *de* for possession and origin.
- *en* for location (with *estar*).
- *con* and pronoun fusion (*conmigo, contigo*).

### Chapter 19 — Word Order in the Core
- Default SVO and the freedoms the core allows.
- Where preposition + relative goes (*la parte con que me muevo*).
- Adjective and adverb placement recap.

---

## Part V — Reference and Author's Apparatus

### Chapter 20 — The Complete Core Paradigm Tables
- Every irregular core verb, full present tense, on facing pages.
- *Ser/estar*, modal set, *ir a* future, reflexive model verbs.

### Chapter 21 — High-Frequency Error Catalogue
- Compiled from interaction patterns: *mi/mí*, *si/sí*, ser/estar confusion, adjective position, *bueno/bien*, modal + infinitive vs. doubled finite verb, missing reflexive pronoun, *que/qué* accent.
- Each with the wrong form, the right form, and the underlying rule.

### Chapter 22 — Notes for the Content Author
- How this grammar maps onto the controlled-vocabulary generation loop.
- The lemma list this grammar sanctions (the OOV checker's allow-set for the core tier).
- Tense/register constraints expressed as generation rules.
- Proper-noun handling for the AVD scorer.
- The boundary where the core ends and the explication ramp begins.

### Appendix A — The Prime → Exponent Quick Reference
- One-page lookup table.

### Appendix B — What the Core Deliberately Omits
- Past tenses, subjunctive, conditional mood, compound tenses, the full pronoun system, passive voice.
- For each: a one-line note on *when* in the ramp the learner will need it, so the omission reads as sequencing, not as a gap.

### Appendix C — Glossary of Grammatical Terms
- Defined, where possible, in plain language — so the grammar book itself stays low on the prerequisite-jargon scale.