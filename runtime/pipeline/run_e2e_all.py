#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
E2E: run all Hesperia flows and write multiple planned outputs to assets/artifacts/e2e/.
Flows: analyze (sentence), L1–L9, R1–R4, sphere_math_values, sphere_math_100 (limited).
No calibration of results; existence of output only.
Usage: python3 -m runtime.pipeline.run_e2e_all [--out-dir path]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parents[1]
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

# Canonical e2e artifact directory
DEFAULT_E2E_DIR = _HESPERIA / "assets" / "artifacts" / "e2e"

# Planned output basenames (all under out_dir)
E2E_OUTPUTS = (
    "run_output_e2e_sentence.json",
    "run_output_e2e_l1_l9.json",
    "run_output_e2e_r1_r4.json",
    "run_output_e2e_sphere_math_values.json",
    "run_output_e2e_sphere_math_100.json",
)


def _round_floats(obj, ndigits=6):
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: _round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(x, ndigits) for x in obj]
    return obj


def run_e2e_sentence(out_path: Path, text: str) -> None:
    """Run analyze (6-key + attribution + dict_b + R1–R4); write JSON."""
    from runtime.pipeline.analyze import analyze

    minimal, extended = analyze(
        text,
        r1_r4=True,
        r1_r4_book_id="e2e",
        r1_r4_levels=["R1", "R2", "R3", "R4"],
    )
    out = {
        "input": {"text_preview": text[:200] + ("..." if len(text) > 200 else ""), "length": len(text)},
        "result": minimal,
        "extended": dict(extended),
    }
    if isinstance(out["extended"].get("family_vector"), list):
        out["extended"]["family_vector"] = {"length": len(out["extended"]["family_vector"]), "_truncated": True}
    if isinstance(out["extended"].get("family_vector_pre_sharpen"), list):
        out["extended"]["family_vector_pre_sharpen"] = {
            "length": len(out["extended"]["family_vector_pre_sharpen"]),
            "_truncated": True,
        }
    out = _round_floats(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_l1_l9(out_path: Path, text: str) -> None:
    """Run L1–L9 pipeline; write JSON."""
    from runtime.pipeline.run_l1_through_l9 import run_pipeline_for_text

    assets = _HESPERIA / "lexicon" / "curated"
    out = run_pipeline_for_text(text, assets_root=assets)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_r1_r4(out_path: Path, text: str) -> None:
    """Run R1–R4 pipeline; write single JSON with units + book_profile."""
    from runtime.pipeline.r1_r4_pipeline import run_full_pipeline_to_json

    result = run_full_pipeline_to_json(text, book_id="e2e", levels=["R1", "R2", "R3", "R4"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")


def run_e2e_sphere_math_values(out_path: Path, text: str) -> None:
    """Run sphere math values flow; write JSON (via main with patched argv)."""
    from runtime.pipeline import run_sphere_math_values

    old_argv = list(sys.argv)
    try:
        sys.argv = ["", "--out", str(out_path), "--text", text]
        run_sphere_math_values.main()
    finally:
        sys.argv = old_argv


def run_e2e_sphere_math_100(out_path: Path, limit: int = 3) -> None:
    """Run sphere math on first N calibration sentences; write JSON."""
    from runtime.pipeline import run_sphere_math_100_sentences

    sentences_path = _HESPERIA / "tools" / "calibration" / "data" / "calibration_100_sentences.json"
    if not sentences_path.exists():
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump([
                {"id": 1, "domain": "e2e", "text": "Justice and fairness support order."},
                {"id": 2, "domain": "e2e", "text": "Harm and conflict reduce trust."},
            ], f, indent=2)
            tmp_path = f.name
        use_path = tmp_path
        try:
            old_argv = list(sys.argv)
            sys.argv = ["", "--out", str(out_path), "--sentences", use_path, "--limit", str(limit)]
            run_sphere_math_100_sentences.main()
        finally:
            sys.argv = old_argv
            Path(tmp_path).unlink(missing_ok=True)
        return
    old_argv = list(sys.argv)
    try:
        sys.argv = ["", "--out", str(out_path), "--sentences", str(sentences_path), "--limit", str(limit)]
        run_sphere_math_100_sentences.main()
    finally:
        sys.argv = old_argv


def run_all(out_dir: Path | None = None, text: str | None = None) -> dict[str, Path]:
    """Run all e2e flows; write to out_dir. Returns map output_basename -> path written."""
    out_dir = out_dir or DEFAULT_E2E_DIR
    out_dir = Path(out_dir)
    text = (text or "Justice and fairness support social order. Harm and conflict reduce trust.").strip()

    written: dict[str, Path] = {}

    # 1. Analyze sentence
    p = out_dir / "run_output_e2e_sentence.json"
    run_e2e_sentence(p, text)
    written["run_output_e2e_sentence.json"] = p

    # 2. L1–L9
    p = out_dir / "run_output_e2e_l1_l9.json"
    run_e2e_l1_l9(p, text)
    written["run_output_e2e_l1_l9.json"] = p

    # 3. R1–R4
    p = out_dir / "run_output_e2e_r1_r4.json"
    run_e2e_r1_r4(p, text)
    written["run_output_e2e_r1_r4.json"] = p

    # 4. Sphere math values
    p = out_dir / "run_output_e2e_sphere_math_values.json"
    run_e2e_sphere_math_values(p, text)
    written["run_output_e2e_sphere_math_values.json"] = p

    # 5. Sphere math 100 (limit 3)
    p = out_dir / "run_output_e2e_sphere_math_100.json"
    run_e2e_sphere_math_100(p, limit=3)
    written["run_output_e2e_sphere_math_100.json"] = p

    return written


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Run all e2e flows; write multiple outputs to assets/artifacts/e2e/.")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_E2E_DIR, help="Output directory for e2e artifacts")
    ap.add_argument("--text", default=None, help="Input text for sentence/L1–L9/R1–R4 flows")
    args = ap.parse_args()

    try:
        written = run_all(out_dir=args.out_dir, text=args.text)
    except Exception as e:
        print(f"E2E run failed: {e}", file=sys.stderr)
        return 1

    for name, path in written.items():
        print(path.resolve(), file=sys.stderr)
    print("e2e_run_ok", len(written), "outputs", file=sys.stderr)
    print("Manifest: assets/artifacts/e2e/E2E_OUTPUTS.md", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
