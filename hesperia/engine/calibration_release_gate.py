# HESPERIA — RAD. Release gate for TFP calibration bundles (Task 10).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from hesperia.engine.output_anomalies import aggregate_file_envelope, codes_to_envelope, default_operational_envelope


def evaluate_bundle(
    bundle_dir: Path,
    *,
    profile: str,
    gold_failed: int | None = None,
    schema_ok: bool | None = None,
    audit_path: Path | None = None,
) -> dict[str, Any]:
    """
    Produce gate decision dict (write as ``11_calibration_release_gate.json``).

    Profiles: research_allow_degraded | internal_review | product_candidate | ship_blocking
    """
    bundle_dir = bundle_dir.resolve()
    checks: list[dict[str, Any]] = []

    def _load(name: str) -> dict[str, Any] | None:
        p = bundle_dir / name
        if not p.is_file():
            checks.append({"check": f"file_present:{name}", "pass": False})
            return None
        checks.append({"check": f"file_present:{name}", "pass": True})
        return json.loads(p.read_text(encoding="utf-8"))

    m = _load("00_manifest.json")
    if m is None:
        if profile == "research_allow_degraded":
            return {
                "run": "calibration_release_gate_v1",
                "profile": profile,
                "pass": True,
                "checks": checks,
                "blocking_reason": None,
                "rollback_advice": "",
                "last_known_good_hint": "research_allow_degraded: manifest optional",
                "operational_envelope": default_operational_envelope(),
            }
        return {
            "run": "calibration_release_gate_v1",
            "profile": profile,
            "pass": False,
            "checks": checks,
            "blocking_reason": "missing_manifest",
            "rollback_advice": "Run run_tfp_file_pipeline to produce 00_manifest.json",
            "last_known_good_hint": "see docs/specs/calibration_release_gate_v1.md",
            "operational_envelope": codes_to_envelope(["G004_MISSING_BUNDLE_MANIFEST"]),
        }
    envs: list[dict[str, Any]] = []
    for fn in ("01_structural_batch.json", "05_sealed_multiscale.json", "06_product_analyze.json"):
        d = _load(fn)
        if isinstance(d, dict) and "operational_envelope" in d:
            envs.append(d["operational_envelope"])

    blocking_any = any(e.get("blocking") for e in envs if isinstance(e, dict))
    failed_status = any(str(e.get("status")) == "failed" for e in envs if isinstance(e, dict))

    checks.append({"check": "operational_envelope_present_core_artifacts", "pass": len(envs) >= 3})
    checks.append({"check": "no_blocking_anomaly", "pass": not blocking_any})

    consistency = None
    ap = audit_path or (bundle_dir / "10_calibration_audit.json")
    if ap.is_file():
        aud = json.loads(ap.read_text(encoding="utf-8"))
        consistency = float(aud.get("consistency_score") or 0.0)
        checks.append({"check": "calibration_audit_consistency", "pass": True, "value": consistency})

    if schema_ok is not None:
        checks.append({"check": "json_schema_validation", "pass": schema_ok})

    if gold_failed is not None:
        checks.append({"check": "goldset_zero_failures", "pass": gold_failed == 0, "value": gold_failed})

    # Profile rules
    pass_gate = all(c.get("pass") is True for c in checks if c.get("pass") is not None)
    if profile == "research_allow_degraded":
        pass_gate = True
    elif profile == "internal_review":
        pass_gate = not blocking_any and not failed_status
    elif profile == "product_candidate":
        pass_gate = (
            not blocking_any
            and not failed_status
            and (schema_ok is not False)
            and (consistency is None or consistency >= 0.5)
            and (gold_failed is None or gold_failed == 0)
        )
    elif profile == "ship_blocking":
        pass_gate = (
            not blocking_any
            and not failed_status
            and (schema_ok is not False)
            and (gold_failed is None or gold_failed == 0)
            and (consistency is None or consistency >= 0.75)
        )

    blocking_reason = None
    rollback_advice = ""
    if not pass_gate:
        blocking_reason = "one_or_more_gate_checks_failed"
        rollback_advice = (
            "Re-run file pipeline on current main; verify calibration Task2 patches; "
            "see docs/specs/calibration_release_gate_v1.md"
        )

    gate_codes: list[str] = []
    if blocking_any:
        gate_codes.append("G001_BLOCKING_ANOMALY")
    if failed_status:
        gate_codes.append("G002_FAILED_PLANE_STATUS")
    if schema_ok is False:
        gate_codes.append("G003_SCHEMA_INVALID")

    out: dict[str, Any] = {
        "run": "calibration_release_gate_v1",
        "profile": profile,
        "pass": pass_gate,
        "checks": checks,
        "blocking_reason": blocking_reason,
        "rollback_advice": rollback_advice,
        "last_known_good_hint": "release/v0.5.1 sealed product proof (separate from TFP research bundle)",
        "operational_envelope": codes_to_envelope(gate_codes)
        if gate_codes
        else aggregate_file_envelope(envs)
        if envs
        else default_operational_envelope(),
    }
    if consistency is not None:
        out["consistency_score_observed"] = consistency
    return out


def write_gate_report(bundle_dir: Path, body: dict[str, Any]) -> Path:
    p = bundle_dir / "11_calibration_release_gate.json"
    p.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return p
