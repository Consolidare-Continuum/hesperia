# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 5 — Deterministic Dict A ↔ Dict B link table."""

from __future__ import annotations

from difflib import SequenceMatcher
from typing import Any


def _sim(a: str, b: str) -> float:
    return SequenceMatcher(None, a.casefold(), b.casefold()).ratio()


def build_links(
    normalized_rows: list[dict[str, Any]],
    anchored_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Map lexical strings to anchored ``concept_id`` using ``from_lexical`` lists
    and normalized / variant strings.
    """
    lexical_to_concept: dict[str, tuple[str, str, float]] = {}
    for row in anchored_rows:
        cid = str(row.get("concept_id", ""))
        fl = list(row.get("calibration_from_lexical") or row.get("from_lexical") or [])
        for lx in fl:
            lx = str(lx).strip()
            if lx and lx not in lexical_to_concept:
                lexical_to_concept[lx] = (cid, "exact", 1.0)

    links: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for r in normalized_rows:
        norm = str(r.get("normalized") or r.get("text", "")).strip()
        if not norm:
            continue
        variants = [norm] + [str(v).strip() for v in (r.get("variants") or []) if str(v).strip()]

        best_cid: str | None = None
        best_type = "unmapped"
        best_pr = 0.0

        for cand in variants:
            if cand in lexical_to_concept:
                cid, mt, pr = lexical_to_concept[cand]
                if pr > best_pr:
                    best_cid, best_type, best_pr = cid, mt, pr
            else:
                for lx, (cid, _, _) in lexical_to_concept.items():
                    s = _sim(cand, lx)
                    if s >= 0.88 and s > best_pr:
                        best_cid, best_type, best_pr = cid, "fuzzy", s

        if not best_cid:
            for lx, (cid, _, _) in lexical_to_concept.items():
                s = _sim(norm, lx)
                if s >= 0.82 and s > best_pr:
                    best_cid, best_type, best_pr = cid, "fuzzy", s

        if best_cid:
            key = (norm, best_cid)
            if key in seen:
                continue
            seen.add(key)
            links.append(
                {
                    "lexical": norm,
                    "concept_id": best_cid,
                    "match_type": best_type,
                    "priority": round(float(best_pr), 4),
                }
            )

    return links


def links_to_engine_dict_a(
    links: list[dict[str, Any]],
    *,
    version: str = "v0.6.0-cal",
    id_prefix: str = "CAL",
) -> list[dict[str, Any]]:
    """Emit DLCR matcher rows (``normalized_form``, ``candidate_concept_ids``, ...)."""
    rows: list[dict[str, Any]] = []
    for i, ln in enumerate(links, start=1):
        cid = str(ln.get("concept_id", ""))
        lex = str(ln.get("lexical", "")).strip()
        if not cid or not lex:
            continue
        mt = str(ln.get("match_type", "phrase"))
        map_type = "phrase" if mt != "exact" else "exact"
        pr = int(round(float(ln.get("priority", 0.8)) * 10))
        pr = max(1, min(10, pr))
        rows.append(
            {
                "entry_id": f"{id_prefix}-{i:05d}",
                "surface_form": lex,
                "normalized_form": lex,
                "match_type": map_type,
                "candidate_concept_ids": [cid],
                "priority": pr,
                "version": version,
            }
        )
    return rows
