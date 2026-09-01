#!/usr/bin/env python3
"""Third-stage grind for syzif corpus .md files: character-level OCR misreads
(e.g. "Bditors" for "Editors", "Ulliversity" for "University") that survive
repair_text.py (mechanical) and clean_corpus_artifacts.py (structural/layout).

This is a different bug class from the prior two passes, and a different tool:
not a general spellchecker. A brute-force edit-distance search against the
system dictionary was tried first and dropped — 2,901 candidate tokens in a
single book, most of them legitimate rare proper nouns/place names the generic
dictionary doesn't know (Yoram, McCubbins, Trumpington, Williamstown, Sabon...),
too slow to search exhaustively and too likely to "correct" a real name into an
unrelated dictionary word purely because they're a couple of edits apart.

Instead: apply only known print/scan OCR glyph-confusion substitutions
(rn<->m, cl<->d, ll<->n, vv<->w, B<->E word-initial, I.<->L merge, ...) at each
position in a token, and accept a fix only if it lands on a known-good word
(system dictionary, or a word that recurs >=3x elsewhere in this corpus, so
real recurring domain vocabulary is protected even off-dictionary) AND the
match is unambiguous (exactly one confusion rule produces a known-good result).
Anything else is left untouched and reported — never guessed by proximity alone.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SYSTEM_DICT = Path("/usr/share/dict/american-english")

_TOKEN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
MIN_LEN = 4
RECUR_PROTECT = 3  # a token seen this many times anywhere in the corpus is treated as real

# (pattern, replacement) — classic print/scan OCR glyph confusions, tried both
# directions at every occurrence in a token. Case-sensitive: some patterns only
# make sense at a specific case (word-initial capital confusions).
_CONFUSIONS: list[tuple[str, str]] = [
    ("rn", "m"), ("m", "rn"),
    ("cl", "d"), ("d", "cl"),
    ("ll", "n"), ("n", "ll"),
    ("vv", "w"), ("w", "vv"),
    ("ii", "n"), ("n", "ii"),
    ("B", "E"), ("E", "B"),
    ("I.", "L"), ("l.", "L"),
    ("O", "D"), ("D", "O"),
    ("S", "5"), ("5", "S"),
    ("l", "I"), ("I", "l"),
    ("0", "O"), ("O", "0"),
    ("c", "e"), ("e", "c"),
]


def load_known_dict() -> set[str]:
    words = set()
    for line in SYSTEM_DICT.read_text(encoding="utf-8", errors="replace").splitlines():
        w = line.strip()
        if len(w) >= 2 and w.isalpha():
            words.add(w.lower())
    return words


def apply_case(source: str, candidate: str) -> str:
    if source.isupper():
        return candidate.upper()
    if source[:1].isupper():
        return candidate[:1].upper() + candidate[1:]
    return candidate


def build_corpus_frequency(files: list[Path]) -> Counter:
    freq: Counter = Counter()
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in _TOKEN.finditer(text):
            freq[m.group(0).lower()] += 1
    return freq


def confusion_candidates(token: str, known_good: set[str]) -> set[str]:
    """All distinct known-good words reachable by one confusion substitution
    (either direction, at every position it occurs) from token. Case-aware:
    tries the substitution on the literal token, checks the result against
    known_good lowercased."""
    hits: set[str] = set()
    for pat, rep in _CONFUSIONS:
        start = 0
        low = token.lower()
        plow = pat.lower()
        while True:
            idx = low.find(plow, start)
            if idx == -1:
                break
            candidate = token[:idx] + rep + token[idx + len(pat):]
            if candidate.lower() in known_good and candidate.lower() != token.lower():
                hits.add(candidate.lower())
            start = idx + 1
    return hits


def process(files: list[Path], apply: bool) -> dict:
    known_dict = load_known_dict()
    corpus_freq = build_corpus_frequency(files)
    known_good = known_dict | {w for w, c in corpus_freq.items() if c >= RECUR_PROTECT}

    fixed_total = 0
    ambiguous_total = 0
    per_file = []
    fixed_samples: list[dict] = []
    ambiguous_samples: list[dict] = []

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        fixed = 0
        ambiguous = 0

        def repl(m: re.Match) -> str:
            nonlocal fixed, ambiguous
            tok = m.group(0)
            low = tok.lower()
            if len(tok) < MIN_LEN or corpus_freq.get(low, 0) != 1 or low in known_good:
                return tok
            cands = confusion_candidates(tok, known_good)
            if len(cands) == 1:
                fixed += 1
                result = apply_case(tok, next(iter(cands)))
                if len(fixed_samples) < 300:
                    fixed_samples.append({"file": path.name, "from": tok, "to": result})
                return result
            if len(cands) >= 2:
                ambiguous += 1
                if len(ambiguous_samples) < 200:
                    ambiguous_samples.append({"file": path.name, "token": tok, "candidates": sorted(cands)})
            return tok

        new_text = _TOKEN.sub(repl, text)

        if apply and new_text != text:
            path.write_text(new_text, encoding="utf-8")

        fixed_total += fixed
        ambiguous_total += ambiguous
        if fixed or ambiguous:
            per_file.append({"file": path.name, "fixed": fixed, "ambiguous": ambiguous})

    return {
        "fixed_total": fixed_total,
        "ambiguous_total": ambiguous_total,
        "per_file": per_file,
        "fixed_samples": fixed_samples,
        "ambiguous_samples": ambiguous_samples,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--apply", action="store_true", help="write fixes (default: report only)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    targets = [Path(f) for f in args.files] if args.files else sorted(ROOT.glob("*.md"))
    if not targets:
        print("no .md files found", file=sys.stderr)
        return 1

    result = process(targets, apply=args.apply)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"files scanned: {len(targets)}  apply={args.apply}")
        print(f"fixed (unique confusion-rule match): {result['fixed_total']}")
        print(f"ambiguous (>=2 confusion-rule matches, left alone): {result['ambiguous_total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
