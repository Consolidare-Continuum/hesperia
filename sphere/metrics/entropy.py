"""
Shannon structural entropy — orchestration only; math lives in core.math.
"""

from __future__ import annotations

from core.math.entropy_metrics import compute_entropy, compute_normalized_entropy

__all__ = ["compute_entropy", "compute_normalized_entropy"]
