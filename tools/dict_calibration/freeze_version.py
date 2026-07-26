# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 10 — Freeze calibrated dicts + metrics under assets/calibration/dicts/vX/."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .jsonl_util import read_jsonl, write_json, write_jsonl


def freeze(
    work_dir: Path,
    version_dir: Path,
    *,
    evaluation_path: Path | None = None,
) -> None:
    work_dir = work_dir.resolve()
    version_dir.mkdir(parents=True, exist_ok=True)

    def cp(name: str, dest: str) -> None:
        src = work_dir / name
        if src.exists():
            shutil.copy2(src, version_dir / dest)

    cp("dict_a_candidates.jsonl", "dict_a_candidates.jsonl")
    cp("dict_a_normalized.jsonl", "dict_a_normalized.jsonl")
    cp("dict_b_draft.jsonl", "dict_b_draft.jsonl")
    cp("dict_b_anchored.jsonl", "dict_b.jsonl")
    cp("dict_a_to_b_links.jsonl", "links.jsonl")
    if (work_dir / "dict_a_to_b_links_patched.jsonl").exists():
        cp("dict_a_to_b_links_patched.jsonl", "links.jsonl")

    eng = work_dir / "dict_a_engine.jsonl"
    if eng.exists():
        shutil.copy2(eng, version_dir / "dict_a.jsonl")

    evp = evaluation_path or (work_dir / "evaluation_run.json")
    metrics: dict[str, Any] = {}
    if evp.exists():
        import json

        metrics = json.loads(evp.read_text(encoding="utf-8"))
    write_json(version_dir / "metrics.json", metrics)
