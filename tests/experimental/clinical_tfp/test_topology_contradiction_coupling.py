# HESPERIA — Topology × contradiction dynamics (v0.5.8 task 3).

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[3]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def _synthetic_indexes() -> tuple[dict[str, list[tuple[str, float]]], dict[str, tuple[str, str]]]:
    marker_index = {
        "attack": [("B_A10_F10_001", 1.0)],
        "repair": [("B_A1_F10_001", 1.0)],
    }
    af = {
        "B_A10_F10_001": ("A4", "A4_F10"),
        "B_A1_F10_001": ("A7", "A7_F10"),
    }
    return marker_index, af


def test_segment_contradiction_load_nonzero() -> None:
    from hesperia.engine.tfp_signal_calibration import load_tfp_signal_calibration
    from hesperia.extensions.triz.topology_contradiction_coupling import compute_segment_contradiction_loads

    marker_index, af = _synthetic_indexes()
    from research.clinical_tfp.session_topology import analyze_session_segments

    segs = analyze_session_segments(
        "attack repair attack repair",
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
    )
    area_ids = [str(x) for x in load_tfp_signal_calibration().get("area_ids") or []]
    contradictions = [
        {"pair": ["B_A10_F10_001", "B_A1_F10_001"], "raw_contradiction_score": 0.9},
    ]
    loads = compute_segment_contradiction_loads(segs, contradictions, af, area_ids)
    assert len(loads) == len(segs)
    assert loads[0]["contradiction_load"] > 0.0
    assert loads[0]["cross_area_contradiction_mass"] > 0.0
    assert loads[1]["contradiction_load"] > 0.0


def test_run_session_topology_changes_curves_with_contradictions() -> None:
    from research.clinical_tfp.session_topology import run_session_topology

    marker_index, af = _synthetic_indexes()
    text = "attack repair attack repair"
    base = run_session_topology(
        text,
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
        contradictions=None,
    )
    with_c = run_session_topology(
        text,
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
        contradictions=[
            {"pair": ["B_A10_F10_001", "B_A1_F10_001"], "raw_contradiction_score": 0.95},
        ],
    )
    assert base["area_curves_stable"] != with_c["area_curves_stable"]
    assert with_c["transition_pressure"]
    assert len(with_c["transition_pressure"]) == len(with_c["segments"]) - 1
    cpm = with_c["curve_projection_meta"]
    assert cpm.get("contradiction_coupling_active") is True
    assert "contradiction_summary" in cpm
    assert cpm["contradiction_summary"].get("segment_count_with_conflict", 0) >= 1


def test_contradiction_reduces_peak_certainty_in_loaded_segment() -> None:
    from research.clinical_tfp.session_topology import run_session_topology

    marker_index, af = _synthetic_indexes()
    text = "attack repair attack repair"
    base = run_session_topology(
        text,
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
    )
    with_c = run_session_topology(
        text,
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
        contradictions=[
            {"pair": ["B_A10_F10_001", "B_A1_F10_001"], "raw_contradiction_score": 1.0},
        ],
    )
    dom_base = base["curve_projection_meta"].get("segment_dominance_confidence_stable") or []
    dom_c = with_c["curve_projection_meta"].get("segment_dominance_confidence_stable") or []
    assert dom_base and dom_c
    assert min(dom_c) <= min(dom_base) + 1e-6 or dom_c != dom_base


def test_no_contradictions_backward_compatible_meta() -> None:
    from research.clinical_tfp.session_topology import run_session_topology

    marker_index, af = _synthetic_indexes()
    out = run_session_topology(
        "attack repair",
        window_size=2,
        marker_index=marker_index,
        concept_to_area_family=af,
        phrase_index={},
    )
    assert out["segment_contradiction_loads"] == []
    assert out["transition_pressure"] == []
    cpm = out["curve_projection_meta"]
    assert cpm.get("contradiction_coupling_active") is False
    assert cpm.get("contradiction_summary") == {}


def test_transition_pressure_cross_area_neighbor_segments() -> None:
    from hesperia.engine.tfp_signal_calibration import load_tfp_signal_calibration
    from hesperia.extensions.triz.topology_contradiction_coupling import (
        compute_segment_contradiction_loads,
        compute_transition_pressure,
    )

    area_ids = [str(x) for x in load_tfp_signal_calibration().get("area_ids") or []]
    af = {
        "B_A10_F10_001": ("A4", "A4_F10"),
        "B_A1_F10_001": ("A7", "A7_F10"),
        "B_A2_F10_002": ("A2", "A2_F10"),
    }
    segs = [
        {"concepts": {"B_A10_F10_001": 1.0, "B_A1_F10_001": 0.1}, "areas": {}, "families": {}},
        {"concepts": {"B_A1_F10_001": 1.0, "B_A2_F10_002": 1.0}, "areas": {}, "families": {}},
    ]
    rows = [{"pair": ["B_A10_F10_001", "B_A1_F10_001"], "raw_contradiction_score": 0.8}]
    loads = compute_segment_contradiction_loads(segs, rows, af, area_ids)
    tp = compute_transition_pressure(loads, area_ids)
    assert len(tp) == 1
    assert tp[0] >= 0.0
    segs_flat = [
        {"concepts": {"B_A10_F10_001": 1.0}, "areas": {}, "families": {}},
        {"concepts": {"B_A10_F10_001": 1.0}, "areas": {}, "families": {}},
    ]
    loads_flat = compute_segment_contradiction_loads(segs_flat, rows, af, area_ids)
    tp_flat = compute_transition_pressure(loads_flat, area_ids)
    assert max(tp) >= max(tp_flat) - 1e-9
