"""Dict B module: concepts to family/area scores (ctx/config only)."""

from __future__ import annotations

class Module:
    name = "core.dict_b"
    version = "v1"
    requires = ["core.dict_a"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.map: dict[str, dict] = {}
        for row in list(config.get("entries") or []):
            cid = str(row.get("concept_id") or "")
            if cid:
                self.map[cid] = row

    def before_run(self, ctx: dict) -> None:
        pass

    def process(self, ctx: dict) -> None:
        family_scores: dict[str, float] = {}
        area_scores: dict[str, float] = {}
        for cid in list(ctx.get("concept_hits") or []):
            meta = self.map.get(str(cid)) or {}
            for f in list(meta.get("family_ids") or []):
                key = str(f)
                family_scores[key] = family_scores.get(key, 0.0) + 1.0
            for a in list(meta.get("area_ids") or []):
                key = str(a)
                area_scores[key] = area_scores.get(key, 0.0) + 1.0
        ctx["family_scores"] = dict(sorted(family_scores.items()))
        ctx["area_scores"] = dict(sorted(area_scores.items()))
        ctx["families"] = sorted(family_scores)
        ctx["areas"] = sorted(area_scores)

    def after_run(self, ctx: dict) -> None:
        pass

