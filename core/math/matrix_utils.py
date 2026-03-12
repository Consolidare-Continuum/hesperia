"""
Matrix utilities: row-normalize, shape checks.
Deterministic; pure numerical operations only.
"""

from __future__ import annotations

import numpy as np


def row_normalize(matrix: np.ndarray, *, fill_zero_rows: float = 0.0) -> np.ndarray:
    """
    Row-normalize so each row sums to 1. Zero-sum rows get fill_zero_rows (default 0).
    Returns float64 array.
    """
    arr = np.asarray(matrix, dtype=np.float64)
    row_sums = arr.sum(axis=1, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(row_sums > 0, arr / row_sums, fill_zero_rows)
    return np.asarray(out, dtype=np.float64)
