#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.6 — Canonical full spec run on 100 sentences (Dict A v0.6 + Dict B v0.6).
Default attribution mode v06. Output: calibration_v06_run.jsonl, calibration_v06_summary.json, calibration_v06_full_spec_run.json.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATASET_PATH = REPO / "tools" / "calibration" / "data" / "calibration_100_sentences.json"
OUT_DIR = REPO / "docs" / "boot" / "hesperia_runtime_output"
RUN_JSONL = "calibration_v06_run.jsonl"
SUMMARY_JSON = "calibration_v06_summary.json"
FULL_SPEC_JSON = "calibration_v06_full_spec_run.json"
SPEC_VERSION = "v0.6.0"
PIPELINE = "Dict A v0.6 (full 288-field) → sentence aggregation → Dict B v0.6 (structural coherence, area projection, diffusion) → 6-key + extended"

for _k in list(os.environ.keys()):
    if _k.startswith("HESPERIA_") and _k != "HESPERIA_ATTRIBUTION_MODE":
        os.environ.pop(_k, None)
os.environ["HESPERIA_ATTRIBUTION_MODE"] = "v06"

if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

ASSETS_ROOT = REPO / "lexicon" / "frozen"


def main() -> int:
    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}", file=sys.stderr)
        return 1
    with open(DATASET_PATH, encoding="utf-8") as f:
        sentences = json.load(f)

    from runtime.pipeline.analyze import analyze

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    run_path = OUT_DIR / RUN_JSONL
    summary_path = OUT_DIR / SUMMARY_JSON

    rows: list[dict] = []
    errors: list[dict] = []
    for s in sentences:
        sid, domain, text = s["id"], s["domain"], s["text"]
        rec = {
            "sentence_id": sid,
            "domain": domain,
            "sentence": text,
            "dominant_area": None,
            "dominant_family": None,
            "governance": None,
            "loopability": None,
            "tension_energy": None,
            "obstacle_score": None,
            "matched_tokens": None,
            "coverage": None,
            "error": None,
        }
        try:
            minimal, extended = analyze(text, shadow_enabled=False, assets_root=ASSETS_ROOT)
            rec["dominant_area"] = minimal.get("dominant_area")
            rec["dominant_family"] = minimal.get("dominant_family")
            rec["governance"] = minimal.get("governance")
            rec["loopability"] = minimal.get("loopability")
            rec["tension_energy"] = minimal.get("tension_energy")
            rec["obstacle_score"] = minimal.get("obstacle_score")
            rec["matched_tokens"] = extended.get("matched_tokens")
            rec["coverage"] = extended.get("attribution_coverage")
            if extended.get("dict_b"):
                rec["dict_b"] = extended["dict_b"]
        except Exception as e:
            rec["error"] = str(e)
            errors.append({"sentence_id": sid, "domain": domain, "error": str(e)})
        rows.append(rec)

    with open(run_path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    n_ok = sum(1 for r in rows if r.get("error") is None)
    summary = {
        "n_sentences": len(sentences),
        "n_ok": n_ok,
        "n_error": len(errors),
        "errors": errors[:20],
        "attribution_mode": "v06",
        "run_jsonl": str(run_path),
    }
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    govs = [r["governance"] for r in rows if r.get("governance") is not None]
    loops = [r["loopability"] for r in rows if r.get("loopability") is not None]
    tensions = [r["tension_energy"] for r in rows if r.get("tension_energy") is not None]
    full_spec = {
        "spec_version": SPEC_VERSION,
        "pipeline": PIPELINE,
        "dataset": str(DATASET_PATH),
        "n_sentences": len(sentences),
        "n_ok": n_ok,
        "n_error": len(errors),
        "summary_stats": {
            "governance_unique": len(set(govs)) if govs else 0,
            "governance_min": min(govs) if govs else None,
            "governance_max": max(govs) if govs else None,
            "loopability_unique": len(set(loops)) if loops else 0,
            "loopability_min": min(loops) if loops else None,
            "loopability_max": max(loops) if loops else None,
            "tension_energy_unique": len(set(tensions)) if tensions else 0,
            "tension_energy_min": min(tensions) if tensions else None,
            "tension_energy_max": max(tensions) if tensions else None,
        },
        "errors": errors[:20],
        "rows": rows,
    }
    full_spec_path = OUT_DIR / FULL_SPEC_JSON
    with open(full_spec_path, "w", encoding="utf-8") as f:
        json.dump(full_spec, f, indent=2, ensure_ascii=False)

    print(f"Written: {run_path} ({len(rows)} rows)")
    print(f"Written: {summary_path}")
    print(f"Written: {full_spec_path} (full spec run — check this file)")
    print(f"Result: {n_ok}/{len(sentences)} OK, {len(errors)} errors")
    if errors:
        for e in errors[:5]:
            print(f"  sentence_id={e['sentence_id']}: {e['error']}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
