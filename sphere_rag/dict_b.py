"""
HESPERIA Dict B v0.6 — Full-field structural layer (no K).
Depends on Dict A v0.6 calibrated 288-vector. No top-K truncation, no sparse hacks.
Operates on W = [w_1..w_288], Σw_i = 1, w_i ≥ 0.
Structural coherence (exclusion damping) → area projection → diffusion → governance / loopability / tension.
"""
from __future__ import annotations

import math
from typing import Any

try:
    from .invariant_catalog import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES
except ImportError:
    AREAS = 12
    FAMILIES_PER_AREA = 24
    TOTAL_FAMILIES = 288

# Ring: area a excludes opposite (a + 6) % 12
OPPOSITE_OFFSET = 6
LAMBDA_COHERENCE = 0.5
ALPHA_DIFFUSION = 0.2
EPS = 1e-12

# Exclusion: (i, j) excluded iff area(i) and area(j) are opposite
def _area(f: int) -> int:
    return f // FAMILIES_PER_AREA


def _excludes(i: int, j: int) -> bool:
    ai, aj = _area(i), _area(j)
    return (ai + OPPOSITE_OFFSET) % AREAS == aj or (aj + OPPOSITE_OFFSET) % AREAS == ai


def build_exclusion_pairs() -> list[tuple[int, int]]:
    """List of (i, j) with i < j that exclude each other."""
    out: list[tuple[int, int]] = []
    for i in range(TOTAL_FAMILIES):
        for j in range(i + 1, TOTAL_FAMILIES):
            if _excludes(i, j):
                out.append((i, j))
    return out


def structural_coherence_pass(
    W: list[float],
    lambda_: float = LAMBDA_COHERENCE,
    exclusion_pairs: list[tuple[int, int]] | None = None,
) -> tuple[list[float], float]:
    """
    Symmetric damping on excluded pairs. C = Σ w_i*w_j over excluded (i,j).
    w_i' = w_i - λ * Σ(w_i*w_j) over j excluded with i; clip ≥ 0; renormalize.
    Returns (W', C).
    """
    if exclusion_pairs is None:
        exclusion_pairs = build_exclusion_pairs()
    # Conflict per pair
    C = 0.0
    for i, j in exclusion_pairs:
        C += W[i] * W[j]
    # Per-family deduction: for each i, sum w_i*w_j over j that exclude i
    deduction = [0.0] * TOTAL_FAMILIES
    for i, j in exclusion_pairs:
        deduction[i] += W[i] * W[j]
        deduction[j] += W[i] * W[j]
    W_prime = [max(0.0, W[f] - lambda_ * deduction[f]) for f in range(TOTAL_FAMILIES)]
    s = sum(W_prime) or 1.0
    W_prime = [W_prime[f] / s for f in range(TOTAL_FAMILIES)]
    return W_prime, C


def area_projection(W: list[float]) -> list[float]:
    """area_score[A] = Σ w_i for family i in area A. Normalize to sum 1."""
    area_score = [0.0] * AREAS
    for f in range(TOTAL_FAMILIES):
        a = _area(f)
        area_score[a] += W[f]
    s = sum(area_score) or 1.0
    return [area_score[a] / s for a in range(AREAS)]


def entropy(p: list[float], eps: float = EPS) -> float:
    """-Σ p_i log(p_i)."""
    return -sum(x * math.log(x + eps) for x in p if x > 0)


def structural_metrics(
    W: list[float],
    exclusion_pairs: list[tuple[int, int]] | None = None,
) -> dict[str, float]:
    """entropy_family, entropy_area, exclusion_conflict_energy C, coherence_index = 1 - C (C clamped)."""
    if exclusion_pairs is None:
        exclusion_pairs = build_exclusion_pairs()
    C = 0.0
    for i, j in exclusion_pairs:
        C += W[i] * W[j]
    entropy_family = entropy(W)
    area_scores = area_projection(W)
    entropy_area = entropy(area_scores)
    # C max when mass split between one excluded pair ~ 0.25; normalize so coherence in [0,1]
    C_norm = min(1.0, C * 4.0)  # scale so C=0.25 -> 1
    coherence_index = 1.0 - C_norm
    return {
        "entropy_family": entropy_family,
        "entropy_area": entropy_area,
        "exclusion_conflict_energy": C,
        "coherence_index": coherence_index,
    }


def build_adjacency_normalized() -> list[list[float]]:
    """Adjacency: same-area neighbors. A[i][j] = 1/(n_a-1) if same area and i!=j, else 0. Row-normalized."""
    # For each family i, neighbors = other families in same area
    A: list[list[float]] = [[0.0] * TOTAL_FAMILIES for _ in range(TOTAL_FAMILIES)]
    for i in range(TOTAL_FAMILIES):
        ai = _area(i)
        neighbors = [j for j in range(TOTAL_FAMILIES) if j != i and _area(j) == ai]
        n = len(neighbors) or 1
        for j in neighbors:
            A[i][j] = 1.0 / n
    return A


def diffusion(
    W: list[float],
    alpha: float = ALPHA_DIFFUSION,
    adjacency: list[list[float]] | None = None,
) -> list[float]:
    """W_propagated = (1-α)*W + α*(A@W). Renormalize."""
    if adjacency is None:
        adjacency = build_adjacency_normalized()
    # (A @ W)[i] = sum_j A[i][j] * W[j]
    AW = [sum(adjacency[i][j] * W[j] for j in range(TOTAL_FAMILIES)) for i in range(TOTAL_FAMILIES)]
    W_prop = [(1.0 - alpha) * W[i] + alpha * AW[i] for i in range(TOTAL_FAMILIES)]
    s = sum(W_prop) or 1.0
    return [W_prop[i] / s for i in range(TOTAL_FAMILIES)]


def governance_from_full_field(
    area_scores: list[float],
    conflict_energy: float,
    entropy_area: float,
) -> float:
    """Governance from area concentration, low conflict, low entropy_area. Clamp [0,1]."""
    # Area concentration: max area score (high = one area dominates)
    conc = max(area_scores) if area_scores else 0.0
    # Low conflict: 1 - C_norm
    C_norm = min(1.0, conflict_energy * 4.0)
    low_conflict = 1.0 - C_norm
    # Low entropy_area: normalized so high entropy -> 0, low -> 1. Max entropy_area = log(12)
    max_ent = math.log(AREAS + EPS)
    low_ent = 1.0 - (entropy_area / max_ent) if max_ent > 0 else 0.0
    gov = 0.4 * conc + 0.35 * low_conflict + 0.25 * max(0.0, low_ent)
    return max(0.0, min(1.0, gov))


def loopability_from_delta(W_before: list[float], W_after: list[float]) -> float:
    """loopability = 1 - delta, delta = L1(W_after - W_before)/2 (so delta in [0,1])."""
    delta = sum(abs(W_after[i] - W_before[i]) for i in range(TOTAL_FAMILIES)) / 2.0
    return max(0.0, min(1.0, 1.0 - delta))


def tension_from_conflict(exclusion_conflict_energy: float) -> float:
    """Tension emerges from diffusion across exclusions. Use conflict energy (bounded)."""
    return min(1.0, exclusion_conflict_energy * 4.0)  # same scale as C_norm


def run_dict_b_pipeline(
    W_S: list[float],
    lambda_: float = LAMBDA_COHERENCE,
    alpha: float = ALPHA_DIFFUSION,
) -> dict[str, Any]:
    """
    Full pipeline: structural coherence on W_S → area projection → metrics → diffusion → loopability.
    Returns dict with W_adjusted, W_propagated, area_score, governance, loopability, tension_energy,
    obstacle_score (1 - coherence_index), exclusion_conflict_energy, coherence_index, entropy_family,
    entropy_area, dominant_family, dominant_area.
    """
    if len(W_S) != TOTAL_FAMILIES:
        raise ValueError(f"W_S must have length {TOTAL_FAMILIES}, got {len(W_S)}")
    exclusion_pairs = build_exclusion_pairs()
    W_adj, C = structural_coherence_pass(W_S, lambda_=lambda_, exclusion_pairs=exclusion_pairs)
    area_scores = area_projection(W_adj)
    metrics = structural_metrics(W_adj, exclusion_pairs=exclusion_pairs)
    adjacency = build_adjacency_normalized()
    W_prop = diffusion(W_adj, alpha=alpha, adjacency=adjacency)
    gov = governance_from_full_field(area_scores, C, metrics["entropy_area"])
    loop = loopability_from_delta(W_adj, W_prop)
    tension = tension_from_conflict(C)
    obstacle = max(0.0, min(1.0, 1.0 - metrics["coherence_index"]))  # high conflict → high obstacle
    # Dominant as summary: argmax of coherence-adjusted vector (not control input)
    best_f = 0
    best_w = W_adj[0]
    for f in range(1, TOTAL_FAMILIES):
        if W_adj[f] > best_w:
            best_w = W_adj[f]
            best_f = f
    dominant_area = best_f // FAMILIES_PER_AREA
    return {
        "W_adjusted": W_adj,
        "W_propagated": W_prop,
        "area_score": area_scores,
        "governance": gov,
        "loopability": loop,
        "tension_energy": tension,
        "obstacle_score": obstacle,
        "exclusion_conflict_energy": C,
        "coherence_index": metrics["coherence_index"],
        "entropy_family": metrics["entropy_family"],
        "entropy_area": metrics["entropy_area"],
        "dominant_family": best_f,
        "dominant_area": dominant_area,
    }
