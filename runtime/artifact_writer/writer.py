# HESPERIA — Central artifact writer. Mode-guarded; public writes require projection.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Rules:
# - Public writes require projection/schema compliance.
# - Internal writes require non-public mode.
# - Direct raw file writes in runtime paths should go through this module.

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

# Env key for runtime mode (public_runtime | internal_review | internal_debug)
MODE_ENV = "HESPERIA_RUNTIME_MODE"
DEFAULT_MODE = "public_runtime"


def get_runtime_mode() -> str:
    """Return current runtime mode. Default: public_runtime."""
    return os.environ.get(MODE_ENV, DEFAULT_MODE).strip().lower() or DEFAULT_MODE


def _is_internal_mode(mode: str) -> bool:
    return mode in ("internal_debug", "internal_review")


def write_public_json(path: Path | str, data: dict[str, Any] | list[Any], *, indent: int = 2) -> None:
    """
    Write JSON that will be visible to operators/API. Applies public projection before write.
    Allowed in any mode. Use for reports, dossiers, e2e outputs, audit manifest.
    """
    from core.projection.public_projection_layer import sanitize_public_trace
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, dict):
        from core.projection import apply_public_projection
        data = apply_public_projection(data)
    else:
        data = sanitize_public_trace(data)
    path.write_text(json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def write_internal_json(path: Path | str, data: Any, *, indent: int = 2) -> None:
    """
    Write raw JSON (e.g. layer dumps, internal traces). Only allowed when mode is internal_debug or internal_review.
    In public_runtime mode, no-op (no write). Raises if strict and mode is public.
    """
    mode = get_runtime_mode()
    if not _is_internal_mode(mode):
        return  # no-op in public mode; do not write internal artifacts
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=indent, ensure_ascii=False), encoding="utf-8")


def write_mode_guarded_artifact(
    path: Path | str,
    data: Any,
    artifact_type: str = "public",
    *,
    indent: int = 2,
) -> None:
    """
    Write artifact with mode guard.
    artifact_type: "public" -> apply projection and write (any mode); "internal" -> write only in internal mode.
    """
    if artifact_type == "public":
        write_public_json(path, data if isinstance(data, (dict, list)) else {"value": data}, indent=indent)
    else:
        write_internal_json(path, data, indent=indent)
