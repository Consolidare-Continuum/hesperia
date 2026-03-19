# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""
Canonical product signals — **Engine Dynamics v0.5** (product_signal_layer.md).

TRIZ contradiction is optional (try_triz_*); default P from C_F @ family vector — swampy if
TRIZ and structural P diverge; document which KPI uses which.
"""

from __future__ import annotations

from typing import Any

import numpy as np

__all__ = ["compute_product_signals"]


def compute_product_signals(
    A_before: np.ndarray,
    A_after: np.ndarray,
    F_family: np.ndarray,
    C_F: np.ndarray | None = None,
    *,
    lam: float = 0.45,
    active_theta: float = 1e-9,
    dt: float = 1.0,
) -> dict[str, Any]:
    """
    Narrative hotspot (mean), contradiction pressure, propagation strength,
    narrative density, innovation potential.
    """
    a0 = np.asarray(A_before, dtype=np.float64)
    a1 = np.asarray(A_after, dtype=np.float64)
    if a0.shape != a1.shape:
        raise ValueError("A_before and A_after same shape")
    nf, nh = a0.shape

    hot_sum = 0.0
    ncell = nf * nh
    for m in range(nf):
        row = a0[m]
        for k in range(nh):
            nbr = row[(k - 1) % nh] + row[(k + 1) % nh]
            hot_sum += float(row[k] + lam * nbr)
    hotspot_mean = hot_sum / max(ncell, 1)

    dA = np.abs(a1 - a0)
    propagation_strength = float(np.mean(dA) / max(dt, 1e-12))

    flat1 = a1.ravel()
    active = int(np.sum(flat1 > active_theta))
    narrative_density = float(np.sum(flat1) / max(active, 1))

    f = np.asarray(F_family, dtype=np.float64).reshape(-1)
    f = np.maximum(f, 0.0)
    fs = float(f.sum())
    if fs > 0:
        p = f / fs
        hhi = float(np.sum(p * p))
        novelty = float(np.clip(1.0 - hhi, 0.0, 1.0))
    else:
        novelty = 0.0

    c = np.asarray(C_F, dtype=np.float64) if C_F is not None else np.zeros((nf, nf))
    if c.shape == (nf, nf) and fs > 0:
        contradiction_pressure = float(f @ (c @ f))
    else:
        contradiction_pressure = 0.0

    contradiction_density = contradiction_pressure / max(fs * fs, 1e-12)
    innovation_potential = float(np.clip(contradiction_density * novelty, 0.0, 1e6))

    return {
        "narrative_hotspot_mean": hotspot_mean,
        "contradiction_pressure": contradiction_pressure,
        "propagation_strength": propagation_strength,
        "narrative_density": narrative_density,
        "innovation_potential": float(np.clip(innovation_potential, 0.0, 100.0)),
        "novelty_index": novelty,
    }


def try_triz_contradiction_pressure(text: str) -> float | None:
    """Optional TRIZ-derived P; None if unavailable."""
    try:
        from hesperia.extensions.triz.pipeline import run_triz_analysis_complete

        r = run_triz_analysis_complete(text[:2000])
        d = r.get("contradiction_density") or r.get("commercial_intel", {}).get("contradiction_density")
        return float(d) if d is not None else None
    except Exception:
        return None
