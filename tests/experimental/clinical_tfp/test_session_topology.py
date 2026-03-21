# HESPERIA — Tests for LEVEL 10 Session topology (temporal dynamics)
"""Segmentation by token windows, segment analysis, state transitions, aggression curve."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[3]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def test_segmentation_works() -> None:
    from research.clinical_tfp.session_topology import segment_session

    # empty
    assert segment_session("") == []
    assert segment_session("  ", window_size=80) == []

    # short text → one segment
    text = "Пациент говорит спокойно."
    segs = segment_session(text, window_size=80)
    assert len(segs) == 1
    assert "пациент" in segs[0].lower() or "говорит" in segs[0].lower()

    # many tokens → multiple windows
    words = ["слово"] * 200
    long_text = " ".join(words)
    segs = segment_session(long_text, window_size=80)
    assert len(segs) == 3  # 80, 80, 40
    assert all(isinstance(s, str) for s in segs)
    assert len(segs[0].split()) == 80
    assert len(segs[1].split()) == 80
    assert len(segs[2].split()) == 40

    # custom window
    segs_small = segment_session(long_text, window_size=50)
    assert len(segs_small) == 4  # 50*4 = 200


def test_segment_analysis_returns_results() -> None:
    from research.clinical_tfp.session_topology import analyze_session_segments

    text = "Пациент сначала говорит спокойно. Затем обвиняет терапевта."
    results = analyze_session_segments(text, window_size=20)
    assert isinstance(results, list)
    assert len(results) >= 1
    for r in results:
        assert "areas" in r
        assert "families" in r
        assert "concepts" in r
        assert isinstance(r["areas"], dict)
        assert isinstance(r["families"], dict)
        assert isinstance(r["concepts"], dict)


def test_transitions_detected_correctly() -> None:
    from research.clinical_tfp.session_topology import detect_state_transitions

    # no transition
    segs = [{"areas": {"A2": 0.5}}, {"areas": {"A2": 0.6}}]
    assert detect_state_transitions(segs) == []

    # one transition A2 → A3
    segs = [
        {"areas": {"A2": 0.8, "A3": 0.2}},
        {"areas": {"A2": 0.2, "A3": 0.9}},
    ]
    assert detect_state_transitions(segs) == [["A2", "A3"]]

    # A2 → A3 → A4
    segs = [
        {"areas": {"A2": 0.9}},
        {"areas": {"A3": 0.9}},
        {"areas": {"A4": 0.9}},
    ]
    assert detect_state_transitions(segs) == [["A2", "A3"], ["A3", "A4"]]

    # single segment
    assert detect_state_transitions([{"areas": {"A2": 0.5}}]) == []


def test_aggression_curve_produced() -> None:
    from research.clinical_tfp.session_topology import detect_aggression_escalation

    segs = [
        {"areas": {"A4": 0.10}},
        {"areas": {"A4": 0.22}},
        {"areas": {"A4": 0.54}},
        {"areas": {"A4": 0.83}},
    ]
    curve = detect_aggression_escalation(segs)
    assert curve == [0.10, 0.22, 0.54, 0.83]

    # missing A4 → 0
    segs = [{"areas": {"A2": 0.5}}, {"areas": {}}]
    assert detect_aggression_escalation(segs) == [0.0, 0.0]


def test_extract_and_build_area_curves() -> None:
    from research.clinical_tfp.session_topology import (
        AREA_CURVE_MAP,
        build_area_curves,
        extract_area_curve,
    )

    segs = [
        {"areas": {"A2": 0.1, "A4": 0.4, "A7": 0.2}},
        {"areas": {"A2": 0.3, "A4": 0.5, "A5": 0.9}},
    ]
    assert extract_area_curve(segs, "A4") == [0.4, 0.5]
    curves = build_area_curves(segs)
    assert set(curves.keys()) == set(AREA_CURVE_MAP.keys())
    assert curves["aggression"] == [0.4, 0.5]
    assert curves["anxiety"] == [0.1, 0.3]
    assert curves["control"] == [0.0, 0.9]
    assert len(curves["shame"]) == 2


def test_postprocess_area_curves_share_and_smooth() -> None:
    from research.clinical_tfp.session_topology import postprocess_area_curves

    segs = [
        {"areas": {"A4": 0.4, "A2": 0.6}},
        {"areas": {"A4": 0.8, "A2": 0.2}},
    ]
    curves, meta, rel = postprocess_area_curves(
        segs, area_competition="share", smooth_alpha=0.7, session_center_curves=True
    )
    assert meta["area_competition"] == "share"
    assert curves["aggression"][0] == 0.4
    assert curves["aggression"][1] == pytest.approx(0.7 * 0.8 + 0.3 * 0.4)
    assert "aggression" in rel
    mu = sum(curves["aggression"]) / len(curves["aggression"])
    assert rel["aggression"][0] == pytest.approx(curves["aggression"][0] - mu)
    raw_only, meta2, _ = postprocess_area_curves(
        segs, area_competition="share", smooth_alpha=None, session_center_curves=False
    )
    assert raw_only["aggression"] == [0.4, 0.8]
    assert meta2["smooth"] is None


def test_build_session_state_sequence() -> None:
    from research.clinical_tfp.session_topology import build_session_state_sequence

    segs = [
        {"areas": {"A2": 0.9}},
        {"areas": {"A3": 0.8}},
        {"areas": {"A3": 0.7}},
        {"areas": {"A4": 0.9}},
        {"areas": {"A7": 0.6}},
    ]
    seq = build_session_state_sequence(segs)
    assert seq == ["A2", "A3", "A3", "A4", "A7"]


def test_detect_defense_shifts() -> None:
    from research.clinical_tfp.session_topology import detect_defense_shifts

    segs = [
        {"families": {"A3_F1": 0.9}},
        {"families": {"A3_F5": 0.8}},
        {"families": {"A2_F1": 0.5}},  # no A3 → empty
    ]
    timeline = detect_defense_shifts(segs)
    assert len(timeline) == 3
    assert timeline[0] == "splitting"
    assert timeline[1] == "projective_identification"
    assert timeline[2] == ""


def test_run_session_topology_output_structure() -> None:
    from research.clinical_tfp.session_topology import run_session_topology

    text = (
        "Пациент сначала говорит спокойно, затем начинает обвинять терапевта, "
        "говорит что тот его предал и выражает сильную злость."
    )
    out = run_session_topology(text, window_size=15)
    assert "segments" in out
    assert "transitions" in out
    assert "area_curves" in out
    assert "aggression_curve" in out
    assert "state_sequence" in out
    assert "defense_timeline" in out
    assert "curve_projection_meta" in out
    assert "area_curves_session_relative" in out
    cpm = out["curve_projection_meta"]
    assert cpm.get("calibration_reference_bands", {}).get("low_tension") == 0.2
    assert isinstance(cpm.get("segment_dominance_confidence"), list)
    assert cpm.get("lexical_controls", {}).get("per_concept_score_cap") == 8.0
    assert cpm.get("lexical_controls", {}).get("evidence_volume_normalize") is True
    assert cpm.get("engine_params", {}).get("area_competition") == "softmax"
    assert cpm.get("area_curve_map", {}).get("aggression") == "A4"
    assert isinstance(out["segments"], list)
    assert isinstance(out["transitions"], list)
    assert isinstance(out["area_curves"], dict)
    assert isinstance(out["aggression_curve"], list)
    assert isinstance(out["state_sequence"], list)
    assert isinstance(out["defense_timeline"], list)
    assert out["aggression_curve"] == out["area_curves"]["aggression"]
    for _name, series in out["area_curves"].items():
        assert isinstance(series, list)
        assert len(series) == len(out["segments"])
    assert len(out["aggression_curve"]) == len(out["segments"])
    assert len(out["state_sequence"]) == len(out["segments"])
    assert len(out["defense_timeline"]) == len(out["segments"])
