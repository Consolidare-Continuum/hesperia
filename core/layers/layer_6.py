# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 Societatea cu Răspundere Limitată "CONSOLIDARE CONTINUUM" (IDNO 1026023120076). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from CONSOLIDARE CONTINUUM S.R.L.
# See LEGAL_NOTICE.md for full terms.

"""
Engine 0.5.0 — Layer-6 (39_SPEC); “v0.4.x” = legacy SPEC-era label only.
25 variables: sensitivity, curvature, rank, depth growth, Lyapunov, stability.
Inputs: L1, L2 (with MASS_AT_DEPTH); when no perturbation, stub with 0/1.0.
Downstream: L7 (CONSIST_STABILITY_REGIME_VALID, MAX_CHAOS_LEVEL), L8 (SI_GLOBAL_STABILITY), L9.

HES-MATH-BEHAV-54..57 (2026-08-05): gradient / curvature / Group-IV Newtonian +
functional slots stay PARTIAL identity constants until a second (perturbed) engine
pass is wired into this signature. Do not invent finite-difference values from
MASS_AT_DEPTH alone — 39_SPEC formulas require E(x±ε). Formula notes live next to
each assignment below.
"""

from __future__ import annotations

import math
import time
from typing import Any

from core.contracts.layer_contract import LayerInput, LayerOutput

eps = 1e-12

# Reserved slots that remain PARTIAL without perturbation series (inventory HES-MATH-BEHAV-54).
L6_PARTIAL_GRADIENT_SLOTS = (
    "COVERAGE_GRADIENT",
    "ENTROPY_GRADIENT",
)
L6_PARTIAL_CURVATURE_SLOTS = (
    "SECOND_ORDER_RESPONSE",
    "DOMINANCE_CURVATURE",
    "ENTROPY_CURVATURE",
)
L6_PARTIAL_GROUP_IV_SLOTS = (
    "POTENTIAL_GRADIENT",
    "ESCAPE_ENERGY_THRESHOLD",
    "FORCE_ANALOG_MAGNITUDE",
    "MONOTONICITY_CHECK",
    "FIXED_POINT_DETECTION",
    "CYCLE_DETECTION_FUNCTIONAL",
)


def compute_L6(
    l1: dict[str, Any],
    l2: dict[str, Any],
    mass_at_depth: list[float] | None = None,
    F: int = 288,
    eps_val: float = eps,
) -> dict[str, Any]:
    """
    Compute Layer-6 25 variables (39_SPEC).
    When no perturbation data: INPUT_PERTURBATION_RESPONSE=0, DOMINANT_FAMILY_STABILITY=True,
    gradients/curvature/rank/condition/spectral_gap=0 or 1.0; depth growth from mass_at_depth when provided.
    LYAPUNOV_ESTIMATE = 0.0 (stable); GLOBAL_STABILITY_SCORE = 1.0; CONCEPTUAL_COHERENCE_INDEX from L1/L2.
    """
    mass_at_depth = mass_at_depth or l2.get("MASS_AT_DEPTH") or [0.0]
    norm_entropy = float(l1.get("NORMALIZED_FAMILY_ENTROPY", 0.0))

    # I. No perturbation → 0 or identity (sealed safe defaults)
    INPUT_PERTURBATION_RESPONSE = 0.0
    DOMINANT_FAMILY_STABILITY = True
    # PARTIAL (HES-MATH-BEHAV-55): 39_SPEC (coverage(x+ε)-coverage(x))/(‖ε‖+eps) — needs E(x+ε).
    COVERAGE_GRADIENT = 0.0
    # PARTIAL (HES-MATH-BEHAV-55): 39_SPEC (entropy(x+ε)-entropy(x))/(‖ε‖+eps) — needs E(x+ε).
    ENTROPY_GRADIENT = 0.0
    STABILITY_RADIUS = 1.0
    # PARTIAL (HES-MATH-BEHAV-56): 39_SPEC (y(x+ε)-2y(x)+y(x-ε))/(‖ε‖²+eps) — needs ±ε runs.
    SECOND_ORDER_RESPONSE = 0.0
    # PARTIAL (HES-MATH-BEHAV-56): 39_SPEC (dom(x+ε)-2dom(x)+dom(x-ε))/(‖ε‖²+eps).
    DOMINANCE_CURVATURE = 0.0
    # PARTIAL (HES-MATH-BEHAV-56): 39_SPEC (ent(x+ε)-2ent(x)+ent(x-ε))/(‖ε‖²+eps).
    ENTROPY_CURVATURE = 0.0
    HIT_VECTOR_RANK = 1
    PRINCIPAL_COMPONENT_ENERGY_RATIO = 1.0
    CONDITION_NUMBER = 1.0
    SPECTRAL_GAP = 0.0

    # III. Depth growth from mass_at_depth (live where data exists)
    if len(mass_at_depth) >= 2 and mass_at_depth[0] > 0:
        DEPTH_GROWTH_RATIO = mass_at_depth[1] / (mass_at_depth[0] + eps_val)
    else:
        DEPTH_GROWTH_RATIO = 0.0
    if len(mass_at_depth) >= 3:
        FIBONACCI_DEVIATION_SCORE = abs(
            mass_at_depth[2] - (mass_at_depth[1] + mass_at_depth[0])
        )
    else:
        FIBONACCI_DEVIATION_SCORE = 0.0
    EXPONENTIAL_FIT_ERROR = 0.0
    POWER_LAW_FIT_ERROR = 0.0

    # IV. Newtonian / functional analogies — PARTIAL (HES-MATH-BEHAV-57); need E(x±ε) / E∘E.
    # 39_SPEC: POTENTIAL_GRADIENT = dominance(x+ε)-dominance(x)
    POTENTIAL_GRADIENT = 0.0
    # 39_SPEC: min ‖ε‖ that flips dominant family; no-flip → max tested (here identity 1.0)
    ESCAPE_ENERGY_THRESHOLD = 1.0
    # 39_SPEC: ‖∇dominance‖ finite-difference magnitude
    FORCE_ANALOG_MAGNITUDE = 0.0
    # 39_SPEC: monotonicity over perturbation sample (vacuous True without sample)
    MONOTONICITY_CHECK = True
    # 39_SPEC: E(E(x))≈E(x); vacuous True without re-entrant E
    FIXED_POINT_DETECTION = True
    # 39_SPEC: E³(x)≈x period-3; vacuous False without re-entrant E
    CYCLE_DETECTION_FUNCTIONAL = False

    LYAPUNOV_ESTIMATE = 0.0
    GLOBAL_STABILITY_SCORE = 1.0 / (1.0 + CONDITION_NUMBER + abs(LYAPUNOV_ESTIMATE))
    CONCEPTUAL_COHERENCE_INDEX = STABILITY_RADIUS * (1.0 - norm_entropy) * GLOBAL_STABILITY_SCORE

    return {
        "INPUT_PERTURBATION_RESPONSE": INPUT_PERTURBATION_RESPONSE,
        "DOMINANT_FAMILY_STABILITY": DOMINANT_FAMILY_STABILITY,
        "COVERAGE_GRADIENT": COVERAGE_GRADIENT,
        "ENTROPY_GRADIENT": ENTROPY_GRADIENT,
        "STABILITY_RADIUS": STABILITY_RADIUS,
        "SECOND_ORDER_RESPONSE": SECOND_ORDER_RESPONSE,
        "DOMINANCE_CURVATURE": DOMINANCE_CURVATURE,
        "ENTROPY_CURVATURE": ENTROPY_CURVATURE,
        "HIT_VECTOR_RANK": HIT_VECTOR_RANK,
        "PRINCIPAL_COMPONENT_ENERGY_RATIO": PRINCIPAL_COMPONENT_ENERGY_RATIO,
        "CONDITION_NUMBER": CONDITION_NUMBER,
        "SPECTRAL_GAP": SPECTRAL_GAP,
        "DEPTH_GROWTH_RATIO": DEPTH_GROWTH_RATIO,
        "FIBONACCI_DEVIATION_SCORE": FIBONACCI_DEVIATION_SCORE,
        "EXPONENTIAL_FIT_ERROR": EXPONENTIAL_FIT_ERROR,
        "POWER_LAW_FIT_ERROR": POWER_LAW_FIT_ERROR,
        "POTENTIAL_GRADIENT": POTENTIAL_GRADIENT,
        "ESCAPE_ENERGY_THRESHOLD": ESCAPE_ENERGY_THRESHOLD,
        "FORCE_ANALOG_MAGNITUDE": FORCE_ANALOG_MAGNITUDE,
        "MONOTONICITY_CHECK": MONOTONICITY_CHECK,
        "FIXED_POINT_DETECTION": FIXED_POINT_DETECTION,
        "CYCLE_DETECTION_FUNCTIONAL": CYCLE_DETECTION_FUNCTIONAL,
        "LYAPUNOV_ESTIMATE": LYAPUNOV_ESTIMATE,
        "GLOBAL_STABILITY_SCORE": GLOBAL_STABILITY_SCORE,
        "CONCEPTUAL_COHERENCE_INDEX": CONCEPTUAL_COHERENCE_INDEX,
    }


def run(input: LayerInput) -> LayerOutput:
    """Layer-6 public entry point. Consumes LayerInput, returns LayerOutput. No other public entry points."""
    t0 = time.perf_counter()
    meta = input.metadata
    layers = meta.get("layers", {})
    l1 = layers.get(1)
    l2 = layers.get(2)
    if not l1 or not l2:
        raise ValueError("Layer 6 requires layer 1 and 2 results in input.metadata['layers']")
    F = int(meta.get("F", 288))
    result = compute_L6(l1, l2, F=F)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return LayerOutput(
        layer_id=6,
        result=result,
        diagnostics={"layer_id": 6, "execution_time_ms": round(elapsed_ms, 6)},
    )
