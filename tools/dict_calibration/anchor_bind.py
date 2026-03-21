# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 4 — Deterministic anchoring: bind draft concepts to Hesperia dict_b + hex (truth layer)."""

from __future__ import annotations

import json
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from core.hexmap.topology import load_hex_index_map

from . import repo_root


def _similarity(a: str, b: str) -> float:
    a, b = a.casefold().strip(), b.casefold().strip()
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def _best_existing_concept(
    draft: dict[str, Any],
    concept_index: dict[str, dict[str, Any]],
    *,
    min_score: float = 0.52,
) -> tuple[str | None, float, str]:
    """Return (existing_concept_id, score, reason)."""
    did = str(draft.get("concept_id", "")).strip()
    if did in concept_index:
        return did, 1.0, "exact_id"

    labels = [str(x) for x in (draft.get("labels") or [])]
    lex = [str(x) for x in (draft.get("from_lexical") or [])]
    needles = [x for x in labels + lex if x]

    best_id: str | None = None
    best = 0.0
    for cid, row in concept_index.items():
        plab = str(row.get("preferred_label") or "")
        defin = str(row.get("definition") or "")[:240]
        for n in needles:
            s1 = _similarity(n, plab)
            s2 = max((_similarity(n, defin[j : j + 60]) for j in range(0, max(1, len(defin) - 40), 20)), default=0.0)
            s = max(s1, s2 * 0.85)
            if s > best:
                best = s
                best_id = cid

    if best_id and best >= min_score:
        return best_id, best, "fuzzy_label"
    return None, best, "no_match"


def anchor_drafts(
    drafts: list[dict[str, Any]],
    concept_index: dict[str, dict[str, Any]],
    anchor_registry: dict[str, str],
    *,
    hex_map_path: Path | None = None,
    min_score: float = 0.52,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Bind each draft to an existing Hesperia concept row when similarity passes.

    Output rows extend dict_b-shaped metadata plus ``hex_id`` (cell index) and ``hex_symbol``.
    """
    root = repo_root()
    hpath = hex_map_path or (
        root / "assets/data/engine_dynamics_v060/anchors/hex_index_map.json"
    )
    hx_map = load_hex_index_map(hpath) if hpath.exists() else {}

    anchored: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    for d in drafts:
        eid, score, why = _best_existing_concept(d, concept_index, min_score=min_score)
        if not eid:
            rejected.append(
                {
                    "draft": d,
                    "reason": "cannot_anchor",
                    "best_score": round(score, 4),
                    "detail": why,
                }
            )
            continue
        base = dict(concept_index[eid])
        sym = anchor_registry.get(eid) or base.get("hex_anchor")
        cell = int(hx_map[str(sym)]) if sym and str(sym) in hx_map else None
        row = {
            **base,
            "concept_id": eid,
            "calibration_bind_score": round(score, 4),
            "calibration_bind_reason": why,
            "calibration_draft_id": d.get("concept_id"),
            "calibration_from_lexical": list(d.get("from_lexical") or []),
            "family_id": (base.get("family_ids") or [""])[0],
            "area_id": (base.get("area_ids") or [""])[0],
            "hex_symbol": sym,
            "hex_id": cell,
        }
        anchored.append(row)

    return anchored, rejected


def load_merged_dict_b(paths: list[Path]) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for p in paths:
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            cid = row.get("concept_id")
            if cid and str(cid) not in by_id:
                by_id[str(cid)] = row
    return [by_id[k] for k in sorted(by_id)]


def load_anchor_registry(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(k): str(v) for k, v in data.items() if isinstance(v, str)}
