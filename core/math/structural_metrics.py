# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Structural metrics: single canonical module for loopability, tension, dominance, coverage, entropy.
Sphere and other modules should import from core.math.structural_metrics.
Deterministic; no pipeline logic.
"""

from __future__ import annotations

from typing import Tuple

import numpy as np

from core.math.sequence_metrics import compute_loopability as _compute_loopability
from core.math.stability_metrics import compute_structural_tension as _compute_structural_tension
from core.math.vector_ops import detect_dominant_area as _detect_dominant_area
from core.math.vector_ops import detect_dominant_family as _detect_dominant_family
from core.math.coverage import compute_family_coverage as _compute_family_coverage
from core.math.coverage import compute_area_coverage as _compute_area_coverage
from core.math.entropy_metrics import compute_entropy as _compute_entropy
from core.math.entropy_metrics import compute_normalized_entropy as _compute_normalized_entropy


def compute_loopability(area_sequence: list[int] | np.ndarray) -> float:
    """Loopability over area sequence. Delegates to core.math.sequence_metrics."""
    return _compute_loopability(area_sequence)


def compute_structural_tension(area_vector: np.ndarray | list[float]) -> float:
    """Structural tension from area vector. Delegates to core.math.stability_metrics."""
    return _compute_structural_tension(area_vector)


def detect_dominant_structure(
    area_vector: np.ndarray | list[float],
    family_counts: np.ndarray | list[float],
) -> Tuple[int, int]:
    """
    Dominant area and dominant family from area vector and family counts.
    Returns (dominant_area_id, dominant_family_id).
    """
    area_id = _detect_dominant_area(area_vector)
    family_id = _detect_dominant_family(family_counts)
    return (int(area_id), int(family_id))


def normalize_coverage(coverage: float) -> float:
    """Clamp coverage to [0, 1]. Idempotent for valid inputs."""
    return max(0.0, min(1.0, float(coverage)))


def standardize_entropy(vector: np.ndarray | list[float]) -> float:
    """Normalized entropy in [0, 1]. Delegates to compute_normalized_entropy."""
    return _compute_normalized_entropy(vector)


# Re-export for callers that need the underlying detectors
def detect_dominant_area(area_vector: np.ndarray | list[float]) -> int:
    return _detect_dominant_area(area_vector)


def detect_dominant_family(family_counts: np.ndarray | list[float]) -> int:
    return _detect_dominant_family(family_counts)


__all__ = [
    "compute_loopability",
    "compute_structural_tension",
    "detect_dominant_structure",
    "normalize_coverage",
    "standardize_entropy",
    "detect_dominant_area",
    "detect_dominant_family",
]
