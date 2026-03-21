# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 3 — Map normalized lexicals to concept proposals (reuse existing ids when possible)."""

from __future__ import annotations

import json as _json
from typing import Any

from .openai_json import chat_json

SYSTEM = """You map lexical phrases (Russian and/or English clinical / TFP discourse) to a controlled concept vocabulary.
Prefer reusing existing concept_id values exactly when meaning matches.
Limit new concepts: only when no existing id fits; use dotted ids like tfp.domain.name
If the input list is non-empty you MUST return at least one concept object with non-empty from_lexical drawn ONLY from that list.
Output strict JSON only."""

USER_TEMPLATE = """Existing concepts (reuse these ids when possible):
{catalog}

Normalized lexical items:
{items}

Return JSON: {{"concepts": [
  {{"concept_id": str, "labels": [str], "from_lexical": [str], "confidence": float}}
]}}
Each from_lexical entry must be copied from the input phrase list. Merge synonyms under one concept.
Cap total concepts at {max_concepts}."""


def _catalog_rows(dict_b_rows: list[dict[str, Any]], *, limit: int = 400) -> str:
    lines = []
    for row in dict_b_rows[:limit]:
        cid = row.get("concept_id")
        lab = row.get("preferred_label") or row.get("definition", "")[:80]
        lines.append(f"- {cid}: {lab}")
    return "\n".join(lines)


def propose_concepts(
    normalized_rows: list[dict[str, Any]],
    dict_b_rows: list[dict[str, Any]],
    *,
    max_concepts: int = 80,
    batch_size: int = 40,
    catalog_limit: int = 400,
) -> list[dict[str, Any]]:
    catalog = _catalog_rows(dict_b_rows, limit=catalog_limit)
    phrases = [str(r.get("normalized") or r.get("text", "")).strip() for r in normalized_rows]
    phrases = [p for p in phrases if p]
    merged: list[dict[str, Any]] = []
    seen: set[str] = set()

    for i in range(0, len(phrases), batch_size):
        chunk = phrases[i : i + batch_size]
        user = USER_TEMPLATE.format(
            catalog=catalog,
            items=_json.dumps(chunk, ensure_ascii=False),
            max_concepts=max_concepts,
        )
        raw = chat_json(system=SYSTEM, user=user)
        arr = raw.get("concepts") if isinstance(raw, dict) else None
        if not isinstance(arr, list):
            raise ValueError("propose_concepts: expected {concepts: [...]}")
        if len(arr) == 0 and chunk:
            raw = chat_json(
                system=SYSTEM,
                user=user
                + "\n\nYour previous reply had an empty concepts array. Regroup the SAME items; minimum 1 concept.",
                temperature=0.25,
            )
            arr = raw.get("concepts") if isinstance(raw, dict) else None
            if not isinstance(arr, list):
                raise ValueError("propose_concepts: retry expected {concepts: [...]}")
        for c in arr:
            if not isinstance(c, dict):
                continue
            cid = str(c.get("concept_id", "")).strip()
            if not cid:
                continue
            fl = [str(x) for x in (c.get("from_lexical") or []) if str(x).strip()]
            key = cid + "|" + "|".join(sorted(fl))
            if key in seen:
                continue
            seen.add(key)
            merged.append(
                {
                    "concept_id": cid,
                    "labels": [str(x) for x in (c.get("labels") or [])],
                    "from_lexical": fl,
                    "confidence": float(c.get("confidence") or 0.5),
                }
            )
    return merged
