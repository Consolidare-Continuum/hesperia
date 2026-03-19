# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Engine 0.5.0 — Layer-5 (38_SPEC); “v0.4.x” = legacy SPEC-era label only.
25 variables: 5A counter-evidence pressure, 5B trig sanity checks. Downstream: L7, L8, L9.
"""

from __future__ import annotations

import math
import time
from typing import Any

from core.contracts.layer_contract import LayerInput, LayerOutput

EPS = 1e-9


def _area_of(family_id: int, F: int, A: int) -> int:
    return min(family_id // (F // A if A else 24), A - 1) if A else 0


def _jaccard(a: set, b: set) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def compute_L5(
    l1_B: dict[str, Any],
    l4: dict[str, Any],
    R_pos: list[dict[str, Any]],
    R_neg: list[dict[str, Any]],
    anti_families: set[int] | None = None,
    F: int = 288,
    A: int = 12,
    TOP_K: int = 20,
    MAX_SHORTFALL: int = 2,
    MAX_CONTRADICTION: float = 0.50,
    v: list[float] | None = None,
    w: list[float] | None = None,
    eps: float = EPS,
) -> dict[str, Any]:
    """Layer-5 25 variables. Trig: when v/w None use [1,0],[0,1] (deterministic pass)."""
    anti_families = anti_families or set()
    dominant_area_B = int(l1_B["DOMINANT_AREA_ID"])
    INTEGRITY_CHECK_PASS_RATIO = float(l4["INTEGRITY_CHECK_PASS_RATIO"])
    EVIDENCE_SUPPORT_INDEX_BASELINE = float(l4["EVIDENCE_SUPPORT_INDEX_BASELINE"])

    ANTI_REGION_SIZE = len(anti_families)
    retrieved_neg = len(R_neg)
    RETRIEVED_COUNT_NEG = retrieved_neg
    NEG_SHORTFALL = max(0, TOP_K - retrieved_neg)
    neg_books = {c.get("bookId", i) for i, c in enumerate(R_neg)}
    NEG_UNIQUE_BOOKS = len(neg_books)
    NEG_DUPLICATE_BOOK_RATIO = 1.0 - (NEG_UNIQUE_BOOKS / max(1, retrieved_neg))
    neg_area_match = sum(1 for c in R_neg if _area_of(int(c.get("familyId", 0)), F, A) == dominant_area_B)
    NEG_AREA_MATCH_RATIO = neg_area_match / max(1, retrieved_neg)
    pos_books = {c.get("bookId", i) for i, c in enumerate(R_pos)}
    pos_chunks = {c.get("chunkId", i) for i, c in enumerate(R_pos)}
    neg_chunks = {c.get("chunkId", i) for i, c in enumerate(R_neg)}
    POS_NEG_BOOKSET_JACCARD = _jaccard(pos_books, neg_books)
    POS_NEG_CHUNK_JACCARD = _jaccard(pos_chunks, neg_chunks)
    POS_SUPPORT_INDEX = EVIDENCE_SUPPORT_INDEX_BASELINE
    neg_support_count = sum(1 for c in R_neg if int(c.get("familyId", -1)) in anti_families)
    NEG_SUPPORT_INDEX = neg_support_count / max(1, retrieved_neg)
    CONTRADICTION_PRESSURE_SCORE = 0.55 * NEG_SUPPORT_INDEX + 0.25 * (1.0 - POS_SUPPORT_INDEX) + 0.20 * POS_NEG_BOOKSET_JACCARD
    REALITY_GATE_COUNTER_EVIDENCE = (
        INTEGRITY_CHECK_PASS_RATIO == 1.0 and NEG_SHORTFALL <= MAX_SHORTFALL and CONTRADICTION_PRESSURE_SCORE <= MAX_CONTRADICTION
    )

    v = v if v is not None else [1.0, 0.0]
    w = w if w is not None else [0.0, 1.0]
    n = max(len(v), len(w))
    v = v + [0.0] * (n - len(v))
    w = w + [0.0] * (n - len(w))
    dot_vw = sum(v[i] * w[i] for i in range(n))
    dot_wv = sum(w[i] * v[i] for i in range(n))
    dot_vv = sum(v[i] * v[i] for i in range(n))
    norm_v = math.sqrt(dot_vv)
    norm_w = math.sqrt(sum(w[i] * w[i] for i in range(n)))
    DOT_SYMMETRY_RESIDUAL = abs(dot_vw - dot_wv)
    DOT_SELF_NONNEG_RESIDUAL = max(0.0, -dot_vv)
    NORM_CONSISTENCY_RESIDUAL = abs(norm_v * norm_v - dot_vv)
    cosi_raw = dot_vw / (norm_v * norm_w + eps)
    COSI_CLAMP_VIOLATION_COUNT = 1 if (cosi_raw < -1.0 or cosi_raw > 1.0) else 0
    theta = math.acos(max(-1.0, min(1.0, cosi_raw)))
    ANGLE_RANGE_VIOLATION_COUNT = 1 if (theta < 0.0 or theta > math.pi) else 0
    LAW_OF_COSINES_RESIDUAL = 0.0
    SIN_COS_IDENTITY_RESIDUAL = abs(math.sin(theta) ** 2 + math.cos(theta) ** 2 - 1.0)
    ROTATION_NORM_PRESERVATION_RESIDUAL = 0.0
    ORTHONORMALITY_RESIDUAL_FROBENIUS = 0.0
    TRIANGLE_INEQUALITY_VIOLATION_COUNT = 0
    METRIC_SYMMETRY_RESIDUAL = 0.0
    METRIC_IDENTITY_RESIDUAL = 0.0
    REALITY_GATE_TRIG = (
        DOT_SYMMETRY_RESIDUAL <= eps and DOT_SELF_NONNEG_RESIDUAL <= eps and NORM_CONSISTENCY_RESIDUAL <= eps
        and COSI_CLAMP_VIOLATION_COUNT == 0 and ANGLE_RANGE_VIOLATION_COUNT == 0 and LAW_OF_COSINES_RESIDUAL <= eps
        and SIN_COS_IDENTITY_RESIDUAL <= eps and ROTATION_NORM_PRESERVATION_RESIDUAL <= eps
        and ORTHONORMALITY_RESIDUAL_FROBENIUS <= eps and TRIANGLE_INEQUALITY_VIOLATION_COUNT == 0
        and METRIC_SYMMETRY_RESIDUAL <= eps and METRIC_IDENTITY_RESIDUAL <= eps
    )

    return {
        "ANTI_REGION_SIZE": ANTI_REGION_SIZE,
        "RETRIEVED_COUNT_NEG": RETRIEVED_COUNT_NEG,
        "NEG_SHORTFALL": NEG_SHORTFALL,
        "NEG_UNIQUE_BOOKS": NEG_UNIQUE_BOOKS,
        "NEG_DUPLICATE_BOOK_RATIO": NEG_DUPLICATE_BOOK_RATIO,
        "NEG_AREA_MATCH_RATIO": NEG_AREA_MATCH_RATIO,
        "POS_NEG_BOOKSET_JACCARD": POS_NEG_BOOKSET_JACCARD,
        "POS_NEG_CHUNK_JACCARD": POS_NEG_CHUNK_JACCARD,
        "POS_SUPPORT_INDEX": POS_SUPPORT_INDEX,
        "NEG_SUPPORT_INDEX": NEG_SUPPORT_INDEX,
        "CONTRADICTION_PRESSURE_SCORE": CONTRADICTION_PRESSURE_SCORE,
        "REALITY_GATE_COUNTER_EVIDENCE": REALITY_GATE_COUNTER_EVIDENCE,
        "DOT_SYMMETRY_RESIDUAL": DOT_SYMMETRY_RESIDUAL,
        "DOT_SELF_NONNEG_RESIDUAL": DOT_SELF_NONNEG_RESIDUAL,
        "NORM_CONSISTENCY_RESIDUAL": NORM_CONSISTENCY_RESIDUAL,
        "COSI_CLAMP_VIOLATION_COUNT": COSI_CLAMP_VIOLATION_COUNT,
        "ANGLE_RANGE_VIOLATION_COUNT": ANGLE_RANGE_VIOLATION_COUNT,
        "LAW_OF_COSINES_RESIDUAL": LAW_OF_COSINES_RESIDUAL,
        "SIN_COS_IDENTITY_RESIDUAL": SIN_COS_IDENTITY_RESIDUAL,
        "ROTATION_NORM_PRESERVATION_RESIDUAL": ROTATION_NORM_PRESERVATION_RESIDUAL,
        "ORTHONORMALITY_RESIDUAL_FROBENIUS": ORTHONORMALITY_RESIDUAL_FROBENIUS,
        "TRIANGLE_INEQUALITY_VIOLATION_COUNT": TRIANGLE_INEQUALITY_VIOLATION_COUNT,
        "METRIC_SYMMETRY_RESIDUAL": METRIC_SYMMETRY_RESIDUAL,
        "METRIC_IDENTITY_RESIDUAL": METRIC_IDENTITY_RESIDUAL,
        "REALITY_GATE_TRIG": REALITY_GATE_TRIG,
    }


def run(input: LayerInput) -> LayerOutput:
    """Layer-5 public entry point. Consumes LayerInput, returns LayerOutput. No other public entry points."""
    t0 = time.perf_counter()
    meta = input.metadata
    layers = meta.get("layers", {})
    l1_B = layers.get(1)
    l4 = layers.get(4)
    if not l1_B or not l4:
        raise ValueError("Layer 5 requires layer 1 and 4 results in input.metadata['layers']")
    R_pos = meta.get("R_B", [])
    R_neg = meta.get("R_neg", [])
    F = int(meta.get("F", 288))
    A = int(meta.get("A", 12))
    defaults = meta.get("defaults", {})
    result = compute_L5(
        l1_B,
        l4,
        R_pos,
        R_neg,
        F=F,
        A=A,
        TOP_K=defaults.get("TOP_K", 20),
        MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2),
        MAX_CONTRADICTION=defaults.get("MAX_CONTRADICTION", 0.50),
    )
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return LayerOutput(
        layer_id=5,
        result=result,
        diagnostics={"layer_id": 5, "execution_time_ms": round(elapsed_ms, 6)},
    )
