# HESPERIA — LEVEL 3 Dict-B concept graph loader
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Load concept_nodes.yaml for concept_id → area, family mapping (activation aggregation).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

_DICT_B_DIR = Path(__file__).resolve().parent
_NODES_PATH = _DICT_B_DIR / "concept_nodes.yaml"


def load_concept_nodes(path: Path | str | None = None) -> list[dict[str, Any]]:
    """Загрузить список узлов концептов из concept_nodes.yaml."""
    p = Path(path) if path is not None else _NODES_PATH
    if not p.exists():
        return []
    with open(p, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("nodes") or []


def build_concept_to_area_family(path: Path | str | None = None) -> dict[str, tuple[str, str]]:
    """
    Построить словарь: concept_id → (area, family).
    Используется для агрегации активации по семьям и областям.
    """
    nodes = load_concept_nodes(path)
    out: dict[str, tuple[str, str]] = {}
    for node in nodes:
        if not isinstance(node, dict):
            continue
        cid = node.get("id")
        area = node.get("area")
        family = node.get("family")
        if cid and area and family:
            out[str(cid)] = (str(area), str(family))
    return out
