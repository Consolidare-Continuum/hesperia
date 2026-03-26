"""Dict A module: token to concept hits (ctx/config only)."""

from __future__ import annotations

class Module:
    name = "core.dict_a"
    version = "v1"
    requires = ["nlp.basic"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        self.entries: dict[str, list[str]] = {}
        for row in list(config.get("entries") or []):
            nf = str(row.get("normalized_form") or "").strip()
            if not nf:
                continue
            self.entries[nf] = list(row.get("candidate_concept_ids") or [])

    def before_run(self, ctx: dict) -> None:
        pass

    def process(self, ctx: dict) -> None:
        hits: list[str] = []
        for token in list(ctx.get("tokens") or []):
            hits.extend(self.entries.get(str(token), []))
        ctx["concept_hits"] = sorted(hits)

    def after_run(self, ctx: dict) -> None:
        pass

