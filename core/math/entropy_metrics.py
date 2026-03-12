"""
Shannon structural entropy over distributions.
Deterministic; zero probabilities ignored. Pure numerical operations only.
"""

from __future__ import annotations

import math

import numpy as np


def compute_entropy(vector: np.ndarray | list[float]) -> float:
    """
    Shannon entropy (base 2) over a non-negative distribution.

    Formula:
      p_i = vector[i] / sum(vector)
      entropy = - Σ (p_i * log2(p_i))   for p_i > 0

    Zero probabilities are ignored. If total mass is zero, returns 0.0.
    Deterministic floating precision.
    """
    arr = np.asarray(vector, dtype=np.float64)
    if arr.size == 0:
        return 0.0
    if np.any(arr < 0):
        raise ValueError("Entropy input must be non-negative")
    total = float(np.sum(arr))
    if total <= 0:
        return 0.0
    probs = arr / total
    out = 0.0
    for i in range(len(probs)):
        if probs[i] > 0:
            out -= probs[i] * math.log2(probs[i])
    return float(out)


def compute_normalized_entropy(vector: np.ndarray | list[float]) -> float:
    """
    Normalized entropy: entropy / log2(N), where N = len(vector).
    Range [0, 1]. Returns 0.0 if N <= 1 or total mass is zero.
    """
    arr = np.asarray(vector, dtype=np.float64)
    N = len(arr)
    if N <= 1:
        return 0.0
    H = compute_entropy(arr)
    if H <= 0:
        return 0.0
    return float(H / math.log2(N))
