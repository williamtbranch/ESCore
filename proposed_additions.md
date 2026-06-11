# Proposed Additions to ESCore Whitelist

Words flagged during story auditing that may deserve a place in the core grammar.
Each entry notes the NSM/ESCore rationale, risk, and a sample ESCore sentence.

---

## Already Added This Session (for transparency/review)

| Token | Rationale | Status |
|-------|-----------|--------|
| `sino` | Required for the NSM **no...sino** construction (contrast: *not X, but rather Y*). Covered in ESCore §15. | Added |
| `cuerpos` | Plural of prime `cuerpo`. Omitting plurals of primes is a gap; `personas`, `cosas`, `palabras` are all already present. | Added |
| `eso`, `esa`, `esos`, `esas` | Demonstratives parallel to `esto`/`esta`/`estos`/`estas` (THIS). Spanish has a three-way deictic system; THAT (medium, `eso/esa`) is a natural support word. | Added |
| `hablar`, `hablo`, `hablas`, `habla`, `hablamos`, `hablan` | SPEAK is an NSM semantic prime. Spanish NSM uses both `decir` (SAY) and `hablar` (SPEAK) as distinct prime exponents. The generated whitelist included only `decir`. | Added |
| `adentro` | Directional variant of INSIDE~IN prime `dentro`. Used after motion verbs (*vamos adentro*). | Added |

---

## Pending Approval

### ~~`afuera`~~ ✅ APPROVED
- Directional "outside/outward", paired with `adentro`. Added to whitelist and ESCore.md alongside `dentro`/`adentro`.

### ~~`cuál` / `cuáles`~~ ✅ APPROVED
- Interrogative pronoun “which one/ones” — belongs with the `qué`/`quién`/`dónde` interrogative family. Added to whitelist and ESCore.md §2.8.

### ~~`adónde` / `adonde`~~ ✅ APPROVED
- Directional interrogative/relative “to where” — contraction of core `a` + `dónde`/`donde`. Added to whitelist and ESCore.md §2.8.

### ~~`algún`~~ ✅ APPROVED (contraction rule)
- Pre-nominal apocope of `algunos` (e.g. *algún tiempo*, *algún lugar*). Components already in core. Added to whitelist.

> **Contraction rule (established here):** Any common contraction or obligatory variant whose components are both already in the ESCore core is automatically admitted. Also covers: `adonde` (relative), `conmigo` (`con`+`yo`), `contigo` (`con`+`tú`), `consigo` (`con`+`sí`) — all added to whitelist.

### ~~`ti`~~ ✅ APPROVED
- Prepositional form of `tú`, parallel to already-approved `mí`. Added to whitelist.

### ~~`volver`~~ → moved to layer1.txt
- Semantically irreplaceable but outside ESCore core. See layer1.txt for documentation and workarounds.

### ~~`hacia`~~ ✅ APPROVED
- Directional preposition "toward". Fills gap between `a` (destination) and motion-direction. Added to whitelist and ESCore.md prepositions table.

### ~~`miedo`~~ → moved to layer1.txt
- Basic emotion noun "fear." Belongs in Layer 1 where the emotional register can open fully. See layer1.txt. ESCore must work around it.

### ~~`vida` / `muerte`~~ ✅ APPROVED
- Nominal forms of the LIVE and DIE primes. `vida` = "life"; `muerte` = "death." Added to whitelist (645 tokens) and ESCore.md §LIFE AND DEATH as a nominal forms table.

---

## Naming Conventions

### Granken — the bad people
- **Granken** is the proper name for the antagonist faction as a whole, not just a leader.
- Already in `PN_whitelist.txt` (tokenizes as a proper noun).
- **Introduction pattern** (first mention in a chapter or context where unfamiliar): *la gente mala — los Granken* or *los Granken, que son la gente mala*.
- **Subsequent references**: *los Granken*, *Granken* (alone, without article), or occasionally *la gente mala* / *los malos* for literary variety.
- `los` + `Granken` — `los` is whitelisted; `Granken` is in PN_whitelist. Clean.

---

## Under Discussion

### ~~`ahí`~~ ✅ APPROVED
- Added to whitelist (`ahí`) and ESCore.md §1.x spatial support words.

### ~~`allí` / `allá`~~ ✅ APPROVED
- Added to whitelist (`allí`, `allá`) and ESCore.md §1.x spatial support words.

---

### `noche` / `día`
- **Meaning**: "night" / "day" (temporal units)
- **NSM status**: TIME is a prime; its natural units in narrative are day and night. Blocking these forces `cuando la gente no puede vernos bien` (night) and `cuando la gente puede vernos bien` (day) — very wordy.
- **Risk**: Medium. Both are content-loaded nouns. However, they name natural phenomena, not cultural or political concepts, so register corruption risk is low.
- **Sample**: *Nos movemos de noche. De día, estamos quietos.* vs. current workaround.
- **Recommendation**: Add both as support words for temporal orientation.

---

### `entrar` (conjugations: `entro`, `entra`, `entramos`, `entran`)
- **Meaning**: "to enter / go inside"
- **NSM status**: INSIDE is a prime (`dentro`/`adentro`). `entrar` is the verbal form of that prime concept — movement toward inside. Currently forces `vamos adentro` or `vamos al lugar`.
- **Risk**: Low. Closed spatial verb.
- **Recommendation**: Add as a support verb alongside `adentro`/`dentro`.

---

### `llegar` (conjugations: `llego`, `llegas`, `llega`, `llegamos`, `llegan`)
- **Meaning**: "to arrive / reach a place"
- **NSM status**: No prime maps directly to ARRIVE, but it is the natural endpoint of MOVE. Currently forces `vamos a estar en ese lugar` instead of `llegamos`.
- **Risk**: Low-medium. Could add precision to journey narratives.
- **Recommendation**: Add as a support verb.

---

### `quedarse` (conjugations: `me quedo`, `se queda`, `nos quedamos`, `se quedan`)
- **Meaning**: "to stay / remain"
- **NSM status**: No direct prime, but STOP + HERE is awkward. `quedarse` is the natural complement to `moverse`.
- **Risk**: Low.
- **Sample**: *Podemos quedarnos aquí.* vs. *Podemos estar aquí todo el tiempo que queremos.*
- **Recommendation**: Add as support verb.

---

*Last updated: Chapter 4 audit pass.*
