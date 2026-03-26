"""Deterministic NLP basic module."""

from __future__ import annotations

from core.lexical.normalization import normalize_text


class Module:
    name = "nlp.basic"
    version = "v1"
    requires: list[str] = []

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.stopwords = set(config.get("stopwords", []))

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        norm = normalize_text(str(ctx.get("text") or ""))
        tokens = [t for t in (norm.get("tokens") or []) if t and t not in self.stopwords]
        ctx["tokens"] = tokens
        ctx["artifacts"]["canonical_text"] = norm.get("canonical_text", "")

    def postprocess(self, ctx: dict) -> None:
        pass

