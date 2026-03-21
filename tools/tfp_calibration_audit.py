#!/usr/bin/env python3
# HESPERIA — RAD. Cross-plane calibration audit for TFP file pipeline bundle (Task 4).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Load ``00``–``09`` JSON artifacts from a pipeline output directory and emit ``10_calibration_audit.json``.

Usage::
  python3 tools/tfp_calibration_audit.py --bundle-dir outputs/tfp_full_ethan_1-11-09-2023
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hesperia.engine.output_anomalies import codes_to_envelope, default_operational_envelope


def _load(p: Path) -> dict[str, Any] | None:
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def _top_keys(d: dict[str, Any], n: int = 8) -> list[str]:
    return sorted(d.keys(), key=lambda k: float(d.get(k) or 0), reverse=True)[:n]


def run_audit(bundle_dir: Path) -> dict[str, Any]:
    bundle_dir = bundle_dir.resolve()
    suspects: list[str] = []
    alarms: list[str] = []
    plane_notes: dict[str, Any] = {}

    s01 = _load(bundle_dir / "01_structural_batch.json")
    s02 = _load(bundle_dir / "02_session_tfp_stages.json")
    s05 = _load(bundle_dir / "05_sealed_multiscale.json")
    s06 = _load(bundle_dir / "06_product_analyze.json")

    l1_attributed = None
    l1_cov = None
    hex_mass = None
    analyze_cov = None
    stage_areas: dict[str, Any] = {}

    if s01 and s01.get("structural_batch"):
        row = s01["structural_batch"][0]
        # `run_structural_analysis_batch` rows may be `{payload: {...}}` (projected public shape).
        core = row.get("payload") if isinstance(row.get("payload"), dict) else row
        L1 = core.get("L1") or {}
        l1_attributed = int(L1.get("ATTRIBUTED_TOKENS") or 0)
        l1_cov = float(L1.get("COVERAGE_RATIO") or 0.0)
        cal = (core.get("diagnostics") or {}).get("calibration_status") or {}
        plane_notes["structural"] = {
            "l1_attributed_tokens": l1_attributed,
            "l1_coverage": l1_cov,
            "calibration_status": cal,
            "l1_fallback": L1.get("CALIBRATION_FALLBACK_USED"),
        }
        if l1_attributed == 0 and not cal.get("l1_calibration_fallback"):
            suspects.append("structural.L1_zero_without_fallback")

    if s05 and s05.get("sessions"):
        sess0 = s05["sessions"][0]
        ham = sess0.get("hex_activation_map") or {}
        hex_mass = float(ham.get("total_mass") or 0.0)
        cl = sess0.get("concept_layer") or {}
        plane_notes["sealed"] = {
            "hex_total_mass": hex_mass,
            "uniform_concept_prior_fallback_used": cl.get("uniform_concept_prior_fallback_used"),
            "hex_upstream_fallback_used": cl.get("hex_upstream_fallback_used"),
        }
        if hex_mass <= 0.0:
            suspects.append("sealed.hex_total_mass_zero")
            alarms.append("IMPOSSIBLE_STATE:hex_mass_zero_with_running_pipeline")

    if s06 and s06.get("sessions"):
        row = s06["sessions"][0]
        ext = row.get("extended") or {}
        analyze_cov = float(ext.get("attribution_coverage") or 0.0)
        plane_notes["analyze"] = {
            "attribution_coverage": analyze_cov,
            "matched_tokens": ext.get("matched_tokens"),
            "total_tokens": ext.get("total_tokens"),
        }

    if s02 and s02.get("session_tfp_stages"):
        st = s02["session_tfp_stages"][0]
        stage_areas = st.get("areas_top") or {}
        plane_notes["stages"] = {"areas_top_keys": _top_keys(stage_areas, 6)}

    # Heuristic consistency score [0,1]
    score = 1.0
    if l1_attributed == 0 and (analyze_cov or 0) >= 0.99:
        score -= 0.35
        alarms.append("HIGH_analyze_coverage_with_zero_L1_attributed")
    if hex_mass is not None and hex_mass <= 0 and (analyze_cov or 0) >= 0.5:
        score -= 0.4
    if stage_areas and l1_attributed == 0 and not plane_notes.get("structural", {}).get(
        "l1_fallback"
    ):
        score -= 0.15
    score = max(0.0, min(1.0, score))

    ranking = ["analyze", "stages", "topology", "kme", "sealed", "structural"]
    if plane_notes.get("structural", {}).get("l1_attributed_tokens", 0) > 0:
        ranking = ["structural", "sealed", "analyze", "stages", "topology", "kme"]

    audit_codes: list[str] = []
    if alarms:
        audit_codes.append("A007_CROSS_PLANE_INCONSISTENCY")
    if "sealed.hex_total_mass_zero" in suspects:
        audit_codes.append("A002_UPSTREAM_NONZERO_DOWNSTREAM_ZERO")

    return {
        "run": "tfp_calibration_audit_v1",
        "bundle_dir": str(bundle_dir),
        "consistency_score": round(score, 4),
        "plane_reliability_ranking": ranking,
        "suspect_fields": suspects,
        "alarms": alarms,
        "likely_breakpoint_stage": "hex_microphysics_line_search"
        if "sealed.hex_total_mass_zero" in suspects
        else None,
        "plane_notes": plane_notes,
        "registry_hint": "assets/config/output_metric_registry_v1.json",
        "operational_envelope": codes_to_envelope(list(dict.fromkeys(audit_codes)))
        if audit_codes
        else default_operational_envelope(),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Emit 10_calibration_audit.json for a TFP bundle directory.")
    ap.add_argument("--bundle-dir", type=Path, required=True, help="Directory with 01_*.json … 09_*.json")
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: bundle-dir/10_calibration_audit.json)",
    )
    args = ap.parse_args()
    out = args.out or (args.bundle_dir.resolve() / "10_calibration_audit.json")
    body = run_audit(args.bundle_dir)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
