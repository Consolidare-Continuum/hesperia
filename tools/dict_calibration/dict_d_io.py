# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Dict D JSONL loader + row validator (Phase A stub — not wired into resolver)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED = ("concept_id_a", "concept_id_b", "cooc_count", "npmi", "g2", "agreement_with_b")
AGREE = frozenset({"agrees", "novel", "contradicts"})


def validate_dict_d_row(row: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    for k in REQUIRED:
        if k not in row:
            errs.append(f"missing:{k}")
    if "cooc_count" in row and int(row["cooc_count"]) < 5:
        errs.append("cooc_count<5")
    if "npmi" in row:
        v = float(row["npmi"])
        if v < -1 or v > 1:
            errs.append("npmi_out_of_range")
    if "agreement_with_b" in row and row["agreement_with_b"] not in AGREE:
        errs.append("bad_agreement_with_b")
    a, b = str(row.get("concept_id_a", "")), str(row.get("concept_id_b", ""))
    if a and b and a > b:
        errs.append("pair_not_canonically_sorted")
    return errs


def load_dict_d_jsonl(path: Path | str) -> list[dict[str, Any]]:
    path = Path(path)
    rows: list[dict[str, Any]] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        errs = validate_dict_d_row(row)
        if errs:
            raise ValueError(f"{path}:{i}: {errs}")
        rows.append(row)
    return rows
