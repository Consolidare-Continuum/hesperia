"""TFP module as external pluggable layer."""

from __future__ import annotations

from hesperia.engine.calculus import compute_tfp_bundle
from hesperia.engine.language import (
    AREA_SCORES,
    CONCEPT_HITS,
    FAMILY_SCORES,
    TEXT,
    TFP_CONFLICTS,
    TFP_PROFILE,
    TFP_VECTOR,
    TOKENS,
)


class Module:
    name = "tfp.v1"
    version = "v0.5.3"
    requires = ["core.dict_b"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.labels = list(config.get("labels", ["control", "aggression", "identity", "trust"]))

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        vector, profile, conflicts = compute_tfp_bundle(
            family_scores=dict(ctx.get(FAMILY_SCORES) or {}),
            area_scores=dict(ctx.get(AREA_SCORES) or {}),
            concept_hits=list(ctx.get(CONCEPT_HITS) or []),
            text=str(ctx.get(TEXT) or ""),
            tokens=list(ctx.get(TOKENS) or []),
            labels=self.labels,
        )
        ctx[TFP_VECTOR] = vector
        ctx[TFP_PROFILE] = profile
        ctx[TFP_CONFLICTS] = conflicts

    def postprocess(self, ctx: dict) -> None:
        pass

