"""
HESPERIA v0.4.x Layer-1 instrumentation (34_SPEC).
25 variables, deterministic, input-bound. No LLM, no shadow, no books.
Inputs: total_tokens, matched list of (family_id, altitude), F, A, eps.
"""

from __future__ import annotations

import math
from typing import Any


def _hits_and_altitude_sum(
    matched: list[tuple[int, float]],
    F: int,
) -> tuple[list[int], list[float]]:
    """Build hits[f] and altitudeSum[f] from matched (familyGlobal, altitude)."""
    hits = [0] * F
    altitude_sum = [0.0] * F
    for fg, alt in matched:
        if 0 <= fg < F:
            hits[fg] += 1
            altitude_sum[fg] += alt
    return hits, altitude_sum


def _compute_gini(hits: list[int], total: float, eps: float) -> float:
    if total <= 0:
        return 0.0
    n = len(hits)
    sorted_hits = sorted(hits)
    return 1.0 - (2.0 / (n * total + eps)) * sum(
        (n - i) * sorted_hits[i] for i in range(n)
    )


def _second_max(hits: list[int]) -> int:
    M = max(hits) if hits else 0
    second = 0
    for h in hits:
        if h < M and h > second:
            second = h
    return second if second > 0 else M  # if all equal, secondMax = M (ratio 1.0)


def compute_L1(
    total_tokens: int,
    matched: list[tuple[int, float]],
    F: int = 288,
    A: int = 12,
    eps: float = 1e-9,
) -> dict[str, Any]:
    """
    Compute Layer-1 25 variables (34_SPEC).
    matched = list of (familyGlobal, altitude) per attributed token.
    Returns dict with keys TOTAL_TOKENS, ATTRIBUTED_TOKENS, COVERAGE_RATIO, ... STRUCTURAL_STABILITY_INDEX.
    """
    FAMILIES_PER_AREA = F // A if A else 24
    hits, altitude_sum = _hits_and_altitude_sum(matched, F)

    attributed = sum(hits)
    coverage = (attributed / total_tokens) if total_tokens > 0 else 0.0
    unique_families = sum(1 for h in hits if h > 0)
    family_activation_density = unique_families / F if F else 0.0
    l2_sum = sum(h * h for h in hits)
    family_hit_l2 = math.sqrt(l2_sum)

    max_hits = max(hits) if hits else 0
    dominant_family = 0
    for f in range(F):
        if hits[f] == max_hits:
            dominant_family = f
            break
    dominant_area = dominant_family // FAMILIES_PER_AREA

    dominance_ratio = max_hits / (attributed + eps)
    alt_sum_global = sum(altitude_sum)
    mean_altitude_global = alt_sum_global / (attributed + eps)
    mean_altitude_dominant = (
        altitude_sum[dominant_family] / (hits[dominant_family] + eps)
        if hits[dominant_family] > 0
        else 0.0
    )

    mu = mean_altitude_global
    var_sum = 0.0
    for f in range(F):
        if hits[f] > 0:
            mf = altitude_sum[f] / (hits[f] + eps)
            var_sum += hits[f] * (mf - mu) * (mf - mu)
    altitude_variance_global = var_sum / (attributed + eps)

    family_entropy = 0.0
    for f in range(F):
        p = hits[f] / (attributed + eps)
        if p > 0:
            family_entropy -= p * math.log(p)
    log_F = math.log(F) if F > 1 else 1.0
    normalized_family_entropy = min(1.0, family_entropy / log_F) if F > 1 else 0.0

    gini = _compute_gini(hits, float(attributed), eps)
    unique_areas = len({f // FAMILIES_PER_AREA for f in range(F) if hits[f] > 0})
    area_spread = unique_areas / A if A else 0.0
    hits_in_dominant_area = sum(
        hits[f] for f in range(F) if f // FAMILIES_PER_AREA == dominant_area
    )
    area_dominance_ratio = hits_in_dominant_area / (attributed + eps)
    second_max_hits = _second_max(hits)
    secondary_family_ratio = second_max_hits / (max_hits + eps)
    remainder = attributed - max_hits
    signal_to_noise = max_hits / (remainder + eps) if remainder >= 0 else 0.0
    sparsity_index = 1.0 - family_activation_density
    token_redundancy = (
        1.0 - (unique_families / (attributed + eps)) if attributed else 0.0
    )
    altitude_weighted_mass = sum(
        hits[f] * (altitude_sum[f] / (hits[f] + eps))
        for f in range(F)
        if hits[f] > 0
    )
    structural_stability = dominance_ratio * (1.0 - normalized_family_entropy)

    return {
        "TOTAL_TOKENS": total_tokens,
        "ATTRIBUTED_TOKENS": attributed,
        "COVERAGE_RATIO": coverage,
        "UNIQUE_FAMILIES_HIT": unique_families,
        "FAMILY_ACTIVATION_DENSITY": family_activation_density,
        "FAMILY_HIT_VECTOR_L1": float(attributed),
        "FAMILY_HIT_VECTOR_L2": family_hit_l2,
        "MAX_FAMILY_HITS": max_hits,
        "DOMINANT_FAMILY_ID": dominant_family,
        "DOMINANT_AREA_ID": dominant_area,
        "DOMINANCE_RATIO": dominance_ratio,
        "MEAN_ALTITUDE_GLOBAL": mean_altitude_global,
        "MEAN_ALTITUDE_DOMINANT": mean_altitude_dominant,
        "ALTITUDE_VARIANCE_GLOBAL": altitude_variance_global,
        "FAMILY_ENTROPY": family_entropy,
        "NORMALIZED_FAMILY_ENTROPY": normalized_family_entropy,
        "GINI_COEFFICIENT": gini,
        "UNIQUE_AREAS_HIT": unique_areas,
        "AREA_SPREAD": area_spread,
        "AREA_DOMINANCE_RATIO": area_dominance_ratio,
        "SECONDARY_FAMILY_RATIO": secondary_family_ratio,
        "SIGNAL_TO_NOISE_RATIO": signal_to_noise,
        "SPARSITY_INDEX": sparsity_index,
        "TOKEN_REDUNDANCY_RATIO": token_redundancy,
        "ALTITUDE_WEIGHTED_MASS": altitude_weighted_mass,
        "STRUCTURAL_STABILITY_INDEX": structural_stability,
    }
