# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA Engine Dynamics — analyze: text → attribution → guards → 6-key result.
Single entry point. Dict A/B via lexicon frozen bundle v0_5_0 (see VERSION.yaml).
"""
from __future__ import annotations

import math
from pathlib import Path
from typing import Any

try:
    from core.attribution.attribution_shared import DEFAULT_TEXT_CAP, run_attribution_pipeline
    from core.propagation.guard_pipeline import run_pipeline as run_propagation_guard_pipeline
    from core.math.core_math import load_config, analyze as _core_analyze
    from core.propagation.output_contracts import to_minimal_operational_result
    import os
    try:
        from core.attribution import attribution
        _MODE = os.environ.get("HESPERIA_ATTRIBUTION_MODE", "v06").lower()
        if _MODE not in ("sparse", "v06"):
            _MODE = "v06"  # legacy mode name: dense bundle loader (path v0_5_0)
    except Exception:
        attribution = None  # type: ignore[assignment]
        _MODE = "sparse"
except ImportError:
    from attribution_shared import DEFAULT_TEXT_CAP, run_attribution_pipeline
    attribution = None  # type: ignore[assignment]
    _MODE = "sparse"  # noqa: F811
    from guard_pipeline import run_pipeline as run_propagation_guard_pipeline
    from core_math import load_config, analyze as _core_analyze
    from output_contracts import to_minimal_operational_result


def _has_nan_inf(d: dict[str, Any]) -> bool:
    for v in d.values():
        if isinstance(v, (int, float)) and (math.isnan(v) or math.isinf(v)):
            return True
        if isinstance(v, dict) and _has_nan_inf(v):
            return True
    return False


# Ethan PO-02: spans match `schemas/lexical_concept/resolver_output.schema.json` (omit `audit` for payload size).
_PO02_MAX_EVIDENCE_SPANS = 24


def _public_dlcr_span_row(row: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(row, dict):
        return {}
    return {k: v for k, v in row.items() if k != "audit"}


def analyze(
    text: str,
    text_cap: int = DEFAULT_TEXT_CAP,
    shadow_enabled: bool | None = None,
    assets_root: Path | None = None,
    r1_r4: bool = False,
    r1_r4_book_id: str = "book",
    r1_r4_levels: list[str] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """
    Run pipeline: normalize → tokenize → attribution → core → Sigma.
    Returns (minimal_6key_result, extended_metrics).

    When r1_r4=True, runs R1–R4 reading-scale pipeline and attaches
    extended["r1_r4"] = {"units": [...], "book_profile": {...}}.
    Ref: docs/R1_R4_INTEGRATION_CONTRACT.md (I2).
    """
    if not text or not str(text).strip():
        raise ValueError("text_missing")
    cfg = load_config()
    cap = int(cfg.get("text_cap", text_cap))
    shadow = shadow_enabled if shadow_enabled is not None else bool(cfg.get("shadow_enabled", False))
    if _MODE == "v06" and attribution is not None:
        v06_dir = (assets_root / "v0_5_0") if assets_root else None
        dominant_family, dominant_area, seed, attr_metrics, extended = attribution.run_attribution_pipeline(
            text, cap=cap, assets_root=assets_root, v06_dir=v06_dir
        )
    else:
        dominant_family, dominant_area, seed, attr_metrics, extended = run_attribution_pipeline(
            text, cap=cap, assets_root=assets_root, mode=_MODE
        )
    family_vector = extended.get("family_vector") if isinstance(extended, dict) else None
    b_result: dict[str, Any] | None = None
    if _MODE == "v06" and family_vector and len(family_vector) == 288:
        try:
            from core.math.dict_b import run_dict_b_pipeline
            b_result = run_dict_b_pipeline(list(family_vector))
            raw = {
                "dominant_area": b_result["dominant_area"],
                "dominant_family": b_result["dominant_family"],
                "governance": b_result["governance"],
                "loopability": b_result["loopability"],
                "tension_energy": b_result["tension_energy"],
                "obstacle_score": b_result["obstacle_score"],
            }
        except Exception:
            raw = None
            b_result = None
    else:
        raw = None
    if raw is None:
        initial_S, initial_L = None, None
        if family_vector and len(family_vector) == 288:
            try:
                from core.math.core_math import perturb_shadow, reduce_288_to_5
                vec = list(family_vector)
                if shadow:
                    vec = perturb_shadow(vec, cfg)
                initial_S, initial_L = reduce_288_to_5(vec)
            except Exception:
                pass
        raw = _core_analyze(initial_S=initial_S, initial_L=initial_L)
        raw["dominant_family"] = dominant_family
        raw["dominant_area"] = dominant_area
    result = run_propagation_guard_pipeline(
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
    if isinstance(extended, dict):
        if extended.get("family_vector") and len(extended["family_vector"]) == 288:
            extended_out["family_vector"] = extended["family_vector"]
        if extended.get("family_vector_pre_sharpen") and len(extended["family_vector_pre_sharpen"]) == 288:
            extended_out["family_vector_pre_sharpen"] = extended["family_vector_pre_sharpen"]
    # Ethan PO-02: optional governed Dict A→B lexical evidence (DLCR pack), not legacy frozen dict alone.
    import os as _os_ev

    if _os_ev.environ.get("HESPERIA_ANALYZE_DLCR_EVIDENCE", "").strip().lower() in ("1", "true", "yes", "on"):
        try:
            _repo = Path(__file__).resolve().parents[2]
            from hesperia.engine.lexical_concept.pipeline import run_dlcr_pipeline

            snip = (text or "")[:8000]
            dlcr = run_dlcr_pipeline(snip, repo_root=_repo, mode="clinical_speech")
            pm = dlcr.get("preprocess_meta") or {}
            raw_spans = dlcr.get("span_resolutions") or []
            pub_spans = [_public_dlcr_span_row(r) for r in raw_spans[:_PO02_MAX_EVIDENCE_SPANS]]
            extended_out["lexical_evidence_dlcr"] = {
                "analysis_text_fingerprint": pm.get("analysis_text_fingerprint"),
                "lexical_hits_accepted": dlcr.get("lexical_hits_accepted"),
                "lexical_hits_rejected": dlcr.get("lexical_hits_rejected"),
                "span_resolution_count": len(raw_spans),
                "resource_versions": dlcr.get("resource_versions"),
                "winning_concept_ids_sample": [
                    r.get("winning_concept_id") for r in raw_spans[:8]
                ],
                "evidence_spans": pub_spans,
                "evidence_spans_max": _PO02_MAX_EVIDENCE_SPANS,
                "evidence_spans_schema_id": "hesperia.schemas.lexical_concept.resolver_output.v0_6_0",
            }
        except Exception as e:
            extended_out["lexical_evidence_dlcr"] = {"_error": str(e)[:240]}
    if b_result is not None:
        extended_out["dict_b"] = {
            "exclusion_conflict_energy": b_result["exclusion_conflict_energy"],
            "coherence_index": b_result["coherence_index"],
            "entropy_area": b_result["entropy_area"],
        }
    if r1_r4:
        try:
            from runtime.pipeline.r1_r4_pipeline import run_full_pipeline
            levels = r1_r4_levels or ["R1", "R2", "R3", "R4"]
            units, book_profile = run_full_pipeline(
                text,
                book_id=r1_r4_book_id,
                assets_root=assets_root,
                levels=levels,
            )
            extended_out["r1_r4"] = {"units": units, "book_profile": book_profile}
        except Exception as e:
            extended_out["r1_r4"] = {"error": str(e), "units": [], "book_profile": None}
    return minimal, extended_out
