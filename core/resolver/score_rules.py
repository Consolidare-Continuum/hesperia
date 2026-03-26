"""Deterministic scoring rules for candidate concepts."""

from __future__ import annotations

from core.dynamics.constants import get_constant
from core.dynamics.numeric import clamp01


MATCH_BASE = {
    "exact": 10.0,
    "phrase": 9.0,
    "lemma": 7.0,
    "stem": 5.0,
    "pattern": 3.0
}


def saturate(value: float) -> float:
    return clamp01(value)


def score_candidate(
    match_type: str,
    priority: int,
    specificity_rank: int = 0,
    context_overlap: int = 0,
    coherence_boost: float = 0.0,
    locality: float = 1.0,
) -> float:
    relevance = clamp01(
        (MATCH_BASE.get(match_type, 0.0) / 10.0)
        + float(priority) / float(get_constant("resolver.priority_norm", 100.0))
    )
    specificity = clamp01(float(specificity_rank) / float(get_constant("resolver.specificity_norm", 10.0)))
    local_signal = clamp01(
        (float(context_overlap) / float(get_constant("resolver.context_overlap_norm", 5.0)))
        + float(coherence_boost)
        + float(locality) * 0.2
    )
    w1 = float(get_constant("resolver.weight_relevance", 0.45))
    w2 = float(get_constant("resolver.weight_specificity", 0.35))
    w3 = float(get_constant("resolver.weight_locality", 0.2))
    return saturate(
        w1 * relevance
        + w2 * specificity
        + w3 * local_signal
    )

