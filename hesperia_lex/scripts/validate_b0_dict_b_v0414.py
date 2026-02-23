#!/usr/bin/env python3
"""Validate B0 token->family fallback dictionary."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

_SUFFIX_RE = re.compile(r"_[0-9]+_[0-9]+$")


def _derive_token(lemma: str) -> str:
    return _SUFFIX_RE.sub("", lemma.strip().lower())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--b0",
        type=Path,
        default=Path("hesperia_lex/frozen/B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.json"),
    )
    parser.add_argument(
        "--dict-a",
        type=Path,
        default=Path("hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_3.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("assets/v0414/b0_dict_b_validation_report.txt"),
    )
    args = parser.parse_args()

    b0 = json.loads(args.b0.read_text(encoding="utf-8"))
    if not isinstance(b0, dict) or not b0:
        raise SystemExit("B0 must be non-empty object")

    bad_entries: list[str] = []
    for token, family in b0.items():
        if not isinstance(token, str) or not token.strip():
            bad_entries.append(f"invalid token key={token!r}")
            continue
        if not isinstance(family, int):
            bad_entries.append(f"token={token} family must be int")
            continue
        if not (0 <= family <= 287):
            bad_entries.append(f"token={token} family out of range: {family}")

    dict_a = json.loads(args.dict_a.read_text(encoding="utf-8"))
    lemma_tokens = {_derive_token(k) for k in dict_a.keys() if isinstance(k, str) and not k.startswith("_")}
    collisions = sorted(t for t in b0.keys() if t in lemma_tokens)

    lines = [
        "B0 Dict B Validation Report v0.4.1.4",
        f"source_b0: {args.b0}",
        f"source_dict_a: {args.dict_a}",
        f"total_tokens: {len(b0)}",
        f"schema_errors: {len(bad_entries)}",
        f"dict_a_lemma_collisions_count: {len(collisions)}",
    ]
    if bad_entries:
        lines.append("schema_error_details:")
        lines.extend(f"- {e}" for e in bad_entries)
    lines.append("dict_a_lemma_collisions:")
    lines.extend(f"- {token}" for token in collisions[:200])
    if len(collisions) > 200:
        lines.append(f"- ... truncated ({len(collisions)-200} more)")

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.report}")

    if bad_entries:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
