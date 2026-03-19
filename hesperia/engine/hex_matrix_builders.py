# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""
Deterministic builders for hex microphysics (ring Laplacian, resistance, P_CH-style sources).

Spec: spec/hex_microphysics_canon.md
Geometry: core.topology.invariant_catalog
"""

from __future__ import annotations

from typing import Sequence

import numpy as np

from core.topology.invariant_catalog import (
    FAMILIES_PER_AREA,
    HEXES_PER_FAMILY,
    TOTAL_FAMILIES,
    TOTAL_HEXES,
)

__all__ = [
    "NUM_FAMILIES_HEX",
    "HEXES_PER_FAMILY_CANON",
    "TOTAL_HEXES_CANON",
    "hex_linear_index",
    "family_and_local_from_linear",
    "build_ring_laplacian",
    "build_uniform_hex_resistance",
    "family_source_to_hex_uniform",
    "concept_family_weights_to_hex_source",
]


NUM_FAMILIES_HEX = TOTAL_FAMILIES
HEXES_PER_FAMILY_CANON = HEXES_PER_FAMILY
TOTAL_HEXES_CANON = TOTAL_HEXES


def hex_linear_index(family_id: int, hex_within_family: int) -> int:
    """Global linear hex index u ∈ [0, Nh)."""
    if not (0 <= family_id < NUM_FAMILIES_HEX) or not (0 <= hex_within_family < HEXES_PER_FAMILY_CANON):
        raise ValueError("family_id or hex_within_family out of range")
    return int(family_id * HEXES_PER_FAMILY_CANON + hex_within_family)


def family_and_local_from_linear(u: int) -> tuple[int, int]:
    """Inverse map: u → (family m, local hex index)."""
    if not (0 <= u < TOTAL_HEXES_CANON):
        raise ValueError(f"hex index u={u} out of [0, {TOTAL_HEXES_CANON})")
    m = u // HEXES_PER_FAMILY_CANON
    j = u % HEXES_PER_FAMILY_CANON
    return m, j


def build_ring_laplacian(n_hex: int) -> np.ndarray:
    """
    Unweighted cycle graph Laplacian L = D - W, W_ij = 1 on ring neighbors.
    Used per family block when W_H is intra-family ring (canon §5).
    """
    if n_hex < 2:
        raise ValueError("n_hex must be >= 2 for ring")
    w = np.zeros((n_hex, n_hex), dtype=np.float64)
    for i in range(n_hex):
        w[i, (i - 1) % n_hex] = 1.0
        w[i, (i + 1) % n_hex] = 1.0
    d = np.diag(w.sum(axis=1))
    return d - w


def build_uniform_hex_resistance(
    n_families: int,
    n_hex_per_family: int,
    r: float,
) -> np.ndarray:
    """R_H diagonal values r_u ≡ r as (n_families, n_hex_per_family)."""
    if r < 0:
        raise ValueError("r must be non-negative")
    return np.full((n_families, n_hex_per_family), float(r), dtype=np.float64)


def family_source_to_hex_uniform(s_family: np.ndarray | Sequence[float]) -> np.ndarray:
    """
    S_H[m, j] = S_f[m] / N_hex — deterministic P_CH-style spread when only family injection exists.
    s_family length = n_families (first k components; pad or slice to match n_families).
    """
    sf = np.asarray(s_family, dtype=np.float64).reshape(-1)
    n = sf.shape[0]
    out = np.zeros((n, HEXES_PER_FAMILY_CANON), dtype=np.float64)
    denom = float(HEXES_PER_FAMILY_CANON)
    for m in range(min(n, out.shape[0])):
        out[m, :] = sf[m] / denom
    return out


def concept_family_weights_to_hex_source(
    weights_by_family: np.ndarray | Sequence[float],
    *,
    n_hex_per_family: int | None = None,
) -> np.ndarray:
    """
    **S_H** for **S_H = P_CH A** when **P_CH = D P_CF** (D = per-family uniform spread over hexes).

    Here ``weights_by_family`` ≡ **P_CF A** (length Nf). Returns shape (Nf, n_hex_per_family).
    """
    nh = n_hex_per_family or HEXES_PER_FAMILY_CANON
    wf = np.maximum(0.0, np.asarray(weights_by_family, dtype=np.float64).reshape(-1))
    n_f = wf.shape[0]
    out = np.zeros((n_f, nh), dtype=np.float64)
    for m in range(n_f):
        out[m, :] = wf[m] / float(nh)
    return out
