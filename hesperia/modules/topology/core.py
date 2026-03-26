"""Topology module: area propagation and tension-ready vector."""

from __future__ import annotations

from hesperia.engine.calculus import normalize_area_scores
from hesperia.engine.language import AREA_SCORES


class Module:
    name = "topology.core"
    version = "v1"
    requires = ["core.dict_b"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.area_count = int(config.get("area_count", 12))

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        area_scores = dict(ctx.get(AREA_SCORES) or {})
        ctx[AREA_SCORES] = normalize_area_scores(area_scores, self.area_count)

    def postprocess(self, ctx: dict) -> None:
        pass

