# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""
Sealed pipeline: concept hits → hex → local microphysics → family bridge → area → product signals → HSPR.

Engine Dynamics v0.5 seal (docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md). Gaps: hits→hex is uniform split, not full P_CH;
sphere/main pipeline still parallel — refactor should unify entry.
Specs: hex_family_bridge.md, hex_microphysics_canon §7b, product_signal_layer.md, hspr_calibration_index.md
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from hesperia.extensions.dynamics.e2e_bridge import _hits_288
from hesperia.engine.hex_family_bridge import compute_family_activation, load_hex_family_overrides
from hesperia.engine.hex_matrix_builders import HEXES_PER_FAMILY_CANON, build_uniform_hex_resistance
from hesperia.engine.hex_dynamics import LocalHexMicrophysicsParams, step_hex_local_microphysics
from hesperia.engine.hspr_index import compute_hspr_index, field_state_from_hex_stack
from hesperia.engine.product_signals import compute_product_signals

NUM_FAMILIES = 288
NUM_AREAS = 12
FAM_PER_AREA = 24


def _area_from_family(F: np.ndarray) -> np.ndarray:
    f = np.asarray(F, dtype=np.float64).reshape(NUM_FAMILIES)
    a = np.zeros(NUM_AREAS, dtype=np.float64)
    for j in range(NUM_FAMILIES):
        a[j // FAM_PER_AREA] += f[j]
    return a


def run_sealed_multiscale_stack(
    text: str,
    assets_root: Path,
    *,
    apply_local_step: bool = True,
    hotspot_list_cap: int = 96,
    use_triz_contradiction: bool = False,
) -> dict[str, Any]:
    """
    Dict A path proxy: structural family hits → hex grid → dynamics → F → area → signals → hspr_index.
    """
    assets = Path(assets_root)
    hits = _hits_288(text, assets)
    h = np.asarray(hits, dtype=np.float64)
    total = float(h.sum())
    if total <= 0:
        h = np.ones(NUM_FAMILIES, dtype=np.float64) / NUM_FAMILIES
        total = 1.0
    from hesperia.engine.hex_matrix_builders import concept_family_weights_to_hex_source

    A0 = concept_family_weights_to_hex_source(h, n_hex_per_family=HEXES_PER_FAMILY_CANON)
    R = build_uniform_hex_resistance(NUM_FAMILIES, HEXES_PER_FAMILY_CANON, 0.35) + 0.15 / (A0 + 0.08)

    from hesperia.extensions.dynamics.semantic_field_v1 import build_default_matrices

    C_F = np.asarray(build_default_matrices()["C"], dtype=np.float64)

    if apply_local_step:
        A1 = step_hex_local_microphysics(
            A0, R, C_F, params=LocalHexMicrophysicsParams(), clip_nonneg=True
        )
    else:
        A1 = A0.copy()

    ov = load_hex_family_overrides()
    F = compute_family_activation(
        A1, n_families=NUM_FAMILIES, n_hex_per_family=HEXES_PER_FAMILY_CANON, overrides=ov
    )
    area = _area_from_family(F)

    sig = compute_product_signals(A0, A1, F, C_F, dt=1.0)
    fs = field_state_from_hex_stack(A1, sig)
    hspr = compute_hspr_index(fs)

    flat_hot = []
    lam = 0.45
    for m in range(min(NUM_FAMILIES, 40)):
        row = A1[m]
        for k in range(min(HEXES_PER_FAMILY_CANON, 8)):
            nbr = row[(k - 1) % HEXES_PER_FAMILY_CANON] + row[(k + 1) % HEXES_PER_FAMILY_CANON]
            flat_hot.append(float(row[k] + lam * nbr))
        if len(flat_hot) >= hotspot_list_cap:
            break
    if use_triz_contradiction:
        try:
            from hesperia.engine.product_signals import try_triz_contradiction_pressure

            triz_p = try_triz_contradiction_pressure(text)
            if triz_p is not None:
                sig = {**sig, "contradiction_pressure_triz": triz_p}
        except Exception:
            pass

    return {
        "pipeline": "sealed_multiscale_v1",
        "hex_activation_map": {
            "shape": [NUM_FAMILIES, HEXES_PER_FAMILY_CANON],
            "sample_ring_slice": A1[: min(8, NUM_FAMILIES), : min(12, HEXES_PER_FAMILY_CANON)].round(6).tolist(),
            "total_mass": float(A1.sum()),
        },
        "family_activation_vector": F.round(8).tolist(),
        "area_activation_vector": area.round(8).tolist(),
        "hotspot_map": {"sample_values": [round(x, 6) for x in flat_hot[:hotspot_list_cap]]},
        "contradiction_pressure": round(sig["contradiction_pressure"], 8),
        "propagation_strength": round(sig["propagation_strength"], 8),
        "narrative_density": round(sig["narrative_density"], 8),
        "innovation_index": round(sig["innovation_potential"], 8),
        "hspr_index": round(hspr["hspr_index"], 8),
        "hspr_components": hspr["components_hat"],
        "product_signals": {k: round(float(v), 8) if isinstance(v, (int, float)) else v for k, v in sig.items()},
    }
