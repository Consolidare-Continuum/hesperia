"""Canonical runtime modules for dynamic loading."""

from core.runtime.dict_a_module import DictAModule, create as create_dict_a
from core.runtime.dict_b_module import DictBModule, create as create_dict_b
from core.runtime.metrics_module import MetricsModule, create as create_metrics
from core.runtime.topology_module import TopologyModule, create as create_topology

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
