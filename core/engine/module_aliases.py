"""Alias map for dynamic module loading (SSOT for core.engine.module_loader)."""

from __future__ import annotations

MODULE_ALIASES: dict[str, str] = {
    "nlp": "hesperia.modules.nlp.basic",
    "dict_a": "core.runtime.dict_a_module",
    "dict_b": "core.runtime.dict_b_module",
    "topology": "core.runtime.topology_module",
    "tfp": "hesperia.modules.tfp.v1",
    "metrics": "core.runtime.metrics_module",
    # Back-compat aliases.
    "nlp.basic": "hesperia.modules.nlp.basic",
    "core.dict_a": "core.runtime.dict_a_module",
    "core.dict_b": "core.runtime.dict_b_module",
    "topology.core": "core.runtime.topology_module",
    "tfp.v1": "hesperia.modules.tfp.v1",
    "metrics.base": "core.runtime.metrics_module",
}
