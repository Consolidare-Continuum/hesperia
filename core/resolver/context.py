# HESPERIA — RAD. Deterministic resolver input_context features (Ethan PO-07).
# Copyright © 2026 Societatea cu Răspundere Limitată "CONSOLIDARE CONTINUUM" (IDNO 1026023120076). See LEGAL_NOTICE.md.

from __future__ import annotations

import re
from typing import Any

_TOKEN_IN_LABEL = re.compile(r"[a-z0-9]+")


def label_token_overlap(canonical_text: str, span_start: int, span_end: int, label: str, *, window: int = 48) -> int:
    """Count label tokens that also appear in a fixed char window around the span."""
    if not label or not canonical_text:
        return 0
    lo = max(0, span_start - window)
    hi = min(len(canonical_text), span_end + window)
    chunk = canonical_text[lo:hi]
    label_tokens = set(_TOKEN_IN_LABEL.findall(label.casefold()))
    if not label_tokens:
        return 0
    chunk_tokens = set(_TOKEN_IN_LABEL.findall(chunk))
    return len(label_tokens & chunk_tokens)


def coherence_from_related(
    concept_id: str,
    concept_index: dict[str, Any],
    *,
    sibling_ids: frozenset[str],
) -> float:
    """
    Tiny deterministic coherence boost when another candidate shares ``related_concept_ids``.
    """
    meta = concept_index.get(concept_id) or {}
    related = frozenset(str(x) for x in (meta.get("related_concept_ids") or []) if x)
    if not related or not sibling_ids:
        return 0.0
    return 0.15 * float(len(related & sibling_ids))
