#!/usr/bin/env python3
"""Validate B1 side->family map if present."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--b1",
        type=Path,
        default=Path("hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.json"),
    )
    parser.add_argument(
        "--surface-source",
        type=Path,
        default=Path("assets/v040/surface_map_v040.json"),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("assets/v0414/b1_dict_b_validation_report.txt"),
    )
    args = parser.parse_args()

    if not args.b1.exists():
        msg = [
            "B1 Dict B Validation Report v0.4.1.4",
            "status: HARD_FAIL",
            f"missing_b1_file: {args.b1}",
            "message: Build B1 first after committing a real surface map source.",
        ]
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text("\n".join(msg) + "\n", encoding="utf-8")
        print(f"wrote {args.report}")
        return 2

    data = json.loads(args.b1.read_text(encoding="utf-8"))
    errors: list[str] = []
    if not isinstance(data, dict) or not data:
        errors.append("B1 must be non-empty object")

    for side_id, family in data.items():
        try:
            int(side_id)
        except Exception:
            errors.append(f"invalid side_id key: {side_id!r}")
        if not isinstance(family, int):
            errors.append(f"side {side_id}: familyGlobal must be int")
            continue
        if not (0 <= family <= 287):
            errors.append(f"side {side_id}: familyGlobal out of range: {family}")

    expected_count = None
    if args.surface_source.exists():
        src = json.loads(args.surface_source.read_text(encoding="utf-8"))
        if isinstance(src, dict) and "sides" in src and isinstance(src["sides"], list):
            expected_count = len(src["sides"])
        elif isinstance(src, dict) and all(str(k).isdigit() for k in src.keys()):
            expected_count = len(src)
        if expected_count is not None and expected_count != len(data):
            errors.append(f"side_count mismatch: b1={len(data)} expected={expected_count}")

    lines = [
        "B1 Dict B Validation Report v0.4.1.4",
        "status: OK" if not errors else "status: FAIL",
        f"source_b1: {args.b1}",
        f"surface_source: {args.surface_source}",
        f"side_count: {len(data) if isinstance(data, dict) else 0}",
    ]
    if expected_count is not None:
        lines.append(f"expected_side_count_from_surface: {expected_count}")
    lines.append(f"error_count: {len(errors)}")
    if errors:
        lines.append("errors:")
        lines.extend(f"- {e}" for e in errors[:200])

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.report}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
