"""Metrics module over deterministic context state."""

from __future__ import annotations

from core.result.contract import compute_loopability, compute_stability, compute_tension


class Module:
    name = "metrics.base"
    version = "v1"
    requires = ["topology.core"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.family_count = int(config.get("family_count", 24))
        self.area_count = int(config.get("area_count", 12))

    def before_run(self, ctx: dict) -> None:
        pass

    def process(self, ctx: dict) -> None:
        area_scores = dict(ctx.get("area_scores") or {})
        family_scores = dict(ctx.get("family_scores") or {})
        area_vector = [float(area_scores.get(f"A{i+1}", 0.0)) for i in range(self.area_count)]
        fam_total = sum(float(v) for v in family_scores.values())
        if fam_total <= 0:
            family_vector = [1.0 / self.family_count for _ in range(self.family_count)]
        else:
            family_vector = [float(family_scores.get(f"F{i+1}", 0.0)) / fam_total for i in range(self.family_count)]
        metrics = {
            "dominant_area": int(max(range(len(area_vector)), key=lambda i: area_vector[i])) if area_vector else 0,
            "dominant_family": int(max(range(len(family_vector)), key=lambda i: family_vector[i])) if family_vector else 0,
            "tension": compute_tension(area_vector),
            "loopability": compute_loopability({"segment_count": 1, "transition_count": 0, "stability_window": 1.0, "jump_distance": 0.0}),
            "stability": compute_stability([0.0]),
            "area_vector": area_vector,
            "family_vector": family_vector,
        }
        ctx["metrics"] = metrics

    def after_run(self, ctx: dict) -> None:
        pass

