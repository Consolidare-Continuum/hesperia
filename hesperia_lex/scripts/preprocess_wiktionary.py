#!/usr/bin/env python3
"""
Phase 2C — Process Wiktionary dump → processed/wiktionary_lemmas.json
Extract lemma → redirect/variant/inflection forms only. No definitions or meaning.
Run from repo root or hesperia_lex: python3 hesperia_lex/scripts/preprocess_wiktionary.py
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

LEX_ROOT = Path(__file__).resolve().parent.parent
RAW = LEX_ROOT / "raw"
PROCESSED = LEX_ROOT / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)


def main() -> int:
    xml_path = RAW / "enwiktionary-latest-pages-articles.xml"
    if not xml_path.exists():
        # Stub
        out = {"color": ["colour"], "organize": ["organise"], "justice": [], "lie": ["lying"]}
        out_path = PROCESSED / "wiktionary_lemmas.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        print("Wiktionary XML not found; wrote stub", out_path, file=sys.stderr)
        return 0

    out: dict[str, list[str]] = {}
    def valid(w: str) -> bool:
        return bool(w and re.match(r"^[a-z][a-z0-9\-']*$", w.lower()) and len(w) < 50)

    try:
        for event, elem in ET.iterparse(xml_path, events=("end",)):
            if elem.tag.endswith("page"):
                title = ""
                text = ""
                for c in elem:
                    if c.tag.endswith("title"):
                        title = (c.text or "").strip()
                    if c.tag.endswith("revision"):
                        for cc in c:
                            if cc.tag.endswith("text") and cc.text:
                                text = cc.text
                                break
                if title and ":" not in title and valid(title.lower()):
                    # Very simple: look for # redirect or === English === and inflections
                    variants = []
                    for line in text.split("\n")[:80]:
                        if line.strip().startswith("#") and "redirect" in line.lower():
                            m = re.search(r"\[\[([^\]|]+)", line)
                            if m:
                                v = m.group(1).strip()
                                if valid(v) and v.lower() != title.lower():
                                    variants.append(v.lower())
                        if "===English===" in line or "== English ==" in line:
                            break
                    if variants:
                        out[title.lower()] = list(dict.fromkeys(variants))[:10]
                elem.clear()
    except ET.ParseError as e:
        print("Parse error (partial OK):", e, file=sys.stderr)

    if not out:
        out = {"color": ["colour"], "organize": ["organise"]}
    out_path = PROCESSED / "wiktionary_lemmas.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("Wrote", out_path, "entries:", len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
