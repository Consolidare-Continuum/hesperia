"""Build-time provenance capture for v0.4.0 embedding artifacts."""

from __future__ import annotations

import hashlib
import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any

from .io_deterministic_json import write_json_deterministic


def sha256_file(path: Path | str) -> str:
    p = Path(path)
    digest = hashlib.sha256()
    with p.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or "UNKNOWN"
    except Exception:
        return "UNKNOWN"


def _pip_freeze() -> list[str]:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            check=True,
            capture_output=True,
            text=True,
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def _pkg_version(module_name: str) -> str:
    try:
        module = __import__(module_name)
        return getattr(module, "__version__", "UNKNOWN")
    except Exception:
        return "MISSING"


def write_build_provenance_v040(
    out_path: Path | str,
    dict_a_path: Path | str,
    model_name: str,
    model_revision: str,
    outputs_dict: dict[str, Any],
) -> None:
    """Write deterministic build provenance JSON for v0.4.0."""
    dict_a = Path(dict_a_path)
    normalized_outputs: dict[str, dict[str, str]] = {}
    for key in sorted(outputs_dict.keys()):
        out_file = Path(outputs_dict[key])
        normalized_outputs[key] = {
            "path": str(out_file),
            "sha256": sha256_file(out_file),
        }

    payload = {
        "git_commit": _git_commit(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "env": {
            "USE_TF": os.environ.get("USE_TF"),
            "TRANSFORMERS_NO_TF": os.environ.get("TRANSFORMERS_NO_TF"),
            "TRANSFORMERS_NO_FLAX": os.environ.get("TRANSFORMERS_NO_FLAX"),
        },
        "pip_freeze": _pip_freeze(),
        "pkg_versions": {
            "torch": _pkg_version("torch"),
            "transformers": _pkg_version("transformers"),
            "sentence_transformers": _pkg_version("sentence_transformers"),
            "huggingface_hub": _pkg_version("huggingface_hub"),
            "numpy": _pkg_version("numpy"),
        },
        "inputs": {
            "dict_a_path": str(dict_a),
            "dict_a_sha256": sha256_file(dict_a),
            "model_name": model_name,
            "model_revision": model_revision,
        },
        "outputs": normalized_outputs,
    }
    write_json_deterministic(out_path, payload)

