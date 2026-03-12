"""
Structural coverage — orchestration only; math lives in core.math.
"""

from __future__ import annotations

from core.math.coverage import (
    DEFAULT_NUM_AREAS,
    DEFAULT_NUM_FAMILIES,
    compute_area_coverage,
    compute_family_coverage,
)

TOTAL_FAMILIES = DEFAULT_NUM_FAMILIES
TOTAL_AREAS = DEFAULT_NUM_AREAS

__all__ = [
    "compute_family_coverage",
    "compute_area_coverage",
    "TOTAL_FAMILIES",
    "TOTAL_AREAS",
]
