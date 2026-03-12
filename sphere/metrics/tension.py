"""
Structural tension — orchestration only; math lives in core.math.
"""

from __future__ import annotations

from core.math.stability_metrics import compute_structural_tension

TOTAL_AREAS = 12

__all__ = ["compute_structural_tension", "TOTAL_AREAS"]
