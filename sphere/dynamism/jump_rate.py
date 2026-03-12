"""
Layer-6 jump rate metric.
Measure frequency of non-local topology jumps (non-adjacent area transitions).
"""

from __future__ import annotations

import numpy as np


def compute_jump_rate(
    area_sequence: list[int] | np.ndarray,
    adjacency_matrix: np.ndarray,
) -> dict[str, int | float]:
    """
    A jump is any transition where source != target and source and target are not adjacent.

    Formula:
      jump_rate = jump_count / max(total_transitions, 1)

    total_transitions = number of consecutive pairs (len(sequence) - 1).
    Returns {"jump_count": int, "jump_rate": float}.
    """
    arr = np.asarray(area_sequence, dtype=np.int64)
    n = len(arr)
    total_transitions = max(n - 1, 0)
    if total_transitions == 0:
        return {"jump_count": 0, "jump_rate": 0.0}

    jump_count = 0
    for i in range(n - 1):
        a, b = int(arr[i]), int(arr[i + 1])
        if a != b and adjacency_matrix[a, b] == 0:
            jump_count += 1

    rate = jump_count / total_transitions
    return {"jump_count": jump_count, "jump_rate": float(rate)}
