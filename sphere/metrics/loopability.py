"""
Loopability: tendency of discourse to return to previously visited structural regions.
Loop event = current area seen earlier with distance > 1. Range [0, 1].
"""

from __future__ import annotations

import numpy as np


def compute_loopability(area_sequence: np.ndarray | list[int]) -> float:
    """
    Loopability = loop_events / total_transitions.

    Loop event: at position i, area_sequence[i] was seen at some j < i-1
    (i.e. we return to an area after at least one step away).
    total_transitions = len(area_sequence) - 1.

    If sequence length < 2, returns 0.0. Range [0, 1].
    """
    arr = np.asarray(area_sequence, dtype=np.int64)
    n = len(arr)
    if n < 2:
        return 0.0
    if np.any(arr < 0) or np.any(arr >= 12):
        raise ValueError("All area_sequence values must be in [0, 11]")
    total_transitions = n - 1
    loop_events = 0
    for i in range(1, n):
        current = int(arr[i])
        # Check if current was seen at some j <= i-2 (distance > 1)
        for j in range(0, i - 1):
            if arr[j] == current:
                loop_events += 1
                break
    return float(loop_events / total_transitions)
