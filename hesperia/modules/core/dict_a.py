"""Dict A module: token to concept hits (ctx/config only)."""

from __future__ import annotations
import json
from pathlib import Path

class Module:
    name = "core.dict_a"
    version = "v1"
    requires = ["nlp.basic"]

    def register(self, engine) -> None:
        self.engine = engine

    def configure(self, config: dict) -> None:
        rows = list(config.get("entries") or [])
        if not rows:
            default_path = Path(__file__).resolve().parents[3] / "assets" / "data" / "engine_dynamics_v060" / "dict_a" / "dict_a_seed.jsonl"
            p = Path(config.get("path") or default_path)
            if p.exists():
                rows = [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.entries: dict[str, list[str]] = {}
        for row in rows:
            nf = str(row.get("normalized_form") or "").strip()
            if not nf:
                continue
            self.entries[nf] = list(row.get("candidate_concept_ids") or [])

    def load(self) -> None:
        pass

    def preprocess(self, ctx: dict) -> None:
        pass

    def project(self, ctx: dict) -> None:
        hits: list[str] = []
        for token in list(ctx.get("tokens") or []):
            hits.extend(self.entries.get(str(token), []))
        ctx["concept_hits"] = sorted(hits)

    def postprocess(self, ctx: dict) -> None:
        pass

