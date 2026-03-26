from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def resolve_calibration_version(explicit: str | None = None) -> str | None:
    v = (explicit or os.environ.get("HESPERIA_CALIB_DICT_VERSION") or "").strip()
    return v or None


def resolve_calibration_dir(repo_root: Path, explicit: str | None = None) -> Path | None:
    version = resolve_calibration_version(explicit)
    if not version:
        return None
    d = repo_root / "assets" / "calibration" / "dicts" / version
    return d if d.is_dir() else None


def resolve_dict_file(repo_root: Path, filename: str, explicit_version: str | None = None) -> Path | None:
    d = resolve_calibration_dir(repo_root, explicit=explicit_version)
    if d is None:
        return None
    p = d / filename
    return p if p.is_file() else None


def calibration_manifest(repo_root: Path, explicit_version: str | None = None) -> dict[str, Any]:
    d = resolve_calibration_dir(repo_root, explicit=explicit_version)
    if d is None:
        return {"enabled": False}
    return {
        "enabled": True,
        "version": d.name,
        "dict_a": str((d / "dict_a.jsonl")),
        "dict_b": str((d / "dict_b.jsonl")),
        "links": str((d / "links.jsonl")),
        "metrics": str((d / "metrics.json")),
    }

