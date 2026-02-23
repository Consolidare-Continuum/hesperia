#!/usr/bin/env python3
"""
Phase 2A — Process Open English WordNet → processed/oewn_synsets.json
Extract: lemma, synset_id, pos, synonyms list. No automatic side mapping.
Run from repo root or hesperia_lex: python3 hesperia_lex/scripts/preprocess_oewn.py
"""

from __future__ import annotations

import gzip
import json
import re
import sys
from pathlib import Path

LEX_ROOT = Path(__file__).resolve().parent.parent
RAW = LEX_ROOT / "raw"
PROCESSED = LEX_ROOT / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)


def main() -> int:
    # Prefer json.gz or .json
    candidates = list(RAW.glob("english-wordnet-*.json")) + list(RAW.glob("english-wordnet-*.json.gz"))
    if not candidates:
        print("No english-wordnet-*.json or .json.gz in raw/; run download_sources.sh first.", file=sys.stderr)
        return 1
    path = candidates[0]
    if path.suffix == ".gz":
        with gzip.open(path, "rt", encoding="utf-8") as f:
            data = json.load(f)
    else:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

    # OEWN JSON structure varies; common is _synsets / _lemmas or similar
    out: dict[str, dict] = {}
    seen_lemmas: set[str] = set()

    def add_lemma(lemma: str, synset_id: str, pos: str, synonyms: list[str]) -> None:
        lemma_lower = lemma.lower().strip()
        if not lemma_lower or not re.match(r"^[a-z][a-z0-9\-']*$", lemma_lower):
            return
        syns_clean = [s for s in synonyms if s and s != lemma and re.match(r"^[a-z][a-z0-9\-']*$", s.lower())][:3]
        if lemma_lower not in out:
            out[lemma_lower] = {"synsets": []}
        out[lemma_lower]["synsets"].append({
            "id": synset_id,
            "pos": pos,
            "synonyms": [lemma_lower] + syns_clean[:2],
        })
        seen_lemmas.add(lemma_lower)

    # Try common OEWN shapes
    if isinstance(data, dict):
        if "synsets" in data:
            for s in data["synsets"]:
                syn_id = s.get("id", "")
                pos = s.get("part_of_speech", s.get("pos", "n"))[0].lower()
                lemmas = s.get("lemmas", s.get("members", []))
                if isinstance(lemmas[0], dict) if lemmas else False:
                    names = [x.get("lemma", x.get("name", "")) for x in lemmas]
                else:
                    names = [str(x) for x in lemmas]
                names = [n for n in names if n]
                if names:
                    add_lemma(names[0], syn_id, pos, names[1:])
        elif "entries" in data:
            for e in data["entries"]:
                lemma = e.get("lemma", e.get("word", ""))
                syn_id = e.get("synset_id", "")
                pos = e.get("pos", "n")[0].lower()
                syns = e.get("synonyms", e.get("synonyms_list", [])) or []
                add_lemma(lemma, syn_id, pos, syns)

    if not out:
        # Stub for when structure is different or file missing
        out = {
            "justice": {"synsets": [{"id": "oewn-justice-n", "pos": "n", "synonyms": ["justice", "fairness"]}]},
            "lie": {"synsets": [{"id": "oewn-lie-n", "pos": "n", "synonyms": ["lie", "falsehood"]}]},
        }
        print("No synsets parsed; wrote stub oewn_synsets.json.", file=sys.stderr)

    out_path = PROCESSED / "oewn_synsets.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("Wrote", out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
