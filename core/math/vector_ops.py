"""
Vector operations: argmax, top-k (dominance detection).
Deterministic; tie-break by lower index. No pipeline logic.
"""

from __future__ import annotations

import numpy as np

DEFAULT_NUM_AREAS = 12
DEFAULT_NUM_FAMILIES = 288


def vector_sum(v: np.ndarray | list[float]) -> float:
    """Sum of vector elements. Deterministic."""
    return float(np.sum(v))


def detect_dominant_area(
    area_vector: np.ndarray | list[float],
    *,
    num_areas: int = DEFAULT_NUM_AREAS,
) -> int:
    """
    Dominant area = argmax(area_vector).
    Tie-break: lower index wins (first maximum).
    """
    arr = np.asarray(area_vector, dtype=np.float64)
    if len(arr) != num_areas:
        raise ValueError(f"area_vector must have length {num_areas}, got {len(arr)}")
    idx = int(np.argmax(arr))
    return idx


def detect_dominant_family(
    family_counts: np.ndarray | list[int | float],
    *,
    num_families: int = DEFAULT_NUM_FAMILIES,
) -> int:
    """
    Dominant family = argmax(family_counts).
    Tie-break: lower index wins (first maximum).
    """
    arr = np.asarray(family_counts, dtype=np.float64)
    if len(arr) != num_families:
        raise ValueError(f"family_counts must have length {num_families}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("family_counts must be non-negative")
    idx = int(np.argmax(arr))
    return idx


def detect_family_peaks(
    family_counts: np.ndarray | list[int | float],
    k: int = 5,
    *,
    num_families: int = DEFAULT_NUM_FAMILIES,
) -> list[int]:
    """
    Top-K family indices by family_counts descending.
    Tie-break: lower index wins (stable sort by (-count, index)).
    Returns list of up to k family indices.
    """
    arr = np.asarray(family_counts, dtype=np.float64)
    if len(arr) != num_families:
        raise ValueError(f"family_counts must have length {num_families}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("family_counts must be non-negative")
    if k <= 0:
        return []
    # argsort: ascending by default; we want descending by value, then ascending by index
    indices = np.argsort(-arr, kind="stable")
    return [int(indices[i]) for i in range(min(k, len(indices)))]
