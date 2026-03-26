"""TFP module as external pluggable layer."""

from __future__ import annotations

from hesperia.modules.tfp.math_v1 import (
    compute_confidence_scores,
    detect_interaction_loops,
    detect_tfp_stage,
    estimate_affect_intensity,
)


class Module:
    name = "tfp.v1"
    version = "v0.5.3"
    requires = ["core.dict_b"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.labels = list(config.get("labels", ["control", "aggression", "identity", "trust"]))

    def before_run(self, ctx: dict) -> None:
        pass

    def process(self, ctx: dict) -> None:
        fam_scores = dict(ctx.get("family_scores") or {})
        area_scores = dict(ctx.get("area_scores") or {})
        buckets = {label: 0.0 for label in self.labels}
        for idx, (fid, val) in enumerate(sorted(fam_scores.items())):
            slot = idx % max(1, len(self.labels))
            buckets[self.labels[slot]] += float(val)
        total = sum(buckets.values())
        if total > 0:
            buckets = {k: v / total for k, v in buckets.items()}
        activation = {
            "areas": area_scores,
            "families": fam_scores,
            "concepts": {str(cid): 1.0 for cid in list(ctx.get("concept_hits") or [])},
        }
        tfp_stage = detect_tfp_stage(area_scores, fam_scores)
        affect_intensity = estimate_affect_intensity(str(ctx.get("text") or ""), list(ctx.get("tokens") or []))
        confidence = compute_confidence_scores(activation)
        loops = detect_interaction_loops([{"areas": area_scores, "families": fam_scores}] * 2, None)
        ctx["tfp_vector"] = buckets
        ctx["tfp_profile"] = {
            "dominant": max(buckets, key=lambda k: buckets[k]) if buckets else None,
            "confidence": max(buckets.values()) if buckets else 0.0,
            "stage": tfp_stage,
            "affect_intensity": affect_intensity,
            "confidence_scores": confidence,
        }
        ctx["tfp_conflicts"] = [k for k, v in buckets.items() if v > 0.4] + [
            "interaction_loop" for _ in loops
        ]

    def after_run(self, ctx: dict) -> None:
        pass

