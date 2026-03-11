"""
HESPERIA layer execution contract.
All layers (L1–L9) consume LayerInput and produce LayerOutput.
Single public entry point per layer: run(input: LayerInput) -> LayerOutput.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class LayerInput:
    """Canonical input for every layer. Metadata carries pipeline context and prior layer results."""

    text: str
    tokens: list[str]
    metadata: Dict[str, Any]


@dataclass
class LayerOutput:
    """Canonical output from every layer. Result is layer-specific; diagnostics for orchestration and performance."""

    layer_id: int
    result: Dict[str, Any]
    diagnostics: Dict[str, Any]


