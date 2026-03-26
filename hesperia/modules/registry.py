"""Optional alias map for module loading."""

ALIASES = {
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

