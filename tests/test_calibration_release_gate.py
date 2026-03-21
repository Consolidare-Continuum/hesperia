# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import json
from pathlib import Path

from hesperia.engine.calibration_release_gate import evaluate_bundle, write_gate_report
from hesperia.engine.output_anomalies import default_operational_envelope


def test_release_gate_research_profile_passes_without_manifest(tmp_path: Path) -> None:
    d = tmp_path / "bare"
    d.mkdir()
    body = evaluate_bundle(d, profile="research_allow_degraded")
    assert body.get("pass") is True
    assert body.get("operational_envelope")


def test_release_gate_research_profile_passes_empty_checks(tmp_path: Path) -> None:
    d = tmp_path / "b"
    d.mkdir()
    (d / "00_manifest.json").write_text(json.dumps({"run": "x"}), encoding="utf-8")
    body = evaluate_bundle(d, profile="research_allow_degraded")
    assert body.get("pass") is True
    assert "operational_envelope" in body


def test_release_gate_writes_11(tmp_path: Path) -> None:
    d = tmp_path / "b2"
    d.mkdir()
    (d / "00_manifest.json").write_text(json.dumps({"run": "x"}), encoding="utf-8")
    for fn in ("01_structural_batch.json", "05_sealed_multiscale.json", "06_product_analyze.json"):
        (d / fn).write_text(
            json.dumps({"run": "t", "operational_envelope": default_operational_envelope()}),
            encoding="utf-8",
        )
    body = evaluate_bundle(d, profile="internal_review", schema_ok=True, gold_failed=0)
    p = write_gate_report(d, body)
    assert p.is_file()
