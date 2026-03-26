"""Topology module: area propagation and tension-ready vector."""

from __future__ import annotations


class Module:
    name = "topology.core"
    version = "v1"
    requires = ["core.dict_b"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.area_count = int(config.get("area_count", 12))

    def before_run(self, ctx: dict) -> None:
        pass

    def process(self, ctx: dict) -> None:
        area_scores = dict(ctx.get("area_scores") or {})
        if not area_scores:
            area_scores = {f"A{i+1}": 0.0 for i in range(self.area_count)}
        total = sum(float(v) for v in area_scores.values())
        if total <= 0:
            normalized = {k: 1.0 / max(1, len(area_scores)) for k in sorted(area_scores)}
        else:
            normalized = {k: float(v) / total for k, v in sorted(area_scores.items())}
        ctx["area_scores"] = normalized

    def after_run(self, ctx: dict) -> None:
        pass

