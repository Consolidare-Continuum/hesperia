#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.4.0 — Calibration autorun. One parsable JSONL file.
Protocol: 100 sentences × 2 (base + shadow) = 200 runs; then 5 random × 10 (determinism) = 50 runs.
Spec: docs/CALIBRATION_RUN_SPEC_v0_4_0.md
Usage: from CLIENTS/hesperia: python3 scripts/run_calibration_v040.py [--output path] [--no-determinism]
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ASSETS_ROOT = REPO / "hesperia_lex" / "frozen"
DATASET_PATH = REPO / "calibration" / "data" / "calibration_100_sentences.json"
DEFAULT_OUTPUT = REPO / "docs" / "hesperia_runtime_output" / "calibration_run.jsonl"

if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))


def load_sentences(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def run_one(
    sentence_id: int,
    domain: str,
    text: str,
    mode: str,
    assets_root: Path,
    determinism_run: bool = False,
    repetition: int | None = None,
) -> dict:
    """Run analyze_v033 once; return one record for JSONL."""
    from sphere_rag.analyze_v033 import analyze_v033

    shadow = mode == "shadow"
    record = {
        "sentence_id": sentence_id,
        "domain": domain,
        "sentence": text,
        "mode": mode,
        "determinism_run": determinism_run,
        "repetition": repetition,
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
        minimal, extended = analyze_v033(text, shadow_enabled=shadow, assets_root=assets_root)
        record["dominant_area"] = minimal.get("dominant_area")
        record["dominant_family"] = minimal.get("dominant_family")
        record["governance"] = minimal.get("governance")
        record["loopability"] = minimal.get("loopability")
        record["tension_energy"] = minimal.get("tension_energy")
        record["obstacle_score"] = minimal.get("obstacle_score")
        record["matched_tokens"] = extended.get("matched_tokens")
        record["coverage"] = extended.get("attribution_coverage")
    except ValueError as e:
        record["error"] = str(e)
    except Exception as e:
        record["error"] = f"{type(e).__name__}: {e}"
    return record


def main() -> int:
    import argparse
    p = argparse.ArgumentParser(description="HESPERIA v0.4.0 calibration run → one JSONL")
    p.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT, help="Output JSONL path")
    p.add_argument("--no-determinism", action="store_true", help="Skip 5×10 determinism runs")
    p.add_argument("--seed", type=int, default=42, help="Random seed for determinism sentence pick")
    args = p.parse_args()

    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}", file=sys.stderr)
        return 1

    sentences = load_sentences(DATASET_PATH)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        # Phase 2: 100 × base, 100 × shadow
        for s in sentences:
            sid, domain, text = s["id"], s["domain"], s["text"]
            for mode in ("base", "shadow"):
                rec = run_one(sid, domain, text, mode, ASSETS_ROOT, determinism_run=False, repetition=None)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

        # Determinism: 5 random sentences × 10 runs (base only)
        if not args.no_determinism and len(sentences) >= 5:
            random.seed(args.seed)
            sample = random.sample(sentences, 5)
            for s in sample:
                sid, domain, text = s["id"], s["domain"], s["text"]
                for rep in range(1, 11):
                    rec = run_one(sid, domain, text, "base", ASSETS_ROOT, determinism_run=True, repetition=rep)
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Written: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
