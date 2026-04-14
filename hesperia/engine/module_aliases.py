"""Alias map for dynamic module loading (SSOT for hesperia.engine.module_loader)."""

from __future__ import annotations

MODULE_ALIASES: dict[str, str] = {
    "nlp": "hesperia.modules.nlp.basic",
    "dict_a": "hesperia.modules.core.dict_a",
    "dict_b": "hesperia.modules.core.dict_b",
    "topology": "hesperia.modules.topology.core",
    "tfp": "hesperia.modules.tfp.v1",
    "metrics": "hesperia.modules.metrics.base",
    # Back-compat aliases.
    "nlp.basic": "hesperia.modules.nlp.basic",
    "core.dict_a": "hesperia.modules.core.dict_a",
    "core.dict_b": "hesperia.modules.core.dict_b",
    "topology.core": "hesperia.modules.topology.core",
    "tfp.v1": "hesperia.modules.tfp.v1",
    "metrics.base": "hesperia.modules.metrics.base",
}
