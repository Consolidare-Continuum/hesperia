"""
Layer-6 transition matrix — orchestration only; math lives in core.math.
"""

from __future__ import annotations

from core.math.transition_matrix import (
    compute_transition_matrix,
    compute_transition_probabilities,
)

__all__ = ["compute_transition_matrix", "compute_transition_probabilities"]
