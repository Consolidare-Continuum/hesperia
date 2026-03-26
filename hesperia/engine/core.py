"""Modular execution kernel for Hesperia."""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib import import_module
import json
from pathlib import Path
from typing import Any, Protocol

import yaml  # type: ignore[import-untyped]


class HesperiaModule(Protocol):
    name: str
    version: str
    requires: list[str]

    def register(self, engine: "HesperiaEngine") -> None: ...
    def configure(self, config: dict[str, Any]) -> None: ...
    def before_run(self, ctx: dict[str, Any]) -> None: ...
    def process(self, ctx: dict[str, Any]) -> None: ...
    def after_run(self, ctx: dict[str, Any]) -> None: ...


@dataclass
class HesperiaEngine:
    modules: list[HesperiaModule] = field(default_factory=list)

    def load_module(self, module_path: str, config: dict[str, Any] | None = None) -> None:
        mod = import_module(module_path)
        module = mod.Module()
        module.register(self)
        module.configure(config or {})
        self.modules.append(module)

    def load_from_config(self, config_path: Path) -> None:
        payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        module_list = list(payload.get("modules") or [])
        module_cfg = dict(payload.get("module_config") or {})
        for key in module_list:
            module_path = self._resolve_module_path(str(key))
            cfg = dict(module_cfg.get(str(key), {}))
            cfg = self._hydrate_module_config(str(key), cfg, config_path)
            self.load_module(module_path, config=cfg)
        self._validate_dependencies()

    def _resolve_module_path(self, key: str) -> str:
        from hesperia.modules.registry import AVAILABLE_MODULES

        if key not in AVAILABLE_MODULES:
            raise ValueError(f"module_not_registered:{key}")
        return AVAILABLE_MODULES[key]

    def _validate_dependencies(self) -> None:
        loaded = [m.name for m in self.modules]
        for m in self.modules:
            for dep in getattr(m, "requires", []):
                if dep not in loaded:
                    raise ValueError(f"module_dependency_missing:{m.name}:{dep}")
                if loaded.index(dep) > loaded.index(m.name):
                    raise ValueError(f"module_dependency_order_invalid:{m.name}:{dep}")

    def run(self, text: str) -> dict[str, Any]:
        ctx = {
            "text": str(text),
            "tokens": [],
            "concept_hits": [],
            "families": [],
            "family_scores": {},
            "areas": [],
            "area_scores": {},
            "metrics": {},
            "artifacts": {},
        }
        for m in self.modules:
            m.before_run(ctx)
        for m in self.modules:
            m.process(ctx)
        for m in self.modules:
            m.after_run(ctx)
        return ctx

    def _hydrate_module_config(self, key: str, cfg: dict[str, Any], config_path: Path) -> dict[str, Any]:
        root = config_path.resolve().parents[1]
        if key == "core.dict_a":
            p = Path(cfg.get("path") or root / "assets" / "data" / "engine_dynamics_v060" / "dict_a" / "dict_a_seed.jsonl")
            cfg["entries"] = self._load_jsonl_rows(p)
        elif key == "core.dict_b":
            p = Path(cfg.get("path") or root / "assets" / "data" / "engine_dynamics_v060" / "dict_b" / "dict_b_seed.jsonl")
            cfg["entries"] = self._load_jsonl_rows(p)
        return cfg

    @staticmethod
    def _load_jsonl_rows(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        rows: list[dict[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
        return rows

