#!/usr/bin/env python3
"""
Run Hesperia analyze_v033 multiple times on a phrase; write all variables to a local output file.
Usage: from CLIENTS/hesperia: python3 scripts/run_hesperia_analyze_report.py
Output: docs/hesperia_runtime_output/latest_run.json (and optional stdout summary).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Repo root = parent of script's parent (CLIENTS/hesperia)
REPO = Path(__file__).resolve().parent.parent
ASSETS_ROOT = REPO / "hesperia_lex" / "frozen"
OUTPUT_DIR = REPO / "docs" / "hesperia_runtime_output"
OUTPUT_FILE = OUTPUT_DIR / "latest_run.json"

# Ensure sphere_rag and hesperia_lex importable
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))


def _token_landings(tokens, dict_a, dict_b, surface_map):
    """Per-token: token -> { landing_source, familyGlobal, altitude }."""
    from sphere_rag.attribution_v033 import attribute, _clamp_altitude
    try:
        from hesperia_lex.definitions.v0414.explain_landing import explain_landing
    except ImportError:
        explain_landing = None
    out = []
    default_alt = 0.5
    for t in tokens:
        key = (surface_map.get(t, t) if surface_map else t)
        if explain_landing:
            ex = explain_landing(key, dict_a=dict_a, b0=dict_b, b1_optional=None)
            src = ex["landing_source"]
            fg = ex.get("familyGlobal")
            if src == "A" and key in dict_a:
                alt = _clamp_altitude(dict_a[key].get("altitude", 0.5))
            elif src in ("B0", "B1") and fg is not None:
                alt = default_alt
            else:
                alt = None
            out.append({"token": t, "key": key, "landing_source": src, "familyGlobal": fg, "altitude": alt})
        else:
            out.append({"token": t, "key": key, "landing_source": "?", "familyGlobal": None, "altitude": None})
    return out


def main():
    phrase = "Altruism and trust reinforce social care and protection within a community."
    n_runs = 5

    from sphere_rag.analyze_v033 import analyze_v033
    from sphere_rag.attribution_v033 import (
        normalize,
        tokenize,
        run_attribution_pipeline,
        load_dict_a_v033,
        load_dict_a_surface_map_v033,
        load_dict_b_v033,
    )
    from sphere_rag.hesperia_v03_core_math import load_config
    from sphere_rag.guard_pipeline import run_pipeline
    from sphere_rag.output_contracts_v032 import to_minimal_operational_result

    # Config variables (used by core math and guards)
    config = load_config()
    dict_a = load_dict_a_v033(assets_root=ASSETS_ROOT)
    dict_b = load_dict_b_v033(assets_root=ASSETS_ROOT)
    surface_map = load_dict_a_surface_map_v033(assets_root=ASSETS_ROOT)

    runs_minimal = []
    runs_extended = []
    runs_attribution_detail = []
    pipeline_result = None
    seed_sample = []

    for i in range(n_runs):
        minimal, extended = analyze_v033(phrase, assets_root=ASSETS_ROOT)
        runs_minimal.append(minimal)
        runs_extended.append(extended)
        dom_fam, dom_area, seed, attr_metrics, ext_attr = run_attribution_pipeline(
            phrase, assets_root=ASSETS_ROOT
        )
        runs_attribution_detail.append({
            "dominant_family": dom_fam,
            "dominant_area": dom_area,
            "seed_size": len(seed),
            "attr_metrics": attr_metrics,
            "per_family": ext_attr.get("per_family", {}),
        })
        if pipeline_result is None:
            from sphere_rag.hesperia_v03_core_math import analyze
            raw = analyze()
            raw["dominant_family"] = dom_fam
            raw["dominant_area"] = dom_area
            pipeline_result = run_pipeline(
                raw,
                traversal_length=0,
                area_hop_count=0,
                evidence_count=1,
                shadow_enabled=bool(config.get("shadow_enabled", False)),
            )
        if i == 0:
            seed_sample = [[s, float(t)] for s, t in (seed[:3] + seed[-3:] if len(seed) > 6 else seed)]

    norm = normalize(phrase)
    tokens = tokenize(norm)
    token_landings = _token_landings(tokens, dict_a, dict_b, surface_map)

    report = {
        "phrase": phrase,
        "n_runs": n_runs,
        "determinism_check": all(
            runs_minimal[0] == m for m in runs_minimal
        ) and all(
            runs_extended[0] == e for e in runs_extended
        ),
        "variables": {
            "config": config,
            "normalized": norm,
            "tokens": tokens,
            "token_landings": token_landings,
            "total_tokens": len(tokens),
            "matched_tokens": runs_attribution_detail[0]["attr_metrics"]["matched_tokens"],
            "unmatched_tokens": runs_attribution_detail[0]["attr_metrics"]["unmatched_tokens"],
            "attribution_coverage": runs_attribution_detail[0]["attr_metrics"]["attribution_coverage"],
            "meanAltitude_global": runs_attribution_detail[0]["attr_metrics"]["meanAltitude_global"],
            "landing_source_counts": runs_attribution_detail[0]["attr_metrics"].get("landing_source_counts", {}),
            "per_family_stats": runs_attribution_detail[0]["per_family"],
            "dominant_family": runs_attribution_detail[0]["dominant_family"],
            "dominant_area": runs_attribution_detail[0]["dominant_area"],
            "seed_size": runs_attribution_detail[0]["seed_size"],
            "seed_sample_first_last": seed_sample,
            "pipeline_result_raw": pipeline_result,
            "minimal_6key": to_minimal_operational_result(pipeline_result) if pipeline_result else runs_minimal[0],
        },
        "minimal_result": runs_minimal[0],
        "extended_metrics": runs_extended[0],
        "all_runs_minimal": runs_minimal,
        "all_runs_extended": runs_extended,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Written: {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
