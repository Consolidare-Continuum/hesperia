"""
Structural tension: competition between structural regions.
Low tension = one area dominates; high tension = balanced. Range [0, 1].
"""

from __future__ import annotations

import numpy as np

TOTAL_AREAS = 12


def compute_structural_tension(area_vector: np.ndarray | list[float]) -> float:
    """
    Tension = 1 - (dominant_area_mass / total_mass).

    Where:
      dominant_area_mass = max(area_vector)
      total_mass = sum(area_vector)

    Interpretation: low tension → one area dominates; high tension → balanced competition.
    Return range: 0 ≤ tension ≤ 1. If total_mass == 0, returns 0.0.
    """
    arr = np.asarray(area_vector, dtype=np.float64)
    if len(arr) != TOTAL_AREAS:
        raise ValueError(f"area_vector must have length {TOTAL_AREAS}, got {len(arr)}")
    if np.any(arr < 0):
        raise ValueError("area_vector must be non-negative")
    total = float(np.sum(arr))
    if total <= 0:
        return 0.0
    dominant_mass = float(np.max(arr))
    return float(1.0 - (dominant_mass / total))
