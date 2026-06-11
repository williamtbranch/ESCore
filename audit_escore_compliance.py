#!/usr/bin/env python3
"""ESCore compliance auditor (Python port).

Scans story text against the ESCore core whitelist and classifies every
out-of-core token into one of three buckets (see ESCore.md 22.8):

  A - Inflectional : a non-present form of a verb whose lemma IS in the core
                     (e.g. hizo<-hacer, era<-ser, sepas<-saber). Near-zero cost.
  B - Transparent  : an ultra-high-frequency concrete noun outside the *prime*
                     core only because it is not a prime (agua, nino, noche...).
  C - New lexeme   : a genuinely new content word. This is the real "+1" load
                     and the number an author should actually police.

Proper nouns (PN whitelist) are a free fourth category.

This replaces audit_escore_compliance.ps1. PowerShell could not lemmatise, so
it could only report the flat (A+B+C) out-of-core number; this tool separates
the buckets so the meaningful Bucket-C figure is visible.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# Token regex: runs of Unicode letters, or runs of digits.
TOKEN_RE = re.compile(r"[^\W\d_]+|\d+", re.UNICODE)

META_PREFIX = "%%META"


# --------------------------------------------------------------------------- #
# Bucket A: non-present forms of the core verbs.
#
# The core verbs are exactly those whose PRESENT forms are in whitelist.txt.
# For each we list the non-present forms (preterite, imperfect, present and
# imperfect subjunctive, past participle with gender/number, gerund). Present
# indicative forms are intentionally omitted: they are already in the core
# whitelist, so they never surface as "unknown". Any overlap (e.g. -ir/-ar
# nosotros preterite == present) is harmless for the same reason.
# --------------------------------------------------------------------------- #
CORE_VERB_NONPRESENT: dict[str, list[str]] = {
    "ser": [
        "fui", "fuiste", "fue", "fuimos", "fueron",
        "era", "eras", "éramos", "eran",
        "sea", "seas", "seamos", "sean",
        "fuera", "fueras", "fuéramos", "fueran",
        "siendo", "sido",
    ],
    "ir": [
        "fui", "fuiste", "fue", "fuimos", "fueron",
        "iba", "ibas", "íbamos", "iban",
        "vaya", "vayas", "vayamos", "vayan",
        "fuera", "fueras", "fuéramos", "fueran",
        "yendo", "ido",
    ],
    "estar": [
        "estuve", "estuviste", "estuvo", "estuvimos", "estuvieron",
        "estaba", "estabas", "estábamos", "estaban",
        "esté", "estés", "estemos", "estén",
        "estuviera", "estuvieras", "estuviéramos", "estuvieran",
        "estando", "estado",
    ],
    "tener": [
        "tuve", "tuviste", "tuvo", "tuvimos", "tuvieron",
        "tenía", "tenías", "teníamos", "tenían",
        "tenga", "tengas", "tengamos", "tengan",
        "tuviera", "tuvieras", "tuviéramos", "tuvieran",
        "teniendo", "tenido",
    ],
    "haber": [
        "hube", "hubiste", "hubo", "hubimos", "hubieron",
        "había", "habías", "habíamos", "habían",
        "haya", "hayas", "hayamos", "hayan",
        "hubiera", "hubieras", "hubiéramos", "hubieran",
        "habiendo", "habido", "ha", "has", "han", "hemos", "he",
    ],
    "hacer": [
        "hice", "hiciste", "hizo", "hicimos", "hicieron",
        "hacía", "hacías", "hacíamos", "hacían",
        "haga", "hagas", "hagamos", "hagan",
        "hiciera", "hicieras", "hiciéramos", "hicieran",
        "haciendo", "hecho", "hecha", "hechos", "hechas",
    ],
    "decir": [
        "dije", "dijiste", "dijo", "dijimos", "dijeron",
        "decía", "decías", "decíamos", "decían",
        "diga", "digas", "digamos", "digan",
        "dijera", "dijeras", "dijéramos", "dijeran",
        "diciendo", "dicho", "dicha", "dichos", "dichas",
        "diría", "dirías", "diríamos", "dirían",
    ],
    "ver": [
        "vi", "viste", "vio", "vimos", "vieron",
        "veía", "veías", "veíamos", "veían",
        "vea", "veas", "veamos", "vean",
        "viera", "vieras", "viéramos", "vieran",
        "viendo", "visto", "vista", "vistos", "vistas",
    ],
    "saber": [
        "supe", "supiste", "supo", "supimos", "supieron",
        "sabía", "sabías", "sabíamos", "sabían",
        "sepa", "sepas", "sepamos", "sepan",
        "supiera", "supieras", "supiéramos", "supieran",
        "sabiendo", "sabido",
    ],
    "querer": [
        "quise", "quisiste", "quiso", "quisimos", "quisieron",
        "quería", "querías", "queríamos", "querían",
        "quiera", "quieras", "queramos", "quieran",
        "quisiera", "quisieras", "quisiéramos", "quisieran",
        "queriendo", "querido",
    ],
    "poder": [
        "pude", "pudiste", "pudo", "pudimos", "pudieron",
        "podía", "podías", "podíamos", "podían",
        "pueda", "puedas", "podamos", "puedan",
        "pudiera", "pudieras", "pudiéramos", "pudieran",
        "pudiendo", "podido",
    ],
    "venir": [
        "vine", "viniste", "vino", "vinimos", "vinieron",
        "venía", "venías", "veníamos", "venían",
        "venga", "vengas", "vengamos", "vengan",
        "viniera", "vinieras", "viniéramos", "vinieran",
        "viniendo", "venido",
    ],
    "dar": [
        "di", "diste", "dio", "dimos", "dieron",
        "daba", "dabas", "dábamos", "daban",
        "dé", "des", "demos", "den",
        "diera", "dieras", "diéramos", "dieran",
        "dando", "dado",
    ],
    "oír": [
        "oí", "oíste", "oyó", "oímos", "oyeron",
        "oía", "oías", "oíamos", "oían",
        "oiga", "oigas", "oigamos", "oigan",
        "oyera", "oyeras", "oyéramos", "oyeran",
        "oyendo", "oído",
    ],
    "pensar": [
        "pensé", "pensaste", "pensó", "pensamos", "pensaron",
        "pensaba", "pensabas", "pensábamos", "pensaban",
        "piense", "pienses", "pensemos", "piensen",
        "pensara", "pensaras", "pensáramos", "pensaran",
        "pensando", "pensado",
    ],
    "sentir": [
        "sentí", "sentiste", "sintió", "sentimos", "sintieron",
        "sentía", "sentías", "sentíamos", "sentían",
        "sienta", "sientas", "sintamos", "sientan",
        "sintiera", "sintieras", "sintiéramos", "sintieran",
        "sintiendo", "sentido",
    ],
    "mover": [
        "moví", "moviste", "movió", "movimos", "movieron",
        "movía", "movías", "movíamos", "movían",
        "mueva", "muevas", "movamos", "muevan",
        "moviera", "movieras", "moviéramos", "movieran",
        "moviendo", "movido",
    ],
    "morir": [
        "morí", "moriste", "murió", "morimos", "murieron",
        "moría", "morías", "moríamos", "morían",
        "muera", "mueras", "muramos", "mueran",
        "muriera", "murieras", "muriéramos", "murieran",
        "muriendo", "muerto", "muerta", "muertos", "muertas",
    ],
    "tocar": [
        "toqué", "tocaste", "tocó", "tocamos", "tocaron",
        "tocaba", "tocabas", "tocábamos", "tocaban",
        "toque", "toques", "toquemos", "toquen",
        "tocara", "tocaras", "tocáramos", "tocaran",
        "tocando", "tocado",
    ],
    "pasar": [
        "pasé", "pasaste", "pasó", "pasamos", "pasaron",
        "pasaba", "pasabas", "pasábamos", "pasaban",
        "pase", "pases", "pasemos", "pasen",
        "pasara", "pasaras", "pasáramos", "pasaran",
        "pasando", "pasado", "pasada", "pasados", "pasadas",
    ],
    "hablar": [
        "hablé", "hablaste", "habló", "hablamos", "hablaron",
        "hablaba", "hablabas", "hablábamos", "hablaban",
        "hable", "hables", "hablemos", "hablen",
        "hablara", "hablaras", "habláramos", "hablaran",
        "hablando", "hablado",
    ],
    "deber": [
        "debí", "debiste", "debió", "debimos", "debieron",
        "debía", "debías", "debíamos", "debían",
        "deba", "debas", "debamos", "deban",
        "debiera", "debieras", "debiéramos", "debieran",
        "debiendo", "debido",
    ],
    "vivir": [
        "viví", "viviste", "vivió", "vivimos", "vivieron",
        "vivía", "vivías", "vivíamos", "vivían",
        "viva", "vivas", "vivamos", "vivan",
        "viviera", "vivieras", "viviéramos", "vivieran",
        "viviendo", "vivido",
    ],
}


# --------------------------------------------------------------------------- #
# Morphological recognition helpers.
#
# These let the auditor recognise trivial inflections of core material without
# enumerating every surface form in the whitelist:
#   * conditional forms (podría...) are generated from the future stem;
#   * enclitic-pronoun forms (dilo, moviéndose) are reduced to the bare verb;
#   * accent-only variants (quien/quién) and plurals of core nouns
#     (parte/partes) are treated as the same core lexeme.
# Accent stripping is used ONLY as a recognition fallback; it never rewrites
# the core itself.
# --------------------------------------------------------------------------- #
SINGLE_ENCLITICS = (
    "me", "te", "se", "nos", "os",
    "lo", "la", "le", "los", "las", "les",
)

# Irregular future/conditional stems among the core verbs. Regular verbs build
# the conditional on the (accent-stripped) infinitive itself.
CONDITIONAL_STEMS: dict[str, str] = {
    "tener": "tendr", "haber": "habr", "hacer": "har", "decir": "dir",
    "saber": "sabr", "querer": "querr", "poder": "podr", "venir": "vendr",
}
CONDITIONAL_ENDINGS = ("ía", "ías", "íamos", "íais", "ían")


def strip_accents(text: str) -> str:
    """Remove combining diacritics (á -> a) for recognition fallbacks only."""
    return "".join(
        c for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )


def build_bucket_a() -> set[str]:
    forms: set[str] = set()
    for variants in CORE_VERB_NONPRESENT.values():
        for form in variants:
            forms.add(form.lower())
    # The conditional spelling reuses the imperfect endings (-ía...) but is
    # built on the future stem, so it must be generated explicitly here.
    for lemma in CORE_VERB_NONPRESENT:
        stem = CONDITIONAL_STEMS.get(lemma, strip_accents(lemma))
        for ending in CONDITIONAL_ENDINGS:
            forms.add(stem + ending)
    return forms


def enclitic_bases(token: str) -> set[str]:
    """Candidate verb forms obtained by stripping up to two enclitic pronouns
    (dilo -> di, moviéndose -> moviendo). Accents introduced by cliticization
    are normalized away."""
    out: set[str] = set()

    def recurse(word: str, depth: int) -> None:
        if depth == 0:
            return
        for enc in SINGLE_ENCLITICS:
            if word.endswith(enc) and len(word) > len(enc) + 1:
                base = word[: -len(enc)]
                out.add(base)
                out.add(strip_accents(base))
                recurse(base, depth - 1)

    recurse(token, 2)
    return out


def is_core_equivalent(token: str, core: set[str], core_noaccent: set[str]) -> bool:
    """True for a trivial variant of a core word: an accent-only spelling
    variant (quien/quién) or the plural of a core noun (parte/partes)."""
    if strip_accents(token) in core_noaccent:
        return True
    if token.endswith("es") and token[:-2] in core:
        return True
    if token.endswith("s") and token[:-1] in core:
        return True
    return False


def is_bucket_a(token: str, bucket_a: set[str], core: set[str]) -> bool:
    """True if the token reduces to an inflected core verb, including
    enclitic-pronoun forms (dilo, moviéndose)."""
    if token in bucket_a:
        return True
    return any(base in bucket_a or base in core for base in enclitic_bases(token))



def load_set(path: Path) -> set[str]:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    result: set[str] = set()
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        token = raw.strip()
        if not token or token.startswith("#"):
            continue
        result.add(token.lower())
    return result


def save_set(path: Path, values: set[str]) -> None:
    path.write_text("\n".join(sorted(values)) + "\n", encoding="utf-8")


def gather_files(target: Path, extensions: list[str], recurse: bool) -> list[Path]:
    if not target.exists():
        raise FileNotFoundError(f"Target path not found: {target}")
    if target.is_file():
        return [target]
    globber = target.rglob("*") if recurse else target.glob("*")
    exts = {e.lower() for e in extensions}
    return sorted(p for p in globber if p.is_file() and p.suffix.lower() in exts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ESCore compliance auditor.")
    parser.add_argument("--target", default="stories",
                        help="File or directory to audit.")
    parser.add_argument("--whitelist", default="whitelist.txt")
    parser.add_argument("--pn-whitelist", default="PN_whitelist.txt")
    parser.add_argument("--local-whitelist", default="")
    parser.add_argument("--bucket-b", default="bucket_b_transparent.txt")
    parser.add_argument("--extensions", nargs="+", default=[".md", ".txt"])
    parser.add_argument("--approve-pn", nargs="+", default=[])
    parser.add_argument("--no-recurse", action="store_true")
    args = parser.parse_args(argv)

    # Ensure accented output renders correctly regardless of console codepage.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    base = Path.cwd()
    core = load_set(base / args.whitelist)
    pn = load_set(base / args.pn_whitelist)

    if args.local_whitelist:
        local_path = base / args.local_whitelist
        if local_path.exists():
            local = load_set(local_path)
            core |= local
            print(f"Loaded local whitelist: {args.local_whitelist} "
                  f"({len(local)} tokens merged into core)")

    bucket_b_path = base / args.bucket_b
    bucket_b = load_set(bucket_b_path) if bucket_b_path.exists() else set()
    bucket_a = build_bucket_a()
    core_noaccent = {strip_accents(w) for w in core}

    if args.approve_pn:
        added = 0
        for name in args.approve_pn:
            n = name.strip().lower()
            if n and n not in pn:
                pn.add(n)
                added += 1
        save_set(base / args.pn_whitelist, pn)
        print(f"Added {added} proper noun token(s) to {args.pn_whitelist}")

    files = gather_files(base / args.target, args.extensions, not args.no_recurse)
    if not files:
        print("No files found to audit.")
        return 0

    total_tokens = 0
    unknown_counts: dict[str, int] = {}
    unknown_locations: dict[str, list[str]] = {}
    pn_candidates: dict[str, int] = {}

    for file in files:
        lines = file.read_text(encoding="utf-8-sig").splitlines()
        for i, line in enumerate(lines):
            if line.lstrip().startswith(META_PREFIX):
                continue
            for match in TOKEN_RE.finditer(line):
                original = match.group(0)
                token = original.lower()
                total_tokens += 1
                if token in core or token in pn or is_core_equivalent(token, core, core_noaccent):
                    continue

                unknown_counts[token] = unknown_counts.get(token, 0) + 1
                locs = unknown_locations.setdefault(token, [])
                if len(locs) < 3:
                    try:
                        rel = file.relative_to(base)
                    except ValueError:
                        rel = file
                    locs.append(f"{rel}:{i + 1}: {line}")

                prefix = line[:match.start()]
                is_first = re.match(r"^[^\w]*$", prefix, re.UNICODE) is not None
                looks_cap = original[:1].isupper()
                if looks_cap and not (is_first and token in core):
                    pn_candidates[token] = pn_candidates.get(token, 0) + 1

    total_unknown = sum(unknown_counts.values())

    # Bucket classification.
    a_count = b_count = c_count = 0
    c_tokens: dict[str, int] = {}
    for token, freq in unknown_counts.items():
        if is_bucket_a(token, bucket_a, core):
            a_count += freq
        elif token in bucket_b:
            b_count += freq
        else:
            c_count += freq
            c_tokens[token] = freq

    def ratio(n: int) -> str:
        if total_tokens == 0 or n == 0:
            return "0% (none)"
        pct = round(100.0 * n / total_tokens, 1)
        one_in = round(total_tokens / n)
        return f"{pct}% (about 1 in {one_in} tokens)"

    print("\n=== ESCore Audit Summary ===")
    print(f"Files scanned: {len(files)}")
    print(f"Total word tokens: {total_tokens}")
    print(f"Out-of-core (flat): {total_unknown}  -> {ratio(total_unknown)}")
    print(f"Unique out-of-core tokens: {len(unknown_counts)}")
    print(f"PN whitelist size: {len(pn)}")
    print("\n=== Bucket Breakdown (ESCore.md 22.8) ===")
    print(f"  A  inflected core verb : {a_count}  -> {ratio(a_count)}")
    print(f"  B  transparent noun    : {b_count}  -> {ratio(b_count)}")
    print(f"  C  NEW lexeme (police) : {c_count}  -> {ratio(c_count)}")

    if total_unknown == 0:
        print("\nNo out-of-core tokens found. Fully within core.")
        return 0

    if c_tokens:
        print("\n=== Bucket C — genuinely new lexemes (frequency) ===")
        for token, freq in sorted(c_tokens.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"{freq:5d}  {token}")
        print("\n=== Bucket C — sample locations (up to 3 each) ===")
        for token, _ in sorted(c_tokens.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"\n[{token}]")
            for loc in unknown_locations[token]:
                print(f"  {loc}")

    if pn_candidates:
        print("\n=== Proper-Noun Candidates (unknown + capitalized) ===")
        for token, freq in sorted(pn_candidates.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"{freq:5d}  {token}")
        print("\nTo approve candidates into PN whitelist:")
        print("  python audit_escore_compliance.py --approve-pn name1 name2 name3")

    return 0


if __name__ == "__main__":
    sys.exit(main())
