"""
Layer-4 Topology Graph loader.
Loads area adjacency matrix and family→area mapping; builds topology graph for runtime.
Deterministic, validated. No propagation logic — data definition + loader only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

import numpy as np

# Default data directory: repo_root/data/topology
_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_DATA_DIR = _REPO_ROOT / "data" / "topology"

ADJACENCY_FILENAME = "area_adjacency_matrix.json"
FAMILY_AREA_FILENAME = "family_to_area_map.json"


def _data_dir(data_root: Optional[Path] = None) -> Path:
    return Path(data_root) if data_root is not None else _DEFAULT_DATA_DIR


def load_area_adjacency(data_root: Optional[Path] = None) -> np.ndarray:
    """
    Load the 12×12 binary area adjacency matrix.
    Returns: adjacency_matrix (np.ndarray, shape (12, 12), dtype int or bool).
    Raises on invalid shape, non-symmetric, or non-zero diagonal.
    """
    path = _data_dir(data_root) / ADJACENCY_FILENAME
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    raw = data.get("matrix")
    if raw is None:
        raise ValueError(f"{path}: missing 'matrix' key")
    adjacency_matrix = np.array(raw, dtype=np.int64)
    # Validation
    if adjacency_matrix.shape != (12, 12):
        raise ValueError(
            f"area adjacency matrix must have shape (12, 12), got {adjacency_matrix.shape}"
        )
    if not np.array_equal(adjacency_matrix, adjacency_matrix.T):
        raise ValueError("area adjacency matrix must be symmetric")
    if np.any(np.diag(adjacency_matrix) != 0):
        raise ValueError("area adjacency matrix diagonal must be 0")
    # Binary check optional but good practice
    if np.any((adjacency_matrix != 0) & (adjacency_matrix != 1)):
        raise ValueError("area adjacency matrix must be binary (0 or 1)")
    return adjacency_matrix


def load_family_area_mapping(data_root: Optional[Path] = None) -> np.ndarray:
    """
    Load the canonical family→area mapping (288 families → area index 0–11).
    Returns: family_to_area (np.ndarray, shape (288,), dtype int64).
    family_to_area[i] = area index for family index i (0-based).
    Raises on wrong size or invalid area ids.
    """
    path = _data_dir(data_root) / FAMILY_AREA_FILENAME
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    mapping = data.get("mapping")
    if mapping is None:
        raise ValueError(f"{path}: missing 'mapping' key")
    # Build array in canonical order: family_001 .. family_288 → indices 0..287
    family_to_area = np.zeros(288, dtype=np.int64)
    for i in range(1, 289):
        key = f"family_{i:03d}"
        if key not in mapping:
            raise ValueError(f"{path}: missing key '{key}' in mapping")
        a = int(mapping[key])
        if not (0 <= a < 12):
            raise ValueError(
                f"{path}: invalid area id {a} for '{key}' (must be 0–11)"
            )
        family_to_area[i - 1] = a
    if len(mapping) != 288:
        raise ValueError(
            f"family_to_area mapping must have exactly 288 entries, got {len(mapping)}"
        )
    return family_to_area


def build_topology_graph(data_root: Optional[Path] = None) -> dict:
    """
    Build the topology graph from the area adjacency matrix.
    Returns dict with:
      - "areas": 12
      - "neighbors": { area_index: [list of adjacent area indices] }
    Uses load_area_adjacency; raises on validation failure.
    """
    adjacency_matrix = load_area_adjacency(data_root)
    neighbors = {}
    for i in range(12):
        neighbors[i] = [j for j in range(12) if adjacency_matrix[i, j] == 1]
    return {"areas": 12, "neighbors": neighbors}


def load_all(
    data_root: Optional[Path] = None,
) -> tuple[np.ndarray, np.ndarray, dict]:
    """
    Load adjacency matrix, family→area mapping, and topology graph.
    Returns (adjacency_matrix, family_to_area, topology_graph).
    All validation is performed; raises on any violation.
    """
    adjacency_matrix = load_area_adjacency(data_root)
    family_to_area = load_family_area_mapping(data_root)
    topology_graph = build_topology_graph(data_root)
    # Cross-checks
    assert adjacency_matrix.shape == (12, 12), adjacency_matrix.shape
    assert len(family_to_area) == 288, len(family_to_area)
    assert np.array_equal(adjacency_matrix, adjacency_matrix.T), "adjacency symmetric"
    assert np.all((family_to_area >= 0) & (family_to_area < 12)), "no invalid area ids"
    return adjacency_matrix, family_to_area, topology_graph
