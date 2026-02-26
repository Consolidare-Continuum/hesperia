#!/usr/bin/env python3
"""
HESPERIA v0.5 — Meaningful calibration: 100×2 dataset, per-domain metrics + family_vector entropy.
Run full 100 sentences × 2 (base, shadow); compute:
  - mean governance per domain
  - mean tension per domain
  - shadow delta magnitude per domain
  - entropy of family_vector before reduction (low entropy → anchors too narrow)
Usage: from CLIENTS/hesperia: HESPERIA_ATTRIBUTION_MODE=dense python3 scripts/calibration_metrics_v05.py [--output path]
"""
from __future__ import annotations

import csv
import json
import math
import os
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
ASSETS_ROOT = REPO / "hesperia_lex" / "frozen"
DATASET_PATH = REPO / "calibration" / "data" / "calibration_100_sentences.json"
DEFAULT_OUTPUT = REPO / "docs" / "hesperia_runtime_output" / "calibration_metrics_v05.json"

if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

os.environ.setdefault("HESPERIA_ATTRIBUTION_MODE", "dense")


def entropy_family_vector(v: list[float], eps: float = 1e-12) -> float:
    """Entropy of distribution from |v| normalized. High = spread; low = concentrated (narrow anchors)."""
    if not v or len(v) != 288:
        return 0.0
    w = [abs(x) for x in v]
    s = sum(w) or 1.0
    p = [x / s for x in w]
    return -sum(pi * math.log(pi + eps) for pi in p if pi > 0)


def top1_top5_mass(v: list[float]) -> tuple[float, float]:
    """From |v| normalized to sum 1: top1_mass = max(p), top5_mass = sum of 5 largest p."""
    if not v or len(v) != 288:
        return 0.0, 0.0
    w = [abs(x) for x in v]
    s = sum(w) or 1.0
    p = [x / s for x in w]
    sorted_p = sorted(p, reverse=True)
    return sorted_p[0], sum(sorted_p[:5])


def main() -> int:
    import argparse
    p = argparse.ArgumentParser(description="HESPERIA v0.5 calibration metrics (100×2, per-domain + entropy)")
    p.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT, help="Output JSON path")
    p.add_argument("--csv", type=Path, default=None, help="If set, write full run-level CSV report (all rows with all values)")
    args = p.parse_args()

    with open(DATASET_PATH, encoding="utf-8") as f:
        sentences = json.load(f)

    from sphere_rag.analyze_v033 import analyze_v033

    rows: list[dict] = []
    for s in sentences:
        sid, domain, text = s["id"], s["domain"], s["text"]
        for mode, shadow in [("base", False), ("shadow", True)]:
            rec = {
                "sentence_id": sid,
                "domain": domain,
                "mode": mode,
                "governance": None,
                "tension_energy": None,
                "family_vector_entropy": None,
                "family_vector_entropy_pre_sharpen": None,
                "top1_mass": None,
                "top5_mass": None,
                "error": None,
            }
            try:
                minimal, extended = analyze_v033(text, shadow_enabled=shadow, assets_root=ASSETS_ROOT)
                rec["governance"] = minimal.get("governance")
                rec["tension_energy"] = minimal.get("tension_energy")
                fv = extended.get("family_vector")
                if fv and len(fv) == 288:
                    rec["family_vector_entropy"] = entropy_family_vector(fv)
                    rec["top1_mass"], rec["top5_mass"] = top1_top5_mass(fv)
                fv_pre = extended.get("family_vector_pre_sharpen")
                if fv_pre and len(fv_pre) == 288:
                    rec["family_vector_entropy_pre_sharpen"] = entropy_family_vector(fv_pre)
            except Exception as e:
                rec["error"] = str(e)
            rows.append(rec)

    # Per-domain aggregates
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r.get("error"):
            continue
        by_domain[r["domain"]].append(r)

    domains = sorted(by_domain.keys())
    report: dict = {
        "n_sentences": len(sentences),
        "n_runs": len(rows),
        "per_domain": {},
        "entropy_note": "entropy_pre_sharpen = before temperature layer; entropy_sharp_norm_mean = after (normalized). Low entropy = concentrated. Max H ≈ log(288) ≈ 5.67.",
    }
    max_entropy = math.log(288)
    all_entropy_pre = [r["family_vector_entropy_pre_sharpen"] for r in rows if r.get("family_vector_entropy_pre_sharpen") is not None]
    all_entropy_sharp = [r["family_vector_entropy"] for r in rows if r.get("family_vector_entropy") is not None]
    report["entropy_before_sharpen_mean"] = sum(all_entropy_pre) / len(all_entropy_pre) if all_entropy_pre else None
    report["entropy_after_sharpen_mean"] = sum(all_entropy_sharp) / len(all_entropy_sharp) if all_entropy_sharp else None
    report["entropy_sharp_norm_mean_global"] = (sum(e / max_entropy for e in all_entropy_sharp) / len(all_entropy_sharp)) if all_entropy_sharp else None
    # top1 / top5 mass (from sharpened family_vector)
    all_top1 = [r["top1_mass"] for r in rows if r.get("top1_mass") is not None]
    all_top5 = [r["top5_mass"] for r in rows if r.get("top5_mass") is not None]
    report["top1_mass_mean"] = sum(all_top1) / len(all_top1) if all_top1 else None
    report["top5_mass_mean"] = sum(all_top5) / len(all_top5) if all_top5 else None
    report["entropy_norm_mean"] = report["entropy_sharp_norm_mean_global"]  # alias for phase-1 spec

    for domain in domains:
        domain_rows = by_domain[domain]
        base_rows = [r for r in domain_rows if r["mode"] == "base"]
        shadow_rows = [r for r in domain_rows if r["mode"] == "shadow"]
        base_by_sid = {r["sentence_id"]: r for r in base_rows}
        shadow_by_sid = {r["sentence_id"]: r for r in shadow_rows}

        gov_base = [r["governance"] for r in base_rows if r.get("governance") is not None]
        gov_shadow = [r["governance"] for r in shadow_rows if r.get("governance") is not None]
        ten_base = [r["tension_energy"] for r in base_rows if r.get("tension_energy") is not None]
        ten_shadow = [r["tension_energy"] for r in shadow_rows if r.get("tension_energy") is not None]

        delta_gov = []
        delta_tension = []
        for sid in base_by_sid:
            if sid not in shadow_by_sid:
                continue
            b, sh = base_by_sid[sid], shadow_by_sid[sid]
            if b.get("governance") is not None and sh.get("governance") is not None:
                delta_gov.append(abs(sh["governance"] - b["governance"]))
            if b.get("tension_energy") is not None and sh.get("tension_energy") is not None:
                delta_tension.append(abs(sh["tension_energy"] - b["tension_energy"]))

        entropies = [r["family_vector_entropy"] for r in domain_rows if r.get("family_vector_entropy") is not None]
        entropies_pre = [r["family_vector_entropy_pre_sharpen"] for r in domain_rows if r.get("family_vector_entropy_pre_sharpen") is not None]
        top1_list = [r["top1_mass"] for r in domain_rows if r.get("top1_mass") is not None]
        top5_list = [r["top5_mass"] for r in domain_rows if r.get("top5_mass") is not None]

        def mean(xs):
            return sum(xs) / len(xs) if xs else None

        all_deltas = delta_gov + delta_tension
        report["per_domain"][domain] = {
            "mean_governance": mean(gov_base),
            "mean_tension": mean(ten_base),
            "mean_shadow_delta_governance": mean(delta_gov),
            "mean_shadow_delta_tension": mean(delta_tension),
            "shadow_delta_magnitude": mean(all_deltas) if all_deltas else None,
            "entropy_pre_sharpen_mean": mean(entropies_pre),
            "entropy_sharp_norm_mean": mean([e / max_entropy for e in entropies]) if entropies else None,
            "family_vector_entropy_mean": mean(entropies),
            "family_vector_entropy_min": min(entropies) if entropies else None,
            "family_vector_entropy_max": max(entropies) if entropies else None,
            "family_vector_entropy_normalized_mean": mean([e / max_entropy for e in entropies]) if entropies else None,
            "top1_mass_mean": mean(top1_list),
            "top5_mass_mean": mean(top5_list),
            "n_base": len(base_rows),
            "n_shadow": len(shadow_rows),
        }

    # Governance spread range (min/max of per-domain mean_governance)
    gov_means = [report["per_domain"][d]["mean_governance"] for d in domains if report["per_domain"][d].get("mean_governance") is not None]
    report["governance_spread_min"] = min(gov_means) if gov_means else None
    report["governance_spread_max"] = max(gov_means) if gov_means else None
    report["governance_spread_range"] = [report["governance_spread_min"], report["governance_spread_max"]]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Written: {args.output}")

    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        csv_columns = [
            "sentence_id", "domain", "mode",
            "governance", "tension_energy",
            "family_vector_entropy", "family_vector_entropy_pre_sharpen",
            "top1_mass", "top5_mass",
            "error",
        ]
        with open(args.csv, "w", encoding="utf-8", newline="") as f:
            t = os.environ.get("HESPERIA_TEMPERATURE", "")
            g = os.environ.get("HESPERIA_GAMMA", "")
            k = os.environ.get("HESPERIA_TOP_K", "")
            f.write(f"# HESPERIA_TEMPERATURE={t}, HESPERIA_GAMMA={g}, HESPERIA_TOP_K={k}\n")
            w = csv.DictWriter(f, fieldnames=csv_columns, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                row_export = {k: r.get(k) for k in csv_columns}
                w.writerow(row_export)
        print(f"Written CSV: {args.csv}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
