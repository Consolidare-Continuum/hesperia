# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Defaults for dict calibration until full C / CD / HC dict pipeline is wired."""

from __future__ import annotations

import os
from pathlib import Path

_WORKER_CAP = 64


def _truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def assert_corpus_not_legacy_research(corpus: Path | str) -> None:
    """TFP-DATA-T10: forbid legacy noone corpus path unless env set."""
    bad = "research" + "/_noone_local"
    s = str(corpus).replace("\\", "/")
    if bad in s and not _truthy("HESPERIA_LEGACY_RESEARCH_CORPUS"):
        raise ValueError(
            f"corpus path under {bad} is deprecated for dict calibration; use "
            "hesperia/modules/tfp/data/tfp_v1/corpus/original/ru (run migrate/sync first) or set "
            "HESPERIA_LEGACY_RESEARCH_CORPUS=1 temporarily."
        )


def apply_dict_calib_offline_bundle() -> None:
    """
    Single switch: no OpenAI network + default 4 worker processes for local stages.

    Sets (only if unset): ``HESPERIA_CALIB_MOCK_OPENAI=1``, ``HESPERIA_DICT_CALIB_WORKERS=4``.
    """
    if _truthy("HESPERIA_DICT_CALIB_OFFLINE"):
        os.environ.setdefault("HESPERIA_CALIB_MOCK_OPENAI", "1")
        os.environ.setdefault("HESPERIA_DICT_CALIB_WORKERS", "4")


def dict_calib_worker_default() -> int:
    """
    Process pool size for anchor / links / eval / errors.

    Env: ``HESPERIA_DICT_CALIB_WORKERS`` (default **4**). Clamped to [1, 64].
    """
    raw = os.environ.get("HESPERIA_DICT_CALIB_WORKERS", "4").strip()
    try:
        w = int(raw)
    except ValueError:
        return 4
    return max(1, min(w, _WORKER_CAP))
