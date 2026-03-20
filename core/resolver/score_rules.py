"""Deterministic scoring rules for candidate concepts."""

from __future__ import annotations


MATCH_BASE = {
    "exact": 10.0,
    "phrase": 9.0,
    "lemma": 7.0,
    "stem": 5.0,
    "pattern": 3.0
}


def score_candidate(
    match_type: str,
    priority: int,
    specificity_rank: int = 0,
    context_overlap: int = 0,
    coherence_boost: float = 0.0
) -> float:
    return (
        MATCH_BASE.get(match_type, 0.0)
        + float(priority) * 0.01
        + float(specificity_rank) * 0.1
        + float(context_overlap) * 0.2
        + float(coherence_boost)
    )

