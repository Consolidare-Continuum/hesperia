#!/usr/bin/env python3
# HESPERIA — Cross-plane contradiction audit for TFP bundle outputs (v0.5.8 task4).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Load 04/05/06/09 session artifacts and report contradiction coherence flags."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _load(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _session_map(blob: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not blob:
        return {}
    sessions = blob.get("sessions")
    if not isinstance(sessions, list):
        return {}
    out: dict[str, dict[str, Any]] = {}
    for row in sessions:
        if isinstance(row, dict) and row.get("session_id") is not None:
            out[str(row["session_id"])] = row
    return out


def inspect_bundle(bundle_dir: Path) -> dict[str, Any]:
    d04 = _load(bundle_dir / "04_dlcr_full.json")
    d05 = _load(bundle_dir / "05_sealed_multiscale.json")
    d06 = _load(bundle_dir / "06_product_analyze.json")
    d09 = _load(bundle_dir / "09_session_topology.json")

    m04 = _session_map(d04)
    m05 = _session_map(d05)
    m06 = _session_map(d06)
    m09 = _session_map(d09)
    sids = sorted(set(m04) | set(m05) | set(m06) | set(m09))

    per_session: list[dict[str, Any]] = []
    for sid in sids:
        row04 = m04.get(sid) or {}
        row05 = m05.get(sid) or {}
        row06 = m06.get(sid) or {}
        row09 = m09.get(sid) or {}
        st = (row09.get("session_topology") or {}) if isinstance(row09, dict) else {}
        meta = (st.get("curve_projection_meta") or {}).get("contradiction_summary") or {}
        g_topo = float(meta.get("max_segment_contradiction_load") or 0.0)
        cpkg = row04.get("crossplane_contradiction_package")
        pkg_g = float(row04.get("contradiction_load") or 0.0)
        if isinstance(cpkg, dict) and cpkg.get("global_contradiction_load") is not None:
            pkg_g = max(pkg_g, float(cpkg.get("global_contradiction_load") or 0.0))
        raw_l = float(cpkg.get("raw_contradiction_load") or 0.0) if isinstance(cpkg, dict) else 0.0
        eff_l = float(cpkg.get("effective_contradiction_load") or 0.0) if isinstance(cpkg, dict) else pkg_g
        mconf = float(cpkg.get("contradiction_confidence_mean") or 1.0) if isinstance(cpkg, dict) else 1.0
        raw_vs_effective_gap = abs(raw_l - eff_l)
        ext = (row06.get("extended") or {}) if isinstance(row06.get("extended"), dict) else {}
        vca = ext.get("verdict_conflict_alignment") or {}
        under = bool(vca.get("verdict_underreports_conflict"))
        mode = str(ext.get("session_contradiction_mode") or "")
        sem_rel = float(ext.get("semantic_conflict_reliability") or 0.0)
        cfs = ext.get("conflict_confidence_summary") or {}
        dlcr_align = row04.get("dlcr_contradiction_alignment") or {}
        spread_ok = bool(dlcr_align.get("spread_vs_contradiction_consistent"))
        sealed_trace = row05.get("sealed_conflict_trace") or {}
        collapse = bool(sealed_trace.get("conflict_collapses_under_aggregation"))
        persistent = bool(sealed_trace.get("persistent_conflict"))

        product_underreports_conflict = bool(g_topo > 0.45 and mode == "coherent" and not under)
        dlcr_conflict_misalignment = bool(row04.get("contradiction_load") is not None and not spread_ok and pkg_g > 0.35)
        multiscale_conflict_collapse = bool(persistent and collapse and pkg_g > 0.4)

        high_raw_low_conf = bool(raw_l > 0.52 and mconf < 0.42)
        likely_lexical_contamination = bool(raw_vs_effective_gap > 0.32 and mconf < 0.48)
        likely_concept_ambiguity_overdrive = bool(
            float((ext.get("conflict_source_balance") or {}).get("concept_ambiguity_component") or 0.0) > 0.45
            and eff_l < 0.35
        )
        conflict_confidence_consistency = not (
            high_raw_low_conf and mode == "conflict_dominant" and sem_rel > 0.72
        )
        crossplane_ok = not (
            product_underreports_conflict
            or dlcr_conflict_misalignment
            or multiscale_conflict_collapse
            or (likely_lexical_contamination and sem_rel > 0.75 and mode == "coherent")
        )
        per_session.append(
            {
                "session_id": sid,
                "topology_max_segment_contradiction_load": round(g_topo, 6),
                "product_session_mode": mode,
                "crossplane_contradiction_consistency": crossplane_ok,
                "product_underreports_conflict": product_underreports_conflict,
                "dlcr_conflict_misalignment": dlcr_conflict_misalignment,
                "multiscale_conflict_collapse": multiscale_conflict_collapse,
                "verdict_underreports_conflict_reported": under,
                "raw_vs_effective_conflict_gap": round(raw_vs_effective_gap, 6),
                "conflict_confidence_consistency": conflict_confidence_consistency,
                "likely_lexical_contamination": likely_lexical_contamination,
                "likely_concept_ambiguity_overdrive": likely_concept_ambiguity_overdrive,
                "semantic_conflict_reliability": round(sem_rel, 6),
                "conflict_confidence_summary_echo": cfs,
                "recommended_next_action": (
                    "review_contradiction_rows_and_rerun"
                    if product_underreports_conflict or dlcr_conflict_misalignment or likely_lexical_contamination
                    else "none"
                ),
            }
        )

    overall = all(s.get("crossplane_contradiction_consistency") for s in per_session) if per_session else True
    return {
        "run": "inspect_tfp_bundle_output",
        "bundle_dir": str(bundle_dir),
        "crossplane_contradiction_consistency": overall,
        "sessions": per_session,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Inspect TFP bundle 04/05/06/09 for contradiction coherence.")
    ap.add_argument("--bundle-dir", "-d", type=Path, required=True, help="Output directory from run_tfp_file_pipeline")
    ap.add_argument("--json", action="store_true", help="Print JSON only")
    args = ap.parse_args()
    report = inspect_bundle(args.bundle_dir.resolve())
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
