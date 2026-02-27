#!/usr/bin/env python3
"""
E2E: run one sentence through analyze (6-key result + attribution + dict_b + R1–R4).
Output JSON contains all math currently calculated: result, extended (attribution, dict_b, r1_r4 units + book_profile).
Usage: python3 -m sphere_rag.run_e2e_sentence [--text "sentence"] [--out path.json] [--no-r1-r4] [--truncate-vector]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE.parent) not in sys.path:
    sys.path.insert(0, str(_HERE.parent))


def _round_floats(obj, ndigits=6):
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: _round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(x, ndigits) for x in obj]
    return obj


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(
        description="E2E: one sentence → full output (result + extended + R1–R4 units & book_profile)."
    )
    ap.add_argument(
        "--text",
        default="Justice and fairness support social order. Harm and conflict reduce trust.",
        help="Input sentence(s)",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=_HERE.parent / "docs" / "run_output_e2e_sentence.json",
        help="Output JSON path",
    )
    ap.add_argument(
        "--no-r1-r4",
        action="store_true",
        help="Do not run R1–R4 pipeline (extended.r1_r4 will be absent)",
    )
    ap.add_argument(
        "--truncate-vector",
        action="store_true",
        help="Write family_vector as length only in extended (keeps file small)",
    )
    ap.add_argument(
        "--no-round",
        action="store_true",
        help="Do not round floats in output",
    )
    args = ap.parse_args()

    text = (args.text or "").strip()
    if not text:
        print("Error: empty --text", file=sys.stderr)
        return 1

    try:
        from sphere_rag.analyze import analyze
    except ImportError:
        print("Error: cannot import sphere_rag.analyze", file=sys.stderr)
        return 1

    try:
        minimal, extended = analyze(
            text,
            r1_r4=not args.no_r1_r4,
            r1_r4_book_id="e2e",
            r1_r4_levels=["R1", "R2", "R3", "R4"],
        )
    except Exception as e:
        print(f"Error: analyze failed: {e}", file=sys.stderr)
        return 1

    out = {
        "input": {
            "text_preview": text[:200] + ("..." if len(text) > 200 else ""),
            "length": len(text),
        },
        "result": minimal,
        "extended": dict(extended),
    }

    if args.truncate_vector and isinstance(out["extended"].get("family_vector"), list):
        out["extended"]["family_vector"] = {"length": len(out["extended"]["family_vector"]), "_truncated": True}
    if args.truncate_vector and isinstance(out["extended"].get("family_vector_pre_sharpen"), list):
        out["extended"]["family_vector_pre_sharpen"] = {
            "length": len(out["extended"]["family_vector_pre_sharpen"]),
            "_truncated": True,
        }

    if not args.no_round:
        out = _round_floats(out)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    if sys.stdout.isatty():
        print(out_path.resolve(), file=sys.stderr)
    else:
        print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
