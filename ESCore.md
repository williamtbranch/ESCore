# NSM-Spanish: A Grammar of the Semantic Core

*A controlled grammar of the subset of Spanish needed to use the Natural Semantic Metalanguage primes and their immediate grammatical support. This is deliberately a subset of full Spanish grammar — but, as noted throughout, not a small one, because the prime inventory forces most high-frequency irregular verbs into scope.*

**Version 0.1 — Vocabulary Foundation**

---

## Front Matter

### Preface — What This Book Is and Is Not

This book has one goal: to equip you to communicate in a carefully bounded subset of Spanish — call it *ESCore* — in which you can say anything that can be said using the 65 universal semantic primes of the Natural Semantic Metalanguage (NSM) plus the grammatical machinery needed to combine them. Nothing more, nothing less.

**What the NSM is.** The NSM is a research program originating with Anna Wierzbicka and developed with Cliff Goddard and others. Its central empirical claim is that all human languages share a small inventory of irreducible meanings — *semantic primes* — that cannot be defined in terms of simpler concepts but in terms of which every other concept *can* be defined. These primes have been identified by cross-linguistic research: they appear in every known language, and every known language has a dedicated, high-frequency word (or construction) for each. In Spanish, as in English, the primes are not exotic technical vocabulary — they are the most ordinary, most frequent words of the language.

**What ESCore is.** ESCore is the Spanish instantiation of the NSM primes, together with the minimal grammatical support words and morphological patterns required to produce well-formed Spanish sentences using those primes. It is a *controlled register*, not a dialect or a pidgin. A speaker of full Spanish who encounters ESCore will understand it as ordinary, if simple, Spanish. An ESCore speaker will understand a significant proportion of everyday Spanish — the core meanings will transfer — even before leaving the controlled register.

**What ESCore is not.** It is not a full Spanish grammar. The following are deliberately outside scope: the morphological past tense (preterite, imperfect), the subjunctive mood, the conditional, compound tenses, the passive voice, the full pronoun system, and the vast lexicon of Spanish beyond the primes and their support words. Each of these is flagged at the boundary where the reader will eventually need it, so the omissions read as *sequencing*, not as gaps.

**The honest caveat about the verb system.** The prime inventory cannot be shrunk. The primes are the most frequent meanings in any language, and in Spanish (as in most languages) the most frequent meanings are encoded by the most irregular verbs. You cannot do NSM-Spanish without *ser*, *estar*, *tener*, *hacer*, *decir*, *ver*, *saber*, *querer*, *poder*, *oír*, *ir*, *venir*, and *dar*. Every one of these is irregular. This book addresses that by teaching the irregular core *together*, as one bounded set, rather than ambushing the reader with irregulars one at a time over months.

**The chatbot use case.** This grammar has a specific practical application: conversing with a language model (LLM) whose context window contains the ESCore specification, so that it stays within the prime register when responding in Spanish. The author has verified through experiments that current frontier models can maintain this constraint with good fidelity. The result is a closed semantic loop: the learner's input and the model's output are both anchored to the same primitive vocabulary, making every exchange a working example of the core in use.

**The explication project.** The deeper purpose, beyond language learning, is semantic. Once you can operate in ESCore, you can begin to *explicate* — to give NSM-style definitions of Spanish words that lie outside the core, using only core vocabulary. This is how the NSM has always been used by researchers: to make the implicit meanings of ordinary words explicit and cross-linguistically comparable. This book gives you the tools; the explication work is the reward.

---

### How to Use This Book

**For the solo learner.** Work through Part I first (the inventory). Learn the prime exponents as a single closed list — they are finite and bounded, and knowing all of them before learning the grammar means you will recognize every word in the grammar examples. Then work through Parts II and III (nouns and verbs) in order, since the verb chapter assumes the noun chapter. Part IV (the sentence) can be read alongside or after the verb chapters.

**For the content author / LLM-prompt designer.** Chapter 22 (Notes for the Content Author) is written specifically for you. The vocabulary inventory in Chapters 1 and 2 is the *allow-set* for the core tier: if a word is not in those lists, it is out of register. The grammar chapters give you the morphological patterns that are sanctioned (present active, ir-a future, modal + infinitive) and those that are not (past tense, subjunctive, passive).

**The "closed set" principle.** The most productive reframe for approaching ESCore is this: you are not learning a language with an open vocabulary. You are learning a *closed system*. The prime list has 65 entries. The support vocabulary in Chapter 2 adds roughly 40 more items. That is a total lexicon of approximately 105 lemmas — smaller than a standard elementary lesson set, yet sufficient to define any word in the language.

**Notation conventions used throughout:**

| Notation | Meaning |
|---|---|
| SMALL CAPS | An NSM semantic prime, language-neutral |
| **bold** | The Spanish prime exponent in running text |
| *italics* | A Spanish word or phrase being discussed |
| [brackets] | An English gloss |
| ✗ before a form | Ungrammatical in ESCore |
| ⚠ before a note | A common learner error |
| → | "is the exponent of" or "maps to" |

---

## Part I — The Inventory

---

### Chapter 1 — The Semantic Primes and Their Spanish Exponents

#### 1.1 What a Prime Exponent Is

Every NSM prime is a universal *concept*. Its *exponent* is the Spanish word (or short fixed phrase) that expresses that concept. The exponent and the prime are not identical: the Spanish word may carry grammatical information (gender, number, conjugation) that the abstract prime does not, and the same Spanish word may sometimes appear in non-prime uses. The tables below give the canonical exponent and note the main alternative forms.

An *allolexe* is a contextually conditioned variant of the same prime. The most important case in Spanish is the BE prime, which has two allolexes: **ser** and **estar**. This is not a matter of two different primes; it is one prime with two phonological realizations conditioned by the type of predication. Chapter 9 treats this in full. In the table below it is marked with †.

#### 1.2 The Prime Inventory with Spanish Exponents

The 65 primes are listed below in the standard NSM category groupings. For each prime the table gives: (a) the English prime label in SMALL CAPS; (b) the canonical Spanish exponent; (c) key variant forms (allolexes, gender/number inflections where relevant); and (d) a brief usage note where the Spanish exponent diverges from English intuition.

---

##### SUBSTANTIVES

These are the basic referential concepts — the things that can be talked about.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| I | **yo** | — | Subject pronoun; often omitted when verb person is clear (see Ch. 7) |
| YOU | **tú** | *vos* (regional) | Informal singular. *Usted* (formal) is outside the core register but noted in Ch. 7 |
| SOMEONE~PERSON | **alguien** | *persona* (noun "a person") | *Alguien* is the prime exponent; *persona/personas* functions as the count noun "a person/people" |
| SOMETHING~THING | **algo** | *cosa* (noun "a thing") | *Algo* is the prime exponent in predicative and indefinite uses; *cosa/cosas* is the count noun "thing(s)" |
| PEOPLE | **gente** | *personas* | *Gente* is grammatically singular in Spanish (*la gente es* — the people are); *personas* is the countable plural |
| BODY | **cuerpo** | *cuerpos* (pl.) | Masculine noun (*el cuerpo*) |

---

##### RELATIONAL SUBSTANTIVES

These describe a relationship between entities rather than standing alone.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| KIND~TYPE | **tipo** | *clase* | Both are used; *tipo* is slightly more informal. *¿De qué tipo es esto?* [What kind of thing is this?] |
| PART | **parte** | *partes* (pl.) | Feminine noun (*la parte*) despite ending in -e. This is a common gender-assignment error |

---

##### DETERMINERS

Determiners pick out or identify referents within the discourse.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| THIS | **este** | *esta* (fem.), *esto* (neuter), *estos/estas* (pl.) | Agreement with the noun's gender and number. *Esto* (neuter) is used when no specific noun is referenced: *¿Qué es esto?* [What is this?] |
| THE SAME | **el mismo** | *la misma, los mismos, las mismas* | Agrees with the noun it modifies. *Es el mismo lugar* [It is the same place] |
| OTHER~ELSE | **otro** | *otra, otros, otras* | Agrees with noun. No article before *otro*: ✗ *el otro* is grammatical only when referring to a specific known item |

---

##### QUANTIFIERS

Quantifiers express amounts, quantities, and totalities.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| ONE | **uno** | *una* (fem.), *un* (before masc. noun) | *Un* before a masculine noun: *un momento* [one moment]. *Una* before feminine: *una parte* |
| TWO | **dos** | — | Invariable for gender: *dos partes, dos cuerpos* |
| SOME | **algunos** | *algunas* (fem.), *algo de* (partitive) | *Algunos/algunas* precede count nouns (*algunas cosas*); *algo de* precedes mass nouns or abstracts (*algo de tiempo* [some time]) |
| MUCH~MANY | **mucho** | *mucha, muchos, muchas* | Agrees with the noun: *mucho tiempo* [much time], *muchas palabras* [many words] |
| LITTLE~FEW | **poco** | *poca, pocos, pocas* | *Poco tiempo* [little time], *pocas palabras* [few words]. Distinct from *pequeño* (physically small) |
| ALL | **todo** | *toda, todos, todas* | *Todo* can also mean "everything" without a noun: *sé todo* [I know everything] |

---

##### EVALUATORS

These assign basic value judgements.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| GOOD | **bueno** | *buena, buenos, buenas*; adverb: **bien** | As adjective: *algo bueno* [something good]. As adverb or predicate of a state: **bien** — *estoy bien* [I am well/fine]. This bueno/bien split is treated in Ch. 6 |
| BAD | **malo** | *mala, malos, malas*; adverb: **mal** | As adjective: *algo malo* [something bad]. *Mal* before a masc. sing. noun: *un mal momento* [a bad moment]. Adverb/state: *estoy mal* [I am not well] |

---

##### DESCRIPTORS

These assign basic perceptual size properties.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| BIG~LARGE | **grande** | *grandes* (pl.) | *Grande* does not change for gender, only for number. Before a noun it shortens to *gran*: *un gran lugar* [a great/big place] — though the core prefers post-nominal position (*un lugar grande*) |
| SMALL~LITTLE | **pequeño** | *pequeña, pequeños, pequeñas* | Regular four-way agreement. Not to be confused with *poco* (small in quantity) |

---

##### MENTAL PREDICATES

These are the verbs of cognition, perception, and experience — the NSM's inner life.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| THINK | **pensar** | *pienso, piensas, piensa...* | Stem-changes e→ie in present (see Ch. 12). *Pienso que...* [I think that...] introduces a complement clause |
| KNOW | **saber** | *sé, sabes, sabe...* | Irregular *yo* form: *sé*. Used for propositional knowledge ("know that/how"). ⚠ Do not confuse with *conocer* (acquaintance knowledge), which is outside the core |
| WANT | **querer** | *quiero, quieres, quiere...* | Stem-changes e→ie in present. Also means "to love" (people), but in the core register the prime meaning WANT is primary |
| FEEL | **sentir** | *siento, sientes, siente...* | Stem-changes e→ie in present; often reflexive *sentirse* for internal states: *me siento bien* [I feel good]. Covers both physical sensation and emotion |
| SEE | **ver** | *veo, ves, ve...* | Irregular *yo*: *veo*. Used for visual perception but extends in explicating to "mental seeing" (perceiving, understanding) |
| HEAR | **oír** | *oigo, oyes, oye...* | Fully irregular; *oigo* (yo), *oyes* (tú), *oye* (él/ella), *oímos* (nosotros), *oyen* (ellos). See full paradigm in Ch. 12 |

---

##### SPEECH

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| SAY | **decir** | *digo, dices, dice, decimos, dicen* | Highly irregular; e→i stem change plus irregular *yo* form *digo*. Full paradigm in Ch. 12 |
| WORD~WORDS | **palabra** | *palabras* (pl.) | Feminine noun (*la palabra*). The plural *palabras* is very frequent in explicating |
| TRUE | **verdad** | — | Feminine noun (*la verdad*). Used predicatively: *esto es verdad* [this is true]. The adjective *verdadero/a* [genuine, real] is outside the core register |

---

##### ACTIONS, EVENTS, MOVEMENT, AND CONTACT

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| DO~MAKE | **hacer** | *hago, haces, hace, hacemos, hacen* | Irregular *yo*: *hago*. Covers both agentive doing and making/creating |
| HAPPEN~OCCUR | **pasar** | *pasa, pasan* | Regular -ar verb. The impersonal pattern *algo pasa* [something happens] and *¿qué pasa?* [what is happening?] are core idioms. Also used in *le pasa algo a alguien* [something happens to someone] |
| MOVE | **moverse** | *me muevo, te mueves, se mueve...* | Used reflexively as the prime form: *me muevo* [I move]. The transitive non-reflexive *mover* also exists but the reflexive is primary in the core |
| TOUCH | **tocar** | *toco, tocas, toca...* | Regular -ar verb. *Tocar* also means "to play (an instrument)" in full Spanish but the core uses only the contact meaning |

---

##### EXISTENCE AND POSSESSION

These cover two distinct but related ontological notions.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| THERE IS~EXIST | **hay** | — | The invariable existential form of *haber*. *Hay algo aquí* [there is something here]. *Hay* does not change for person or number: *hay una persona / hay muchas personas*. The infinitive *haber* and other conjugations of the existential are outside the core |
| BE† | **ser** / **estar** | see below | The single NSM prime BE has two Spanish allolexes. This is the most important structural fact in the whole book. See §1.3 and Ch. 9 |
| HAVE~BE SOMEONE'S | **tener** | *tengo, tienes, tiene, tenemos, tienen*; possessive: *mío/mía* | *Tener* for physical possession. *Es mío/mía* [it is mine] for the "be someone's" reading. The irregular *yo* form *tengo* is encountered immediately |

---

##### LIFE AND DEATH

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| LIVE | **vivir** | *vivo, vives, vive, vivimos, viven* | Regular -ir verb |
| DIE | **morir** | *muero, mueres, muere, morimos, mueren* | Stem-changes o→ue. Appears in explicating life-event concepts |

**Nominal forms** — the noun forms of these two primes carry the same semantic weight as the verbs and are approved ESCore vocabulary:

| Noun | Meaning | Notes |
|---|---|---|
| **vida** | life | *una vida buena* [a good life]; *su vida* [her/his life] — the nominalization of LIVE; use where "how one lives" would be clunky |
| **muerte** | death | *la muerte de alguien* [someone's death] — the nominalization of DIE; use where *muere/murió* cannot serve as a noun |

---

##### TIME

The time primes introduce both interrogative/relative words and temporal adverbials.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| WHEN~TIME | **cuando** / **tiempo** | Interrogative: **cuándo** (accented) | *Cuando* [when] as conjunction/relative; *cuándo* [when?] as interrogative (accent marks the question). *Tiempo* [time] as the noun: *mucho tiempo* [a long time] |
| NOW | **ahora** | — | Temporal adverb |
| BEFORE | **antes** | *antes de* (+ noun/inf.) | *Antes* alone as adverb; *antes de esto* [before this]; *antes de hacer* [before doing] |
| AFTER | **después** | *después de* (+ noun/inf.) | Mirror of *antes*: *después de esto* [after this] |
| A LONG TIME | **mucho tiempo** | — | Fixed phrase; no article needed: *por mucho tiempo* [for a long time] |
| A SHORT TIME | **poco tiempo** | — | Fixed phrase: *en poco tiempo* [in a short time] — note: no article before *poco tiempo* |
| FOR SOME TIME | **por un tiempo** | — | Fixed phrase with article: *por un tiempo* [for some time / for a while] |
| MOMENT~INSTANT | **momento** | *momentos* (pl.) | Masculine noun (*el momento*): *en este momento* [at this moment] |

---

##### SPACE

The space primes include both interrogative/relative forms and positional adverbs.

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| WHERE~PLACE | **donde** / **lugar** | Interrogative: **dónde** (accented) | *Donde* [where] as relative/conjunction; *dónde* [where?] as interrogative. *Lugar* [place] as noun: *un buen lugar* [a good place] |
| HERE | **aquí** | — | ⚠ Accent is obligatory: *aquí*, never *aqui* |
| *(support)* | **ahí** | — | "There" (visible, reachable — near the addressee). Support word for the medial deictic: *Hay personas ahí* [There are people there]. Not an NSM prime, but required to complete the Spanish deictic triad alongside *aquí*. |
| *(support)* | **allí** / **allá** | — | "There" (far, not immediately reachable). *allí* is more precise; *allá* more directional or vague. Both are equivalent in ESCore: *Vamos allí* [We go there]; *está allá* [it is over there]. |
| ABOVE~UP | **arriba** | — | Both spatial (above/up) and directional (upward) |
| BELOW~DOWN | **abajo** | — | Mirror of *arriba* |
| FAR | **lejos** | *lejos de* (+ noun) | *Está lejos* [it is far]; *lejos de aquí* [far from here] |
| NEAR | **cerca** | *cerca de* (+ noun) | *Está cerca* [it is near]; *cerca de este lugar* [near this place] |
| SIDE | **lado** | *lados* (pl.) | Masculine noun (*el lado*): *a un lado* [to one side], *de este lado* [on this side] |
| INSIDE~IN | **dentro** / **adentro** | *dentro de* (+ noun) | *dentro* = static position (*está dentro* [it is inside]; *dentro de este cuerpo* [inside this body]). *adentro* = directional/motion variant (*vamos adentro* [we go inside]). Both are accepted ESCore exponents of this prime. |
| *(support)* | **afuera** | — | "Outside / outward" — directional complement to *adentro*: *habla con alguien de afuera* [speaks with someone from outside]. Spatial adverb, no inflection. |

---

##### LOGICAL AND DISCOURSE CONCEPTS

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| NOT | **no** | — | Placed immediately before the verb: *no sé* [I don't know], *no puedo hacer esto* [I can't do this] |
| MAYBE~PERHAPS | **quizá** | *quizás, tal vez* | All three are equivalent; *quizá/quizás* take indicative in the core register (the subjunctive after *quizá* is excluded) |
| CAN~BE ABLE TO | **poder** | *puedo, puedes, puede, podemos, pueden* | Stem-changes o→ue. Used as modal: *puedo decir esto* [I can say this]. Full irregulars in Ch. 12 |
| BECAUSE | **porque** | — | ⚠ Written as one word: *porque* (conjunction). Distinct from *¿por qué?* (interrogative, two words with accent) and *el porqué* (the reason, noun). *Por esto / por eso* [because of this] uses a different structure |
| IF | **si** | — | ⚠ No accent: *si* [if]. Distinct from *sí* [yes] (with accent) |

---

##### INTENSIFIER AND AUGMENTOR

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| VERY | **muy** | — | Invariable adverb: *muy bueno* [very good], *muy lejos* [very far]. ⚠ Never *muy mucho* — use *muchísimo* (outside core) |
| MORE | **más** | — | ⚠ Accent is obligatory: *más*, never *mas* (which is an archaic conjunction). *Quiero saber más* [I want to know more] |

---

##### SIMILARITY

| NSM Prime | Spanish Exponent | Key Variants | Notes |
|---|---|---|---|
| LIKE~AS~WAY | **como** | — | ⚠ No accent: *como* [like, as, the way]. Distinct from *¿cómo?* (how?, with accent) and *como* (I eat, first-person of *comer*). *Es como algo bueno* [it is like something good] |

---

#### 1.3 The BE Allolexy: *Ser* and *Estar*

The NSM prime BE has a single exponent in most languages. In Spanish it has two: **ser** and **estar**. Both are exponents of the same prime — neither is "more BE" than the other — but Spanish grammar requires you to choose between them based on the type of predication. This is the most consequential structural fact in the ESCore grammar, and it is addressed head-on here rather than buried in a later chapter.

**Ser** expresses:
- *Identity and essential nature:* what something fundamentally is.
  - *Es una parte de algo.* [It is a part of something.]
  - *Son palabras.* [They are words.]
  - *Soy yo.* [It is me. / I am I.]
- *Category membership:* belonging to a type or kind.
  - *Es algo bueno.* [It is something good.]
  - *¿Qué es esto?* [What is this? / What kind of thing is this?]
- *Origin and ownership:*
  - *Es mío.* [It is mine.]

**Estar** expresses:
- *Location:* where something is at a given moment.
  - *Está aquí.* [It is here.]
  - *Estamos cerca del lugar.* [We are near the place.]
- *Condition or transient state:* how something is at a given moment.
  - *Está bien.* [It is/He is well.]
  - *Estoy mal.* [I am not well / I feel bad.]
  - *Están dentro.* [They are inside.]

**Quick decision rule:**
> Use **ser** when you are saying what something *is* (its nature, type, or identity).
> Use **estar** when you are saying where something *is* or how something *is right now* (its location or state).

The full conjugation tables for both verbs and a decision flowchart appear in Chapter 9.

---

#### 1.4 The Prime Exponents at a Glance — One-Page Reference

The following table lists all 65 primes in alphabetical order by English label, with their primary Spanish exponent. Post this table and learn it as a unit.

| English Prime | Spanish Exponent | | English Prime | Spanish Exponent |
|---|---|---|---|---|
| ABOVE~UP | arriba | | KNOW | saber |
| AFTER | después | | LIKE~AS~WAY | como |
| ALL | todo | | LITTLE~FEW | poco |
| A LONG TIME | mucho tiempo | | LIVE | vivir |
| A SHORT TIME | poco tiempo | | MAYBE | quizá |
| BAD | malo / mal | | MOMENT | momento |
| BE (identity) | ser | | MORE | más |
| BE (state/place) | estar | | MOVE | moverse |
| BECAUSE | porque | | MUCH~MANY | mucho |
| BEFORE | antes | | NEAR | cerca |
| BIG~LARGE | grande | | NOT | no |
| BODY | cuerpo | | NOW | ahora |
| CAN | poder | | ONE | uno |
| DIE | morir | | OTHER~ELSE | otro |
| DO~MAKE | hacer | | PART | parte |
| FAR | lejos | | PEOPLE | gente |
| FEEL | sentir | | SAY | decir |
| FOR SOME TIME | por un tiempo | | SEE | ver |
| GOOD | bueno / bien | | SIDE | lado |
| HAPPEN | pasar | | SMALL | pequeño |
| HAVE~BE SOMEONE'S | tener / mío | | SOME | algunos |
| HEAR | oír | | SOMEONE~PERSON | alguien |
| HERE | aquí | | SOMETHING~THING | algo |
| I | yo | | THE SAME | el mismo |
| IF | si | | THERE IS~EXIST | hay |
| INSIDE~IN | dentro | | THINK | pensar |
| KIND~TYPE | tipo | | THIS | este |
| TOUCH | tocar | | TRUE | verdad |
| TWO | dos | | VERY | muy |
| WANT | querer | | WHEN~TIME | cuando / tiempo |
| WHERE~PLACE | donde / lugar | | WORD~WORDS | palabra |
| YOU | tú | | | |

---

### Chapter 2 — The Grammatical Support Layer

#### 2.1 Why Grammar Words Are Not Primes but Are Still Obligatory

The NSM prime inventory is a set of *semantic* atoms — irreducible meanings. Grammar words like *el*, *de*, *y*, and *que* are not irreducible meanings in the same sense; they are structural glue. You cannot coherently assign them a prime status because they do not add referential content in isolation. Yet removing them would make Spanish sentences ungrammatical.

Consider: *veo algo bueno.* [I see something good.] Every word here is a prime exponent. Now consider: *veo la parte del cuerpo* [I see the part of the body]. The words *la* and *del* (= *de* + *el*) are not primes; they carry no propositional meaning. But omitting them — ✗ *veo parte cuerpo* — produces non-Spanish.

The grammar words of Chapter 2 are therefore necessary consequences of choosing Spanish as the carrier language for the NSM. They are not part of the semantic core; they are the *grammatical shell* that the semantic core must wear in Spanish. A learner who internalizes the content of Chapter 1 and Chapter 2 has the complete lexical inventory of ESCore.

**Total ESCore lexical inventory: approximately 105–110 lemmas.** This is the allow-set. Every word used in the core register must be on one of these two lists.

---

#### 2.2 Articles

Spanish requires that most noun phrases carry an article, and the article must agree with the noun in gender and number. ESCore uses both definite and indefinite articles.

##### Definite Articles

| Form | Gender | Number | Example |
|---|---|---|---|
| **el** | masculine | singular | *el cuerpo* [the body], *el lugar* [the place] |
| **la** | feminine | singular | *la parte* [the part], *la gente* [the people] |
| **los** | masculine | plural | *los cuerpos* [the bodies] |
| **las** | feminine | plural | *las palabras* [the words], *las partes* [the parts] |

**Contraction:** When *de* immediately precedes *el*, they contract to **del**: *parte del cuerpo* [part of the body]. When *a* precedes *el*, they contract to **al**: *al lado* [to/at the side]. These contractions are obligatory. ✗ *parte de el cuerpo* and ✗ *a el lado* are both wrong.

**The definite article before abstract/generic nouns.** Spanish uses the definite article where English uses none in generic statements: *la gente piensa cosas* [people think things] — note *la gente* with article. This is a constant source of English-interference errors.

##### Indefinite Articles

| Form | Gender | Number | Example |
|---|---|---|---|
| **un** | masculine | singular | *un momento* [a moment], *un lugar* [a place] |
| **una** | feminine | singular | *una parte* [a part], *una cosa* [a thing] |
| **unos** | masculine | plural | *unos momentos* [some moments] |
| **unas** | feminine | plural | *unas palabras* [some words] |

**When no article is used.** In the core register, articles are dropped in a small number of fixed patterns:
- After *ser* with a bare predicate noun when no modifier is present: *soy alguien* [I am someone — no article needed]
- In certain time expressions: *en poco tiempo* [in a short time], *mucho tiempo* [a long time] — no article
- Before unmodified *otro*: *quiero otra cosa* [I want another thing — no *un* before *otra*]

---

#### 2.3 Prepositions

The core uses eight prepositions. Their meanings in the ESCore register are given below; full Spanish preposition use extends beyond this, but the core is restricted to these functions.

| Preposition | Core Meaning(s) | Examples |
|---|---|---|
| **a** | to, toward; personal direct object marker | *voy a este lugar* [I go to this place]; *veo a alguien* [I see someone (a person)] |
| **hacia** | toward (directional motion) | *va hacia ese lugar* [he/she moves toward that place] — distinct from *a* (destination reached) vs. *hacia* (direction of movement, arrival not implied) |
| **de** | of, from; possession; composition | *parte de algo* [part of something]; *es de aquí* [he/she is from here]; *algo de tiempo* [some time] |
| **en** | in, at, on (location) | *está en un lugar* [it is in a place]; *en este momento* [at this moment] |
| **con** | with | *estoy con alguien* [I am with someone] |
| **para** | for (purpose or intended recipient) | *esto es para ti* [this is for you]; *quiero hacer algo para alguien* [I want to do something for someone] |
| **por** | because of; through; for (duration/exchange) | *por esto* [because of this]; *por un tiempo* [for a time]; *pasa por aquí* [it passes through here] |
| **sin** | without | *no puedo vivir sin esto* [I can't live without this] |
| **sobre** | about; on top of | *digo algo sobre esto* [I say something about this]; *está sobre esto* [it is on top of this] |

**The personal *a***: When the direct object of a verb is a specific person or *alguien*, Spanish requires the preposition *a* before it. This is called the *a personal*. It carries no meaning; it is a pure grammatical marker.
- *veo algo* [I see something] — no *a*, because *algo* is not a person
- *veo a alguien* [I see someone] — *a* required, because the object is a person
- *quiero a alguien* [I love/want someone] — *a* required

**Compound prepositions from primes.** Several prime-derived spatial adverbs function as prepositions when followed by *de*:
- *dentro de* [inside of]: *dentro de este cuerpo* [inside this body]
- *cerca de* [near]: *cerca de aquí* [near here]
- *lejos de* [far from]: *lejos de ese lugar* [far from that place]
- *antes de* [before]: *antes de hacer esto* [before doing this]
- *después de* [after]: *después de esto* [after this]
- *al lado de* [beside, next to]: *al lado de algo* [next to something]

---

#### 2.4 Subject Pronouns Beyond *Yo* and *Tú*

*Yo* [I] and *tú* [you] are prime exponents and appear in Chapter 1. But Spanish requires subject pronouns for all six persons. The full set used in the core:

| Person | Pronoun | Notes |
|---|---|---|
| 1st sing. | **yo** | Prime exponent of I |
| 2nd sing. | **tú** | Prime exponent of YOU |
| 3rd sing. masc. | **él** | [he / it (masc.)] ⚠ Accent required on *él* [he]; *el* without accent is the article |
| 3rd sing. fem. | **ella** | [she / it (fem.)] |
| 1st pl. | **nosotros** / **nosotras** | [we] fem. form when the group is all-female |
| 3rd pl. | **ellos** / **ellas** | [they] *ellas* for all-female groups |

**Subject pronouns are usually omitted** in Spanish because the verb ending encodes person. They are used for emphasis or contrast: *yo sé esto, pero tú no sabes* [I know this, but you don't]. In the core register, omission is the default; inclusion is marked.

---

#### 2.5 Object and Reflexive Pronouns

Object pronouns are required in the core because several prime-exponent verbs demand them: *sentirse* [to feel], *moverse* [to move], *decirse* [to say to oneself], and the "something happens to someone" pattern (*le pasa algo*). A full treatment is in Chapter 11; this section provides the reference set.

**Reflexive pronouns** (used when subject and object are the same person):

| Person | Reflexive | Example |
|---|---|---|
| yo | **me** | *me muevo* [I move (myself)] |
| tú | **te** | *te sientes bien* [you feel good] |
| él/ella | **se** | *se mueve* [he/she/it moves] |
| nosotros | **nos** | *nos movemos* [we move] |
| ellos/ellas | **se** | *se mueven* [they move] |

**Indirect object pronouns** (used for "to someone" — the recipient or the experiencer):

| Person | Indirect | Example |
|---|---|---|
| yo | **me** | *me pasa algo* [something happens to me] |
| tú | **te** | *te digo algo* [I say something to you] |
| él/ella | **le** | *le pasa algo* [something happens to him/her] |
| nosotros | **nos** | *nos dice algo* [he/she says something to us] |
| ellos/ellas | **les** | *les digo esto* [I say this to them] |

**Direct object pronouns** (used when you replace a previously mentioned noun object):

| | Masculine | Feminine |
|---|---|---|
| Singular | **lo** | **la** |
| Plural | **los** | **las** |

*Veo algo* → *lo veo* [I see it (masc.)]. *Veo la parte* → *la veo* [I see it/her (fem.)].

---

#### 2.6 Coordinators

The three core coordinators are all you need to build compound clauses in the register.

| Coordinator | Meaning | Notes |
|---|---|---|
| **y** | and | ⚠ Before a word beginning with *i-* or *hi-*, *y* changes to **e**: *cuerpo e ideas* — but this pattern rarely arises in the core |
| **o** | or | ⚠ Before a word beginning with *o-* or *ho-*, *o* changes to **u** — again, rare in the core |
| **pero** | but | Introduces a contrasting clause: *quiero saber esto, pero no puedo* [I want to know this, but I can't] |

---

#### 2.7 The Relative and Complementizer *Que*

**Que** [that / which / who] is the single most frequent word in Spanish and is indispensable in the core. It has three distinct uses, all obligatory in ESCore:

1. **Complementizer** (introduces a that-clause after a mental or speech predicate):
   - *pienso que esto es bueno* [I think that this is good]
   - *sé que alguien está aquí* [I know that someone is here]
   - *dice que no quiere hacer esto* [he says that he doesn't want to do this]
   ⚠ Unlike English, the complementizer *que* cannot be omitted in Spanish: ✗ *pienso esto es bueno*.

2. **Relative pronoun** (introduces a relative clause):
   - *algo que quiero saber* [something that I want to know]
   - *la parte que se mueve* [the part that moves]
   - *alguien que sabe esto* [someone who knows this]

3. **Comparative** (after *más*, *menos*, *mejor*, *peor*):
   - *esto es más grande que aquello* [this is bigger than that]
   - *sé más que tú* [I know more than you]

⚠ **Critical accent distinction:** *que* (no accent) = that / which / who. *¿qué?* (with accent) = what? (interrogative). These are two different words in two different grammatical roles that happen to be homophones in spoken Spanish.

---

#### 2.8 Interrogative Words

The interrogatives are closely tied to several prime exponents (WHEN, WHERE, WHO, WHAT) but take orthographic accents that their relative/conjunction counterparts lack.

| Interrogative | Meaning | Accent note |
|---|---|---|
| **¿qué?** | what? | ¿*Qué* es esto? [What is this?] |
| **¿cuál?** / **¿cuáles?** | which one? / which ones? | ¿*Cuál* es? [Which one is it?] — selects from a known set; complements *¿qué?* (asks about type) and *¿quién?* (asks about person). *Cuál* without a noun; *qué* + noun: *¿qué lugar?* |
| **¿quién?** | who? | ¿*Quién* sabe esto? [Who knows this?] |
| **¿cuándo?** | when? | ¿*Cuándo* pasa esto? [When does this happen?] |
| **¿dónde?** | where? | ¿*Dónde* está esto? [Where is this?] |
| **¿adónde?** | to where? | ¿*Adónde* vamos? [Where are we going?] — directional form of *dónde*; contraction of *a* + *dónde*. The relative (non-interrogative) form *adonde* is equally valid: *el lugar adonde vamos*. |
| **¿cómo?** | how? | ¿*Cómo* se siente? [How does he/she feel?] |
| **¿por qué?** | why? | ¿*Por qué* dices esto? [Why do you say this?] |
| **¿cuánto?** | how much? | ¿*Cuánto* tiempo? [How much time?] |

All interrogatives require the inverted opening question mark ¿ in written Spanish. In spoken interaction (and in chatbot exchange) this is less critical, but it is maintained throughout this book.

---

#### 2.9 Demonstratives Beyond *Este*

*Este/esta/esto* (THIS) is a prime exponent and appears in Chapter 1. Spanish has two additional levels of demonstrative distance that arise in the core register, particularly for spatial reference and anaphora (referring back to previously mentioned items).

| Distance | Masc. sing. | Fem. sing. | Neuter | Masc. pl. | Fem. pl. | Meaning |
|---|---|---|---|---|---|---|
| Close (THIS) | *este* | *esta* | *esto* | *estos* | *estas* | near the speaker |
| Medium (THAT) | *ese* | *esa* | *eso* | *esos* | *esas* | near the listener or already mentioned |
| Far (THAT over there) | *aquel* | *aquella* | *aquello* | *aquellos* | *aquellas* | distant from both |

In the core register, **ese/eso** functions as the anaphoric demonstrative — it refers back to something already mentioned: *digo algo; ese algo es importante* [I say something; that something is important]. The distal *aquel* is included for completeness but rarely required in the immediate-context register.

---

#### 2.10 Common Adverbs of Discourse

A small set of high-frequency adverbs are so embedded in Spanish discourse structure that excluding them would make the core register feel unnatural and parsing difficult. These are not primes but are sanctioned support words.

| Word | Meaning | Notes |
|---|---|---|
| **sí** | yes | ⚠ Accent required: *sí* [yes]. Distinct from *si* [if] |
| **también** | also, too | *yo también sé esto* [I also know this] |
| **tampoco** | neither, not either | *yo tampoco sé esto* [I don't know this either] |
| **ya** | already; now (in context) | *ya sé* [I already know / I get it]; very high-frequency in conversation |
| **aún** / **todavía** | still, yet | *aún no sé* [I still don't know] |
| **siempre** | always | *siempre pasa esto* [this always happens] |
| **nunca** | never | Used in negation, see Ch. 15 |
| **así** | like this, in this way | *puedo hacerlo así* [I can do it like this]; key in giving instructions and explicating processes |
| **entonces** | then; so (consequence) | *pienso esto; entonces digo esto* [I think this; so I say this] |
| **solo** / **solamente** | only, just | *solo quiero saber esto* [I only want to know this] |
| **aquí** | here | Already a prime exponent; listed for completeness |

---

#### 2.11 Negative Polarity Items

Three words form a sub-system with the prime NOT. They are not themselves primes but are required for natural negation in Spanish. (Chapter 15 treats negation in full.)

| Word | Meaning | Spanish double-negative pattern |
|---|---|---|
| **nada** | nothing | *no sé nada* [I know nothing / I don't know anything] |
| **nadie** | nobody, no one | *no veo a nadie* [I see nobody] |
| **nunca** | never | *no pasa nunca* [it never happens] |

**The Spanish double negative:** Unlike English, Spanish requires both *no* before the verb and the negative word after it. *No sé nada* is correct and not redundant; ✗ *sé nada* (without *no*) is ungrammatical unless the negative word precedes the verb: *nada sé* (literary/emphatic, rare in the core register).

---

#### 2.12 The Core Verb *Ir* (to go) — A Support Verb, Not a Prime

The verb **ir** [to go] is not a semantic prime, but it earns its place in the support layer for two reasons: it is the auxiliary in the core's only future construction (*ir a + infinitive*), and movement toward a place is constantly needed in explicating spatial and event concepts.

| Person | Form |
|---|---|
| yo | **voy** |
| tú | **vas** |
| él/ella | **va** |
| nosotros | **vamos** |
| ellos/ellas | **van** |

*Voy a hacer algo* [I am going to do something — future]. *Va a pasar algo* [something is going to happen — future]. This is the only future construction in the core register (Chapter 14).

---

#### 2.13 Possessives

Possessive adjectives and pronouns appear frequently in explicating, especially with body parts (*mi cuerpo* [my body]) and internal states (*mis palabras* [my words]).

**Possessive adjectives** (before the noun):

| Owner | Before sing. noun | Before pl. noun | Example |
|---|---|---|---|
| yo | **mi** | **mis** | *mi cuerpo, mis palabras* |
| tú | **tu** | **tus** | *tu cuerpo, tus palabras* |
| él/ella/usted | **su** | **sus** | *su cuerpo, sus palabras* |
| nosotros | **nuestro/nuestra** | **nuestros/nuestras** | *nuestro cuerpo* |
| ellos/ellas | **su** | **sus** | *su cuerpo* |

⚠ *mi* (no accent) = my. *mí* (accent) = me (after a preposition): *para mí* [for me], *conmigo* [with me — special fusion form].

**Strong/predicative possessives** (after the noun or after *ser*):

| Owner | Masc. sing. | Fem. sing. | Meaning |
|---|---|---|---|
| yo | **mío** | **mía** | mine |
| tú | **tuyo** | **tuya** | yours |
| él/ella | **suyo** | **suya** | his/hers/its |
| nosotros | **nuestro** | **nuestra** | ours |
| ellos | **suyo** | **suya** | theirs |

*Es mío* [it is mine — the NSM "BE SOMEONE'S" exponent]. *¿Es tuyo esto?* [Is this yours?]

---

#### 2.14 The Special Fusion Form *Conmigo / Contigo*

When the preposition **con** [with] combines with the personal pronouns *mí* and *ti*, it fuses into a single word:

- *con* + *mí* → **conmigo** [with me]
- *con* + *ti* → **contigo** [with you]

These are not irregular; they are archaic fusions that have been preserved. They appear frequently: *estoy aquí contigo* [I am here with you], *quiero hacer esto contigo* [I want to do this with you].

---

### Chapter 2 Summary: The Complete ESCore Vocabulary

The table below consolidates the full allow-set — every lemma sanctioned in the ESCore register. A word not on this list is out of register.

**65 Prime Exponents** (see Chapter 1 for full details):

> *yo, tú, alguien, algo, gente, cuerpo, parte, tipo, este, el mismo, otro, uno, dos, algunos, mucho, poco, todo, bueno/bien, malo/mal, grande, pequeño, pensar, saber, querer, sentir, ver, oír, decir, palabra, verdad, hacer, pasar, moverse, tocar, hay, ser, estar, tener/mío, vivir, morir, cuando/tiempo, ahora, antes, después, mucho tiempo, poco tiempo, por un tiempo, momento, donde/lugar, aquí, arriba, abajo, lejos, cerca, lado, dentro, no, quizá, poder, porque, si, muy, más, como*

**~45 Grammatical Support Items** (Chapter 2):

> **Articles:** el, la, los, las, un, una, unos, unas
>
> **Prepositions:** a, de, en, con, para, por, sin, sobre
>
> **Coordinators:** y, o, pero
>
> **Subordinators / complementizers:** que
>
> **Pronouns (non-prime):** él, ella, nosotros/nosotras, ellos/ellas, me, te, se, le, lo, la, nos, les, los, las
>
> **Demonstrative extension:** ese/esa/eso, aquel/aquella/aquello
>
> **Possessives:** mi/mis, tu/tus, su/sus, nuestro/nuestra, mío/mía, tuyo/tuya, suyo/suya
>
> **Special fusion:** conmigo, contigo
>
> **Discourse adverbs:** sí, también, tampoco, ya, aún/todavía, siempre, nunca, así, entonces, solo
>
> **Negative polarity:** nada, nadie (nunca already listed above)
>
> **Interrogatives:** qué, quién, cuándo, dónde, cómo, por qué, cuánto
>
> **Support verb:** ir (voy/vas/va/vamos/van)
>
> **Contractions:** del (de + el), al (a + el)

---

### A Note on What Is Needed to Explicate in This Language

The prime list and the support vocabulary above are sufficient — in principle — to define any word in Spanish. This claim comes from NSM theory and has been validated over decades of cross-linguistic lexicographic work. The practical experience of using a language model constrained to this vocabulary confirms it: given a sufficiently large context window, the model can produce naturalistic, intelligible Spanish while staying within the register, and it can construct explicating sentences for target words on request.

However, "sufficient in principle" does not mean "effortless in practice." Certain things are harder to explicate in Spanish than in English because Spanish grammatical structure introduces complexity that the prime list itself does not:

1. **The ser/estar split** means that any explication involving BE requires a grammatical judgment before the semantic one. This is overhead not present in NSM-English, but it is unavoidable.

2. **Grammatical gender** means every noun-slot in an explication must be assigned a gender, and agreement must be maintained across the sentence. This is cognitively real overhead during composition.

3. **Verb conjugation** means that every verb in an explication must be conjugated, which introduces person/number information that may or may not be semantically relevant. The present-tense constraint of the core helps here: there are only six present-tense forms to learn, and most explicating uses third-person singular.

4. **The infinitive restriction** means that verbs in subordinate positions must either be finite (with a conjugated auxiliary) or infinitival (only after a modal). This prevents some English-style explication shortcuts.

Despite these complications, the ESCore grammar is a fully functional meaning-description system. A learner who masters this book's content can do real semantic work in Spanish — exploring, refining, and testing meaning by constructing and revising explicating definitions. That is the goal.

---

*End of Part I. Part II (The Noun System) begins with Chapter 3: Gender.*

---

## Part II — The Noun System

The chapters in this part cover the properties that every noun carries in Spanish and that every sentence involving a noun must respect: grammatical gender, number, the article system, adjective behavior, and the pronouns that substitute for noun phrases. None of this is optional — a Spanish sentence with agreement errors is not "simplified Spanish," it is broken Spanish. The good news is that the ESCore noun inventory is small and closed, so the agreement facts can be learned noun by noun, up front, rather than encountered unpredictably over time.

---

### Chapter 3 — Gender

#### 3.1 What Grammatical Gender Is

Every Spanish noun is classified as either **masculine** or **feminine**. This classification is called grammatical gender. It is not primarily about biological sex — it is a formal property of the noun that determines which forms of articles, adjectives, demonstratives, and pronouns must be used alongside it. When you know a noun, you must also know its gender: the two are inseparable.

Gender is not assigned by meaning or logic in most cases. *Cuerpo* [body] is masculine; *parte* [part] is feminine. There is no semantic reason for this difference. The learner must simply memorize it. The practical strategy for the ESCore inventory is straightforward: the noun set is small enough to learn all at once. This chapter lists every core noun with its gender so that the learner never has to guess.

#### 3.2 Default Patterns

While gender is not strictly predictable, there are strong default patterns that apply to most nouns in the language.

| Ending | Default gender | Examples |
|---|---|---|
| **-o** | masculine | *el cuerpo, el tiempo, el momento, el lado, el tipo* |
| **-a** | feminine | *la cosa, la persona, la clase, la palabra* |
| **-dad / -tad / -tud** | feminine | *la verdad, la ciudad* (outside core) |
| **-ión** | feminine | *la acción, la condición* (outside core) |
| Consonants (other) | usually masc. | *el lugar, el dolor* (outside core) |
| **-e** | unpredictable — must learn | *la parte* (fem.), *la gente* (fem.), *el nombre* (masc., outside core) |

#### 3.3 The Gender of Every Core Noun

The following table lists all nouns that appear in the ESCore register with their assigned gender. Every one of these must be internalized before proceeding.

| Noun | Gender | Article | Meaning | Pattern note |
|---|---|---|---|---|
| *cuerpo* | masculine | el cuerpo | body | Regular -o → masc. |
| *tiempo* | masculine | el tiempo | time | Regular -o → masc. |
| *momento* | masculine | el momento | moment | Regular -o → masc. |
| *lado* | masculine | el lado | side | Regular -o → masc. |
| *tipo* | masculine | el tipo | kind, type | Regular -o → masc. |
| *lugar* | masculine | el lugar | place | Consonant → masc. |
| *parte* | **feminine** | la parte | part | ⚠ Exception: -e ending, feminine |
| *gente* | **feminine** | la gente | people | ⚠ Exception: -e ending, feminine |
| *clase* | **feminine** | la clase | kind, class | ⚠ Exception: -e ending, feminine |
| *cosa* | feminine | la cosa | thing | Regular -a → fem. |
| *persona* | feminine | la persona | person | Regular -a → fem. |
| *palabra* | feminine | la palabra | word | Regular -a → fem. |
| *verdad* | **feminine** | la verdad | truth | -dad ending → fem. |

**The three traps.** Among these nouns, three gender assignments consistently cause errors:

1. *la parte* — The ending -e gives no gender signal, and learners sometimes guess masculine. It is feminine. *la parte del cuerpo* [the part of the body], never ✗ *el parte*.

2. *la gente* — Collective noun referring to people. It is grammatically feminine singular, even though it refers to multiple people. *La gente sabe esto* [people know this], not ✗ *la gente saben*.

3. *la verdad* — The -dad ending is a reliable feminine marker in Spanish. *La verdad es esto* [the truth is this].

#### 3.4 Nouns That Are Both: Natural Gender Pairs

Two core nouns have natural-gender pairs where the suffix changes depending on biological sex:

- *la persona* is always feminine regardless of the person's sex. There is no masculine form *el persono*.
- *alguien* [someone] is grammatically neither — it is an indefinite pronoun and takes no article, but adjectives referring to it default to masculine: *alguien bueno* [someone good].

#### 3.5 Why Gender Must Be Learned Before Articles and Adjectives

Every subsequent chapter in Part II builds on gender. The article must agree with the noun's gender (*el* vs. *la*). The adjective must agree with the noun's gender (*bueno* vs. *buena*). The demonstrative must agree (*este* vs. *esta*). The possessive must agree (*mío* vs. *mía*). Learning gender now, as a self-contained task, means that all of those chapters fall into place without additional memorization of the noun-gender pairing.

---

### Chapter 4 — Number

#### 4.1 Singular and Plural

Spanish nouns have two number values: singular (one) and plural (more than one). Plural is formed from the singular by a regular rule with only two cases.

**Rule 1 — Add *-s*:** If the singular ends in an unstressed vowel (-a, -e, -o, -u), add *-s*.

| Singular | Plural | Meaning |
|---|---|---|
| *cuerpo* | *cuerpos* | bodies |
| *parte* | *partes* | parts |
| *cosa* | *cosas* | things |
| *persona* | *personas* | people / persons |
| *clase* | *clases* | kinds, classes |
| *palabra* | *palabras* | words |
| *lugar* | *lugares* | places (see Rule 2) |
| *momento* | *momentos* | moments |
| *lado* | *lados* | sides |
| *tipo* | *tipos* | kinds, types |

**Rule 2 — Add *-es*:** If the singular ends in a consonant or a stressed vowel, add *-es*.

| Singular | Plural | Meaning |
|---|---|---|
| *lugar* | *lugares* | places |
| *verdad* | *verdades* | truths |

**Spelling adjustment:** Nouns ending in *-z* change to *-c* before *-es*. None of the core nouns end in *-z*, so this rule does not arise in the register.

#### 4.2 The Plural of *Gente*

*Gente* [people] is a collective noun and is used grammatically as singular in Spanish: *la gente sabe* [people know — singular verb]. Using a plural verb with *gente* is a standard English-interference error: ✗ *la gente saben*.

When you want to refer to distinct countable individuals, use *personas*: *dos personas* [two people/persons], *algunas personas* [some people].

The pair to internalize: *la gente* [people, as a collective mass] vs. *las personas* [people, as countable individuals].

#### 4.3 Plural of Compound Prime Phrases

Several primes are expressed as fixed phrases rather than single words. These phrases do not pluralize in the ordinary sense — they are used as invariable blocks.

| Phrase | Notes |
|---|---|
| *mucho tiempo* | Does not pluralize — quantity is already expressed by *mucho* |
| *poco tiempo* | Does not pluralize |
| *por un tiempo* | *un* could theoretically vary but the phrase is fixed |
| *el mismo* | The whole phrase *el mismo / la misma* agrees with the noun it modifies |
| *a un lado* | Fixed spatial expression |

#### 4.4 Number Agreement as a System

Number, like gender, propagates through the noun phrase: article, adjective, demonstrative, and pronoun must all match the noun's number. This agreement is treated in detail in Chapter 5 (articles) and Chapter 6 (adjectives), but the principle is introduced here: the noun is the grammatical *head* of the noun phrase, and everything else in the phrase copies its gender and number from the noun.

> Noun phrase structure: **Article + (Adjective) + Noun + (Adjective)**
> All elements agree in gender and number with the noun.

---

### Chapter 5 — Articles and Agreement

#### 5.1 The Article System

Articles in Spanish form a two-by-four grid: definiteness (definite vs. indefinite) crossed with gender (masc. vs. fem.) and number (sing. vs. pl.). Chapter 2 introduced the forms; this chapter explains when and why to use each.

**Definite articles** (*the*):

| | Masculine | Feminine |
|---|---|---|
| Singular | **el** | **la** |
| Plural | **los** | **las** |

**Indefinite articles** (*a/an, some*):

| | Masculine | Feminine |
|---|---|---|
| Singular | **un** | **una** |
| Plural | **unos** | **unas** |

#### 5.2 Choosing Definite vs. Indefinite

The definite article marks a noun as **already identified** — the speaker and listener share a reference for it. The indefinite article marks a noun as **not yet identified** — the speaker is introducing it or leaving it open.

| Context | Article | Example |
|---|---|---|
| Introducing a new referent | indefinite | *hay un lugar lejos de aquí* [there is a place far from here] |
| Referring back to it | definite | *el lugar está arriba* [the place is above/up] |
| Generic statement about a class | definite | *la gente quiere vivir bien* [people want to live well] |
| A specific known instance | definite | *la parte del cuerpo que toco* [the part of the body that I touch] |
| An unspecified member of a class | indefinite | *veo a alguien — es una persona buena* [I see someone — they are a good person] |

**The generic definite.** One of the most consistent English-interference errors in Spanish is dropping the definite article before generic nouns. In Spanish, generic statements require *la/el/los/las*:
- ✗ *gente piensa* → ✓ *la gente piensa* [people think]
- ✗ *palabras son importantes* → ✓ *las palabras son importantes* [words are important]

The rule: if you would say "the X" in English meaning X-in-general, use the article. If you would say just "X" in English meaning X-in-general, use the article anyway in Spanish.

#### 5.3 Agreement in the Full Noun Phrase

Every element that modifies the noun must carry the same gender and number as the noun itself. "Agreement" means all the words in a noun phrase carrying the same -o/-a and singular/plural endings.

| Core noun | Gender | Number | Article | Prime adjective | Full phrase |
|---|---|---|---|---|---|
| *cuerpo* | masc. | sing. | *el* | *bueno* | *el cuerpo bueno* |
| *parte* | fem. | sing. | *la* | *buena* | *la parte buena* |
| *palabras* | fem. | pl. | *las* | *buenas* | *las palabras buenas* |
| *lugares* | masc. | pl. | *los* | *buenos* | *los lugares buenos* |
| *momento* | masc. | sing. | *un* | *bueno* | *un momento bueno* |
| *verdad* | fem. | sing. | *la* | *misma* | *la misma verdad* |
| *persona* | fem. | sing. | *una* | *buena* | *una persona buena* |

**Agreement propagates to demonstratives and possessives too:**
- *este cuerpo, esta parte, estos cuerpos, estas partes*
- *mi cuerpo, mi parte, mis cuerpos, mis partes*
- *el mismo lugar, la misma parte, los mismos lugares, las mismas partes*

#### 5.4 When the Article Is Dropped

The article is omitted in these ESCore contexts:

**After *ser* with bare role/category nouns (no modifier present):**
- *soy alguien* [I am someone] — no article before *alguien* (it is a pronoun, not a noun)
- *eres una persona buena* [you are a good person] — article present because an adjective modifies the noun
- *es parte de algo* [it is part of something] — *parte de* in this partitive sense drops the article

**In fixed temporal expressions:**
- *mucho tiempo* [a long time / much time] — no article
- *poco tiempo* [a short time] — no article
- *en este momento* [at this moment] — demonstrative replaces article
- *en poco tiempo* [in a short time] — no article before *poco tiempo*
- *por un tiempo* [for a while] — article retained here; the phrase is fixed with *un*

**Before *otro*:**
- Spanish does not use an indefinite article before *otro*: *quiero otra cosa* [I want another thing], not ✗ *quiero una otra cosa*.
- The definite article before *otro* is used only when referring to a specific already-identified other item: *el otro lugar* [the other place (that we know about)].

**After prepositions in some fixed collocations:**
- *en poco tiempo* [in a short time]
- *de parte de* [on behalf of / from the side of]
- *sin algo* [without something]

#### 5.5 *El* Before Feminine Nouns Beginning with Stressed *A-*

There is one apparent exception to the gender-article pairing: feminine nouns beginning with a stressed *a-* (or *ha-*) take *el* instead of *la* in the singular, to avoid the awkward vowel clash. This does not change the noun's gender — it remains feminine, and adjectives still take feminine agreement.

No core ESCore nouns trigger this rule, but it is noted here because learners encounter it early in broader Spanish. The word *agua* [water] is the classic example outside the core register.

---

### Chapter 6 — Adjective Agreement and Position

#### 6.1 Adjectives Must Agree with Their Noun

A Spanish adjective is not a fixed form. Its ending changes to match the gender and number of the noun it modifies. Every prime-exponent adjective in the core follows this system.

The full agreement paradigm for a regular adjective:

| | Masculine | Feminine |
|---|---|---|
| Singular | -o | -a |
| Plural | -os | -as |

This applies to: *bueno, malo, pequeño, otro, mismo.*

Adjectives ending in *-e* or a consonant (like *grande*) do not change for gender — only for number.

#### 6.2 Agreement Tables for All Core Adjectives

| Adjective | Masc. sing. | Fem. sing. | Masc. pl. | Fem. pl. | Prime |
|---|---|---|---|---|---|
| good | **bueno** | *buena* | *buenos* | *buenas* | GOOD |
| bad | **malo** | *mala* | *malos* | *malas* | BAD |
| big | **grande** | *grande* | *grandes* | *grandes* | BIG~LARGE |
| small | **pequeño** | *pequeña* | *pequeños* | *pequeñas* | SMALL |
| other | **otro** | *otra* | *otros* | *otras* | OTHER~ELSE |
| same | **mismo** | *misma* | *mismos* | *mismas* | THE SAME |
| much/many | **mucho** | *mucha* | *muchos* | *muchas* | MUCH~MANY |
| little/few | **poco** | *poca* | *pocos* | *pocas* | LITTLE~FEW |
| all | **todo** | *toda* | *todos* | *todas* | ALL |
| some | **algunos** | *algunas* | *algunos* | *algunas* | SOME |
| one | **uno** → *un* | *una* | — | — | ONE |

*Grande* deserves a special note: it is invariable for gender (*un lugar grande, una cosa grande*) but does take a plural *grandes* (*muchos lugares grandes*).

#### 6.3 The Short Forms: *Bueno/Malo/Grande* Before a Noun

When *bueno*, *malo*, and *grande* precede a masculine singular noun, they shorten:

| Full form | Short form | Context |
|---|---|---|
| *bueno* | **buen** | before masc. sing. noun: *un buen momento* |
| *malo* | **mal** | before masc. sing. noun: *un mal momento* |
| *grande* | **gran** | before any sing. noun: *un gran lugar, una gran parte* |

The core register **defaults to post-nominal position** (adjective after noun), so these shortened forms arise mainly in set phrases. When the adjective follows the noun, the full form is always used: *un momento bueno, un momento malo, un lugar grande*.

⚠ The short form rule applies only when the adjective *precedes* the noun. Post-nominally, the full form is always correct.

#### 6.4 Default Word Order: Adjective After Noun

This is the most common error made by English speakers learning Spanish. In English, adjectives precede nouns almost universally: "a good thing," "a small part." In Spanish, descriptive adjectives default to **post-nominal position**: the adjective follows the noun.

| Spanish (correct) | Spanish (error) | English |
|---|---|---|
| *algo bueno* | ✗ *bueno algo* | something good |
| *una parte pequeña* | ✗ *una pequeña parte* | a small part |
| *un lugar grande* | ✗ *(in most contexts) un grande lugar* | a big place |
| *palabras verdaderas* | ✗ *verdaderas palabras* | true words |
| *una cosa mala* | ✗ *una mala cosa* | a bad thing |

**When pre-nominal placement is used:** A small set of adjectives can precede the noun with a different or nuanced meaning. In the core, *mismo*, *otro*, *mucho*, *poco*, *todo*, *algunos*, *uno*, and the quantifiers are all pre-nominal as a rule, because they are *quantifying or identifying* rather than *describing*:
- *el mismo lugar* [the same place] — *mismo* always precedes
- *otro momento* [another moment] — *otro* always precedes
- *muchas palabras* [many words] — *mucho* always precedes
- *todas las partes* [all the parts] — *todo* always precedes

Descriptive adjectives from the primes (*bueno, malo, grande, pequeño*) belong after the noun by default in the core register.

#### 6.5 The *Bueno/Bien* and *Malo/Mal* Distinction

This distinction is one of the most frequent sources of error in the core, because the primes GOOD and BAD each have two Spanish surface forms that are used in completely different grammatical positions.

| | Adjective (modifies a noun, or predicate after *ser*) | Adverb (modifies a verb or predicate after *estar*) |
|---|---|---|
| **GOOD** | *bueno/buena/buenos/buenas* | **bien** |
| **BAD** | *malo/mala/malos/malas* | **mal** |

**Adjective use (what something fundamentally is — with *ser*):**
- *es algo bueno* [it is something good] — *bueno* after *ser* + noun
- *eres una persona buena* [you are a good person] — *buena* agreeing with *persona*
- *eso es malo* [that is bad] — *malo* after *ser*

**Adverb use (how something is right now — with *estar*, or modifying a verb):**
- *estoy bien* [I am well / I'm fine] — ✗ *estoy bueno* (means something different — "I am attractive" in some dialects)
- *se siente bien* [he/she feels good] — *bien* modifying the verb *sentir*
- *está mal* [it is wrong / he/she is unwell] — ✗ *está malo* (means "he/she is sick" specifically — narrower meaning)
- *lo hace bien* [he/she does it well] — *bien* as adverb of manner
- *lo hace mal* [he/she does it badly] — *mal* as adverb of manner

**The decision rule:**
> After *ser* modifying a noun → *bueno/buena/buenos/buenas* or *malo/mala/malos/malas*
> After *estar* or modifying a verb → *bien* or *mal*

This is the adjectival face of the ser/estar split. Chapter 9 treats that distinction in full; this rule follows directly from it.

#### 6.6 Agreement with Indefinite Reference

When an adjective follows *algo* [something] or *nada* [nothing], Spanish uses the masculine singular form regardless of context, because these pronouns are semantically genderless.

- *algo bueno* [something good] — masculine singular, even though no noun is specified
- *nada malo* [nothing bad]
- *algo pequeño* [something small]

This pattern is extremely frequent in explicating, because many NSM definitions begin "something that is..." or "it is something...".

---

### Chapter 7 — Pronouns

The pronoun system of ESCore is built from pieces introduced across Chapters 1 and 2 — the prime-exponent personal pronouns (*yo, tú*), the extended subject pronouns (*él, ella, nosotros, ellos, ellas*), the object and reflexive pronouns, and the possessives. This chapter consolidates the whole system and addresses the grammatical behaviors that a scattered introduction cannot cover: the pro-drop rule, the accent distinctions, the ordering of multiple pronouns, and the possessive/prepositional alternation.

#### 7.1 Subject Pronouns and Pro-Drop

Spanish is a **pro-drop language**: the subject pronoun is usually omitted because the verb ending carries sufficient person-and-number information. The ending *-o* on a present-tense verb means first-person singular; *-as* or *-es* means second-person singular; *-a* or *-e* means third-person singular; and so on (see Chapter 10 for full paradigms). Because the ending is present, the pronoun is redundant and therefore typically absent.

| With pronoun (emphatic/contrastive) | Without pronoun (default) | Meaning |
|---|---|---|
| *Yo sé esto.* | *Sé esto.* | I know this. |
| *Tú piensas esto.* | *Piensas esto.* | You think this. |
| *Ella quiere algo.* | *Quiere algo.* | She wants something. |
| *Nosotros vivimos aquí.* | *Vivimos aquí.* | We live here. |
| *Ellos dicen esto.* | *Dicen esto.* | They say this. |

**When to include the pronoun:**

1. **Emphasis or contrast:** *Yo sé esto, pero tú no sabes nada.* [I know this, but you know nothing.] The contrast between the two people makes the pronouns communicatively useful.

2. **Disambiguation:** The third-person forms (*él, ella, ellos, ellas*) all share the same verb endings. When it is not clear from context whether the subject is *él* or *ella*, the pronoun is included.

3. **After a topic shift:** If the subject changes from the previous sentence, a pronoun helps the listener track who is doing what.

In the chatbot/explicating register, pro-drop is the default and the learner should not feel obligated to include pronouns. Models constrained to the core register will produce the dropped form most of the time.

#### 7.2 The Full Subject Pronoun Set

| Person | Pronoun | Notes |
|---|---|---|
| 1st sing. | *yo* | Prime exponent I |
| 2nd sing. | *tú* | Prime exponent YOU — informal |
| 3rd sing. masc. | *él* | ⚠ Must have accent: *él* [he]. Without accent: *el* [the article] |
| 3rd sing. fem. | *ella* | [she, it (fem.)] |
| 1st pl. | *nosotros / nosotras* | [we] — *nosotras* when the group is all female |
| 3rd pl. masc. | *ellos* | [they (masc. or mixed)] |
| 3rd pl. fem. | *ellas* | [they (all female)] |

The second-person plural (*vosotros* in Spain, *ustedes* in Latin America) and the formal singular (*usted*) are outside the ESCore register. The core uses *tú* for YOU and relies on *ellos/ellas* + context for groups.

#### 7.3 Object Pronouns: Position and Forms

Object pronouns in Spanish are placed **before the conjugated verb** (pre-verbal position) in standard finite sentences.

**Reflexive pronouns** (subject = object, same person):

| Person | Pronoun | Example | Meaning |
|---|---|---|---|
| yo | *me* | *me muevo* | I move (myself) |
| tú | *te* | *te sientes* | you feel |
| él/ella | *se* | *se mueve* | he/she/it moves |
| nosotros | *nos* | *nos movemos* | we move |
| ellos/ellas | *se* | *se mueven* | they move |

**Indirect object pronouns** (to whom or for whom):

| Person | Pronoun | Example | Meaning |
|---|---|---|---|
| yo | *me* | *me dices algo* | you say something to me |
| tú | *te* | *te digo algo* | I say something to you |
| él/ella | *le* | *le pasa algo* | something happens to him/her |
| nosotros | *nos* | *nos dices algo* | you say something to us |
| ellos/ellas | *les* | *les digo algo* | I say something to them |

The pattern *le pasa algo* [something happens to him/her] is a core idiom worth drilling as a unit. The indirect object pronoun *le* marks the experiencer — the person who undergoes or receives what the verb describes.

**Direct object pronouns** (what is acted on, replacing a noun that has already been mentioned):

| | Masculine | Feminine |
|---|---|---|
| Singular | *lo* | *la* |
| Plural | *los* | *las* |

- *Sé la verdad. La sé.* [I know the truth. I know it (fem.).] — *la verdad* is feminine → *la*
- *Veo el cuerpo. Lo veo.* [I see the body. I see it (masc.).] — *el cuerpo* is masculine → *lo*

#### 7.4 Pronoun Position with Infinitives

When an object pronoun accompanies an infinitive (in the modal constructions of Chapter 13), it may either precede the conjugated auxiliary or attach to the end of the infinitive. Both forms are grammatical in the core register.

| Pre-verbal (before auxiliary) | Attached (to infinitive) | Meaning |
|---|---|---|
| *lo quiero hacer* | *quiero hacerlo* | I want to do it |
| *me puedo mover* | *puedo moverme* | I can move |
| *te voy a decir algo* | *voy a decirte algo* | I am going to say something to you |
| *se va a sentir bien* | *va a sentirse bien* | he/she is going to feel well |

In the core register, attached-to-infinitive is the more common written form and is preferred in explicating texts.

#### 7.5 Accent Distinctions in the Pronoun and Possessive System

A cluster of monosyllables differ only in the presence or absence of a written accent mark. These are among the most common written errors in Spanish. Each pair must be learned as two distinct words.

| With accent | Without accent | The difference |
|---|---|---|
| *él* [he] | *el* [the — masc. article] | *él viene* vs. *el cuerpo* |
| *tú* [you — subject] | *tu* [your — possessive adj.] | *tú sabes* vs. *tu cuerpo* |
| *mí* [me — after preposition] | *mi* [my — possessive adj.] | *para mí* vs. *mi cuerpo* |
| *sí* [yes; -self] | *si* [if; whether] | *sí, lo sé* vs. *si sabes* |
| *sé* [I know; be! — imperative] | *se* [reflexive pronoun] | *sé que* vs. *se mueve* |
| *té* [tea — outside core] | *te* [you — pronoun] | n/a in core |
| *más* [more] | *mas* [but — archaic] | *quiero más* vs. archaic *mas* |
| *qué* [what? — interrogative] | *que* [that/which — subordinator] | *¿qué sabes?* vs. *sé que* |
| *cuándo* [when? — interrogative] | *cuando* [when — relative/conjunction] | *¿cuándo pasa?* vs. *cuando pasa* |
| *dónde* [where? — interrogative] | *donde* [where — relative] | *¿dónde está?* vs. *el lugar donde* |
| *cómo* [how? — interrogative] | *como* [like/as — prime] | *¿cómo?* vs. *como algo* |

In chatbot exchanges, which are informal written interactions, these accent errors are common and usually intelligible from context. However, the core register maintains the distinctions, and a well-prompted model will too. The learner should aim to use them correctly from the start.

#### 7.6 Possessives: Review and Full System

Possessives were introduced in Chapter 2 (§2.13). This section consolidates them in the context of pronoun grammar.

**Short possessives (adjectives, precede the noun):**

| Owner pronoun | Before sing. | Before pl. | Example |
|---|---|---|---|
| *yo* | *mi* | *mis* | *mi parte, mis palabras* |
| *tú* | *tu* | *tus* | *tu cuerpo, tus cosas* |
| *él/ella* | *su* | *sus* | *su lugar, sus momentos* |
| *nosotros* | *nuestro/nuestra* | *nuestros/nuestras* | *nuestro lado, nuestra parte* |
| *ellos/ellas* | *su* | *sus* | *su verdad* |

Note: *nuestro* agrees with the gender of the noun possessed, not the gender of the owner.

**Long possessives (pronouns or post-nominal adjectives):**

| Owner | Masc. sing. | Fem. sing. | Masc. pl. | Fem. pl. |
|---|---|---|---|---|
| yo | *mío* | *mía* | *míos* | *mías* |
| tú | *tuyo* | *tuya* | *tuyos* | *tuyas* |
| él/ella | *suyo* | *suya* | *suyos* | *suyas* |
| nosotros | *nuestro* | *nuestra* | *nuestros* | *nuestras* |
| ellos | *suyo* | *suya* | *suyos* | *suyas* |

The long possessives are used:
1. After *ser* to express ownership: *es mío* [it is mine], *¿es tuyo?* [is it yours?]
2. After a noun for emphasis: *un cuerpo mío* [a body of mine], *palabras mías* [words of mine]
3. As standalone pronouns (no noun): *el mío es bueno* [mine is good]

The NSM prime meaning HAVE~BE SOMEONE'S is primarily expressed by the *ser + long possessive* construction: *es mío / es tuyo / es suyo*. Alongside *tener* for physical possession, this gives two paths to the possession meaning:
- *tengo algo* [I have something — I possess it]
- *es mío* [it is mine — it belongs to me]

---

*End of Part II. Part III (The Verb System) begins with Chapter 8.*

---

## Part III — The Verb System (The Core's Real Weight)

The verb system is where ESCore's honest cost becomes fully visible. The noun system — five chapters — is tractable because the core noun inventory is small and gender is learnable as a closed list. The verb system cannot be made tractable that way. The prime inventory forces eleven irregular verbs into scope, and those verbs must be conjugated correctly every time they appear, which is constantly.

The design response to this is not to hide the cost. It is to bound it precisely and address it head-on. This part does three things: it explains *why* the irregular core is the size it is (Chapter 8); it teaches the single most important verb distinction in the language (Chapter 9); it covers the regular conjugation engine that everything else rests on (Chapter 10); and it works through every irregular and complex construction in the core as a single bounded set (Chapters 11–14).

**The three-tier verb system of ESCore.** The core register restricts the verb surface to exactly three licensed constructions:

| Tier | Construction | Example |
|---|---|---|
| 1 | **Present active** — finite verb conjugated for person/number | *sé esto, se mueve, pasa algo* |
| 2 | **Modal + infinitive** — *poder/querer/deber* + bare infinitive | *puedo decir esto, quiero moverme* |
| 3 | ***Ir a* + infinitive** — the only future | *va a pasar algo, voy a hacer esto* |

The infinitive appears only as a dependent form in Tiers 2 and 3. It is never a standalone finite form. Past tense, subjunctive, conditional, compound tenses, and passive voice are all outside the register and are treated in Appendix B.

**The bootstrap principle.** This restriction is not merely a pedagogical shortcut — it is intellectually principled. Once you can operate in the present-active register, you can use the language *itself* to acquire the forms that lie beyond it. A chatbot constrained to ESCore can explain, in ESCore Spanish, what the preterite is, what the subjunctive does, and how they work. The grammar of the rest of the language becomes learnable from inside the language, inductively, through a medium you already control. The core is not the destination; it is the entry point from which the rest is reachable.

---

### Chapter 8 — Why the Verb Core Is Large

#### 8.1 The Frequency–Irregularity Correlation

Languages resist the regularization of their most frequently used forms. The mechanism is straightforward: regular forms are learned by analogy; irregular forms are learned by rote from repeated encounter. When a form is encountered rarely, rote memory fades and the speaker defaults to the regular pattern. When a form is encountered constantly — every day, hundreds of times — the irregular form is reinforced and survives. The most frequent words in any language therefore accumulate the heaviest irregularity, precisely because frequency is what preserves it.

The semantic primes are, by definition, the most fundamental and universal meanings in human language. They are also, for exactly that reason, among the most frequently used meanings. In Spanish, the prime-exponent verbs are not only high-frequency in the language overall — they are the verbs that appear in essentially every utterance about states, actions, mental events, and relations. The consequence is unavoidable: the prime-exponent verbs in Spanish are the most irregular verbs in Spanish.

#### 8.2 The Obligatory Irregular Inventory

The following prime-exponent verbs have present-tense irregular forms that cannot be predicted from the regular conjugation rules. There is no pedagogical sleight of hand that removes them from scope. The learner must learn every one.

| Verb | Prime | Type of irregularity |
|---|---|---|
| *ser* | BE (identity) | Suppletive — forms from three different Latin roots |
| *estar* | BE (state/location) | Irregular *yo*, accent shift in other forms |
| *tener* | HAVE | Irregular *yo* + stem change |
| *hacer* | DO~MAKE | Irregular *yo* |
| *decir* | SAY | Irregular *yo* + e→i stem change |
| *ver* | SEE | Irregular *yo* + irregular stem |
| *saber* | KNOW | Irregular *yo* |
| *querer* | WANT | e→ie stem change |
| *poder* | CAN | o→ue stem change |
| *oír* | HEAR | Fully irregular throughout |
| *ir* | support verb (future) | Suppletive — forms from two Latin roots |
| *venir* | support for motion context | e→ie + irregular *yo* |
| *dar* | give (support) | Irregular *yo*, unusual endings |
| *pensar* | THINK | e→ie stem change |
| *sentir* | FEEL | e→ie/i stem change |
| *morir* | DIE | o→ue stem change |

*Vivir* and *tocar* are regular -ir and -ar verbs respectively and require no special treatment.

This is sixteen verbs carrying irregularities of one kind or another. That is the true scope of the irregular core. It is not small. But it is **finite, closed, and entirely learnable as a single project** — and that is the framing this book adopts.

#### 8.3 The Design Response: Constrain the Surface, Not the Set

The irregular verbs cannot be removed from scope. They can, however, be constrained in *how they are used*. ESCore applies three constraints that make the irregular core manageable:

**Constraint 1: Present tense only.** Each irregular verb has distinct forms in each tense. The past tense (preterite) of *ser* is entirely different from its present; the imperfect, subjunctive, and conditional add further paradigms. By restricting to the present tense, the learner faces at most six forms per verb (one per person-number combination) rather than six times the number of tenses.

**Constraint 2: Third-person singular dominance in explicating.** The register's primary use — writing and reading definitions and explications — leans heavily on third-person singular: *es algo*, *pasa cuando*, *se siente*, *se hace*. In practice, the learner will use the *yo/tú* forms in conversation and the *él/ella* form in explicating. This means four of the six present-tense slots per verb get the most exposure.

**Constraint 3: The irregular *yo* pattern.** The most common irregularity in this list is a *yo*-specific irregularity: *tengo, hago, digo, veo, sé, oigo, doy, vengo* — the first-person singular is irregular, but the remaining five forms (tú, él, nosotros, ellos) are either regular or follow a predictable stem-change pattern. Learning the *yo* form as a distinct item, and then applying the regular endings to the stem, recovers most of the paradigm from two pieces of information.

#### 8.4 Grouping by Irregularity Type

Chapter 12 presents all irregular core verbs grouped by the type of irregularity, so that the patterns are learnable rather than memorized one form at a time. The groups are:

| Group | Verbs | Pattern |
|---|---|---|
| Fully suppletive | *ser, ir* | Completely unpredictable — must be learned whole |
| Irregular *yo* only | *estar, hacer, ver, saber, dar* | *yo* form is irregular; other forms are regular or near-regular |
| Irregular *yo* + stem change | *tener, decir, venir, oír* | *yo* form is irregular AND stem changes in stressed syllables |
| Stem-change e→ie | *querer, pensar, sentir, venir* | All stressed-syllable forms change; *nosotros* does not |
| Stem-change o→ue | *poder, morir* | Same pattern, different vowel |

Once the learner internalizes these five groups, the paradigms in Chapter 12 are not memorization exercises — they are confirmations of patterns already understood.

---

### Chapter 9 — *Ser* and *Estar* (The BE Allolexy)

#### 9.1 One Prime, Two Verbs

Chapter 1 introduced the key fact: the NSM prime BE has two Spanish exponents, *ser* and *estar*, and choosing between them is not a semantic decision but a grammatical one conditioned by the type of predication. This chapter gives the learner everything needed to make that choice correctly and automatically.

The distinction can be stated simply: *ser* tells you what something *is* (nature, identity, category); *estar* tells you where something *is* or how it *is right now* (location, current state). But this simple statement collapses under pressure in many real cases, so this chapter provides a complete account organized by predicate type rather than by vague intuition.

#### 9.2 Present-Tense Conjugation of *Ser*

*Ser* is suppletive — its forms come from three different Latin roots (*esse, sedere, fuere*) — and must be learned whole. There is no stem to extract.

| Person | Form | Example in ESCore |
|---|---|---|
| yo | **soy** | *soy alguien* — I am someone |
| tú | **eres** | *eres una persona buena* — you are a good person |
| él/ella | **es** | *es algo malo* — it is something bad |
| nosotros | **somos** | *somos gente* — we are people |
| ellos/ellas | **son** | *son palabras* — they are words |

#### 9.3 Present-Tense Conjugation of *Estar*

*Estar* has an irregular *yo* form (*estoy*) and unusual stress — the written accent on *estás, está, están* marks stress on the final syllable, which is irregular for -ar verbs.

| Person | Form | Example in ESCore |
|---|---|---|
| yo | **estoy** | *estoy bien* — I am well |
| tú | **estás** | *estás lejos* — you are far |
| él/ella | **está** | *está aquí* — it is here |
| nosotros | **estamos** | *estamos dentro* — we are inside |
| ellos/ellas | **están** | *están cerca* — they are near |

#### 9.4 When to Use *Ser*: Predicate Types

Use *ser* when the predicate expresses something about the **essential nature, identity, or category** of the subject — the kind of thing it is, what it belongs to, who it fundamentally is.

**1. Category and type** (*qué tipo de cosa es* — what kind of thing it is):
- *Esto es algo bueno.* — This is something good.
- *Son palabras.* — They are words.
- *Es una parte del cuerpo.* — It is a part of the body.
- *¿Qué es esto?* — What is this?

**2. Identity** (equating the subject with itself or a description):
- *Soy yo.* — It is me. / I am I.
- *Eso es la verdad.* — That is the truth.
- *El mismo lugar es este.* — This is the same place.

**3. Ownership / origin** (what something belongs to):
- *Es mío.* — It is mine.
- *Es tuyo.* — It is yours.
- *Es de alguien.* — It belongs to someone.

**4. Material or composition** (what something is made of or composed of):
- *Es parte de algo grande.* — It is part of something big.

**5. Time expressions with clock/date** (outside core but noted for recognition):
- *Es el momento.* — It is the moment. (within core)

#### 9.5 When to Use *Estar*: Predicate Types

Use *estar* when the predicate expresses **where** the subject is or **how** it currently is — a location or a state that can change.

**1. Location** (where something physically is):
- *Está aquí.* — It is here.
- *Estamos dentro.* — We are inside.
- *¿Dónde está?* — Where is it?
- *Está lejos de este lugar.* — It is far from this place.

**2. Current condition or state** (how something is at this moment — can be different at another moment):
- *Estoy bien.* — I am well / I'm fine.
- *Está mal.* — It is wrong / He is unwell.
- *Se siente mal — está mal.* — He feels bad — he is unwell.

**3. Progressive (ongoing action)** — outside the core register's primary use but recognized:
- *Está pasando algo.* — Something is happening. (marginal in core)

#### 9.6 Cases That Seem Ambiguous

**"She is good" — *es buena* or *está bien*?**

Both are grammatical but mean different things:
- *Es buena.* — She is a good person (by nature). [*ser* — identity/character]
- *Está bien.* — She is well / She is fine (right now). [*estar* — current state]

This is not an edge case — it is the central difference in concentrated form. The English sentence "she is good" collapses a distinction that Spanish requires you to make.

**Locations of events vs. locations of things:**

Fixed locations of entities use *estar*: *el lugar está aquí* [the place is here]. But permanent, essential location in defining statements uses *ser*: this distinction rarely arises in the core register, where *estar* is used for all physical location.

**"Dead" and "alive":**

- *Está muerto.* — He is dead (current state, result of dying). [*estar*]
- *Está vivo.* — He is alive (current state). [*estar*]

These use *estar* because being dead or alive is treated grammatically as a state. This surprises English speakers who expect "is dead" to be an identity statement.

#### 9.7 Decision Flowchart

```
Is the predicate a LOCATION (where is it)?
  └─ YES → ESTAR: está aquí / está lejos / está dentro

Is the predicate a CURRENT STATE or CONDITION (how is it right now)?
  └─ YES → ESTAR: está bien / está mal / estoy cansado*

Is the predicate a CATEGORY, TYPE, or IDENTITY (what kind of thing is it)?
  └─ YES → SER: es algo bueno / es una parte / es mío / es la verdad

When in doubt about a descriptive predicate:
  → If it describes a CHANGEABLE CONDITION → ESTAR
  → If it describes a PERMANENT NATURE or CATEGORY → SER
```

*Outside core register but useful for recognition.

#### 9.8 Quick Contrast Drills

Each pair uses the same adjective or predicate with both verbs to show the contrast:

| *Ser* sentence | *Estar* sentence |
|---|---|
| *Es bueno.* — It is good (by nature). | *Está bien.* — It is well / fine (right now). |
| *Es malo.* — It is bad (in nature/kind). | *Está mal.* — It is wrong / not well (currently). |
| *Es grande.* — It is big (in size — inherent). | *Está grande.* — It has gotten big (has grown — change). |
| *Es aquí.* ✗ — ungrammatical | *Está aquí.* ✓ — It is here. |
| *Es mío.* — It is mine (ownership). | *Está conmigo.* — It is with me (location/proximity). |
| *Somos gente.* — We are people (identity). | *Estamos bien.* — We are fine (state). |

---

### Chapter 10 — The Present Tense (Active)

#### 10.1 The Present as the Core's Workhorse

The present tense in ESCore does more work than it does in full Spanish. In the core register it covers:

1. **Current states:** *sé esto* [I know this], *hay algo aquí* [there is something here]
2. **Habitual actions:** *la gente piensa esto* [people think this]
3. **Definitions and category statements:** *una parte es algo de un todo* [a part is something of a whole]
4. **Narrative sequences (including past events):** Spanish allows the "narrative present" to describe sequences of events — *algo pasa, alguien lo ve, dice algo* [something happens, someone sees it, they say something]. This is how the core handles event sequences that in English would use the past tense. It is not a workaround; it is a fully standard Spanish register used in storytelling.

The narrative present is what allows ESCore to operate without a past tense. A sequence of events can be described in full using present-tense verbs, and a fluent listener or reader understands the sequential interpretation from context and from the temporal adverbs (*antes, después, entonces*).

#### 10.2 The Regular Conjugation Engine

Spanish verbs belong to one of three classes, identified by the infinitive ending: *-ar*, *-er*, or *-ir*. The present tense is formed by removing the infinitive ending and adding person-number suffixes to the stem.

**Class I — *-ar* verbs** (model: *tocar* [to touch]):

| Person | Ending | Form | Example |
|---|---|---|---|
| yo | **-o** | *toco* | I touch |
| tú | **-as** | *tocas* | you touch |
| él/ella | **-a** | *toca* | he/she touches |
| nosotros | **-amos** | *tocamos* | we touch |
| ellos/ellas | **-an** | *tocan* | they touch |

**Class II — *-er* verbs** (model: *ver* is irregular; using *beber* [to drink] as regular example — but noting *ver* below; regular model *entender* outside core. For reference, here is the pattern):

| Person | Ending | Example (*saber*, irregular *yo*, but endings shown) |
|---|---|---|
| yo | **-o** | *-o* (but see irregular *yo* forms in Ch. 12) |
| tú | **-es** | *sabes* |
| él/ella | **-e** | *sabe* |
| nosotros | **-emos** | *sabemos* |
| ellos/ellas | **-en** | *saben* |

**Class III — *-ir* verbs** (model: *vivir* [to live]):

| Person | Ending | Form | Example |
|---|---|---|---|
| yo | **-o** | *vivo* | I live |
| tú | **-es** | *vives* | you live |
| él/ella | **-e** | *vive* | he/she lives |
| nosotros | **-imos** | *vivimos* | we live |
| ellos/ellas | **-en** | *viven* | they live |

**Key differences between the classes:**
- *tú* ending: *-ar* → **-as**; *-er/-ir* → **-es**
- *él/ella* ending: *-ar* → **-a**; *-er/-ir* → **-e**
- *nosotros* ending: *-ar* → **-amos**; *-er* → **-emos**; *-ir* → **-imos**
- *yo* ending is always **-o** for regular verbs in all three classes

The *ellos/ellas* ending is always **-an** for -ar verbs and **-en** for -er/-ir verbs.

#### 10.3 Regular Core Verbs: Full Paradigms

The ESCore verb inventory has only two fully regular prime-exponent verbs. Learn these paradigms as the template for the regular engine.

***Tocar*** [to touch — prime TOUCH]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *toco* | *tocas* | *toca* | *tocamos* | *tocan* |

***Vivir*** [to live — prime LIVE]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *vivo* | *vives* | *vive* | *vivimos* | *viven* |

***Pasar*** [to happen — prime HAPPEN, regular -ar]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *paso* | *pasas* | *pasa* | *pasamos* | *pasan* |

#### 10.4 The Pro-Drop Reminder

The person-number endings listed above are why subject pronouns are optional in Spanish (Chapter 7). Each ending uniquely identifies the person-number combination (with the caveat that *él/ella/usted* share the same third-person singular ending — which is why context or an explicit pronoun is needed when third-person is ambiguous). In practice, the learner should:
- Default to dropping *yo* in first-person statements: *sé esto*, not *yo sé esto*
- Include *él/ella* when the referent might be ambiguous
- Include *tú* in questions and direct address for clarity

#### 10.5 Temporal Adverbs That Anchor the Present Tense

Because the present tense carries narrative-past, habitual, and current-state meanings all at once, temporal adverbs are important for disambiguation. The following are all within the core register:

| Adverb | Meaning | Example |
|---|---|---|
| *ahora* | now, at this moment | *ahora sé esto* [now I know this] |
| *antes* | before (that), previously | *antes no sé esto* [before, I don't know this — narrative] |
| *después* | after (that), then | *después pasa algo malo* [after that, something bad happens] |
| *ya* | already, now (with new info) | *ya sé* [I already know / I get it now] |
| *siempre* | always | *siempre pasa esto* [this always happens] |
| *nunca* | never | *esto nunca pasa* [this never happens] |
| *entonces* | then, so (consequence) | *entonces digo algo* [so then I say something] |
| *en este momento* | at this moment | *en este momento no puedo* [at this moment I can't] |

---

### Chapter 11 — Reflexive Verbs

#### 11.1 What a Reflexive Verb Is

A reflexive verb is one where the subject and the grammatical object refer to the same entity — the subject is, in some sense, acting on itself or experiencing something within itself. In Spanish, reflexive verbs are marked by a reflexive pronoun (*me, te, se, nos*) that appears before the conjugated verb.

In the ESCore register, reflexives are not an edge case. They are the primary form for three major prime-exponent verbs (*moverse, sentirse*) and they appear constantly in the "something happens to someone" pattern. The learner cannot proceed far in the register without being fluent with reflexives.

#### 11.2 The Reflexive Pronoun Set (Review)

| Person | Reflexive pronoun | Example with *moverse* |
|---|---|---|
| yo | *me* | *me muevo* — I move |
| tú | *te* | *te mueves* — you move |
| él/ella | *se* | *se mueve* — he/she/it moves |
| nosotros | *nos* | *nos movemos* — we move |
| ellos/ellas | *se* | *se mueven* — they move |

The reflexive pronoun always precedes the conjugated verb in finite sentences. It may attach to the infinitive in modal constructions (see §11.5).

#### 11.3 Core Reflexive Verb Paradigms

***(Moverse)* — prime MOVE:**

*Moverse* is the prime exponent of MOVE. The stem-change o→ue applies in all stressed forms.

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *me muevo* | *te mueves* | *se mueve* | *nos movemos* | *se mueven* |

Note: *nosotros* has no stem change because the stress falls on the ending (-e**mos**), not the stem.

- *No me muevo.* — I don't move.
- *¿Por qué se mueve?* — Why does it move?
- *Algo se mueve dentro.* — Something moves inside.

***(Sentirse)* — prime FEEL:**

*Sentirse* is the reflexive form of *sentir*. Stem-change e→ie in stressed forms.

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *me siento* | *te sientes* | *se siente* | *nos sentimos* | *se sienten* |

- *Me siento bien.* — I feel good.
- *Se siente mal.* — He/she feels bad.
- *¿Cómo te sientes?* — How do you feel?
- *No sé cómo se siente.* — I don't know how he/she feels.

#### 11.4 The "Something Happens to Someone" Pattern

The construction *le pasa algo a alguien* is one of the most productive patterns in the core register. It uses the indirect object pronoun *le* (or *les* for plural) to mark the experiencer — the person to whom something happens.

**Structure:** [indirect object pronoun] + *pasar* (conjugated) + *algo/esto/nada*

| Spanish | English |
|---|---|
| *Me pasa algo.* | Something happens to me. |
| *¿Qué te pasa?* | What is happening to you? / What's wrong? |
| *Le pasa algo malo.* | Something bad happens to him/her. |
| *Nos pasa esto.* | This happens to us. |
| *Les pasa algo.* | Something happens to them. |

This pattern is essential for explicating experiences, sensations, events, and psychological states. Any explication that involves an entity undergoing something — rather than actively doing something — will likely use this construction.

#### 11.5 Pronoun Placement with Infinitives (Reflexive)

In Tier 2 and Tier 3 constructions (modal + infinitive, *ir a* + infinitive), the reflexive pronoun can either precede the auxiliary or attach to the end of the infinitive.

| Pre-auxiliary | Attached to infinitive | Meaning |
|---|---|---|
| *me puedo mover* | *puedo moverme* | I can move |
| *se quiere mover* | *quiere moverse* | he/she wants to move |
| *me voy a sentir bien* | *voy a sentirme bien* | I am going to feel well |
| *te vas a mover* | *vas a moverte* | you are going to move |

Both forms are grammatical. Attaching to the infinitive is the more standard written form and is preferred in explicating contexts.

#### 11.6 Other Reflexive Constructions in the Core

Several other verbs occur reflexively in the core register, even though their prime exponent is not strictly reflexive. These are conventional reflexive uses that the learner will encounter immediately.

| Reflexive form | Meaning | Example |
|---|---|---|
| *decirse* | to say to oneself | *me digo: esto es malo* — I say to myself: this is bad |
| *hacerse* | to become; to make oneself | *se hace grande* — it becomes big |
| *verse* | to see oneself; to appear | *se ve bien* — it looks good / he looks well |
| *saberse* | to know (something) within oneself | *se sabe que...* — it is known that... (impersonal) |

The impersonal *se* construction (*se sabe, se dice, se hace*) is worth noting as a productive pattern: *se* + third-person singular verb = "one does X / it is X-ed." This is how the core handles impersonal statements without a passive construction.

- *Se sabe que esto pasa.* — It is known that this happens.
- *Se dice que...* — It is said that... / People say that...
- *Así se hace.* — This is how it is done. / That's how you do it.

---

### Chapter 12 — The Irregular Core, as a Closed Set

This chapter presents the complete present-tense paradigms for every irregular prime-exponent verb in ESCore. They are organized by irregularity type so that the patterns are learnable. Learn the groups, not the individual forms, and each paradigm becomes a confirmation rather than a memorization.

#### 12.1 Group A — Fully Suppletive Verbs: *Ser* and *Ir*

These two verbs are so irregular that no pattern carries over from the infinitive. They must be learned whole. (The paradigm of *ser* was given in Chapter 9; it is repeated here for reference alongside *ir*.)

***Ser*** [to be — identity/nature]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *soy* | *eres* | *es* | *somos* | *son* |

***Ir*** [to go — support verb for future]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *voy* | *vas* | *va* | *vamos* | *van* |

Memory note for *ir*: The *tú* form *vas* rhymes with *más* [more]. The *nosotros* form *vamos* also serves as "let's go!" — a high-frequency utterance.

#### 12.2 Group B — Irregular *Yo* Only

In this group, the first-person singular form is irregular, but the remaining five forms follow regular -er or -ar endings from a predictable stem. Once you know the *yo* form and the stem, the rest follows the regular engine.

***Estar*** [to be — state/location] (Chapter 9 paradigm repeated; accent marks are part of the form):

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *estoy* | *estás* | *está* | *estamos* | *están* |

Stem for non-*yo* forms: *est-*. Endings are regular -ar endings but with accent on the final syllable (marked with written accent on *tú/él/ellos* forms).

***Hacer*** [to do/make — prime DO~MAKE]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *hago* | *haces* | *hace* | *hacemos* | *hacen* |

Irregular *yo*: *hago*. Remaining forms: stem *hac-* + regular -er endings.

***Ver*** [to see — prime SEE]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *veo* | *ves* | *ve* | *vemos* | *ven* |

Irregular *yo*: *veo*. Stem *v-* for non-*yo* forms is very short — shorter than expected from the infinitive *ver*.

***Saber*** [to know — prime KNOW]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *sé* | *sabes* | *sabe* | *sabemos* | *saben* |

Irregular *yo*: *sé*. ⚠ Written accent distinguishes *sé* [I know] from *se* [reflexive pronoun]. Remaining forms: stem *sab-* + regular -er endings.

***Dar*** [to give — support verb]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *doy* | *das* | *da* | *damos* | *dan* |

Irregular *yo*: *doy*. Unusually, *dar* is an -ar verb but takes -er/-ir endings in all non-*yo* forms (*das, da, dan* rather than the expected *-as, -a, -an* pattern — though in this case they overlap). The key irregularity is the *yo* form.

#### 12.3 Group C — Irregular *Yo* + Stem Change

These verbs have both an irregular *yo* form and a stem change in the remaining present-tense forms. The stem change follows the stressed-syllable rule: the stem vowel changes when the stress falls on it (all forms except *nosotros*).

***Tener*** [to have — prime HAVE]:
- Irregular *yo*: *tengo*
- Stem change e→ie in stressed forms

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *tengo* | *tienes* | *tiene* | *tenemos* | *tienen* |

- *Tengo algo.* — I have something.
- *¿Qué tienes?* — What do you have?
- *Tiene una parte.* — He/she has a part.
- *No tenemos mucho tiempo.* — We don't have much time.

***Decir*** [to say — prime SAY]:
- Irregular *yo*: *digo*
- Stem change e→i in stressed forms (note: *i*, not *ie* — this verb changes to *i*)

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *digo* | *dices* | *dice* | *decimos* | *dicen* |

- *Digo algo.* — I say something.
- *¿Qué dices?* — What are you saying?
- *Dice que sabe.* — He/she says that he/she knows.
- *Decimos la verdad.* — We tell the truth.

***Venir*** [to come — support for motion/source]:
- Irregular *yo*: *vengo*
- Stem change e→ie in stressed forms

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *vengo* | *vienes* | *viene* | *venimos* | *vienen* |

- *Vengo de ese lugar.* — I come from that place.
- *¿De dónde vienes?* — Where do you come from?
- *Algo viene de dentro.* — Something comes from inside.

***Oír*** [to hear — prime HEAR]:
- Irregular *yo*: *oigo*
- Unusual formation in all forms due to the vowel cluster

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *oigo* | *oyes* | *oye* | *oímos* | *oyen* |

*Oír* is the most unusual conjugation in the core. The *tú/él/ellos* forms insert a *y* between the stem vowel and the ending (*oy-es, oy-e, oy-en*). The *nosotros* form *oímos* retains the written accent on the *i* to indicate that *o-í-mos* is three syllables, not two.

- *Oigo algo.* — I hear something.
- *¿Oyes eso?* — Do you hear that?
- *Oye algo dentro.* — He/she hears something inside.

#### 12.4 Group D — Stem-Change e→ie (No Irregular *Yo*)

These verbs have a regular *yo* form (-o) but change the stem vowel e→ie in all forms where the stress falls on the stem (everything except *nosotros*).

***Querer*** [to want — prime WANT]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *quiero* | *quieres* | *quiere* | *queremos* | *quieren* |

- *Quiero saber esto.* — I want to know this.
- *¿Qué quieres?* — What do you want?
- *Quiere hacer algo.* — He/she wants to do something.
- *No queremos esto.* — We don't want this.

***Pensar*** [to think — prime THINK]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *pienso* | *piensas* | *piensa* | *pensamos* | *piensan* |

- *Pienso que esto es verdad.* — I think that this is true.
- *¿Qué piensas?* — What do you think?
- *Piensa en algo.* — He/she thinks about something.

***Sentir*** [to feel — prime FEEL] (non-reflexive base form; reflexive paradigm in Ch. 11):

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *siento* | *sientes* | *siente* | *sentimos* | *sienten* |

Note: *sentir* is an -ir verb; its stem change is e→ie in stressed positions and e→i in the *ellos* form of certain tenses (the latter is outside the core tense). In the present tense, all stressed forms are e→ie.

***Poder*** [can/be able to — prime CAN]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *puedo* | *puedes* | *puede* | *podemos* | *pueden* |

*Poder* has stem change o→ue (Group E, below), not e→ie. It is listed here as a cross-reference.

#### 12.5 Group E — Stem-Change o→ue

The o→ue stem change follows exactly the same stressed-syllable rule as e→ie: all forms except *nosotros* show the changed vowel.

***Poder*** [can/be able to — prime CAN]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *puedo* | *puedes* | *puede* | *podemos* | *pueden* |

- *Puedo decir esto.* — I can say this.
- *¿Puedes hacer algo?* — Can you do something?
- *No puede moverse.* — He/she can't move.
- *No podemos saber esto.* — We can't know this.

***Morir*** [to die — prime DIE]:

| yo | tú | él/ella | nosotros | ellos/ellas |
|---|---|---|---|---|
| *muero* | *mueres* | *muere* | *morimos* | *mueren* |

- *Todo muere.* — Everything dies.
- *No quiero morir.* — I don't want to die.

#### 12.6 Special Case: *Hay* (Existential *Haber*)

The existential *hay* [there is / there are] is the ESCore exponent of THERE IS~EXIST. It is the third-person singular present of *haber* used impersonally, but it functions as a completely invariable form in the core: it does not change for number, person, or gender.

- *Hay algo aquí.* — There is something here.
- *Hay muchas personas.* — There are many people.
- *No hay nada.* — There is nothing.
- *¿Hay alguien?* — Is there someone? / Is anyone there?
- *Hay un momento para esto.* — There is a moment for this.

⚠ *Hay* never agrees with the noun that follows it. ✗ *Han muchas personas* is wrong. The form is always *hay* regardless of whether what follows is singular or plural.

#### 12.7 The Irregular Core — Master Reference Table

| Verb | yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|---|
| *ser* | soy | eres | es | somos | son |
| *estar* | estoy | estás | está | estamos | están |
| *ir* | voy | vas | va | vamos | van |
| *tener* | tengo | tienes | tiene | tenemos | tienen |
| *hacer* | hago | haces | hace | hacemos | hacen |
| *decir* | digo | dices | dice | decimos | dicen |
| *ver* | veo | ves | ve | vemos | ven |
| *saber* | sé | sabes | sabe | sabemos | saben |
| *querer* | quiero | quieres | quiere | queremos | quieren |
| *poder* | puedo | puedes | puede | podemos | pueden |
| *oír* | oigo | oyes | oye | oímos | oyen |
| *venir* | vengo | vienes | viene | venimos | vienen |
| *dar* | doy | das | da | damos | dan |
| *pensar* | pienso | piensas | piensa | pensamos | piensan |
| *sentir* | siento | sientes | siente | sentimos | sienten |
| *morir* | muero | mueres | muere | morimos | mueren |
| *moverse* | me muevo | te mueves | se mueve | nos movemos | se mueven |
| *hay* | — | — | hay | — | — |

This table is the complete irregular core. Post it. Return to it. After a short period of regular use, the forms become automatic.

---

### Chapter 13 — Modal / Auxiliary Verbs and the Infinitive

#### 13.1 The Infinitive in ESCore

The infinitive is the citation form of the verb — the dictionary entry form ending in *-ar*, *-er*, or *-ir*. In full Spanish, the infinitive appears in many constructions. In ESCore, the infinitive appears in **exactly two licensed positions**:

1. After a modal verb (*poder, querer, deber*)
2. After *ir a* (the periphrastic future — Chapter 14)

In all other positions, a finite conjugated form is required. This restriction is what keeps the core register grammatically bounded.

#### 13.2 The Three Core Modals

***Poder + infinitive*** [can / be able to — prime CAN]:

This is the primary modal. It expresses ability, possibility, and permission.

| | Example | Meaning |
|---|---|---|
| Ability | *puedo hacer esto* | I can do this |
| Possibility | *puede pasar algo malo* | something bad can happen |
| Inability | *no puedo moverme* | I can't move |
| Question | *¿puedes decir algo?* | can you say something? |

The conjugation of *poder* follows the o→ue stem-change pattern (Chapter 12). The modal is conjugated for person; the following infinitive does not change.

***Querer + infinitive*** [want to — prime WANT]:

*Querer* followed by an infinitive expresses desire or intent.

| | Example | Meaning |
|---|---|---|
| Desire | *quiero saber esto* | I want to know this |
| Intent | *quiere hacer algo bueno* | he/she wants to do something good |
| Negated | *no quiero sentir esto* | I don't want to feel this |
| Question | *¿qué quieres decir?* | what do you want to say? / what do you mean? |

Note: *¿Qué quieres decir?* [What do you want to say? / What do you mean?] is an extremely high-frequency phrase in explicating conversations. The chatbot user will need this to ask for clarification.

***Deber + infinitive*** [should / must / ought to]:

*Deber* expresses obligation or strong expectation. It is not a prime exponent but is necessary for making normative statements in the core register.

| Person | Form |
|---|---|
| yo | *debo* |
| tú | *debes* |
| él/ella | *debe* |
| nosotros | *debemos* |
| ellos/ellas | *deben* |

*Deber* is a regular -er verb.

| | Example | Meaning |
|---|---|---|
| Obligation | *debo decir algo* | I must/should say something |
| Negated | *no debo hacer esto* | I shouldn't do this |
| Impersonal | *se debe hacer bien* | it should be done well / one should do it well |

#### 13.3 Negation with Modals

Negation in modal constructions is placed before the modal (before the conjugated verb), never between the modal and the infinitive.

| Correct | Wrong | Meaning |
|---|---|---|
| *no puedo hacer esto* | ✗ *puedo no hacer esto* | I can't do this |
| *no quiero decir nada* | ✗ *quiero no decir nada* | I don't want to say anything |
| *no debo moverme* | ✗ *debo no moverme* | I shouldn't move |

The exception is *querer no* (want not to), which is grammatical but shifts the meaning: *quiero no sentir esto* [I want to not feel this — I want the feeling to stop] vs. *no quiero sentir esto* [I don't want to feel this — I'd prefer not to]. In the core register the *no + modal* order covers most communicative needs.

#### 13.4 Object Pronoun Placement with Modals

When an object or reflexive pronoun accompanies a modal + infinitive construction, it may go in one of two positions (both grammatical, Chapter 11):

**Before the modal:**
- *lo puedo hacer* — I can do it
- *me quiero mover* — I want to move
- *te debo decir algo* — I should tell you something

**Attached to the infinitive:**
- *puedo hacerlo* — I can do it
- *quiero moverme* — I want to move
- *debo decirte algo* — I should tell you something

The attached-to-infinitive form is more common in written explicating; the pre-modal form is more common in spoken interaction. Both are within the core register.

#### 13.5 *Hay que + Infinitive* — Impersonal Obligation

The construction *hay que + infinitive* means "one must / it is necessary to." It uses the existential *hay* as the fixed impersonal auxiliary. It is invariable — no person or number agreement.

- *Hay que saber esto.* — One must know this. / You have to know this.
- *Hay que hacer algo.* — Something must be done. / One must do something.
- *No hay que decir nada.* — One need not say anything.

This construction is very productive in explicating because it expresses necessity without specifying who is under the obligation.

#### 13.6 *Tener que + Infinitive* — Personal Obligation

The construction *tener que + infinitive* means "to have to / to need to." Unlike *hay que*, it is conjugated for person through *tener*.

- *Tengo que saber esto.* — I have to know this.
- *Tienes que decir algo.* — You have to say something.
- *Tiene que pasar.* — It has to happen.
- *No tenemos que hacer nada.* — We don't have to do anything.

This is distinct from *deber* in that *tener que* expresses a concrete obligation (something you are required to do), while *deber* expresses a normative expectation (something you ought to do).

---

### Chapter 14 — Periphrastic Future ("Going-To")

#### 14.1 No Morphological Future in ESCore

Spanish has a morphological future tense (formed by adding endings to the infinitive: *hablaré, hablarás*...). It is entirely outside the ESCore register. The core uses one construction and one construction only to express futurity: **ir a + infinitive**, the periphrastic or "going-to" future.

This is not a significant restriction. The periphrastic future is:
- More frequent than the morphological future in everyday spoken Spanish
- More natural in the informal register of chatbot interaction
- Semantically equivalent for the purposes of the core — all future statements the learner needs to make can be expressed with *ir a + infinitive*

The morphological future and what it adds (including its use for epistemic modality: *serán las dos* — it must be two o'clock) are noted in Appendix B as out-of-register features.

#### 14.2 Structure of the Construction

**[conjugated *ir*] + *a* + [infinitive]**

The verb *ir* is conjugated for person and number (Chapter 12, Group A). The particle *a* is invariable. The infinitive does not change.

| Person | *Ir* form | + *a* + infinitive | Meaning |
|---|---|---|---|
| yo | *voy* | *voy a hacer algo* | I am going to do something |
| tú | *vas* | *vas a saber esto* | you are going to know this |
| él/ella | *va* | *va a pasar algo* | something is going to happen |
| nosotros | *vamos* | *vamos a decir la verdad* | we are going to tell the truth |
| ellos/ellas | *van* | *van a sentir algo* | they are going to feel something |

#### 14.3 Negative Future

Negation precedes the conjugated *ir*, not the infinitive.

- *No voy a hacer esto.* — I am not going to do this.
- *No va a pasar nada.* — Nothing is going to happen.
- *No vamos a saber nada.* — We are not going to know anything.

#### 14.4 Object Pronouns in the Future Construction

As with modals, object and reflexive pronouns may attach to the infinitive or precede *ir* — both positions are grammatical.

| Pre-verbal | Attached | Meaning |
|---|---|---|
| *lo voy a hacer* | *voy a hacerlo* | I am going to do it |
| *me voy a mover* | *voy a moverme* | I am going to move |
| *te voy a decir algo* | *voy a decirte algo* | I am going to tell you something |
| *se va a sentir bien* | *va a sentirse bien* | he/she is going to feel well |

#### 14.5 The Future in Explicating

In the core register, the periphrastic future serves to mark the later part of an "if-then" sequence and to describe what will happen when conditions are met.

- *Si haces esto, va a pasar algo bueno.* — If you do this, something good is going to happen.
- *Si alguien no sabe esto, no va a poder decirlo.* — If someone doesn't know this, they won't be able to say it.
- *Cuando lo sabes, vas a querer decírselo a alguien.* — When you know it, you are going to want to tell someone.

These "if-then" and "when-then" constructions are among the most important in the explicating register, because definitions frequently take the form: "when X happens, Y happens to someone; because of this, the person feels/wants/does Z."

#### 14.6 *Vamos a* as a Cohortative ("Let's")

The first-person plural *vamos a + infinitive* has a secondary use as a cohortative — an invitation to do something together.

- *Vamos a hacer algo.* — Let's do something. / We're going to do something.
- *Vamos a decir esto.* — Let's say this. / We're going to say this.

In chatbot interaction, this form can be used by either party to propose a direction: *vamos a pensar en esto* [let's think about this].

---

#### 14.7 Clitic Pronoun Placement — Complete Reference

Sections 11.5, 13.4, and 14.4 each touched on pronoun placement for a specific construction. This section unifies all those rules into one place, adds every core pronoun with extensive examples, and addresses the one irregular combination (double pronouns) that trips up even intermediate learners.

The subject is called **clitic pronoun placement** ("clitic" from Greek *klitikos*, "leaning" — these pronouns lean against the verb rather than standing alone). In everyday pedagogy it is simply called **pronoun placement**.

---

##### The Two Environments

**Environment 1 — Finite verb only (no following infinitive)**

When the verb is a conjugated form with no following infinitive, the pronoun can *only* go **immediately before the verb**. Attaching it after the verb is not grammatical in the present tense.

| Correct | ✗ Wrong | Meaning |
|---|---|---|
| *lo veo* | ✗ *veo lo* | I see it |
| *me siento bien* | ✗ *siento me bien* | I feel well |
| *te digo algo* | ✗ *digo te algo* | I tell you something |
| *le pasa algo* | ✗ *pasa le algo* | something happens to him/her |
| *nos movemos* | ✗ *movemos nos* | we move |
| *la conozco* | ✗ *conozco la* | I know her/it |
| *los veo* | ✗ *veo los* | I see them |
| *se dice que...* | ✗ *dice se que...* | it is said that... |

The rule: **pronoun immediately before the conjugated verb, never after it, never split from it.**

---

**Environment 2 — Infinitive construction (modal + inf, or *ir a* + inf)**

When a conjugated auxiliary (*poder, querer, deber, tener que, ir a*) precedes an infinitive, the pronoun has **two equally grammatical positions**:

- **Position A:** before the conjugated auxiliary
- **Position B:** attached to the end of the infinitive

Both are correct. The meaning does not change. Position A (*lo quiero hacer*) is more natural in fast speech. Position B (*quiero hacerlo*) is more standard in writing and explicating.

---

##### Pronoun-by-Pronoun Reference with Full Examples

---

**me — 1st person singular (reflexive, direct object, or indirect object)**

| Finite only | Position A (before aux) | Position B (on infinitive) | Meaning |
|---|---|---|---|
| *me muevo* | *me puedo mover* | *puedo moverme* | I can move |
| *me siento bien* | *me quiero sentir bien* | *quiero sentirme bien* | I want to feel well |
| *me voy a mover* | *me voy a mover* | *voy a moverme* | I am going to move |
| *me dice algo* | *me puede decir algo* | *puede decirme algo* | he/she can tell me something |
| *me va a decir algo* | *me va a decir algo* | *va a decirme algo* | he/she is going to tell me something |

---

**te — 2nd person singular (reflexive, direct object, or indirect object)**

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *te mueves* | *te puedes mover* | *puedes moverte* | you can move |
| *te veo* | *te puedo ver* | *puedo verte* | I can see you |
| *te digo algo* | *te quiero decir algo* | *quiero decirte algo* | I want to tell you something |
| *te voy a decir algo* | *te voy a decir algo* | *voy a decirte algo* | I am going to tell you something |
| *te va a pasar algo* | *te va a pasar algo* | *va a pasarte algo* | something is going to happen to you |

---

**lo — 3rd person masculine/neuter singular direct object ("it", "him", or a whole fact/statement)**

*Lo* is the single most frequent object pronoun in explicating because it stands for any previously mentioned thing, fact, claim, or statement — regardless of grammatical gender when referring to a concept.

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *lo veo* | *lo puedo ver* | *puedo verlo* | I can see it/him |
| *lo sé* | *lo puedo saber* | *puedo saberlo* | I can know it |
| *lo hago* | *lo quiero hacer* | *quiero hacerlo* | I want to do it |
| *lo digo* | *lo debo decir* | *debo decirlo* | I must say it |
| *lo entiendo* | *lo puedo entender* | *puedo entenderlo* | I can understand it |
| *lo voy a hacer* | *lo voy a hacer* | *voy a hacerlo* | I am going to do it |
| *lo voy a decir* | *lo voy a decir* | *voy a decirlo* | I am going to say it |
| *lo voy a saber* | *lo voy a saber* | *voy a saberlo* | I am going to know it |

---

**la — 3rd person feminine singular direct object ("her", "it" for feminine nouns)**

*La* agrees with feminine nouns: *la verdad* [truth], *una persona* [a person], *una cosa* [a thing].

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *la veo* | *la puedo ver* | *puedo verla* | I can see her/it |
| *la siento* | *la puedo sentir* | *puedo sentirla* | I can feel it (f.) |
| *la digo* | *la quiero decir* | *quiero decirla* | I want to say it (f.) |
| *la voy a conocer* | *la voy a conocer* | *voy a conocerla* | I am going to know her/it |
| *la voy a ver* | *la voy a ver* | *voy a verla* | I am going to see her/it |

---

**le — 3rd person singular indirect object ("to him", "to her", "to it")**

*Le* does not change for gender. It covers "to him" and "to her" equally. It marks the recipient or experiencer of an action.

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *le digo algo* | *le quiero decir algo* | *quiero decirle algo* | I want to tell him/her something |
| *le doy esto* | *le puedo dar esto* | *puedo darle esto* | I can give him/her this |
| *le pasa algo* | — | *va a pasarle algo* | something is going to happen to him/her |
| *le voy a decir algo* | *le voy a decir algo* | *voy a decirle algo* | I am going to tell him/her something |
| *le voy a dar esto* | *le voy a dar esto* | *voy a darle esto* | I am going to give him/her this |

---

**se — 3rd person reflexive (subject and object are the same person/thing)**

*Se* also functions as the impersonal pronoun ("one does X," "it is X-ed") and, critically, **replaces *le/les* when a direct object pronoun follows** (see Double Pronouns below).

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *se mueve* | *se puede mover* | *puede moverse* | he/she can move |
| *se siente bien* | *se quiere sentir bien* | *quiere sentirse bien* | he/she wants to feel well |
| *se va a mover* | *se va a mover* | *va a moverse* | he/she is going to move |
| *se dice que...* | — | — | it is said that... (impersonal, finite only) |
| *se hace así* | — | — | it is done this way (impersonal, finite only) |

---

**nos — 1st person plural (reflexive, direct object, or indirect object)**

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *nos movemos* | *nos podemos mover* | *podemos movernos* | we can move |
| *nos sentimos bien* | *nos queremos sentir bien* | *queremos sentirnos bien* | we want to feel well |
| *nos dice algo* | *nos puede decir algo* | *puede decirnos algo* | he/she can tell us something |
| *nos vamos a mover* | *nos vamos a mover* | *vamos a movernos* | we are going to move |
| *nos va a decir algo* | *nos va a decir algo* | *va a decirnos algo* | he/she is going to tell us something |

---

**los / las — 3rd person plural direct object**

*Los* for masculine or mixed groups; *las* for all-feminine groups.

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *los veo* | *los puedo ver* | *puedo verlos* | I can see them (m.) |
| *las veo* | *las puedo ver* | *puedo verlas* | I can see them (f.) |
| *los hago* | *los quiero hacer* | *quiero hacerlos* | I want to do them |
| *los voy a ver* | *los voy a ver* | *voy a verlos* | I am going to see them |
| *las voy a sentir* | *las voy a sentir* | *voy a sentirlas* | I am going to feel them |

---

**les — 3rd person plural indirect object ("to them")**

| Finite only | Position A | Position B | Meaning |
|---|---|---|---|
| *les digo algo* | *les quiero decir algo* | *quiero decirles algo* | I want to tell them something |
| *les doy esto* | *les puedo dar esto* | *puedo darles esto* | I can give them this |
| *les pasa algo* | — | *va a pasarles algo* | something is going to happen to them |
| *les voy a decir algo* | *les voy a decir algo* | *voy a decirles algo* | I am going to tell them something |

---

##### Double Pronouns: *le/les* + *lo/la/los/las* → *se* + *lo/la/los/las*

When an indirect object pronoun (*le* or *les*) and a direct object pronoun (*lo, la, los, las*) appear in the same clause, the indirect pronoun **must change to *se***. The forms *le lo*, *le la*, *les lo*, *les la* are ungrammatical in Spanish.

**Why it happens:** the sequence *le lo* is phonetically awkward (two *l*-sounds colliding), and Spanish resolved this long ago by replacing the indirect pronoun with *se* in this context only. The *se* here is not reflexive — it simply means "to him/her/them."

| Full noun version | With both pronouns (correct) | ✗ Ungrammatical |
|---|---|---|
| *Digo la verdad a él.* | *Se la digo.* | ✗ *Le la digo.* |
| *Doy esto a ella.* | *Se lo doy.* | ✗ *Le lo doy.* |
| *Digo algo a ellos.* | *Se lo digo.* | ✗ *Les lo digo.* |
| *Doy las cosas a ellos.* | *Se las doy.* | ✗ *Les las doy.* |

In infinitive constructions, the same substitution applies, and both positions remain available:

| Position A (before auxiliary) | Position B (on infinitive) | Meaning |
|---|---|---|
| *Se lo quiero decir.* | *Quiero decírselo.* | I want to tell it to him/her. |
| *Se lo voy a dar.* | *Voy a dárselo.* | I am going to give it to him/her. |
| *Se lo puedo hacer.* | *Puedo hacérselo.* | I can do it for him/her. |
| *Se lo voy a decir a ella.* | *Voy a decírselo a ella.* | I am going to tell it to her. |

**Accent rule:** When two pronouns attach to an infinitive, the original stress of the verb must be preserved with a written accent:
- *decir* → *decír* + *se* + *lo* → **decírselo**
- *dar* → *dár* + *se* + *lo* → **dárselo**
- *hacer* → *hacér* + *se* + *lo* → **hacérselo**
- *ver* → *vér* + *se* + *la* → **vérsela** (rare, but follows the same rule)

Count three syllables back from the end of the combined form — if the stress falls outside the last two syllables, add the accent.

---

##### Quick Decision Chart

**Step 1.** Is there an infinitive in the construction?
- **No** (plain present tense) → pronoun goes *immediately before the conjugated verb*. You are done.
- **Yes** (modal + inf or *ir a* + inf) → go to Step 2.

**Step 2.** Where do you want the pronoun?
- **Before the auxiliary** → place it right before the conjugated auxiliary (*lo puedo hacer, me voy a mover*). Done.
- **On the infinitive** → attach it to the end of the infinitive (*puedo hacerlo, voy a moverme*). Done.

**Step 3.** Are there two pronouns (one indirect, one direct)?
- **Yes** → if the indirect pronoun is *le* or *les*, change it to *se* first. Then apply Step 1 or Step 2 to the *se + lo/la* pair as a unit. If attaching both to an infinitive, add an accent to preserve the verb's stress.

---

*End of Part III. Part IV (The Sentence) begins with Chapter 15.*

---

## Part IV — The Sentence

The preceding parts built the vocabulary (Part I) and the morphology of nouns (Part II) and verbs (Part III). This part assembles those pieces into sentences — complete propositions that express a thought. The chapters here are shorter than the verb chapters, but they address the structures that appear in nearly every sentence: negation, questions, multi-clause combinations, prepositions under pressure, and word order. Mastery of Part IV is what turns a vocabulary list and paradigm table into actual communication.

---

### Chapter 15 — Negation

#### 15.1 The Core Negative: *No* Before the Verb

The prime NOT is expressed in Spanish by the adverb **no**, placed immediately before the conjugated verb. This is the one indispensable negation rule. Everything else in this chapter builds on it.

| Affirmative | Negative | Meaning |
|---|---|---|
| *Sé esto.* | *No sé esto.* | I don't know this. |
| *Hay algo aquí.* | *No hay nada aquí.* | There is nothing here. |
| *Se mueve.* | *No se mueve.* | It doesn't move. |
| *Puede hacer esto.* | *No puede hacer esto.* | He/she can't do this. |
| *Va a pasar algo.* | *No va a pasar nada.* | Nothing is going to happen. |

When the subject pronoun is present, *no* follows it and precedes the verb: *yo no sé, tú no puedes, él no viene*.

#### 15.2 Negation with Reflexives and Pronouns

When reflexive or object pronouns appear, *no* precedes the entire pronoun-plus-verb block. The pronoun is not separated from its verb.

| With reflexive | With object pronoun | Meaning |
|---|---|---|
| *No me muevo.* | *No lo veo.* | I don't move. / I don't see it. |
| *No se siente bien.* | *No la conozco.* | He/she doesn't feel well. |
| *No nos movemos.* | *No te digo nada.* | We don't move. / I say nothing to you. |

The sequence is always: **no → [pronoun(s)] → [verb]**. Never ✗ *me no muevo* or ✗ *lo no veo*.

#### 15.3 The Spanish Double Negative

Spanish requires negative concord: when a negative element (*nada, nadie, nunca*) follows the verb, the negative *no* must also appear before the verb. This is not redundancy — it is obligatory grammar.

| Negative word | Example | Meaning |
|---|---|---|
| *nada* [nothing] | *No sé nada.* | I know nothing / I don't know anything. |
| *nadie* [nobody] | *No veo a nadie.* | I see nobody / I don't see anyone. |
| *nunca* [never] | *No pasa nunca.* | It never happens. |
| *ninguno* [none] | *No hay ninguno.* | There are none. (outside core; noted for recognition) |

**Exception — pre-verbal negative word:** If the negative word is moved before the verb (for emphasis or literary effect), the *no* is dropped because the negative word itself is sufficient:

- *Nadie sabe esto.* — Nobody knows this. (emphatic, formal)
- *Nunca pasa.* — It never happens. (emphatic)
- *Nada pasa.* — Nothing happens. (emphatic)

In the conversational and explicating registers, the *no + verb + negative-word* order is the default.

#### 15.4 Negating the Infinitive

When the infinitive itself is negated (e.g., "the ability to not do something" or "wanting to not feel something"), *no* is placed immediately before the infinitive:

- *Quiero no saber esto.* — I want to not know this. (I want to be unaware of this.)
- *Puedo no decir nada.* — I can choose to say nothing.

This differs from the more common *no quiero saber esto* [I don't want to know this] — the position of *no* changes the scope of the negation.

In practice, in the core register the *no + modal* pattern (*no quiero, no puedo*) covers most communicative needs. The negated-infinitive construction is noted here because it arises in nuanced explicating.

#### 15.5 *No... sino* — Not X, But Rather Y

The construction *no... sino...* [not X, but rather Y] corrects a false proposition by substituting one element. It is stronger than *pero* [but] and is used specifically when the second clause replaces, rather than merely contrasts with, the first.

- *No es algo bueno, sino algo malo.* — It is not something good, but rather something bad.
- *No quiero esto, sino aquello.* — I don't want this, but rather that.
- *No pasa aquí, sino allí.* — It doesn't happen here, but rather there.

⚠ *Sino* (one word) is used after a negation to substitute a noun or adjective. *Si no* (two words) means "if not." These are different words: *sino* [but rather] vs. *si no* [if not / otherwise].

---

### Chapter 16 — Questions

#### 16.1 Two Ways to Ask a Question

Spanish has two question formation strategies, both fully available in the core register:

**1. Intonation questions:** The word order is identical to a statement; the question is signaled by rising intonation in speech and by question marks in writing. This is the simplest strategy.

- Statement: *Sabes esto.* — You know this.
- Question: *¿Sabes esto?* — Do you know this?
- Statement: *Hay algo aquí.* — There is something here.
- Question: *¿Hay algo aquí?* — Is there something here?

**2. Interrogative-word questions:** A wh-word (Chapter 2, §2.8) appears at the front of the sentence. The subject-verb order may invert (verb before subject), though inversion is not obligatory in all varieties.

- *¿Qué sabes?* — What do you know?
- *¿Quién está aquí?* — Who is here?
- *¿Dónde está esto?* — Where is this?

#### 16.2 The Accented Interrogatives — Contrast with Their Twins

Every interrogative word carries a written accent that its relative-pronoun or conjunction counterpart lacks. This is the most persistent accent error in the register and is treated here at length.

| Interrogative (question) | Relative/conjunction (not a question) | Contrast pair |
|---|---|---|
| *¿qué?* — what? | *que* — that, which | *¿Qué sabes?* vs. *Sé que estás aquí.* |
| *¿quién?* — who? | — (no unaccented twin) | *¿Quién dice esto?* |
| *¿cuándo?* — when? | *cuando* — when (conjunction) | *¿Cuándo pasa?* vs. *Pasa cuando quiero.* |
| *¿dónde?* — where? | *donde* — where (relative) | *¿Dónde está?* vs. *El lugar donde está.* |
| *¿cómo?* — how? | *como* — like, as (prime LIKE) | *¿Cómo se siente?* vs. *Se siente como algo bueno.* |
| *¿por qué?* — why? | *porque* — because (prime BECAUSE) | *¿Por qué dices esto?* vs. *Lo digo porque es verdad.* |
| *¿cuánto?* — how much/many? | *cuanto* — as much as | *¿Cuánto tiempo?* vs. rare in core |

The accent marks on interrogatives are obligatory in written Spanish. In chatbot exchanges, where typed Spanish is common, these accents are often omitted by native speakers, but the core register maintains them because they distinguish grammatical roles. A model prompted to the core register will use them.

#### 16.3 Common Question Patterns in the Core

The following question structures recur constantly in explicating conversations and should be internalized as units.

| Question | Meaning | Why it arises |
|---|---|---|
| *¿Qué es esto?* | What is this? | Asking for a category or type (*ser*) |
| *¿Qué significa esto?* | What does this mean? | Requesting an explication |
| *¿Qué quieres decir?* | What do you mean? | Asking for clarification |
| *¿Cómo se dice X?* | How do you say X? | Asking for the exponent of a concept |
| *¿Dónde está?* | Where is it? | Location (*estar*) |
| *¿Cómo te sientes?* | How do you feel? | State (*estar* + *sentir*) |
| *¿Qué sientes?* | What do you feel? | Content of feeling |
| *¿Qué pasa?* | What is happening? | Requesting event description |
| *¿Quién sabe esto?* | Who knows this? | Identifying a knower |
| *¿Por qué dices esto?* | Why do you say this? | Asking for reasoning |
| *¿Puedes decir más?* | Can you say more? | Requesting elaboration |
| *¿Es verdad esto?* | Is this true? | Verification question |

#### 16.4 The "What Is This?" Structure — A Common Error

The question *¿qué son las palabras?* [What are the words?] confuses learners because English uses "what are X" meaning "what do X mean" or "what is the category of X" — a category question that requires *ser*. The error is using *estar* instead.

| Correct | Wrong | Why |
|---|---|---|
| *¿Qué es esto?* | ✗ *¿Qué está esto?* | Category question → *ser* |
| *¿Qué son las palabras?* | ✗ *¿Qué están las palabras?* | Category question → *ser* |
| *¿Dónde está?* | ✗ *¿Dónde es?* | Location question → *estar* |

The rule from Chapter 9 applies directly: what something fundamentally *is* uses *ser*; where it *is* uses *estar*.

---

### Chapter 17 — Basic Clause Combination

#### 17.1 Coordination

The three coordinators (*y, o, pero*) connect clauses of equal grammatical status.

***Y*** [and] — joins elements that are both true simultaneously:
- *Pienso esto y digo algo.* — I think this and I say something.
- *Hay algo bueno y algo malo en esto.* — There is something good and something bad in this.
- *Sé lo que quiero y lo que no quiero.* — I know what I want and what I don't want.

***O*** [or] — presents alternatives:
- *Puedes quedarte aquí o moverte.* — You can stay here or move.
- *¿Es algo bueno o algo malo?* — Is it something good or something bad?
- *No sé si es esto o aquello.* — I don't know if it is this or that.

***Pero*** [but] — introduces a contrast or complication:
- *Quiero hacer esto, pero no puedo.* — I want to do this, but I can't.
- *Sé que pasa algo, pero no sé qué.* — I know that something is happening, but I don't know what.
- *Es algo bueno, pero también es algo pequeño.* — It is something good, but it is also something small.

#### 17.2 *Porque* vs. *Por Esto / Por Eso*

The prime BECAUSE has two distinct expressions in Spanish depending on whether what follows is a clause or a noun phrase:

***Porque*** [because — followed by a full clause with a conjugated verb]:
- *No puedo hacer esto porque no sé cómo.* — I can't do this because I don't know how.
- *Digo esto porque es verdad.* — I say this because it is true.
- *Se siente mal porque algo malo le pasa.* — He/she feels bad because something bad is happening to him/her.

***Por esto / por eso*** [because of this / therefore — followed by a noun phrase or standing alone]:
- *No sé esto. Por esto, no puedo decir nada.* — I don't know this. Because of this, I can't say anything.
- *Algo malo pasa; por eso quiero moverme.* — Something bad is happening; because of that, I want to move.
- *Por esto digo que es verdad.* — This is why I say it is true.

The practical rule: if you can follow it with a subject + verb, use *porque*. If you are pointing back to something already said, use *por esto/eso*.

#### 17.3 Conditional *Si* [If]

The prime IF is expressed by *si* (no accent). In the ESCore register, the conditional is restricted to the **present-tense conditional** — the simple "if X [present tense], Y [present tense]" pattern. The subjunctive conditional (*si tuvieras* — if you had) is outside the register.

**Structure:** *Si* + [present-tense clause], [present-tense consequence]

- *Si sabes esto, puedes decirlo.* — If you know this, you can say it.
- *Si algo malo pasa, alguien lo siente.* — If something bad happens, someone feels it.
- *Si quieres hacer algo bueno, hay que saber por qué.* — If you want to do something good, you have to know why.
- *Si no puedo moverme, alguien me tiene que ayudar.* — If I can't move, someone has to help me.

**Future consequence:** The consequence clause may use the periphrastic future:
- *Si haces esto, va a pasar algo.* — If you do this, something is going to happen.
- *Si no sabes esto, no vas a poder decirlo.* — If you don't know this, you won't be able to say it.

⚠ The *si* + present + consequence is a present-oriented conditional (a real possibility or general truth). It does not require the subjunctive, which is the key reason it fits within the core register.

#### 17.4 *Como* for Similarity and Manner

The prime LIKE~AS~WAY is expressed by *como* (no accent). It introduces similarity comparisons and manner clauses.

**Similarity:**
- *Es como algo bueno.* — It is like something good.
- *Se mueve como algo vivo.* — It moves like something alive.
- *Sé cómo se hace — es como esto.* — I know how it is done — it is like this.

**Manner clauses** (how something happens):
- *Lo hace como yo lo hago.* — He/she does it the way I do it.
- *Habla como alguien que sabe.* — He/she speaks like someone who knows.
- *Pasa como siempre.* — It happens the way it always does.

**Comparative equality** (*tan... como* — as... as):
- *Es tan grande como esto.* — It is as big as this.
- *Se siente tan mal como antes.* — He/she feels as bad as before.

#### 17.5 *Cuando* [When] — Temporal Clauses

The prime WHEN in its conjunctive use introduces temporal clauses. In the core register, the verb in the *cuando*-clause is always present tense (never subjunctive — that usage is outside register).

- *Cuando pasa algo malo, me muevo.* — When something bad happens, I move.
- *Cuando sé algo, lo digo.* — When I know something, I say it.
- *Cuando alguien quiere saber algo, tiene que preguntar.* — When someone wants to know something, they have to ask.
- *Cuando esto pasa, se siente algo dentro del cuerpo.* — When this happens, something is felt inside the body.

#### 17.6 Relative Clauses with *Que*

Relative clauses modify a noun by adding information about it. In Spanish, the relative pronoun is *que* (for both persons and things) in subject and direct-object positions.

**Structure:** [Noun] + *que* + [clause with verb]

- *algo que sé* — something that I know
- *una persona que dice la verdad* — a person who tells the truth
- *el lugar que veo* — the place that I see
- *palabras que tienen sentido* — words that have meaning
- *todo lo que sé* — everything that I know

**The *lo que* construction:** When the antecedent (the thing being modified) is a whole idea rather than a specific noun, use *lo que*:
- *Lo que dices es verdad.* — What you say is true.
- *No entiendo lo que pasa.* — I don't understand what is happening.
- *Esto es lo que quiero decir.* — This is what I want to say.

*Lo que* is among the most productive constructions in explicating because definitions frequently need to refer to "what X is" or "what happens when."

---

### Chapter 18 — Prepositional Patterns That Trip Learners

#### 18.1 *A* — Motion, Direction, and the Personal Object Marker

*A* has two distinct uses in the core register that require different explanations.

**Motion and direction** (toward a destination):
- *Voy a ese lugar.* — I go to that place.
- *Se mueve a un lado.* — It moves to one side.
- *Viene a este lugar.* — He/she comes to this place.

**The personal *a*** (before a direct object that is a specific person or *alguien*):

This use has no parallel in English and is purely a grammatical marker. It carries no meaning. It is required whenever the direct object of a verb is a person.

- *Veo a alguien.* — I see someone. (*a* required: object is a person)
- *Escucho a alguien.* — I hear someone. (*a* required)
- *Quiero a alguien.* — I love/want someone. (*a* required)
- *Veo algo.* — I see something. (no *a*: object is not a person)
- *Toco algo.* — I touch something. (no *a*: object is a thing)

⚠ When *alguien* is the subject (not the object), no *a*: *Alguien sabe esto.* [Someone knows this.] The personal *a* is only for objects.

#### 18.2 *De* — Possession, Origin, Composition, and Partitive

*De* is the most versatile preposition in Spanish. In the core register it serves four functions:

**Possession** (X of Y = Y's X):
- *la parte del cuerpo* — the part of the body (the body's part)
- *las palabras de alguien* — someone's words
- *el lado de este lugar* — this place's side

**Origin** (where something comes from):
- *viene de aquí* — he/she comes from here
- *es de ese lugar* — he/she is from that place

**Composition / categorization** (made of / consisting of / belonging to type):
- *algo de esto* — something of this / something from this
- *es de este tipo* — it is of this kind
- *es parte de algo grande* — it is part of something big

**Partitive** (some of a quantity — with *algo*):
- *algo de tiempo* — some time
- *algo de esto* — some of this

*De* + *el* always contracts to **del**: *parte del cuerpo, del mismo lado, del lugar*.

#### 18.3 *En* — Location and Temporal Setting

*En* expresses the location where something exists or the temporal setting in which something happens. It corresponds to English "in," "at," and "on" in location contexts.

**Location:**
- *está en ese lugar* — it is in/at that place
- *está en este lado* — it is on this side
- *hay algo en el cuerpo* — there is something in the body
- *estamos en el mismo lugar* — we are in the same place

**Time setting:**
- *en este momento* — at this moment
- *en poco tiempo* — in a short time
- *en un momento* — in a moment / just a moment

⚠ Location uses *estar + en*, not *ser + en*. ✗ *Es en ese lugar* is wrong. Location is always *estar*.

#### 18.4 *Con* — With, and Pronoun Fusions

*Con* [with] expresses accompaniment or instrument.

- *estoy aquí con alguien* — I am here with someone
- *lo hago con algo pequeño* — I do it with something small
- *habla con la verdad* — he/she speaks with truth / truthfully

**Pronoun fusions** (Chapter 2, §2.14):
- *con* + *mí* → **conmigo** — with me
- *con* + *ti* → **contigo** — with you
- *con* + *sí* → **consigo** — with himself/herself (rare in core)

These fusions are obligatory — ✗ *con mí* and ✗ *con ti* are ungrammatical.

#### 18.5 *Para* vs. *Por*

Both *para* and *por* can be translated as "for" in English, which is the source of persistent confusion. Their meanings in the core register are distinct.

***Para*** — purpose, intended recipient, direction toward a goal:
- *esto es para ti* — this is for you (recipient)
- *hago esto para saber más* — I do this (in order) to know more (purpose)
- *es bueno para alguien* — it is good for someone (benefit)

***Por*** — cause, reason, agent, passage through, in exchange for, duration:
- *por esto* — because of this (cause)
- *pasa por aquí* — it passes through here (passage)
- *por un tiempo* — for a time (duration)
- *lo hago por alguien* — I do it for someone's sake / on someone's behalf (agent of benefit)
- *lo sé por esto* — I know it because of this / through this

**The key distinction:** *para* faces toward the future (purpose, goal, recipient); *por* faces toward the cause or agent behind the action.

| *Para* (forward-facing) | *Por* (backward-facing) |
|---|---|
| *lo digo para que sepas* — I say it so that you know | *lo digo por esto* — I say it because of this |
| *es para ti* — it is for you (to have) | *lo hago por ti* — I do it for your sake |
| *voy para ese lugar* — I'm heading toward that place | *paso por ese lugar* — I pass through that place |

#### 18.6 *Sin* [Without] and *Sobre* [About / On Top Of]

***Sin*** + noun phrase or infinitive:
- *no puedo vivir sin esto* — I can't live without this
- *sin saber nada* — without knowing anything
- *algo sin nombre* — something without a name

***Sobre*** — primarily means "about" (topic) and "on top of" (surface location):
- *digo algo sobre esto* — I say something about this
- *pienso sobre esto* — I think about this
- *está sobre algo* — it is on top of something

⚠ *Sobre* meaning "about" (topic of speech or thought) is used in the core. *De* is used for possession and origin. These two do not substitute for each other: *hablo sobre la verdad* [I speak about the truth — topic] vs. *las palabras de alguien* [someone's words — possession].

---

### Chapter 19 — Word Order in the Core

#### 19.1 The Default: Subject — Verb — Object

Spanish has a default SVO (Subject-Verb-Object) word order that matches English and is the safest choice in the core register.

- *Alguien sabe esto.* — Someone knows this. [S-V-O]
- *Yo veo algo bueno.* — I see something good. [S-V-O]
- *La gente dice palabras.* — People say words. [S-V-O]
- *Algo pasa aquí.* — Something happens here. [S-V-Adverb]

The SVO order is not rigid in Spanish, but it is the unmarked default. Departures from SVO are possible and common, but they are stylistically marked — they signal emphasis, topic shift, or contrast. In the core register, the learner should default to SVO and treat other orders as things to recognize, not produce unpredictably.

#### 19.2 Subject-Verb Inversion

Spanish inverts subject and verb (V-S order) in several predictable contexts:

**After interrogative words:**
- *¿Qué dice alguien?* or *¿Qué dice?* — What does someone say? (verb often precedes subject)

**In sentences beginning with location or time adverbials:**
- *Aquí está algo.* — Here is something. (more natural than *Algo está aquí*)
- *Ahora pasa algo.* — Now something happens.

**With *hay*:**
- *Hay algo* is always verb-first because *hay* is itself the verb: *Hay algo aquí* [There is something here], never ✗ *Algo hay aquí* (possible but emphatic).

**For emphasis on the subject:**
- *Lo hace ella, no yo.* — She does it, not me. (subject moved to after verb for contrast)

#### 19.3 Topicalization — Moving an Element to Front Position

Any element can be moved to the front of the sentence to signal that it is the topic — the thing the sentence is about. When this is done, the original position is often left empty (for pronouns) or repeated with a pronoun.

- *Esto, yo no lo sé.* — This (topic), I don't know it.
- *A alguien bueno, siempre le pasa algo malo.* — To a good person, something bad always happens.
- *Eso que dices — no es verdad.* — What you say — it is not true.

Topicalization is common in spoken registers and will appear in chatbot output. Recognizing it is more important than producing it in the early stages.

#### 19.4 Adjective and Adverb Placement Summary

This restates the rules from Chapters 6 and 10 in a single reference.

**Adjectives:**
- Descriptive adjectives (*bueno, malo, grande, pequeño*): **after the noun** by default — *algo bueno, un lugar grande*
- Quantifying and identifying adjectives (*mucho, poco, todo, otro, mismo, algunos*): **before the noun** — *muchas palabras, todo el tiempo, otro lugar*
- Short forms *buen/mal/gran*: before the noun when the adjective precedes — *un buen momento* — but only when the speaker chooses pre-nominal position (which the core mostly avoids for descriptives)

**Adverbs:**
- Adverbs of manner (*bien, mal, así*): immediately after the verb or at the end of the clause — *lo hace bien, se siente mal*
- Adverbs of time and place (*ahora, antes, aquí, lejos*): freely placed at the beginning or end of the clause — *ahora sé esto* / *sé esto ahora*; *aquí pasa algo* / *pasa algo aquí*
- *No* (negation): always immediately before the verb — *no sé, no puedo hacer esto*

#### 19.5 Relative Clause Placement

A relative clause modifying a noun immediately follows that noun.

- *la parte del cuerpo **que se mueve*** — the part of the body that moves
- *algo **que quiero saber*** — something that I want to know
- *un lugar **donde alguien puede vivir bien*** — a place where someone can live well

A relative clause never separates an article from its noun:
- ✗ *el que se mueve parte* — ungrammatical
- ✓ *la parte que se mueve* — correct

#### 19.6 The Placement of *También*, *Tampoco*, *Solo*, *Siempre*, *Nunca*, *Ya*

These high-frequency discourse adverbs have conventional positions worth noting explicitly.

| Adverb | Typical position | Example |
|---|---|---|
| *también* [also] | before verb or at end | *también sé esto / sé esto también* |
| *tampoco* [neither] | before verb | *tampoco sé nada* |
| *solo / solamente* [only] | before the element it modifies | *solo quiero esto / quiero solo esto* |
| *siempre* [always] | before verb or at end | *siempre pasa / pasa siempre* |
| *nunca* [never] | before verb (or after *no*) | *nunca pasa / no pasa nunca* |
| *ya* [already/now] | before verb | *ya sé esto* |

When *nunca* or *tampoco* precedes the verb, the *no* is dropped (since the negative word is already present). When they follow the verb, *no* must appear before the verb.

---

*End of Part IV. Part V (Reference and Author's Apparatus) begins with Chapter 20.*

---

## Part V — Reference and Author's Apparatus

Part V does not introduce new grammar. It consolidates what has been taught, catalogues the errors that appear most often in practice, provides guidance for the content author, and maps the boundaries of the register. The learner returning to check a paradigm or verify a rule will use Part V constantly. The author constraining an LLM to the core register will use Chapter 22 and the appendices as a specification document.

---

### Chapter 20 — The Complete Core Paradigm Tables

This chapter collects every conjugation table from Parts II–III in one place for reference. No new information is introduced.

#### 20.1 *Ser* and *Estar* — The BE Allolexes

| | *ser* | *estar* |
|---|---|---|
| yo | *soy* | *estoy* |
| tú | *eres* | *estás* |
| él/ella | *es* | *está* |
| nosotros | *somos* | *estamos* |
| ellos/ellas | *son* | *están* |

**ser** → identity, category, nature, ownership
**estar** → location, current condition, state

#### 20.2 Regular Verb Paradigms

**-ar (model: *tocar*):**

| yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|
| *toco* | *tocas* | *toca* | *tocamos* | *tocan* |

**-er (model: *saber*, irregular *yo* shown; regular -er endings for tú–ellos):**

| yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|
| *sé* | *sabes* | *sabe* | *sabemos* | *saben* |

Regular -er endings: tú **-es**, él **-e**, nosotros **-emos**, ellos **-en**

**-ir (model: *vivir*):**

| yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|
| *vivo* | *vives* | *vive* | *vivimos* | *viven* |

Regular -ir endings: tú **-es**, él **-e**, nosotros **-imos**, ellos **-en**

#### 20.3 All Irregular Core Verbs — Complete Present-Tense Reference

| Verb | yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|---|
| *ser* | soy | eres | es | somos | son |
| *estar* | estoy | estás | está | estamos | están |
| *ir* | voy | vas | va | vamos | van |
| *tener* | tengo | tienes | tiene | tenemos | tienen |
| *hacer* | hago | haces | hace | hacemos | hacen |
| *decir* | digo | dices | dice | decimos | dicen |
| *ver* | veo | ves | ve | vemos | ven |
| *saber* | sé | sabes | sabe | sabemos | saben |
| *querer* | quiero | quieres | quiere | queremos | quieren |
| *poder* | puedo | puedes | puede | podemos | pueden |
| *oír* | oigo | oyes | oye | oímos | oyen |
| *venir* | vengo | vienes | viene | venimos | vienen |
| *dar* | doy | das | da | damos | dan |
| *pensar* | pienso | piensas | piensa | pensamos | piensan |
| *sentir* | siento | sientes | siente | sentimos | sienten |
| *morir* | muero | mueres | muere | morimos | mueren |

#### 20.4 Reflexive Model Verbs

***Moverse* (o→ue stem change):**

| yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|
| *me muevo* | *te mueves* | *se mueve* | *nos movemos* | *se mueven* |

***Sentirse* (e→ie stem change):**

| yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|
| *me siento* | *te sientes* | *se siente* | *nos sentimos* | *se sienten* |

#### 20.5 Modal Constructions — Quick Reference

| Modal | yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|---|
| *poder* + inf. | *puedo* | *puedes* | *puede* | *podemos* | *pueden* |
| *querer* + inf. | *quiero* | *quieres* | *quiere* | *queremos* | *quieren* |
| *deber* + inf. | *debo* | *debes* | *debe* | *debemos* | *deben* |
| *ir a* + inf. | *voy a* | *vas a* | *va a* | *vamos a* | *van a* |
| *hay que* + inf. | — | — | *hay que* | — | — |
| *tener que* + inf. | *tengo que* | *tienes que* | *tiene que* | *tenemos que* | *tienen que* |

#### 20.6 Pronoun Reference Tables

**Subject pronouns:**

| Person | Pronoun |
|---|---|
| 1st sing. | *yo* |
| 2nd sing. | *tú* |
| 3rd sing. masc. | *él* |
| 3rd sing. fem. | *ella* |
| 1st pl. | *nosotros / nosotras* |
| 3rd pl. masc. | *ellos* |
| 3rd pl. fem. | *ellas* |

**Object pronoun placement:** before conjugated verb, or attached to infinitive.

| Function | yo | tú | él/ella | nosotros | ellos |
|---|---|---|---|---|---|
| Reflexive | *me* | *te* | *se* | *nos* | *se* |
| Indirect (to/for) | *me* | *te* | *le* | *nos* | *les* |
| Direct masc. | *me* | *te* | *lo* | *nos* | *los* |
| Direct fem. | *me* | *te* | *la* | *nos* | *las* |

---

### Chapter 21 — High-Frequency Error Catalogue

This chapter documents the errors that appear most reliably when learners and LLMs operate in the ESCore register. Each entry gives the wrong form, the right form, and the rule that resolves it.

---

**Error 1: *mi* vs. *mí***

| Wrong | Right | Rule |
|---|---|---|
| *para mi* | *para mí* | After a preposition, "me" is *mí* (accent). *mi* without accent = "my". |
| *esto es de mi* | *esto es de mí* / *esto es mío* | Same rule. Possessive after *ser* uses the long form *mío*. |

---

**Error 2: *si* vs. *sí***

| Wrong | Right | Rule |
|---|---|---|
| *si, sé esto* | *sí, sé esto* | "Yes" = *sí* (accent). "If" = *si* (no accent). |
| *sí haces esto...* | *si haces esto...* | The conditional conjunction "if" never has an accent. |

---

**Error 3: *el* vs. *él***

| Wrong | Right | Rule |
|---|---|---|
| *el viene* | *él viene* | "He" = *él* (accent). "The" = *el* (no accent). |
| *él cuerpo* | *el cuerpo* | The article "the" never has an accent. |

---

**Error 4: *tu* vs. *tú***

| Wrong | Right | Rule |
|---|---|---|
| *tu sabes esto* | *tú sabes esto* | "You" (subject) = *tú* (accent). "Your" = *tu* (no accent). |
| *tú cuerpo* | *tu cuerpo* | "Your" (possessive adjective) never has an accent. |

---

**Error 5: *se* vs. *sé***

| Wrong | Right | Rule |
|---|---|---|
| *se que pasa algo* | *sé que pasa algo* | "I know" = *sé* (accent). The reflexive pronoun = *se* (no accent). |
| *sé mueve* | *se mueve* | The reflexive pronoun "se" never has an accent. |

---

**Error 6: *que* vs. *qué***

| Wrong | Right | Rule |
|---|---|---|
| *¿que es esto?* | *¿qué es esto?* | Interrogative "what" = *qué* (accent). Complementizer "that/which" = *que* (no accent). |
| *sé qué pasa* | *sé que pasa* | After a declarative verb (*saber, pensar, decir*), "that" = *que* (no accent). |

---

**Error 7: Ser vs. Estar — Category vs. Location**

| Wrong | Right | Rule |
|---|---|---|
| *¿dónde es?* | *¿dónde está?* | Location always uses *estar*. |
| *estoy alguien* | *soy alguien* | Identity/category always uses *ser*. |
| *estoy bien persona* | *soy una buena persona* | Character/essential nature uses *ser*. |

---

**Error 8: Ser vs. Estar — Bueno/Bien and Malo/Mal**

| Wrong | Right | Rule |
|---|---|---|
| *estoy bueno* (intended: I'm well) | *estoy bien* | With *estar* (current state), use the adverb *bien/mal*. |
| *es bien* | *es bueno* | With *ser* (nature), use the adjective *bueno/malo*. |
| *se siente bueno* | *se siente bien* | *Sentirse* (a state verb) takes *bien/mal*. |

---

**Error 9: Adjective Position — Post-Nominal Default**

| Wrong | Right | Rule |
|---|---|---|
| *una buena cosa* | *una cosa buena* | Descriptive adjectives follow the noun by default. |
| *algo malo* ✓ | *algo malo* ✓ | After *algo/nada*, the adjective follows (this is correct). |
| *muchas buenas palabras* | *muchas palabras buenas* | Even with quantifiers, the descriptive adjective stays after the noun. |

---

**Error 10: Modal + Infinitive vs. Doubled Finite Verb**

| Wrong | Right | Rule |
|---|---|---|
| *puedo sé esto* | *puedo saber esto* | After a modal, the dependent verb must be an infinitive, not a conjugated form. |
| *quiero hago algo* | *quiero hacer algo* | Same rule — the second verb is always the infinitive. |
| *voy a sé* | *voy a saber* | The periphrastic future requires the infinitive after *a*. |

---

**Error 11: Missing Reflexive Pronoun**

| Wrong | Right | Rule |
|---|---|---|
| *muevo* (intended: I move) | *me muevo* | *Moverse* is reflexive; the pronoun is part of the verb. |
| *siente bien* (intended: he/she feels good) | *se siente bien* | *Sentirse* is reflexive in the "feel" sense. |
| *¿cómo sientes?* | *¿cómo te sientes?* | The reflexive pronoun must match the subject. |

---

**Error 12: *Porque* vs. *Por qué* vs. *El porqué***

| Form | Use | Example |
|---|---|---|
| *porque* (one word, no accent) | conjunction "because" | *lo digo porque es verdad* |
| *¿por qué?* (two words, accent on *qué*) | interrogative "why?" | *¿por qué lo dices?* |
| *el porqué* (one word, accent, with article) | noun "the reason" | *quiero saber el porqué* |

---

**Error 13: *Sino* vs. *Si No***

| Wrong | Right | Rule |
|---|---|---|
| *no es bueno, si no malo* | *no es bueno, sino malo* | After negation, "but rather" = *sino* (one word). |
| *sino sabes...* | *si no sabes...* | "If not" = *si no* (two words). |

---

**Error 14: *Hay* Agreement Error**

| Wrong | Right | Rule |
|---|---|---|
| *han muchas personas* | *hay muchas personas* | *Hay* is invariable — never changes for number. |
| *hay unos* (meaning: there exist some) | *hay algunos* | *Hay* can precede any quantifier; the quantifier agrees with the noun. |

---

**Error 15: Dropping the Complementizer *Que***

| Wrong | Right | Rule |
|---|---|---|
| *sé esto es verdad* | *sé que esto es verdad* | Spanish never drops *que* before a complement clause, unlike English dropping "that". |
| *pienso es bueno* | *pienso que es bueno* | Same rule after all mental and speech predicates. |
| *dice está aquí* | *dice que está aquí* | Same rule after *decir*. |

---

### Chapter 22 — Notes for the Content Author

This chapter is written for the person who is setting up a language model to converse in ESCore — either as a teaching interlocutor or as a controlled-vocabulary generation system. It translates the grammar of this book into operational constraints.

#### 22.1 What the Register Is, in Constraint Form

A text is within the ESCore register if and only if it satisfies all of the following:

1. **Lexical:** Every content word in the text is a prime exponent from Chapter 1 or a sanctioned support item from Chapter 2. No word outside those lists appears.

2. **Tense:** All finite verbs are in the present tense. No preterite, imperfect, conditional, or future morphological forms appear.

3. **Mood:** All verbs are in the indicative mood. No subjunctive forms appear.

4. **Infinitive restriction:** Infinitives appear only as the second element in a modal + infinitive construction (*poder/querer/deber/tener que/hay que + inf.*) or as the second element in a periphrastic future (*ir a + inf.*).

5. **Voice:** Active voice only. No passive *ser + past participle* constructions appear.

6. **Compound tenses:** None. No *haber* + past participle (*ha dicho, ha pasado*) constructions appear.

7. **Agreement:** All noun-adjective and noun-article agreement is maintained correctly.

#### 22.2 The Lemma Allow-Set

The following is the complete list of lemmas (dictionary-entry forms) sanctioned in the core tier. For generation purposes, a word is out of register if its lemma does not appear in this list.

**Prime exponent lemmas (65):**
*yo, tú, alguien, algo, gente, cuerpo, parte, tipo, clase, este, mismo, otro, uno, dos, algunos, mucho, poco, todo, bueno, malo, grande, pequeño, pensar, saber, querer, sentir, ver, oír, decir, palabra, verdad, hacer, pasar, moverse, tocar, haber, ser, estar, tener, vivir, morir, cuando, tiempo, ahora, antes, después, momento, donde, lugar, aquí, arriba, abajo, lejos, cerca, lado, dentro, no, quizá, poder, porque, si, muy, más, como, mío*

**Support lemmas (~45):**
*el, la, los, las, un, una, a, de, en, con, para, por, sin, sobre, y, o, pero, que, él, ella, nosotros, ellos, me, te, se, le, lo, nos, les, ese, aquel, mi, tu, su, nuestro, tuyo, suyo, conmigo, contigo, sí, también, tampoco, ya, aún, todavía, siempre, nunca, así, entonces, solo, nada, nadie, qué, quién, cuándo, dónde, cómo, cuánto, ir, del, al, bien, mal, cosa, persona, deber*

**Note on surface forms vs. lemmas:** The lemma *mucho* covers *mucho/mucha/muchos/muchas*; *bueno* covers *bueno/buena/buenos/buenas/buen*; *ir* covers *voy/vas/va/vamos/van*; etc. An OOV (out-of-vocabulary) checker should lemmatize before checking.

#### 22.3 Expressing the Register as Generation Rules

If you are writing a system prompt for an LLM:

> *"Respond only in present-tense active Spanish. Use only the vocabulary from the NSM-Spanish prime list and its grammatical support words. Do not use the past tense, subjunctive, conditional, or passive voice. Infinitives may appear only after poder, querer, deber, tener que, hay que, and ir a. If you need to refer to a past event, use the narrative present."*

For stricter enforcement, add:

> *"If a concept requires a word outside the allowed vocabulary, explicate it using allowed words rather than introducing the out-of-register word. Do not apologize for restrictions; work within them naturally."*

#### 22.4 Proper Noun Handling

Proper nouns (names of people, places) are not in the prime list but are permitted in the core register because they carry no semantics that require explication — they are pure labels. A model in the ESCore register may freely use proper nouns as subjects, objects, and locatives. The AVD (average vocabulary diversity) scorer should treat proper nouns as zero-cost additions, not OOV violations.

#### 22.5 The Tense/Register Boundary Table

| Feature | ESCore register | Out of register |
|---|---|---|
| Present indicative | ✓ | — |
| Narrative present (for past events) | ✓ | — |
| *Ir a + infinitive* future | ✓ | — |
| Modal + infinitive | ✓ | — |
| Preterite (past tense) | ✗ | flagged in Appendix B |
| Imperfect | ✗ | flagged in Appendix B |
| Present subjunctive | ✗ | flagged in Appendix B |
| Conditional | ✗ | flagged in Appendix B |
| Morphological future | ✗ | flagged in Appendix B |
| Passive (*ser* + past participle) | ✗ | flagged in Appendix B |
| Present perfect (*haber* + pp.) | ✗ | flagged in Appendix B |

#### 22.6 The Explication Loop

The intended workflow for the content author is:

1. **Core input:** The learner writes or receives a sentence in ESCore.
2. **Out-of-register word appears:** Either the learner encounters a word they do not know, or they want to understand a concept outside the prime list.
3. **Request for explication:** The learner asks *¿qué es X?* or *¿qué significa X?* (using the interrogative form from Chapter 16).
4. **LLM produces explication:** The model generates a definition of X using only core vocabulary — a mini-NSM explication in Spanish.
5. **Learner processes the explication:** The definition itself is in the learnable register, so the learner can parse it. The meaning is acquired inductively from within the language.

This loop is the operational proof of concept. Every cycle of the loop is simultaneously a language lesson, a semantic analysis, and a demonstration that the prime vocabulary is sufficient for meaning-description.

#### 22.7 Two Tiers: The Core as Anchor, Not Boundary

The constraints in §22.1 define the **anchor tier** — the strict prime register. That tier is the right target for the explication loop and for an LLM interlocutor whose job is to *stay inside* the primes. But it is the wrong target for **story** content intended as comprehensible-input reading or listening (the kind published to a learner audience).

For narrative, ESCore is the **anchor the story revolves around — not the fence that bounds it.** The core must carry the semantic spine: the load-bearing meanings, the connective tissue, the repeated frame sentences should all be prime vocabulary. But a story may spend a budgeted layer of *out-of-core but high-transparency* words on top of that spine. This is the **story tier**, or **ESCore+1**, in the sense of Krashen's *i+1*: comprehensible input is input that is mostly known, with a thin margin of the new. A register with *zero* margin cannot advance the learner from ultra-basic toward merely-simple Spanish; the +1 is the mechanism of advancement, not a contamination of the core.

The design rule that follows: **do not bend over backwards with strained explications for words that are knowable from context.** If a word's meaning is recoverable from the surrounding text (and, for video, the illustration), forcing it into a five-clause prime paraphrase makes the prose *worse*, not purer. Spend explication effort only where context cannot do the work.

#### 22.8 The Three Buckets of "Out of Core"

Not every out-of-core word costs the reader the same. A raw out-of-register percentage is misleading because it counts very different things as equal. Decompose every out-of-core token into one of three buckets (proper nouns are a free fourth category, per §22.4):

| Bucket | What it is | Reader cost | Story-tier policy |
|---|---|---|---|
| **A — Inflectional** | A non-present form (preterite, imperfect, perfect, fixed-frame subjunctive) of a verb whose **lemma is already in the core** — *hizo* (hacer), *era* (ser), *vino* (venir), *sepas* (saber) | Near zero — the concept is known; only the tense form is new, and it is recognised, not decoded | Permitted in narrative (see §22.10) |
| **B — Transparent concrete** | An ultra-high-frequency concrete noun that is outside the *prime* core only because it is not a *prime* — *agua, niño, noche, fuego, mujer, ojos, casa, sol* | Very low — week-one vocabulary, instantly anchored by context and image | Freely allowed within budget |
| **C — New lexeme** | A genuinely new content verb or abstract noun not in the core — *escuchar, caminar, sostener, jalar, sentimiento, oscuridad* | Real but modest — this is the true *+1* lexical load | Rationed; tracked in the story's local whitelist |

The empirical case study behind this table is the *La Llorona* text. Of ~2,167 tokens, a flat audit flags ~28% as out-of-core — an alarming figure. Decomposed, the great majority is Bucket A (tense forms of core verbs) and Bucket B (transparent nouns); genuinely new lexemes (Bucket C) are on the order of **1 in 25–30 tokens**. The text reads as no harder than a strict-core story, yet is markedly warmer and more natural. *That* is the +1 working as intended: same comprehensibility, more expressiveness.

The lesson for the audit and the author: **measure Bucket C, not the flat percentage.** Buckets A and B are the productive margin; Bucket C is the thing to keep on a budget.

#### 22.9 The Contextual-Learnability Test (the *Lingua Latina* Principle)

Hans Ørberg's *Lingua Latina per se Illustrata* taught an entire language with no glosses, because every new word was introduced in a context that *forced* its meaning. That is the standard to aim for, as closely as a living project can.

A new (Bucket B or C) word may enter the story tier **without explication** if it passes the contextual-learnability test: a reader who does not know the word can recover its meaning from the text itself within a sentence or two. Mere mention is not enough:

> *"Jim toma una manzana."* — On its own, *manzana* is unrecoverable. The reader learns only that it is a takeable thing.
> *"Jim toma una manzana. Piensa en comerla. Tiene hambre."* — Now *manzana* is constrained to *an edible thing one eats when hungry.* The word has taught itself.

Practical checklist for admitting a new word into a story:

1. **Is it Bucket A or B?** If so, it is almost always self-evident; admit it.
2. **If Bucket C, is it constrained by its neighbours?** Look for a following sentence that says what one *does* with it, what it *is like*, or what *happens* to it. If none exists, either add one or cut the word.
3. **Does repetition reinforce it?** A new word used once and dropped is a vocabulary tax; a new word echoed across the scene becomes anchored. Prefer the latter.
4. **For video: does the illustration disambiguate it?** A picture of fire makes *fuego* free. Lean on this, but do not rely on it for words that also need to work in audio-only listening.

The author's posture is to be **as cognisant of every new word as Ørberg was** — to know, for each non-core word, exactly *how* the reader is expected to acquire it. A new word with no acquisition path is a defect, even if it is "simple."

#### 22.10 Frozen Frames: Narrative Past and Fixed-Frame Subjunctive

Two grammatical features barred from the anchor tier are admitted to the **story tier** as *frozen frames* — high-frequency strings processed holistically by even beginning listeners, not as productive morphology:

- **Narrative past.** A legend or recounted story may be told in the past (*había una mujer… vino un hombre… los dos tuvieron niños*). The preterite/imperfect of core verbs is Bucket A: recognised, not decoded. The present-tense framing sentences ("Quiero que sepas una cosa…", "Escucha eso…") keep the listener anchored.
- **Fixed-frame subjunctive.** A small set of canonical frames may appear:
  - *quiero que + [subj.]* — *Quiero que sepas una cosa.*
  - *hace/hizo que + [subj.]* — *Hizo que él la mirara.*
  - *antes de que + [subj.]* — *Antes de que salga el sol.*
  - *hasta que + [subj.]* — *No pares hasta que los encuentres.*

These are among the most frequent strings in spoken Spanish; a learner receives them whole. Notably, the canonical *Quiero que sepas* is *more* natural to a Spanish-tuned ear than the strict-core workaround *Quiero esto: tú sabes…* — so in the story tier the frame is preferred. The frames remain **out of the anchor tier**: an LLM interlocutor enforcing the strict register still avoids them; only authored story content uses them.

#### 22.11 Summary: Anchor Tier vs. Story Tier

| | Anchor tier (strict ESCore) | Story tier (ESCore+1) |
|---|---|---|
| Purpose | LLM interlocutor, explication loop | Comprehensible-input reading/listening |
| Vocabulary | Prime + support only | Core spine + budgeted Bucket B/C |
| Out-of-core budget | None | ~1 new lexeme (Bucket C) per 25–30 tokens, by judgment |
| Tense | Present indicative only | + narrative past (Bucket A) |
| Subjunctive | None | + frozen frames (§22.10) |
| New-word discipline | Explicate within core | Contextual-learnability test (§22.9) |

This is a living distinction and will be refined as more stories are produced. The fixed point is the principle: **the core is the anchor every story revolves around; it is not the boundary the story may not cross.**

---

## Appendix A — The Prime → Exponent Quick Reference

One-page lookup: English prime in alphabetical order, Spanish exponent, part of speech.

| English Prime | Spanish Exponent | POS | | English Prime | Spanish Exponent | POS |
|---|---|---|---|---|---|---|
| ABOVE~UP | arriba | adv. | | KNOW | saber | v. |
| AFTER | después | adv./prep. | | LIKE~AS~WAY | como | conj./prep. |
| ALL | todo | det./pron. | | LITTLE~FEW | poco | det./adj. |
| A LONG TIME | mucho tiempo | phrase | | LIVE | vivir | v. |
| A SHORT TIME | poco tiempo | phrase | | MAYBE~PERHAPS | quizá | adv. |
| BAD | malo / mal | adj./adv. | | MOMENT~INSTANT | momento | n. |
| BE (identity) | ser | v. | | MORE | más | adv./det. |
| BE (state/place) | estar | v. | | MOVE | moverse | v. |
| BECAUSE | porque | conj. | | MUCH~MANY | mucho | det./adj. |
| BEFORE | antes | adv./prep. | | NEAR | cerca | adv./prep. |
| BIG~LARGE | grande | adj. | | NOT | no | adv. |
| BODY | cuerpo | n. | | NOW | ahora | adv. |
| CAN~BE ABLE TO | poder | v. | | ONE | uno / un | det./pron. |
| DIE | morir | v. | | OTHER~ELSE | otro | det./adj. |
| DO~MAKE | hacer | v. | | PART | parte | n. |
| FAR | lejos | adv./prep. | | PEOPLE | gente | n. |
| FEEL | sentir | v. | | SAY | decir | v. |
| FOR SOME TIME | por un tiempo | phrase | | SEE | ver | v. |
| GOOD | bueno / bien | adj./adv. | | SIDE | lado | n. |
| HAPPEN~OCCUR | pasar | v. | | SMALL~LITTLE | pequeño | adj. |
| HAVE~BE SOMEONE'S | tener / mío | v./adj. | | SOME | algunos | det. |
| HEAR | oír | v. | | SOMEONE~PERSON | alguien | pron. |
| HERE | aquí | adv. | | SOMETHING~THING | algo | pron. |
| I | yo | pron. | | THE SAME | el mismo | det.+adj. |
| IF | si | conj. | | THERE IS~EXIST | hay | v. |
| INSIDE~IN | dentro | adv./prep. | | THINK | pensar | v. |
| KIND~TYPE | tipo / clase | n. | | THIS | este | det./pron. |
| TOUCH | tocar | v. | | TWO | dos | det./pron. |
| TRUE | verdad | n. | | VERY | muy | adv. |
| WANT | querer | v. | | WHEN~TIME | cuando / tiempo | conj./n. |
| WHERE~PLACE | donde / lugar | adv./n. | | WORD~WORDS | palabra | n. |
| YOU | tú | pron. | | | | |

---

## Appendix B — What the Core Deliberately Omits

The following grammatical features are outside the ESCore register. Each entry notes the boundary at which the learner will next need it and what it adds to expressive capacity.

---

**The Preterite (Simple Past)**
*Boundary:* The first time you want to say "I did this yesterday" or anchor an event to a specific past time that the narrative present does not suit.
*What it adds:* Completed, bounded past events. The narrative present substitutes for it within the core but cannot carry perfect aspect (*I have done*) or definite past reference (*last week*). The preterite has fully suppletive forms for *ser/ir* (*fui*) and irregular stems for most core verbs.
*Example out of register:* *Dije la verdad ayer.* — I told the truth yesterday.

---

**The Imperfect (Habitual/Background Past)**
*Boundary:* When you want to describe what things were like over a period (background) or what habitually used to happen.
*What it adds:* Ongoing or habitual past states. The narrative present handles narrative sequences but not "when I was young, people always..." type descriptions.
*Example out of register:* *Sabía que algo pasaba.* — I knew that something was happening.

---

**The Present Subjunctive**
*Boundary:* When you want to express doubt, desire, or emotion about a non-factual complement clause — "I want you to know this," "It's possible that something bad happens," after *quizá* with deliberate irrealis marking.
*What it adds:* Modal subordination. Within the core, *quizá* takes the indicative; the subjunctive adds a distinct irrealis register. Also required after conjunctions like *para que* [so that], *antes de que* [before], *cuando* in future contexts.
*Example out of register:* *Quiero que sepas esto.* — I want you to know this.

---

**The Conditional**
*Boundary:* When you want to express what would happen (hypothetically) — "If I knew this, I would say it."
*What it adds:* Counterfactual and polite constructions. *Quisiera* (conditional of *querer*) is the polite "I would like," which appears very early in social register.
*Example out of register:* *Si supiera esto, lo diría.* — If I knew this, I would say it.

---

**The Morphological Future**
*Boundary:* When the periphrastic *ir a* + infinitive feels unnatural or when epistemic modality is needed (*serán las dos* — it must be about two o'clock).
*What it adds:* Slightly more formal future reference and epistemic probability readings.
*Example out of register:* *Lo sabrás.* — You will know it.

---

**The Present Perfect (*Haber* + Past Participle)**
*Boundary:* When you want to say "I have done X" — an event in the past that is relevant to the present.
*What it adds:* Perfect aspect — connecting a past event to the current moment. Very high frequency in everyday Spanish.
*Example out of register:* *He dicho la verdad.* — I have told the truth.

---

**The Passive Voice (*Ser* + Past Participle)**
*Boundary:* When the agent of an action is unknown, irrelevant, or deliberately backgrounded.
*What it adds:* Agent demotion. The impersonal *se* construction (*se dice, se sabe*) substitutes for many passive uses within the core.
*Example out of register:* *Esto fue dicho por alguien.* — This was said by someone.

---

**The Full Pronoun System (Object Clitics in All Positions)**
*Boundary:* Immediately — the core already includes the basic object pronouns. The full system includes double-object clitic ordering (*le lo doy* → *se lo doy*), clitic climbing edge cases, and emphatic forms.
*What it adds:* Nuance in reference tracking and the *le* → *se* substitution rule before *lo/la/los/las*.

---

**The Full Subjunctive in Conditional Clauses**
*Boundary:* When you want *si* + imperfect subjunctive + conditional for counterfactual ("if I were...").
*What it adds:* Hypothetical contrary-to-fact conditions. Core register handles only real/open conditions with *si* + present indicative.

---

## Appendix C — Glossary of Grammatical Terms

This glossary defines the technical terms used throughout the book, in plain language wherever possible.

---

**Agreement** — The requirement that two words in the same phrase carry matching grammatical features (gender, number, person). In *las palabras buenas*, the article *las*, the noun *palabras*, and the adjective *buenas* all agree: feminine, plural.

**Allolexy** — Two or more surface forms of a single semantic prime, used in different grammatical contexts. *Ser* and *estar* are allolexes of the prime BE in Spanish.

**Auxiliary verb** — A verb that combines with another verb (usually an infinitive or participle) to express tense, mood, or aspect. In ESCore: *poder, querer, deber, ir* (in *ir a*).

**Clause** — A unit containing a subject and a predicate (a conjugated verb). A sentence may contain one clause (*sé esto*) or more than one (*sé esto porque lo veo*).

**Complement clause** — A clause that functions as the object or subject of a verb. In *sé que esto es verdad*, the clause *que esto es verdad* is the complement of *saber*.

**Complementizer** — A word that introduces a complement clause. In Spanish, the complementizer is *que* [that].

**Conjugation** — The variation of a verb's form to express person, number, tense, and mood. *Sé, sabes, sabe, sabemos, saben* are the present-tense conjugations of *saber*.

**Coordinator** — A word that joins two clauses or phrases of equal grammatical status. In ESCore: *y, o, pero*.

**Demonstrative** — A word that points to a referent in space or discourse. In ESCore: *este/esta/esto* (THIS), *ese/esa/eso* (that one).

**Exponent** — The specific word or phrase in a given language that expresses a semantic prime. *Saber* is the Spanish exponent of the prime KNOW.

**Gender** — A grammatical classification of nouns into categories (masculine/feminine in Spanish) that governs agreement on articles, adjectives, and pronouns.

**Infinitive** — The citation (dictionary) form of a verb, ending in *-ar*, *-er*, or *-ir* in Spanish. In ESCore, infinitives appear only after modals and after *ir a*.

**Lemma** — The dictionary entry form of a word, abstracting away from inflected variants. The lemma *bueno* covers *bueno/buena/buenos/buenas/buen*.

**Modal verb** — A verb that modifies the meaning of another verb, typically expressing possibility, necessity, or desire. In ESCore: *poder* (can), *querer* (want to), *deber* (should).

**Mood** — A grammatical category expressing the speaker's attitude toward the truth of a proposition. The indicative mood presents propositions as facts; the subjunctive presents them as hypothetical, desired, or doubted. ESCore uses only the indicative.

**Narrative present** — The use of present-tense verbs to narrate a sequence of past events. Fully standard in Spanish; the mechanism by which ESCore avoids the past tense.

**Number** — The grammatical distinction between singular (one) and plural (more than one). Both the noun and its modifiers carry number.

**Object** — The noun phrase that receives the action of the verb. In *veo algo*, *algo* is the direct object.

**Periphrastic future** — A future construction formed with an auxiliary rather than inflectional endings. In ESCore: *ir a + infinitive*.

**Personal *a*** — The preposition *a* placed before a human direct object in Spanish, carrying no independent meaning. *Veo a alguien* [I see someone].

**Prime** — In the NSM framework, an irreducible semantic unit — a meaning that cannot be defined in simpler terms and that appears in all human languages. The full inventory is 65 primes.

**Pro-drop** — The property of a language that allows subject pronouns to be omitted when the verb ending makes the subject recoverable. Spanish is a pro-drop language.

**Reflexive verb** — A verb whose subject and object are the same entity, marked by a reflexive pronoun (*me, te, se, nos*). In ESCore: *moverse, sentirse*, and several others.

**Relative clause** — A clause that modifies a noun, introduced by a relative pronoun. In *algo que sé*, the clause *que sé* is a relative clause modifying *algo*.

**Register** — A variety of language used in a particular social context or for a particular purpose. ESCore is a controlled register of Spanish.

**Semantic prime** — See *Prime*.

**Stem change** — An alternation in the vowel of a verb's stem in certain conjugated forms. In ESCore: e→ie in *querer, pensar, tener, venir*; o→ue in *poder, morir, moverse*.

**Subject** — The noun phrase that performs the action or is described by the predicate. In *alguien sabe esto*, *alguien* is the subject.

**Subordinator** — A word that introduces a dependent clause. In ESCore: *que* (complementizer), *si* (conditional), *cuando* (temporal), *porque* (causal).

**Suppletion** — The use of forms from etymologically unrelated roots in a single paradigm. *Ser* (*soy, eres, es*...) and *ir* (*voy, vas, va*...) are both suppletive — their forms come from multiple Latin roots.

**Tense** — A grammatical category that locates events in time. ESCore uses only the present tense (and the periphrastic future as a separate construction).

**Topicalization** — Moving an element to the front of a sentence to signal it as the topic. *Esto, yo no lo sé* [This, I don't know].

**Voice** — The grammatical distinction between active (subject performs the action) and passive (subject receives the action). ESCore uses active voice only; the impersonal *se* construction substitutes for passive when needed.

---

*End of NSM-Spanish: A Grammar of the Semantic Core.*

---
