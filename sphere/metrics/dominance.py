"""
Dominant structure detection: dominant area, dominant family, family peaks.
Tie-break: lower index wins. Deterministic ordering.
"""

from __future__ import annotations

import numpy as np

TOTAL_FAMILIES = 288
TOTAL_AREAS = 12


def detect_dominant_area(area_vector: np.ndarray | list[float]) -> int:
    """
    Dominant area = argmax(area_vector).
    Tie-break: lower index wins (first maximum).
    """
    arr = np.asarray(area_vector, dtype=np.float64)
    if len(arr) != TOTAL_AREAS:
        raise ValueError(f"area_vector must have length {TOTAL_AREAS}, got {len(arr)}")
    idx = int(np.argmax(arr))
    return idx


def detect_dominant_family(family_counts: np.ndarray | list[int | float]) -> int:
    """
    Dominant family = argmax(family_counts).
    Tie-break: lower index wins (first maximum).
    """
    arr = np.asarray(family_counts, dtype=np.float64)
    if len(arr) != TOTAL_FAMILIES:
        raise ValueError(f"family_counts must have length {TOTAL_FAMILIES}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("family_counts must be non-negative")
    idx = int(np.argmax(arr))
    return idx


def detect_family_peaks(
    family_counts: np.ndarray | list[int | float],
    k: int = 5,
) -> list[int]:
    """
    Top-K family indices by family_counts descending.
    Tie-break: lower index wins (stable sort by (-count, index)).
    Returns list of up to k family indices.
    """
    arr = np.asarray(family_counts, dtype=np.float64)
    if len(arr) != TOTAL_FAMILIES:
        raise ValueError(f"family_counts must have length {TOTAL_FAMILIES}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("family_counts must be non-negative")
    if k <= 0:
        return []
    # argsort: ascending by default; we want descending by value, then ascending by index
    indices = np.argsort(-arr, kind="stable")
    return [int(indices[i]) for i in range(min(k, len(indices)))]
