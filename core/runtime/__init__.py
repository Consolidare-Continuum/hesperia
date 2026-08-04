"""Canonical runtime modules for dynamic loading.

Module implementations (dict_a, dict_b, topology, metrics) live in
hesperia/modules/default/ — universal/domain-agnostic capabilities, Class A in
docs/specs/HESPERIA-CORE-MODULES-AND-BRANCHES.md. Re-exported here for back-compat
with any importer still expecting core.runtime.*.
"""

from hesperia.modules.default.dict_a_module import DictAModule, create as create_dict_a
from hesperia.modules.default.dict_b_module import DictBModule, create as create_dict_b
from hesperia.modules.default.metrics_module import MetricsModule, create as create_metrics
from hesperia.modules.default.topology_module import TopologyModule, create as create_topology

__all__ = [
    "DictAModule",
    "DictBModule",
    "MetricsModule",
    "TopologyModule",
    "create_dict_a",
    "create_dict_b",
    "create_metrics",
    "create_topology",
]
