# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""HES-MATH-BEHAV-54..58 — L6 gradient/curvature/Group-IV PARTIAL inventory + sealed defaults."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from core.layers.layer_6 import (
    L6_PARTIAL_CURVATURE_SLOTS,
    L6_PARTIAL_GRADIENT_SLOTS,
    L6_PARTIAL_GROUP_IV_SLOTS,
    compute_L6,
)


def test_l6_partial_slot_inventory_complete() -> None:
    """HES-MATH-BEHAV-54: reserved gradient / curvature / Group-IV names are enumerated."""
    assert set(L6_PARTIAL_GRADIENT_SLOTS) == {"COVERAGE_GRADIENT", "ENTROPY_GRADIENT"}
    assert set(L6_PARTIAL_CURVATURE_SLOTS) == {
        "SECOND_ORDER_RESPONSE",
        "DOMINANCE_CURVATURE",
        "ENTROPY_CURVATURE",
    }
    assert set(L6_PARTIAL_GROUP_IV_SLOTS) == {
        "POTENTIAL_GRADIENT",
        "ESCAPE_ENERGY_THRESHOLD",
        "FORCE_ANALOG_MAGNITUDE",
        "MONOTONICITY_CHECK",
        "FIXED_POINT_DETECTION",
        "CYCLE_DETECTION_FUNCTIONAL",
    }


def test_l6_partial_stubs_keep_sealed_identity() -> None:
    """Without perturbation, PARTIAL slots stay safe identity constants (no invented FD)."""
    l1 = {"NORMALIZED_FAMILY_ENTROPY": 0.25}
    l2 = {"MASS_AT_DEPTH": [4.0, 2.0, 1.0]}
    out = compute_L6(l1, l2)
    assert out["COVERAGE_GRADIENT"] == 0.0
    assert out["ENTROPY_GRADIENT"] == 0.0
    assert out["SECOND_ORDER_RESPONSE"] == 0.0
    assert out["DOMINANCE_CURVATURE"] == 0.0
    assert out["ENTROPY_CURVATURE"] == 0.0
    assert out["POTENTIAL_GRADIENT"] == 0.0
    assert out["ESCAPE_ENERGY_THRESHOLD"] == 1.0
    assert out["FORCE_ANALOG_MAGNITUDE"] == 0.0
    assert out["MONOTONICITY_CHECK"] is True
    assert out["FIXED_POINT_DETECTION"] is True
    assert out["CYCLE_DETECTION_FUNCTIONAL"] is False
    # Live depth fields still compute from MASS_AT_DEPTH (ratio uses +eps).
    assert abs(out["DEPTH_GROWTH_RATIO"] - 0.5) < 1e-9
    assert out["FIBONACCI_DEVIATION_SCORE"] == abs(1.0 - (2.0 + 4.0))
    # Composite from sealed CONDITION_NUMBER=1, LYAPUNOV=0 → 0.5
    assert abs(out["GLOBAL_STABILITY_SCORE"] - 0.5) < 1e-12
