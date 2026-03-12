# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.5 — Dense projection attribution (optional replacement for sparse Dict A).
MODE = "sparse" | "dense"; default = "dense".
Dense: token -> 288-dim vector (project_token); aggregate -> sentence_vector; dominant = argmax(abs);
weighted seed from all families with abs(sentence_vector[f]) > eps.
Backward compatible: same (dominant_family, dominant_area, seed, attr_metrics, extended) and 6-key contract.
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Any

from .attribution_v033 import (
    DEFAULT_TEXT_CAP,
    normalize,
    tokenize,
)
from .invariant_catalog import (
    FAMILIES_PER_AREA,
    HEXES_PER_FAMILY,
    SIDES_PER_HEX,
    forward,
    validate_side_id,
)

# Mode: "dense" (default) or "sparse" (fallback to v033 pipeline)
ATTRIBUTION_MODE = "dense"
EPS = 1e-9  # min family mass for seed contribution


def _sentence_vector_dense(tokens: list[str], centroids_path: Path | None = None) -> list[float]:
    """Sum project_token(t) over tokens, then mean. Returns 288-dim."""
    from .dense_projection_v05 import project_token
    if not tokens:
        return [0.0] * 288
    vec_sum: list[float] = [0.0] * 288
    for t in tokens:
        v = project_token(t, centroids_path=centroids_path)
        for i in range(288):
            vec_sum[i] += v[i]
    n = len(tokens)
    return [vec_sum[i] / n for i in range(288)]


def _dominant_from_vector(sentence_vector: list[float]) -> tuple[int, int]:
    """dominant_family = argmax(abs(sentence_vector)); dominant_area = family // 24."""
    best_f = 0
    best_abs = abs(sentence_vector[0])
    for f in range(1, 288):
        a = abs(sentence_vector[f])
        if a > best_abs:
            best_abs = a
            best_f = f
    return best_f, best_f // FAMILIES_PER_AREA


def _build_seed_weighted(sentence_vector: list[float], eps: float = EPS) -> list[tuple[int, float]]:
    """For each family f with abs(sentence_vector[f]) > eps, add 1500 sides with tau = altitude_f (normalized)."""
    masses = [(f, abs(sentence_vector[f])) for f in range(288) if abs(sentence_vector[f]) > eps]
    if not masses:
        return []
    total = sum(m for _, m in masses)
    if total <= 0:
        return []
    seed: list[tuple[int, float]] = []
    for f, m in masses:
        tau = max(0.0, min(1.0, m / total))
        if not math.isfinite(tau):
            tau = 0.0
        area = f // FAMILIES_PER_AREA
        family_local = f % FAMILIES_PER_AREA
        for hex_local in range(HEXES_PER_FAMILY):
            for side_local in range(SIDES_PER_HEX):
                side_id = forward(area, family_local, hex_local, side_local)
                validate_side_id(side_id)
                seed.append((side_id, tau))
    return seed


def run_attribution_pipeline_dense(
    text: str,
    cap: int = DEFAULT_TEXT_CAP,
    assets_root: Path | None = None,
    centroids_path: Path | None = None,
) -> tuple[int, int, list[tuple[int, float]], dict[str, Any], dict[str, Any]]:
    """
    Dense path: normalize -> tokenize -> project each token -> sentence_vector = mean(sum) ->
    dominant = argmax(abs), weighted seed. No semantic vacuum (all tokens contribute).
    Returns (dominant_family, dominant_area, seed, attr_metrics, extended).
    """
    normalized = normalize(text, cap=cap)
    tokens = tokenize(normalized)
    if not tokens:
        raise ValueError("semantic_vacuum: no tokens after tokenize")
    if centroids_path is None and assets_root:
        centroids_path = assets_root / "FAMILY_CENTROIDS_v0_5.json"
        if not centroids_path.exists():
            centroids_path = Path(__file__).resolve().parent.parent / "hesperia_lex" / "frozen" / "FAMILY_CENTROIDS_v0_5.json"
    sentence_vector_raw = _sentence_vector_dense(tokens, centroids_path=centroids_path)
    # v0.5.1: temperature sharpening before shadow/reduce (increases contrast, reduces entropy)
    from .dense_projection_v05 import temperature_sharpen, get_top_k, top_k_truncate
    sentence_vector = temperature_sharpen(sentence_vector_raw)
    if get_top_k() > 0:
        sentence_vector = top_k_truncate(sentence_vector)
    dominant_family, dominant_area = _dominant_from_vector(sentence_vector)
    seed = _build_seed_weighted(sentence_vector, eps=EPS)
    # Metrics: coverage = 1.0, matched = all tokens
    n = len(tokens)
    mean_alt_global = sum(abs(sentence_vector[f]) for f in range(288)) / 288 if sentence_vector else 0.0
    attr_metrics = {
        "total_tokens": n,
        "matched_tokens": n,
        "unmatched_tokens": 0,
        "attribution_coverage": 1.0,
        "meanAltitude_global": mean_alt_global,
        "mode": "dense",
    }
    per_family = {
        str(f): {
            "hits": 1 if abs(sentence_vector[f]) > EPS else 0,
            "meanAltitude": abs(sentence_vector[f]),
            "hitDensity": abs(sentence_vector[f]) if sentence_vector else 0.0,
        }
        for f in range(288)
    }
    extended = {
        **attr_metrics,
        "per_family": per_family,
        "family_vector": sentence_vector,
        "family_vector_pre_sharpen": sentence_vector_raw,
    }
    return dominant_family, dominant_area, seed, attr_metrics, extended


def run_attribution_pipeline(
    text: str,
    cap: int = DEFAULT_TEXT_CAP,
    dict_a_path: Path | None = None,
    dict_b_path: Path | None = None,
    assets_root: Path | None = None,
    mode: str | None = None,
) -> tuple[int, int, list[tuple[int, float]], dict[str, Any], dict[str, Any]]:
    """
    Single entrypoint. If mode == "dense" (or default): run dense path.
    Else: delegate to attribution_v033.run_attribution_pipeline.
    """
    use = (mode or ATTRIBUTION_MODE).lower()
    if use == "dense":
        return run_attribution_pipeline_dense(text, cap=cap, assets_root=assets_root)
    from .attribution_v033 import run_attribution_pipeline as _run_sparse
    return _run_sparse(text, cap=cap, dict_a_path=dict_a_path, dict_b_path=dict_b_path, assets_root=assets_root)
