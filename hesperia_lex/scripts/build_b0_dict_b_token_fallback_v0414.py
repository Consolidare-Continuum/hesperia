#!/usr/bin/env python3
"""Build B0 token->family fallback dictionary from Dict A v0.4.1.3."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

SIDES_PER_FAMILY = 1500
OUTPUT_JSON = "B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.json"
OUTPUT_SHA = "B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.sha256"


_SUFFIX_RE = re.compile(r"_[0-9]+_[0-9]+$")


def _derive_token(lemma: str) -> str:
    return _SUFFIX_RE.sub("", lemma.strip().lower())


def build_b0(dict_a_path: Path) -> tuple[dict[str, int], dict[str, str]]:
    raw = json.loads(dict_a_path.read_text(encoding="utf-8"))
    token_to_family_votes: dict[str, dict[int, int]] = {}
    token_anchor: dict[str, str] = {}

    for lemma in sorted(raw.keys()):
        if lemma.startswith("_"):
            continue
        entry = raw.get(lemma)
        if not isinstance(entry, list) or not entry:
            continue
        head = entry[0]
        if not isinstance(head, dict) or "side_id" not in head:
            continue
        side_id = int(head["side_id"])
        if side_id < 0:
            continue
        family = side_id // SIDES_PER_FAMILY
        if not (0 <= family <= 287):
            continue
        token = _derive_token(lemma)
        if not token:
            continue
        token_to_family_votes.setdefault(token, {})
        token_to_family_votes[token][family] = token_to_family_votes[token].get(family, 0) + 1
        token_anchor.setdefault(token, lemma)

    out: dict[str, int] = {}
    for token in sorted(token_to_family_votes.keys()):
        votes = token_to_family_votes[token]
        family, _vote = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        out[token] = family
    return out, token_anchor


def _write_sha(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix(".sha256").write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dict-a",
        type=Path,
        default=Path("hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_3.json"),
    )
    parser.add_argument("--out-dir", type=Path, default=Path("hesperia_lex/frozen"))
    parser.add_argument("--anchor-map", type=Path, default=Path("assets/v0414/b0_anchor_map_v0414.json"))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.anchor_map.parent.mkdir(parents=True, exist_ok=True)

    b0, anchor_map = build_b0(args.dict_a)
    out_path = args.out_dir / OUTPUT_JSON
    out_path.write_text(json.dumps(b0, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    sha_path = args.out_dir / OUTPUT_SHA
    digest = hashlib.sha256(out_path.read_bytes()).hexdigest()
    sha_path.write_text(f"{digest}  {out_path.name}\n", encoding="utf-8")

    args.anchor_map.write_text(
        json.dumps(anchor_map, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"wrote {out_path}")
    print(f"wrote {sha_path}")
    print(f"tokens={len(b0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
