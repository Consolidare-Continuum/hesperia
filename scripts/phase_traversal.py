#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from sphere_rag.guards import run_sigma_preflight  # noqa: E402
from sphere_rag.phase_engine import PhasePolicy, run_phases  # noqa: E402
from sphere_rag.semantic_engine import keywords_to_seed  # noqa: E402


def main() -> int:
    sigma_status = run_sigma_preflight(strict=True)
    ap = argparse.ArgumentParser(description="Deterministic Phase I/II traversal with waterline cut (keywords → seed → paths)")
    ap.add_argument("--keywords", type=str, default="", help="Comma-separated keywords (preferred) or empty to read --keyword")
    ap.add_argument("--keyword", action="append", default=[], help="Repeatable keyword flag")
    ap.add_argument(
        "--families-table",
        type=str,
        default=str(REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"),
        help="Path to 31_FAMILIES__area_family_table_full.txt",
    )
    ap.add_argument("--provenance-weight", type=float, default=1.0, help="provenanceWeight for keyword seeds (default 1.0)")

    # Phase policy overrides (keep small; deterministic)
    ap.add_argument("--alpha", type=float, default=0.50, help="Half-sphere rule alpha (default 0.50)")
    ap.add_argument("--alpha-delta", type=float, default=0.05, help="Revert increment delta for alpha (default 0.05)")
    ap.add_argument("--theta-loopability", type=float, default=0.10, help="Flood threshold theta1 (default 0.10)")
    ap.add_argument("--theta-tension", type=float, default=0.35, help="Flood threshold theta2 (default 0.35)")
    ap.add_argument("--theta-coherence", type=float, default=0.15, help="Flood threshold theta3 (default 0.15)")
    args = ap.parse_args()

    kws = []
    if args.keywords.strip():
        kws.extend([k.strip() for k in args.keywords.split(",") if k.strip()])
    kws.extend([k.strip() for k in (args.keyword or []) if k.strip()])
    if not kws:
        print(json.dumps({"error": "no keywords provided (use --keywords or --keyword)"}, indent=2), file=sys.stderr)
        return 2

    seed = keywords_to_seed(
        kws,
        families_table_path=args.families_table,
        provenance_weight=args.provenance_weight,
    )
    policy = PhasePolicy(
        alpha=args.alpha,
        alpha_step_delta=args.alpha_delta,
        theta_loopability=args.theta_loopability,
        theta_tension=args.theta_tension,
        theta_coherence=args.theta_coherence,
    )
    result = run_phases(seed, policy)

    # JSON-friendly projection
    def _asdict(x):
        return dataclasses.asdict(x) if dataclasses.is_dataclass(x) else x

    out = {
        "sigma_status": sigma_status,
        "input_keywords": kws,
        "semantic_seed": {
            "start_area_id": result.seed.start_area_id,
            "start_family_global": result.seed.start_family_global,
            "hits": [_asdict(h) for h in result.seed.hits],
            "seed_sides": [
                {"side_id": s.side_id, "tau": s.tau, "provenance_weight": s.provenance_weight, "w": s.w}
                for s in result.seed.seed_sides
            ],
            "area_activation_mass": result.seed.area_activation,
            "family_activation_mass_top10": sorted(
                [{"family_global": i, "mass": m} for i, m in enumerate(result.seed.family_activation) if m > 0],
                key=lambda x: (x["mass"], -x["family_global"]),
                reverse=True,
            )[:10],
        },
        "phase_i": {
            "flood": {
                "triggered": result.phase_i.flood.triggered,
                "reason": result.phase_i.flood.reason,
                "at_pass": result.phase_i.flood.at_pass,
                "at_step": result.phase_i.flood.at_step,
                "loopability": result.phase_i.flood.loopability,
                "metrics": _asdict(result.phase_i.flood.metrics),
            },
            "paths": result.phase_i.pass_paths,
            "metrics_history_tail": result.phase_i.metrics_history[-25:],
            "active_sides": len(result.phase_i.region_weights),
            "truth_mass_total": sum(result.phase_i.region_weights.values()),
        },
        "phase_transition": {
            "alpha_used": result.cut.alpha_used,
            "k_star": result.cut.k_star,
            "total_truth_mass": result.cut.total_truth_mass,
            "kept_truth_mass": result.cut.kept_truth_mass,
            "kept_ratio": result.cut.kept_ratio,
            "reverted": result.cut.reverted,
            "revert_reason": result.cut.revert_reason,
        },
        "phase_ii": {
            "active_sides_core": len(result.cut.core_weights),
            "metrics_core": _asdict(result.phase_ii.metrics_core),
            "loopability_core": 0.0,
            "stability_score": result.phase_ii.stability_score,
            "bridge_retention_ratio": result.phase_ii.bridge_retention_ratio,
        },
        "invariants": result.invariants,
        "gamma_status": result.gamma_status,
        "theta_decision": result.theta_decision,
        "dynamic_failure_class": result.dynamic_failure_class,
        "metrics": result.metrics,
    }

    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
