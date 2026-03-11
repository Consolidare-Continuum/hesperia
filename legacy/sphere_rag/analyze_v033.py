"""
HESPERIA v0.3.3 — analyze with deterministic attribution.
Flow: text → normalize → tokenize → attribution → (seed) → traversal → guards → (optional shadow) → 6-key result.
Contract unchanged. Extended metrics (total_tokens, matched_tokens, attribution_coverage, etc.) not in minimal result.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

try:
    from .attribution_v033 import (
        DEFAULT_TEXT_CAP,
        run_attribution_pipeline,
    )
    from .guard_pipeline import run_pipeline
    from .hesperia_v03_core_math import load_config, analyze
    from .output_contracts_v032 import to_minimal_operational_result
except ImportError:
    from attribution_v033 import DEFAULT_TEXT_CAP, run_attribution_pipeline
    from guard_pipeline import run_pipeline
    from hesperia_v03_core_math import load_config, analyze
    from output_contracts_v032 import to_minimal_operational_result


def _has_nan_inf(d: dict[str, Any]) -> bool:
    for v in d.values():
        if isinstance(v, (int, float)) and (math.isnan(v) or math.isinf(v)):
            return True
        if isinstance(v, dict) and _has_nan_inf(v):
            return True
    return False


def analyze_v033(
    text: str,
    text_cap: int = DEFAULT_TEXT_CAP,
    shadow_enabled: bool | None = None,
    assets_root: Path | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """
    Run full v0.3.3 pipeline: normalize → tokenize → attribution → core → Sigma.
    Returns (minimal_6key_result, extended_metrics).
    - If text is missing or empty after normalize: raises ValueError("text_missing") for 400.
    - If no tokens matched: raises ValueError("semantic_vacuum") for 400.
    - If any metric NaN/Inf after Sigma: raises ValueError("metric_nan_inf") for 500.
    """
    if not text or not str(text).strip():
        raise ValueError("text_missing")
    cfg = load_config()
    cap = int(cfg.get("text_cap", text_cap))
    shadow = shadow_enabled if shadow_enabled is not None else bool(cfg.get("shadow_enabled", False))
    dominant_family, dominant_area, seed, attr_metrics, extended = run_attribution_pipeline(
        text, cap=cap, assets_root=assets_root
    )
    # Single entrypoint: always guarded pipeline (Sigma → Gamma → Theta); shadow is a flag inside it.
    raw = analyze()
    raw["dominant_family"] = dominant_family
    raw["dominant_area"] = dominant_area
    result = run_pipeline(
        raw,
        traversal_length=0,
        area_hop_count=0,
        evidence_count=1,
        shadow_enabled=shadow,
    )
    if _has_nan_inf(result):
        raise ValueError("metric_nan_inf")
    minimal = to_minimal_operational_result(result)
    extended_out = {
        "total_tokens": attr_metrics["total_tokens"],
        "matched_tokens": attr_metrics["matched_tokens"],
        "unmatched_tokens": attr_metrics["unmatched_tokens"],
        "attribution_coverage": attr_metrics["attribution_coverage"],
        "meanAltitude_global": attr_metrics["meanAltitude_global"],
        "seed_size": len(seed),
    }
    return minimal, extended_out
