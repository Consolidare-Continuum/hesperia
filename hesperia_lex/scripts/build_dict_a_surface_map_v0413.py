#!/usr/bin/env python3
"""
Build DICT_A_SURFACE_MAP from Dict A (v0.4.1.3) at freeze time.

Surface map: user-facing token (no underscores from structural suffix) -> structural key.
So runtime can resolve normalized token to structural ID without exposing _1_10 to users.
Tokenizer is unchanged; underscore remains stripped.

Rule: strip trailing _\\d+_\\d+ from each Dict A key to get surface; surface -> structural_key.
On duplicate surface: prefer key where map_code is structural_label_slug (canonical word);
else first encountered.

Output: hesperia_lex/curated/DICT_A_SURFACE_MAP_v0_4_1_3.json
        {"altruism": "altruism_1_10", "trust": "trust_3_4", ...}

Run from repo root:
  python3 CLIENTS/hesperia/hesperia_lex/scripts/build_dict_a_surface_map_v0413.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CURATED = Path(__file__).resolve().parent.parent / "curated"
DICT_A_NAME = "A_CORE_STAR_MAP_v0_4_1_3.json"
OUT_NAME = "DICT_A_SURFACE_MAP_v0_4_1_3.json"

# Trailing _<digits>_<digits> (structural suffix)
SUFFIX_RE = re.compile(r"_\d+_\d+$")


def surface_from_key(structural_key: str) -> str | None:
    """Derive surface form: strip trailing _N_M. Lowercase for lookup."""
    m = SUFFIX_RE.search(structural_key)
    if not m:
        return None
    surface = structural_key[: m.start()].strip().lower()
    return surface if surface else None


def main() -> int:
    dict_a_path = CURATED / DICT_A_NAME
    if not dict_a_path.exists():
        dict_a_path = REPO_ROOT / "CLIENTS" / "hesperia" / "hesperia_lex" / "curated" / DICT_A_NAME
    if not dict_a_path.exists():
        print(f"Dict A not found: {DICT_A_NAME}", file=sys.stderr)
        return 1

    with open(dict_a_path, encoding="utf-8") as f:
        data = json.load(f)

    # Build surface -> structural_key. Prefer structural_label_slug entries on duplicate surface.
    by_surface: dict[str, tuple[str, bool]] = {}  # surface -> (structural_key, is_slug)

    for k, v in data.items():
        if k.startswith("_") or v is None:
            continue
        surface = surface_from_key(k)
        if not surface:
            continue
        is_slug = False
        if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
            is_slug = (v[0].get("map_code") or "").startswith("structural_label_slug")
        if surface not in by_surface:
            by_surface[surface] = (k, is_slug)
        else:
            _, prev_slug = by_surface[surface]
            if is_slug and not prev_slug:
                by_surface[surface] = (k, is_slug)

    surface_map = {s: key for s, (key, _) in by_surface.items()}

    out_path = CURATED / OUT_NAME
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(surface_map, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(surface_map)} surface -> structural entries to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
