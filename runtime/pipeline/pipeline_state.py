"""
HESPERIA pipeline state container.
Accumulates layer results and diagnostics from L1–L9 execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class PipelineState:
    """Mutable state for a single L1→L9 run. layers[key] = layer result dict; diagnostics = per-layer diagnostics."""

    layers: Dict[int, Dict[str, Any]] = field(default_factory=dict)
    diagnostics: Dict[str, Any] = field(default_factory=dict)
