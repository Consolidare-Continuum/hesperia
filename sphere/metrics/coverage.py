"""
Structural coverage: fraction of active families (or areas).
Deterministic; canonical total_families = 288.
"""

from __future__ import annotations

import numpy as np

TOTAL_FAMILIES = 288
TOTAL_AREAS = 12


def compute_family_coverage(family_counts: np.ndarray | list[int | float]) -> float:
    """
    Family coverage = number_of_active_families / total_families (288).

    active_family: family_counts[f] > 0
    Returns coverage in [0, 1].
    """
    arr = np.asarray(family_counts, dtype=np.float64)
    if len(arr) != TOTAL_FAMILIES:
        raise ValueError(f"family_counts must have length {TOTAL_FAMILIES}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("family_counts must be non-negative")
    active = int(np.sum(arr > 0))
    return float(active / TOTAL_FAMILIES)


def compute_area_coverage(area_vector: np.ndarray | list[int | float]) -> float:
    """
    Area coverage = number_of_active_areas / total_areas (12).
    active_area: area_vector[a] > 0. Returns coverage in [0, 1].
    """
    arr = np.asarray(area_vector, dtype=np.float64)
    if len(arr) != TOTAL_AREAS:
        raise ValueError(f"area_vector must have length {TOTAL_AREAS}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("area_vector must be non-negative")
    active = int(np.sum(arr > 0))
    return float(active / TOTAL_AREAS)
