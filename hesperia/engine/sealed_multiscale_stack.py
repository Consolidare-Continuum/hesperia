# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""
Sealed pipeline: concept hits → hex → local microphysics → family bridge → area → product signals → HSPR.

Engine Dynamics v0.5 seal (docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md). Shipping path: ``runtime.services.analysis_service``
→ this module → ``project_to_public``. Legacy ``sphere.pipeline.run_pipeline`` is dev-only
(``HESPERIA_SPHERE_PIPELINE_DEV=1``).

**Hex causality:** ``compute_product_signals`` consumes only ``A_hex`` tensors (before/after step).
Family ``F`` and area vectors are written for aggregation / projection only, not for signal formulas.

Specs: hex_family_bridge.md, hex_microphysics_canon §7b, product_signal_layer.md, hspr_calibration_index.md
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import numpy as np

from hesperia.extensions.dynamics.e2e_bridge import markers_to_concept_activation
from hesperia.engine.hex_family_bridge import compute_family_activation, load_hex_family_overrides
from hesperia.engine.energy import EnergyControlParams, EnergyMode, compute_energy_hex_2d
from hesperia.engine.hex_matrix_builders import (
    HEXES_PER_FAMILY_CANON,
    apply_pch_to_concept_activation,
    build_ring_laplacian,
    build_uniform_hex_resistance,
)
from hesperia.engine.pch_loader import load_pch
from hesperia.system.version import pch_bundle_id
from hesperia.engine.hex_dynamics import LocalHexMicrophysicsParams, step_hex_local_microphysics
from hesperia.engine.hspr_index import compute_hspr_index, field_state_from_hex_stack
from hesperia.engine.product_signals import compute_product_signals, hex_hotspot_ring_values, try_triz_contradiction_pressure

NUM_FAMILIES = 288
NUM_AREAS = 12
FAM_PER_AREA = 24


def _area_from_family(F: np.ndarray) -> np.ndarray:
    f = np.asarray(F, dtype=np.float64).reshape(NUM_FAMILIES)
    a = np.zeros(NUM_AREAS, dtype=np.float64)
    for j in range(NUM_FAMILIES):
        a[j // FAM_PER_AREA] += f[j]
    return a


def _require_hex_for_signals(A0: np.ndarray, A1: np.ndarray) -> None:
    if A0 is None or A1 is None:
        raise RuntimeError("Hex layer required for signal computation (missing A_hex tensor)")
    if A0.size == 0 or A1.size == 0:
        raise RuntimeError("Hex layer required for signal computation (empty A_hex)")
    if A0.shape != A1.shape or len(A0.shape) != 2:
        raise RuntimeError("Hex layer required for signal computation (invalid A_hex shape)")


def run_sealed_multiscale_stack(
    text: str,
    assets_root: Path,
    *,
    apply_local_step: bool = True,
    hotspot_list_cap: int = 96,
    use_triz_contradiction: bool = False,
) -> dict[str, Any]:
    """
    Dict A path proxy: structural family hits → hex grid → dynamics → F / area (aggregates) → hex signals → hspr_index.
    """
    assets = Path(assets_root)
    concept_act = markers_to_concept_activation(text, assets)
    hits = concept_act["a_concept_counts"]
    h_raw = np.asarray(hits, dtype=np.float64)
    marker_concept_mass = float(h_raw.sum())
    uniform_concept_prior_fallback_used = marker_concept_mass <= 0.0
    h = h_raw.copy()
    if uniform_concept_prior_fallback_used:
        h = np.ones(NUM_FAMILIES, dtype=np.float64) / NUM_FAMILIES
    a_concept = np.asarray(h, dtype=np.float64).reshape(-1)
    pch = load_pch()
    A0 = apply_pch_to_concept_activation(
        a_concept, pch, n_hex_per_family=HEXES_PER_FAMILY_CANON
    )
    pch_bundle_version = pch_bundle_id()
    R = build_uniform_hex_resistance(NUM_FAMILIES, HEXES_PER_FAMILY_CANON, 0.35) + 0.15 / (A0 + 0.08)

    from hesperia.engine.matrix_loader import load_production_matrices

    _mats = load_production_matrices()
    C_F = np.asarray(_mats["C_F"], dtype=np.float64)
    matrix_bundle_version = str(_mats["bundle_version"])

    L_ring = build_ring_laplacian(HEXES_PER_FAMILY_CANON)
    hex_energy_control = EnergyControlParams(mode=EnergyMode.soft, epsilon_energy_soft=1e-4)
    hex_energy_trace: list[float] = []
    if apply_local_step:
        s_ref = A0.copy()
        e0 = float(compute_energy_hex_2d(A0, L_ring, C_F, s_ref, lam_contra=1.0))
        A1 = step_hex_local_microphysics(
            A0,
            R,
            C_F,
            params=LocalHexMicrophysicsParams(),
            clip_nonneg=True,
            S_H=s_ref,
            L_ring=L_ring,
            energy_control=hex_energy_control,
            lam_contra=1.0,
        )
        e1 = float(compute_energy_hex_2d(A1, L_ring, C_F, s_ref, lam_contra=1.0))
        hex_energy_trace = [e0, e1]
    else:
        A1 = A0.copy()

    hex_upstream_fallback_used = False
    if float(np.sum(A1)) <= 0.0 and float(np.sum(A0)) > 0.0:
        A1 = np.maximum(A0, 0.0)
        hex_upstream_fallback_used = True
        if apply_local_step:
            s_ref_fb = A0.copy()
            e1_fb = float(compute_energy_hex_2d(A1, L_ring, C_F, s_ref_fb, lam_contra=1.0))
            hex_energy_trace = [hex_energy_trace[0], e1_fb] if hex_energy_trace else [e1_fb]

    _require_hex_for_signals(A0, A1)

    ov = load_hex_family_overrides()
    F = compute_family_activation(
        A1, n_families=NUM_FAMILIES, n_hex_per_family=HEXES_PER_FAMILY_CANON, overrides=ov
    )
    area = _area_from_family(F)

    sig = compute_product_signals(A0, A1, C_F=C_F, dt=1.0)
    fs = field_state_from_hex_stack(A1, sig)
    hspr = compute_hspr_index(fs)

    flat_hot = hex_hotspot_ring_values(
        A1,
        lam=0.45,
        cap=hotspot_list_cap,
        max_families=40,
        max_slots=min(HEXES_PER_FAMILY_CANON, 8),
    )

    if use_triz_contradiction:
        triz_p = try_triz_contradiction_pressure(text)
        if triz_p is not None:
            sig = {**sig, "contradiction_pressure_triz": triz_p}

    trace_cap = 64
    mtrace = concept_act.get("marker_concept_trace") or []
    interpretability_trace = {
        "stages": ["markers", "concept", "hex_microcell", "family_aggregate", "area_aggregate"],
        "registry_version": concept_act.get("registry_version"),
        "n_concept": concept_act.get("n_concept"),
        "marker_concept_sample": mtrace[:trace_cap],
    }

    out: dict[str, Any] = {
        "execution_flow": "sealed_multiscale_v1",
        "matrix_bundle_version": matrix_bundle_version,
        "pch_bundle_version": pch_bundle_version,
        "concept_layer": {
            "registry_version": concept_act.get("registry_version"),
            "n_concept": concept_act.get("n_concept"),
            "a_concept_nonzero_count": int(np.count_nonzero(h)),
            "marker_concept_mass": round(marker_concept_mass, 12),
            "uniform_concept_prior_fallback_used": uniform_concept_prior_fallback_used,
            "hex_upstream_fallback_used": hex_upstream_fallback_used,
            "interpretability_trace": interpretability_trace,
        },
        "hex_energy_trace": [round(x, 10) for x in hex_energy_trace],
        "hex_energy_mode": hex_energy_control.mode.value if apply_local_step else "none",
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
    if os.environ.get("HESPERIA_SEALED_DLCR_SIDECAR", "").strip().lower() in ("1", "true", "yes", "on"):
        try:
            from hesperia.engine.lexical_concept.pipeline import run_dlcr_pipeline

            repo = Path(__file__).resolve().parents[2]
            d_bundle = run_dlcr_pipeline(text, repo_root=repo)
            cw = d_bundle.get("concept_weights") or {}
            top_c = sorted(cw.items(), key=lambda x: -float(x[1]))[:12]
            out["clinical_resolution_sidecar"] = {
                "matched_span_count": d_bundle.get("lexical_hits_accepted"),
                "resource_versions": d_bundle.get("resource_versions"),
                "top_concepts": [{"concept_id": k, "weight": round(float(v), 6)} for k, v in top_c],
            }
        except Exception as ex:  # noqa: BLE001
            out["clinical_resolution_sidecar"] = {"_error": str(ex)}
    return out
