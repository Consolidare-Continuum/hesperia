"""Schema validation for surface_map_v040.json."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


class SurfaceMapValidationError(ValueError):
    """Raised when surface_map_v040.json does not meet schema expectations."""


def _is_valid_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(float(value))


def _validate_item(item: Any, side_key: str) -> None:
    if isinstance(item, str):
        if not item.strip():
            raise SurfaceMapValidationError(f"side '{side_key}': token entries must be non-empty strings")
        return
    if isinstance(item, list) and len(item) == 2:
        anchor_id, score = item
        if not isinstance(anchor_id, (str, int)):
            raise SurfaceMapValidationError(
                f"side '{side_key}': pair[0] anchor_id must be string/int, got {type(anchor_id).__name__}"
            )
        if not _is_valid_number(score):
            raise SurfaceMapValidationError(
                f"side '{side_key}': pair[1] score must be finite number, got {score!r}"
            )
        return
    raise SurfaceMapValidationError(
        f"side '{side_key}': unsupported item {item!r}; expected string token or [anchor_id, score] pair"
    )


def validate_surface_map_payload(payload: Any, require_non_empty_lists: bool = True) -> None:
    if not isinstance(payload, dict):
        raise SurfaceMapValidationError("surface map must be a JSON object (dict)")

    for raw_key, value in payload.items():
        if not isinstance(raw_key, (str, int)):
            raise SurfaceMapValidationError(
                f"top-level key must be string/int side id, got {type(raw_key).__name__}"
            )
        side_key = str(raw_key)
        if not isinstance(value, list):
            raise SurfaceMapValidationError(f"side '{side_key}' value must be a list")
        if require_non_empty_lists and len(value) == 0:
            raise SurfaceMapValidationError(f"side '{side_key}' list must be non-empty")
        for item in value:
            _validate_item(item, side_key)


def validate_surface_map_file(path: Path | str) -> None:
    surface_path = Path(path)
    if not surface_path.exists():
        raise SurfaceMapValidationError(f"surface map file does not exist: {surface_path}")
    payload = json.loads(surface_path.read_text(encoding="utf-8"))
    validate_surface_map_payload(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate schema of surface_map_v040.json")
    parser.add_argument(
        "path",
        nargs="?",
        default="assets/v040/surface_map_v040.json",
        help="Path to surface_map_v040.json",
    )
    args = parser.parse_args()

    try:
        validate_surface_map_file(args.path)
    except (SurfaceMapValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL: invalid surface_map_v040 schema: {exc}")
        return 1

    print(f"surface_map_v040 schema OK: {Path(args.path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
