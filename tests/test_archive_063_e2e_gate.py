"""0.6.3 GitHub archive gate — runnable without prod dicts or corpus."""
from __future__ import annotations

import os
from pathlib import Path

import yaml


def test_version_is_063() -> None:
    doc = yaml.safe_load((Path(__file__).resolve().parents[1] / "VERSION.yaml").read_text(encoding="utf-8"))
    assert doc.get("system_version") == "0.6.3"
    assert doc.get("archive", {}).get("excludes_prod_dicts") is True


def test_analyze_offline_no_prod_dict() -> None:
    os.environ["HESPERIA_DICT_CALIB_OFFLINE"] = "1"
    from runtime.pipeline.analyze import analyze

    minimal, _extended = analyze("Справедливость и порядок в обществе.", r1_r4=False)
    assert "dominant_area" in minimal
    assert "dominant_family" in minimal


def test_archive_manifest_excludes_corpus() -> None:
    root = Path(__file__).resolve().parents[1]
    exclude = (root / "release/v0.6.3/packaging_exclude.txt").read_text(encoding="utf-8")
    assert "corpus/" in exclude
    assert "dicts/v0_6" in exclude or "v0_6_0" in exclude


def test_release_folder_present() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "release/v0.6.3/RELEASE_SCOPE.md").is_file()
    assert (root / "docs/specs/0.6.3-IRC-TEACHER-RUN.md").is_file()
