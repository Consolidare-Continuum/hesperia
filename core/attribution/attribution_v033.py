"""
Deprecated: use core.attribution.structural instead.
Re-exports for backward compatibility; version stripped (v0.5).
"""
from __future__ import annotations

from core.attribution.structural import (
    DEFAULT_TEXT_CAP,
    aggregate_dominant,
    attribute,
    build_region_seed,
    load_dict_a,
    load_dict_b,
    normalize,
    run_attribution_pipeline,
    tokenize,
)

# Old names (strip version in new code)
load_dict_a_v033 = load_dict_a
load_dict_b_v033 = load_dict_b

__all__ = [
    "DEFAULT_TEXT_CAP",
    "aggregate_dominant",
    "attribute",
    "build_region_seed",
    "load_dict_a",
    "load_dict_b",
    "load_dict_a_v033",
    "load_dict_b_v033",
    "normalize",
    "run_attribution_pipeline",
    "tokenize",
]
