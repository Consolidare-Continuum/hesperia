"""Metrics module over deterministic context state."""

from __future__ import annotations

from hesperia.engine.calculus import compute_metrics_bundle
from hesperia.engine.language import AREA_SCORES, FAMILY_SCORES, METRICS


class Module:
    name = "metrics.base"
    version = "v1"
    requires = ["topology.core"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.family_count = int(config.get("family_count", 24))
        self.area_count = int(config.get("area_count", 12))

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        metrics = compute_metrics_bundle(
            area_scores=dict(ctx.get(AREA_SCORES) or {}),
            family_scores=dict(ctx.get(FAMILY_SCORES) or {}),
            area_count=self.area_count,
            family_count=self.family_count,
        )
        ctx[METRICS] = metrics

    def postprocess(self, ctx: dict) -> None:
        pass

