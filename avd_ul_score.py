#!/usr/bin/env python3
"""
avd_ul_score.py — Standalone AVD / UL (User Level) scorer for ESCore stories.

This reproduces, in-process and WITHOUT touching the WeaveLang application or
its running state, the same measurement that weavelang's
`measure_user_score` / `measure_avd` terminal commands produce.

Pipeline (kept in lock-step with weavelang):
  1. Tokenize Spanish text with spaCy `es_core_news_lg`
     (disable=["ner","parser"]), exactly as src/python/linguistic_engine.py.
  2. Normalize each lemma with `normalize_spanish_lemma` (ASCII-fold accents,
     strip to [a-z-]).
  3. Rank each lemma against the master Spanish frequency list using the
     "wlemma" bucket scheme: Snowball-Spanish stem -> min rank in bucket
     (src/simulation/frequency_manager.rs + src/domain/stemmer.rs).
  4. Build TextMetrics with the 0.2% "Gregor" tally cap (english words = 0),
     compute the tail-weighted AVD = (p85_rank + 2*p95_rank)/3
     (src/simulation/metrics.rs::calculate_avd_score).
  5. Map AVD -> User Level: UL = 4.15 * ln(AVD + 1) + 0.02
     (src/simulation/calibrator.rs::get_user_level_from_avd).

Only STATIC data is read from the weavelang folder (the spaCy model files and
the frequency list). The weavelang executable / GUI / daemon is never invoked,
so there is no risk of corrupting its project state.

NOTE - intentional divergences from exact weavelang parity. This is ESCore's
OWN difficulty metric: a fast, linguistically-corrected pre-screen, NOT a 1:1
replica. We deliberately do not chase weavelang parity — relative difficulty
ordering is what carries over, and these corrections make that ordering more
accurate (a story that scores lower here is genuinely easier).
  * Frequency list is trimmed to the top 10k ranks for speed; lemmas not in it
    get UNKNOWN_RANK (20000) instead of being dropped (conservative screen).
  * Proper nouns (spaCy POS == PROPN, e.g. "John"/"Alice") are excluded.
  * A small LEMMA_OVERRIDES table corrects known spaCy mis-lemmatizations.
  * Verb-form rescue (see rescue_verb_lemma) repairs spaCy mis-lemmatizations
    of enclitic imperatives ("diselo"->decir) and guillemet-mistagged verbs
    ("«Vuelve"->volver) that otherwise rank as spuriously rare. This lowers the
    UL of dialogue-heavy text by ~1 versus the old buggy behaviour; that is the
    correct direction (those verbs are common), so the numbers below differ
    from weavelang's and from this tool's earlier output by design.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

# --- Defaults: static assets borrowed (read-only) from the weavelang repo ---
SCRIPT_DIR = Path(__file__).resolve().parent
WEAVELANG_DIR = Path(r"E:\Bill\development\weavelang")
# Trimmed top-10k frequency list (generated from the weavelang master list).
# Using the top 10k ranks instead of the full 3.48M makes startup near-instant
# because we only Snowball-stem 10k lemmas instead of millions. Any lemma whose
# stem bucket is NOT in this list is treated as rare (UNKNOWN_RANK) rather than
# being dropped — a deliberately conservative screen for simple-register stories.
DEFAULT_FREQ_LIST = SCRIPT_DIR / "assets" / "es_freq_top10k.txt"
DEFAULT_MODEL_PATH = (
    WEAVELANG_DIR / ".venv" / "Lib" / "site-packages"
    / "es_core_news_lg" / "es_core_news_lg-3.8.0"
)

# --- AVD <-> UL fit constants (calibrator.rs) ---
A_FIT = 4.15
B_FIT = 0.02

# --- "Gregor effect" cap: rare lemmas (rank > 400) are capped at 0.2% of tokens ---
TALLY_CAP_FRACTION = 0.002
RARE_RANK_THRESHOLD = 400

# Rank assigned to any lemma not found in the trimmed frequency list.
UNKNOWN_RANK = 20000

# Spacy coarse POS tags whose tokens are excluded from scoring entirely
# (proper nouns like "John"/"Alice" must not count toward difficulty).
EXCLUDED_POS = {"PROPN"}

# Manual lemma corrections for tokens spaCy mis-lemmatizes. The KEY is the
# normalized lemma spaCy produced (after normalize_spanish_lemma); the VALUE is
# the correct dictionary lemma to rank instead. Grow this as bad cases surface
# via `--show-rare`. Example: {"sonreir": "sonreir"} (kept here intentionally
# empty until a real mis-lemmatization is observed).
LEMMA_OVERRIDES: dict[str, str] = {}

# --- Mis-lemmatized verb-form rescue -----------------------------------------
# spaCy's es_core_news_lg routinely mangles two classes of conjugated verbs,
# assigning them garbage lemmas that rank as "rare" and wrongly inflate the
# score (verified via --show-rare):
#   1. Imperatives/infinitives/gerunds carrying ENCLITIC PRONOUNS
#      ("diselo"->"diselir", "pidemelo"->..., "cuentame", "hazlo", "ponme");
#      some are even mistagged PROPN and silently dropped.
#   2. Verbs immediately after an opening guillemet « get mistagged NOUN, so a
#      form like «Vuelve» lemmatizes to "vuelve" (rare) instead of "volver",
#      even though the SAME word in isolation lemmatizes correctly.
# We rescue both generically: strip a trailing enclitic-pronoun cluster and/or
# re-lemmatize the bare word in isolation, accepting the result ONLY when it is
# a valid infinitive that ranks BETTER than the current lemma. That guard means
# genuinely rare words can never be "rescued" into looking common.

# Closed set of Spanish enclitic-pronoun clusters (one or two pronouns),
# longest alternatives first so the regex strips the maximal cluster.
_ENCLITIC = (
    r"(?:me|te|se|nos|os)(?:lo|la|le|los|las|les)"  # e.g. -selo, -telo, -melo
    r"|me|te|se|lo|la|le|nos|os|los|las|les"
)
ENCLITIC_RE = re.compile(rf"^(?P<stem>.{{2,}}?)(?:{_ENCLITIC})$", re.IGNORECASE)

# Irregular singular imperative stems (after accent folding) -> infinitive.
# These do not lemmatize correctly even in isolation, so they are mapped
# explicitly. Only consulted once an enclitic cluster has been stripped, which
# unambiguously marks the token as a verb (so "se"->ser, "ve"->ir, etc. cannot
# collide with the standalone pronoun/word).
IMPERATIVE_BASE_OVERRIDES: dict[str, str] = {
    "di": "decir", "haz": "hacer", "pon": "poner", "ten": "tener",
    "sal": "salir", "ve": "ir", "ven": "venir", "se": "ser", "oye": "oir",
}

# POS tags whose tokens are candidates for verb rescue. NOUN is deliberately
# excluded: real nouns ending in enclitic-looking syllables ("tomate", "clase")
# must never be stripped. PROPN is included because spaCy frequently mistags
# enclitic imperatives (e.g. "Pidemelo", "Ponme") as proper nouns.
_RESCUE_POS = {"VERB", "AUX", "PROPN"}

# Fancy quotation marks (incl. Spanish dialogue guillemets) are normalized to
# spaces before tagging: a verb immediately following « is otherwise mistagged
# NOUN, which breaks its lemma (e.g. «Vuelve» -> "vuelve" instead of "volver").
_QUOTE_RE = re.compile(r"[\u00ab\u00bb\u2039\u203a\u201c\u201d\u201e\u201f]")


def normalize_quotes(text: str) -> str:
    return _QUOTE_RE.sub(" ", text)


def _looks_like_infinitive(lemma: str) -> bool:
    return len(lemma) >= 2 and lemma[-2:] in ("ar", "er", "ir")


def normalize_spanish_lemma(lemma_str: str) -> str:
    """Exact port of linguistic_engine.normalize_spanish_lemma."""
    s = lemma_str.lower().strip().split(" ")[0]
    s = (
        s.replace("á", "a").replace("é", "e").replace("í", "i")
        .replace("ó", "o").replace("ú", "u").replace("ñ", "n").replace("ü", "u")
    )
    s = re.sub(r"^[^\w]+|[^\w]+$", "", s)
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s)
    if re.search(r"[^a-z-]", s):
        return ""
    return s


_FOLD_MAP = str.maketrans({
    "á": "a", "à": "a", "ä": "a", "â": "a",
    "é": "e", "è": "e", "ë": "e", "ê": "e",
    "í": "i", "ì": "i", "ï": "i", "î": "i",
    "ó": "o", "ò": "o", "ö": "o", "ô": "o",
    "ú": "u", "ù": "u", "ü": "u", "û": "u",
    "ñ": "n",
})


def fold_diacritics(word: str) -> str:
    """Port of SpanishSnowball::fold_diacritics (stemmer.rs)."""
    return word.translate(_FOLD_MAP)


class FrequencyRanker:
    """Builds the Snowball wlemma -> min-rank bucket map and looks lemmas up."""

    def __init__(self, freq_list_path: Path):
        import snowballstemmer

        self._stemmer = snowballstemmer.stemmer("spanish")
        self.bucket_rank: dict[str, int] = {}
        self._load(freq_list_path)

    def _stem(self, word: str) -> str:
        return self._stemmer.stemWord(fold_diacritics(word.strip().lower()))

    def _load(self, path: Path) -> None:
        if not path.is_file():
            raise FileNotFoundError(f"Frequency list not found: {path}")
        with path.open("r", encoding="utf-8") as fh:
            next(fh, None)  # skip header line
            for line in fh:
                # weavelang's parser splits on TAB; be tolerant of whitespace too.
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 2:
                    parts = line.split()
                if len(parts) < 2:
                    continue
                lemma = parts[0].strip()
                try:
                    rank = int(parts[1])
                except ValueError:
                    continue
                if not lemma:
                    continue
                key = self._stem(lemma)
                cur = self.bucket_rank.get(key)
                if cur is None or rank < cur:
                    self.bucket_rank[key] = rank
        if not self.bucket_rank:
            raise ValueError(f"Frequency list empty or unparseable: {path}")

    def rank_of(self, lemma: str) -> int:
        """Min rank of the lemma's stem bucket, or UNKNOWN_RANK if absent."""
        return self.bucket_rank.get(self._stem(lemma), UNKNOWN_RANK)


def calculate_avd(ranked_tallies: list[tuple[int, int]]) -> float:
    """Port of TextMetrics::calculate_avd_score (metrics.rs)."""
    total = sum(t for _, t in ranked_tallies)
    if total == 0:
        return 0.0
    p85_target = math.ceil(total * 0.85)
    p95_target = math.ceil(total * 0.95)
    cumulative = 0
    p85_rank = 0.0
    p95_rank = 0.0
    p85_found = False
    for rank, tally in sorted(ranked_tallies, key=lambda kv: kv[0]):
        cumulative += tally
        if not p85_found and cumulative >= p85_target:
            p85_rank = float(rank)
            p85_found = True
        if cumulative >= p95_target:
            p95_rank = float(rank)
            break
    return (p85_rank + 2.0 * p95_rank) / 3.0


def user_level_from_avd(avd: float) -> float:
    """Port of calibrator::get_user_level_from_avd."""
    return A_FIT * math.log(avd + 1.0) + B_FIT


def build_metrics(lemmas: list[str], ranker: FrequencyRanker):
    """Replicate TextMetrics::new (capped) with english_word_count = 0."""
    total_tokens = len(lemmas)  # includes lemmas not in the frequency list
    tally_cap = max(1, math.ceil(total_tokens * TALLY_CAP_FRACTION))

    counts = Counter(lemmas)
    ranked_tallies: list[tuple[int, int]] = []
    found = 0
    # Per-lemma (rank, capped_tally) detail for diagnostics (--show-rare).
    detail: list[tuple[int, int, str]] = []
    for lemma, tally in counts.items():
        rank = ranker.rank_of(lemma)
        if rank != UNKNOWN_RANK:
            found += tally
        if rank > RARE_RANK_THRESHOLD and tally > tally_cap:
            tally = tally_cap
        ranked_tallies.append((rank, tally))
        detail.append((rank, tally, lemma))
    return ranked_tallies, total_tokens, found, detail


def load_nlp(model_path: Path):
    import spacy

    if model_path and model_path.exists():
        return spacy.load(str(model_path), disable=["ner", "parser"])
    # Fall back to an importable package install.
    return spacy.load("es_core_news_lg", disable=["ner", "parser"])


def strip_directives(text: str) -> str:
    """Remove %%META ...%% directive lines so header metadata (e.g. the words
    'META', 'on', 'es' in `%%META simple_mode: on%%`) never counts as prose.
    weavelang consumes these directives before measuring, so stripping them
    keeps us consistent and avoids junk inflating the rare-word tail.
    """
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%%")
    )


def _isolated_lemma(nlp, word: str, require_verb: bool = False,
                    _cache: dict[tuple[str, bool], str] = {}) -> str:
    """Lemmatize a single word out of context (normalized). With
    ``require_verb`` the result is returned only if spaCy tags the word as a
    verb in isolation — this rejects non-verbs (e.g. "car" from "Carmelo",
    tagged PROPN) that merely happen to end in -ar/-er/-ir. Cached."""
    key = (word, require_verb)
    if key in _cache:
        return _cache[key]
    result = ""
    for tok in nlp(word):
        if tok.is_punct or tok.is_space:
            continue
        if require_verb and tok.pos_ not in ("VERB", "AUX"):
            break
        result = normalize_spanish_lemma(tok.lemma_)
        break
    _cache[key] = result
    return result


def rescue_verb_lemma(nlp, ranker: "FrequencyRanker", token, current_rank: int):
    """Try to recover the correct lemma for a verb form carrying enclitic
    pronouns ("diselo", "pidemelo", "hazlo", "ponme"). Strips the trailing
    enclitic cluster and resolves the bare verb. Returns the rescued lemma only
    if it is a valid infinitive that ranks strictly better than
    ``current_rank``; otherwise None (leave the token as-is). That guard means
    a genuinely rare word can never be "rescued" into looking common.
    """
    if token.pos_ not in _RESCUE_POS:
        return None
    m = ENCLITIC_RE.match(token.text)
    if not m:
        return None
    base = fold_diacritics(m.group("stem").lower())
    cand = IMPERATIVE_BASE_OVERRIDES.get(base)
    if cand is None:
        cand = _isolated_lemma(nlp, base, require_verb=True)
    if not cand or not _looks_like_infinitive(cand):
        return None
    return cand if ranker.rank_of(cand) < current_rank else None


def lemmas_for_text(nlp, text: str, ranker: "FrequencyRanker") -> list[str]:
    """Tokenize like linguistic_engine, then screen for this tool:
    skip punct/space, apply LEMMA_OVERRIDES, rescue mis-lemmatized verb forms
    (enclitic pronouns / context mistags), skip proper nouns that are not
    rescued, and drop tokens that normalize to an empty lemma (junk/symbols).
    """
    doc = nlp(text.strip())
    out: list[str] = []
    for token in doc:
        if token.is_punct or token.is_space:
            continue
        lemma = normalize_spanish_lemma(token.lemma_)
        lemma = LEMMA_OVERRIDES.get(lemma, lemma)
        rank = ranker.rank_of(lemma) if lemma else UNKNOWN_RANK
        # Only spend effort rescuing tokens that are currently penalized
        # (rare/unknown rank) or that would otherwise be dropped (PROPN). This
        # keeps already-correct rankings untouched.
        if rank > RARE_RANK_THRESHOLD or token.pos_ == "PROPN" or not lemma:
            rescued = rescue_verb_lemma(nlp, ranker, token, rank)
            if rescued is not None:
                out.append(rescued)
                continue
        if token.pos_ in EXCLUDED_POS:
            continue
        if not lemma:
            continue
        out.append(lemma)
    return out


def score_file(path: Path, nlp, ranker: FrequencyRanker) -> dict:
    text = path.read_text(encoding="utf-8")
    text = normalize_quotes(strip_directives(text))
    lemmas = lemmas_for_text(nlp, text, ranker)
    ranked_tallies, total_tokens, in_freq, detail = build_metrics(lemmas, ranker)
    avd = calculate_avd(ranked_tallies)
    ul = user_level_from_avd(avd)
    return {
        "story": path.name,
        "path": str(path),
        "tokens": total_tokens,
        "in_freq_list": in_freq,
        "unique_lemmas": len({l for l in lemmas if l}),
        "avd": round(avd, 2),
        "ul_exact": round(ul, 1),
        "ul": round(ul),
        "detail": detail,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Measure AVD score and UL (User Level) of Spanish story text files, "
        "replicating weavelang's measure_user_score."
    )
    parser.add_argument("files", nargs="+", help="Spanish .txt story files to score.")
    parser.add_argument("--freq-list", type=Path, default=DEFAULT_FREQ_LIST,
                        help=f"Master frequency list (default: {DEFAULT_FREQ_LIST}).")
    parser.add_argument("--model-path", type=Path, default=DEFAULT_MODEL_PATH,
                        help="Path to the es_core_news_lg model data directory.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a table.")
    parser.add_argument("--show-rare", type=int, metavar="N", default=0,
                        help="After scoring, list the N rarest contributing lemmas "
                             "(rank, count, lemma) per story — use this to spot "
                             "mis-lemmatized words or stray proper nouns.")
    args = parser.parse_args(argv)

    files = [Path(f) for f in args.files]
    missing = [f for f in files if not f.is_file()]
    for f in missing:
        print(f"WARNING: not found, skipping: {f}", file=sys.stderr)
    files = [f for f in files if f.is_file()]
    if not files:
        print("No valid files to score.", file=sys.stderr)
        return 1

    print(f"Loading frequency list: {args.freq_list}", file=sys.stderr)
    ranker = FrequencyRanker(args.freq_list)
    print(f"Loading spaCy model: {args.model_path}", file=sys.stderr)
    nlp = load_nlp(args.model_path)

    results = [score_file(f, nlp, ranker) for f in files]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    name_w = max(len(r["story"]) for r in results)
    name_w = max(name_w, len("Story"))
    header = f"{'Story':<{name_w}}  {'Tokens':>7}  {'InList':>7}  {'AVD':>7}  {'UL(x)':>6}  {'UL':>4}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(
            f"{r['story']:<{name_w}}  {r['tokens']:>7}  {r['in_freq_list']:>7}  "
            f"{r['avd']:>7.2f}  {r['ul_exact']:>6.1f}  UL{r['ul']:<2}"
        )

    if args.show_rare > 0:
        for r in results:
            print(f"\nRarest {args.show_rare} contributing lemmas in {r['story']} "
                  f"(rank {UNKNOWN_RANK} = not in top-10k list):")
            print(f"  {'rank':>6}  {'count':>5}  lemma")
            for rank, tally, lemma in sorted(
                r["detail"], key=lambda d: (-d[0], -d[1])
            )[: args.show_rare]:
                print(f"  {rank:>6}  {tally:>5}  {lemma}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
