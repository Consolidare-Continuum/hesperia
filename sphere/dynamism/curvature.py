"""
Layer-6 curvature metric.
Measure how much the trajectory changes direction structurally.
Uses adjacency matrix as source of truth; deterministic and bounded.
"""

from __future__ import annotations

import numpy as np


# Scoring (deterministic first-version):
SAME_AREA = 0.0
ADJACENT_MOVE = 1.0
NON_ADJACENT_MOVE = 2.0


def compute_curvature(
    area_sequence: list[int] | np.ndarray,
    adjacency_matrix: np.ndarray,
) -> float:
    """
    Structural curvature: average step score over all transitions.

    Per-step scores:
      - Same area (a_t == a_{t+1}): 0.0  (no curvature event)
      - Move to adjacent area:       1.0  (low curvature)
      - Move to non-adjacent area:   2.0  (high curvature)

    Formula:
      curvature = sum(step_curvature_scores) / max(number_of_transitions, 1)

    number_of_transitions = len(area_sequence) - 1.
    Sequence length 1: curvature = 0.
    Bounded: result in [0, 2]. Reproducible and deterministic.
    """
    arr = np.asarray(area_sequence, dtype=np.int64)
    n = len(arr)
    num_transitions = max(n - 1, 0)
    if num_transitions == 0:
        return 0.0

    total = 0.0
    for i in range(n - 1):
        a, b = int(arr[i]), int(arr[i + 1])
        if a == b:
            total += SAME_AREA
        elif adjacency_matrix[a, b] != 0:
            total += ADJACENT_MOVE
        else:
            total += NON_ADJACENT_MOVE

    return float(total / num_transitions)
