"""
Layer-6 stability index metric.
Measure structural persistence versus volatility (repeated stays in same area).
"""

from __future__ import annotations

import numpy as np


def compute_stability_index(area_sequence: list[int] | np.ndarray) -> float:
    """
    Deterministic formula:

      repeated_stays = count of transitions where a_t == a_{t+1}
      total_transitions = len(area_sequence) - 1  (number of consecutive pairs)
      stability_index = repeated_stays / max(total_transitions, 1)

    High value = stable / persistent structure (many stays in same area).
    Low value = volatile movement (many changes).
    Sequence length 1: total_transitions = 0 → stability_index = 0.
    """
    arr = np.asarray(area_sequence, dtype=np.int64)
    n = len(arr)
    total_transitions = max(n - 1, 0)
    if total_transitions == 0:
        return 0.0

    repeated_stays = int(np.sum(arr[:-1] == arr[1:]))
    return float(repeated_stays / total_transitions)
