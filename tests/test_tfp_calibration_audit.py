# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
_TCA = _REPO / "tools" / "tfp_calibration_audit.py"
_spec = importlib.util.spec_from_file_location("tfp_calibration_audit", _TCA)
assert _spec and _spec.loader
_mod = importlib.util.module_from_spec(_spec)
sys.modules["tfp_calibration_audit"] = _mod
_spec.loader.exec_module(_mod)
run_audit = _mod.run_audit


def test_calibration_audit_detects_analyze_structural_mismatch(tmp_path: Path) -> None:
    d = tmp_path / "bundle"
    d.mkdir()
    (d / "01_structural_batch.json").write_text(
        json.dumps(
            {
                "structural_batch": [
                    {
                        "payload": {
                            "L1": {"ATTRIBUTED_TOKENS": 0, "COVERAGE_RATIO": 0.0},
                            "diagnostics": {"calibration_status": {}},
                        }
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (d / "02_session_tfp_stages.json").write_text(
        json.dumps({"session_tfp_stages": [{"areas_top": {"A2": 1.0}}]}),
        encoding="utf-8",
    )
    (d / "05_sealed_multiscale.json").write_text(
        json.dumps(
            {
                "sessions": [
                    {
                        "hex_activation_map": {"total_mass": 0.0},
                        "concept_layer": {},
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (d / "06_product_analyze.json").write_text(
        json.dumps(
            {
                "sessions": [
                    {
                        "extended": {
                            "attribution_coverage": 1.0,
                            "matched_tokens": 100,
                            "total_tokens": 100,
                        }
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    rep = run_audit(d)
    assert "HIGH_analyze_coverage_with_zero_L1_attributed" in rep["alarms"]
    assert rep["consistency_score"] < 0.5
