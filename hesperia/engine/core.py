"""Modular execution kernel for Hesperia."""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib import import_module
from pathlib import Path
from types import MappingProxyType
from typing import Any, Protocol

import yaml  # type: ignore[import-untyped]
from hesperia.engine.context_guard import GuardedContext
from hesperia.engine.language import ARTIFACTS, ENGINE_CONTEXT, SIGNALS, build_ctx, validate_signals


class HesperiaModule(Protocol):
    name: str
    version: str
    requires: list[str]

    def register(self, engine: "HesperiaEngine") -> None: ...
    def configure(self, config: dict[str, Any]) -> None: ...
    def load(self) -> None: ...
    def preprocess(self, ctx: dict[str, Any]) -> None: ...
    def project(self, ctx: dict[str, Any]) -> None: ...
    def postprocess(self, ctx: dict[str, Any]) -> None: ...


@dataclass
class HesperiaEngine:
    modules: list[HesperiaModule] = field(default_factory=list)
    _required_versions: dict[str, str] = field(default_factory=dict)

    def load_module(self, module_path: str, config: dict[str, Any] | None = None) -> None:
        mod = import_module(module_path)
        module = mod.Module()
        module.register(self)
        module.configure(config or {})
        if hasattr(module, "load"):
            module.load()
        self.modules.append(module)

    def load_from_config(self, config_path: Path) -> None:
        payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        module_list = list(payload.get("modules") or [])
        if len(set(module_list)) != len(module_list):
            raise ValueError("module_config_duplicate_entries")
        module_cfg = dict(payload.get("module_config") or {})
        for key in module_list:
            module_path = self._resolve_module_path(str(key))
            cfg = dict(module_cfg.get(str(key), {}))
            req_ver = cfg.pop("required_version", None)
            if req_ver:
                self._required_versions[str(key)] = str(req_ver)
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
            for method in ("load", "preprocess", "project", "postprocess"):
                if not hasattr(m, method):
                    raise ValueError(f"module_interface_invalid:{m.name}:{method}")
            version = str(getattr(m, "version", "") or "").strip()
            if not version:
                raise ValueError(f"module_version_missing:{m.name}")
            req = self._required_versions.get(m.name)
            if req and version != req:
                raise ValueError(f"module_version_mismatch:{m.name}:{version}:{req}")
            for dep in getattr(m, "requires", []):
                if dep not in loaded:
                    raise ValueError(f"module_dependency_missing:{m.name}:{dep}")
                if loaded.index(dep) > loaded.index(m.name):
                    raise ValueError(f"module_dependency_order_invalid:{m.name}:{dep}")

    def run(self, text: str, *, signals: list[dict[str, Any]] | None = None) -> dict[str, Any]:
        base_ctx = build_ctx(text)
        ctx = GuardedContext(base_ctx, protected_keys={ENGINE_CONTEXT})
        dict.__setitem__(
            ctx,
            ENGINE_CONTEXT,
            MappingProxyType({"module_order": [m.name for m in self.modules], "module_count": len(self.modules)}),
        )
        ctx[SIGNALS] = validate_signals(signals)
        for m in self.modules:
            m.preprocess(ctx)
        for m in self.modules:
            m.project(ctx)
        for m in self.modules:
            m.postprocess(ctx)
        ctx[ARTIFACTS]["engine_context_mutation_log"] = ctx.mutation_log
        return ctx

