"""
E2E flow tests: run all Hesperia entrypoints and assert output exists (no calibration).
Covers: analyze (sentence), L1–L9, R1–R4, sphere_math_values, sphere_math_100, and unified run_e2e_all.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def test_e2e_analyze_sentence_output_exists() -> None:
    """Analyze pipeline returns result + extended with expected keys; output exists."""
    from runtime.pipeline.analyze import analyze

    text = "Justice and fairness support social order."
    minimal, extended = analyze(
        text,
        r1_r4=True,
        r1_r4_book_id="e2e_test",
        r1_r4_levels=["R1", "R2", "R3", "R4"],
    )
    assert minimal is not None
    assert isinstance(minimal, dict)
    for key in ("dominant_area", "dominant_family", "governance", "loopability", "tension_energy", "obstacle_score"):
        assert key in minimal, f"result missing {key}"
    assert extended is not None
    assert isinstance(extended, dict)
    assert "r1_r4" in extended or "family_vector" in extended or "dict_b" in extended


def test_e2e_l1_l9_output_exists() -> None:
    """L1–L9 pipeline returns all layers and diagnostics; output exists."""
    from runtime.pipeline.run_l1_through_l9 import run_pipeline_for_text

    text = "justice lie fairness truth good order harm freedom"
    assets = _REPO / "lexicon" / "curated"
    out = run_pipeline_for_text(text, assets_root=assets)
    assert out is not None
    assert "run" in out and out["run"] == "L1_through_L9"
    for lid in range(1, 10):
        key = f"L{lid}"
        assert key in out, f"Layer {key} missing"
        assert isinstance(out[key], dict)
    assert "diagnostics" in out
    assert "L7" in out and "DECISION_STATUS_CODE" in out["L7"]
    assert "L9" in out and "BRAND_WORD_TRUST" in out["L9"]


def test_e2e_r1_r4_output_exists() -> None:
    """R1–R4 pipeline returns units and book_profile; output exists."""
    from runtime.pipeline.r1_r4_pipeline import run_full_pipeline_to_json

    text = "Justice and fairness support social order. Harm and conflict reduce trust."
    result = run_full_pipeline_to_json(text, book_id="e2e_test", levels=["R1", "R2", "R3", "R4"])
    assert result is not None
    assert "units" in result
    assert "book_profile" in result
    assert isinstance(result["units"], list)
    assert isinstance(result["book_profile"], dict)
    assert result["book_profile"].get("book_id") == "e2e_test"


def test_e2e_sphere_math_values_output_exists() -> None:
    """Sphere math values flow produces JSON with L1–L9 keys; output exists."""
    from runtime.pipeline.run_e2e_all import run_e2e_sphere_math_values

    import tempfile
    with tempfile.TemporaryDirectory() as d:
        out_path = Path(d) / "sphere_math_values.json"
        run_e2e_sphere_math_values(out_path, "justice fairness order")
        assert out_path.exists()
        data = json.loads(out_path.read_text(encoding="utf-8"))
        for key in ("L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9"):
            assert key in data, f"sphere_math_values missing {key}"


def test_e2e_sphere_math_100_output_exists() -> None:
    """Sphere math 100 (limited) produces list of results; output exists."""
    from runtime.pipeline.run_e2e_all import run_e2e_sphere_math_100

    import tempfile
    with tempfile.TemporaryDirectory() as d:
        out_path = Path(d) / "sphere_math_100.json"
        run_e2e_sphere_math_100(out_path, limit=2)
        assert out_path.exists()
        data = json.loads(out_path.read_text(encoding="utf-8"))
        assert isinstance(data, list)
        assert len(data) >= 1
        for item in data:
            assert "L1" in item or "text_preview" in item


def test_e2e_run_e2e_all_produces_all_artifacts() -> None:
    """Unified run_e2e_all writes all planned outputs; each file exists."""
    from runtime.pipeline.run_e2e_all import run_all, E2E_OUTPUTS

    import tempfile
    with tempfile.TemporaryDirectory() as d:
        out_dir = Path(d)
        written = run_all(out_dir=out_dir)
        assert len(written) == len(E2E_OUTPUTS)
        for name in E2E_OUTPUTS:
            assert name in written
            path = written[name]
            assert path.exists(), f"E2E output missing: {name}"
            content = path.read_text(encoding="utf-8")
            assert len(content) > 0
            if path.suffix == ".json":
                json.loads(content)
