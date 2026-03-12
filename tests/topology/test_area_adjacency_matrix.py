"""
Tests for area adjacency matrix (12x12, symmetric, diagonal 0).
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def test_adjacency_matrix_shape() -> None:
    """Loaded adjacency matrix is 12x12."""
    from sphere.topology import load_area_adjacency
    matrix = load_area_adjacency()
    assert matrix.shape == (12, 12)


def test_adjacency_matrix_symmetric() -> None:
    """Adjacency matrix is symmetric."""
    from sphere.topology import load_area_adjacency
    import numpy as np
    matrix = load_area_adjacency()
    assert np.array_equal(matrix, matrix.T)


def test_adjacency_matrix_diagonal_zero() -> None:
    """Diagonal elements are 0."""
    from sphere.topology import load_area_adjacency
    matrix = load_area_adjacency()
    for i in range(12):
        assert matrix[i, i] == 0


def test_adjacency_matrix_binary() -> None:
    """All entries are 0 or 1."""
    from sphere.topology import load_area_adjacency
    import numpy as np
    matrix = load_area_adjacency()
    assert np.all((matrix == 0) | (matrix == 1))
