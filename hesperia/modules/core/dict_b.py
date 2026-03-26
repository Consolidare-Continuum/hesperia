"""Dict B module: concepts to family/area scores (ctx/config only)."""

from __future__ import annotations
import json
from pathlib import Path
from hesperia.engine.calculus import concepts_to_family_area_scores
from hesperia.engine.language import AREA_SCORES, AREAS, CONCEPT_HITS, FAMILIES, FAMILY_SCORES

class Module:
    name = "core.dict_b"
    version = "v1"
    requires = ["core.dict_a"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        rows = list(config.get("entries") or [])
        if not rows:
            default_path = Path(__file__).resolve().parents[3] / "assets" / "data" / "engine_dynamics_v060" / "dict_b" / "dict_b_seed.jsonl"
            p = Path(config.get("path") or default_path)
            if p.exists():
                rows = [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.map: dict[str, dict] = {}
        for row in rows:
            cid = str(row.get("concept_id") or "")
            if cid:
                self.map[cid] = row

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        family_scores, area_scores, families, areas = concepts_to_family_area_scores(
            list(ctx.get(CONCEPT_HITS) or []), self.map
        )
        ctx[FAMILY_SCORES] = family_scores
        ctx[AREA_SCORES] = area_scores
        ctx[FAMILIES] = families
        ctx[AREAS] = areas

    def postprocess(self, ctx: dict) -> None:
        pass

