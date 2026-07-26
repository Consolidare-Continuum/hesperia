# HESPERIA — Tests for LEVEL 1 area structure (TFP domain).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Tests for area_structure_tfp.yaml and load_area_structure_tfp."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def test_load_area_structure_tfp_returns_10_areas() -> None:
    """T1.1: YAML defines exactly 10 areas with area_id A1–A10."""
    from sphere.topology import load_area_structure_tfp
    path = _REPO / "spec" / "area_structure_tfp.yaml"
    data = load_area_structure_tfp(path)
    areas = data["areas"]
    assert len(areas) == 10
    for i, a in enumerate(areas):
        assert a["area_id"] == f"A{i + 1}"
        assert a["area_index"] == i


def test_area_purpose_fields() -> None:
    """T1.2: Each area has description, clinical_scope, activation_signals, exclusions."""
    from sphere.topology import load_area_structure_tfp
    path = _REPO / "spec" / "area_structure_tfp.yaml"
    data = load_area_structure_tfp(path)
    for a in data["areas"]:
        assert "description" in a
        assert "clinical_scope" in a
        assert "activation_signals" in a
        assert isinstance(a["activation_signals"], list)
        assert "exclusions" in a
        assert isinstance(a["exclusions"], list)


def test_area_neighbors_operational_only() -> None:
    """T1.3: area_neighbors only contain indices 0–9."""
    from sphere.topology import load_area_structure_tfp
    path = _REPO / "spec" / "area_structure_tfp.yaml"
    data = load_area_structure_tfp(path)
    for a in data["areas"]:
        neighbors = a["area_neighbors"]
        assert all(0 <= j <= 9 for j in neighbors), f"area {a['area_id']} has invalid neighbor"


def test_area_distance_matrix_10x10() -> None:
    """T1.3: area_distance_matrix is 10×10, symmetric, zero diagonal, diameter ≤ 3."""
    from sphere.topology import load_area_structure_tfp, get_area_distance_matrix
    path = _REPO / "spec" / "area_structure_tfp.yaml"
    data = load_area_structure_tfp(path)
    matrix = get_area_distance_matrix(path)
    assert len(matrix) == 10
    for i, row in enumerate(matrix):
        assert len(row) == 10
        assert row[i] == 0
        for j in range(10):
            assert row[j] == matrix[j][i], "matrix must be symmetric"
            assert 0 <= row[j] <= 3, "operational diameter is 3"


def test_get_operational_area_neighbors() -> None:
    """get_operational_area_neighbors(0) returns neighbors of A1 from YAML."""
    from sphere.topology import get_operational_area_neighbors
    path = _REPO / "spec" / "area_structure_tfp.yaml"
    neighbors = get_operational_area_neighbors(0, path=path)
    assert set(neighbors) == {1, 5, 7}
