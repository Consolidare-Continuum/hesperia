"""
Deprecated: use core.propagation.output_contracts instead.
Re-exports for backward compatibility; version stripped (v0.5).
"""
from __future__ import annotations

from core.propagation.output_contracts import (
    make_error_result,
    to_minimal_operational_result,
)

__all__ = ["make_error_result", "to_minimal_operational_result"]
