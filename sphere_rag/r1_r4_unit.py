# Map L1–L9 outputs to R1–R4 Unit schema. Ref: schema/Unit.schema.json, Part C.
from __future__ import annotations

from typing import Any

from .r1_r4_esm_defaults import get_top_n


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def _top_families_from_hits(hits: list[int], top_n: int, F: int, eps: float = 1e-9) -> list[dict[str, Any]]:
    """Build top_families list: family_id F1..F288, coverage, rank. Tie-break by family_id ascending."""
    total = sum(hits)
    if total <= 0:
        return []
    order = sorted(range(F), key=lambda f: (-hits[f], f))
    out = []
    for rank, f in enumerate(order[:top_n], 1):
        if hits[f] <= 0:
            break
        coverage = _clamp01(hits[f] / (total + eps))
        out.append({"family_id": f"F{f + 1}", "coverage": round(coverage, 6), "rank": rank})
    return out


def _top_areas_from_hits(hits: list[int], F: int, A: int, top_n: int = 12, eps: float = 1e-9) -> list[dict[str, Any]]:
    """Aggregate hits by area; return top areas as area_id A1..A12, coverage, rank."""
    if not A:
        return []
    fpa = F // A
    area_hits = [0] * A
    for f in range(F):
        if 0 <= f < F and hits[f] > 0:
            a = f // fpa
            if a < A:
                area_hits[a] += hits[f]
    total = sum(area_hits)
    if total <= 0:
        return []
    order = sorted(range(A), key=lambda a: (-area_hits[a], a))
    out = []
    for rank, a in enumerate(order[:top_n], 1):
        if area_hits[a] <= 0:
            break
        coverage = _clamp01(area_hits[a] / (total + eps))
        out.append({"area_id": f"A{a + 1}", "coverage": round(coverage, 6), "rank": rank})
    return out


def _si_metrics_from_layers(
    l1: dict[str, Any],
    l3: dict[str, Any],
    l5: dict[str, Any],
    l6: dict[str, Any],
    l7: dict[str, Any],
) -> dict[str, Any]:
    """Build SI_metrics dict for Unit schema (all [0,1], trust_tier T0–T3)."""
    coverage = _clamp01(l1.get("COVERAGE_RATIO", 0.0))
    dominance = _clamp01(l1.get("DOMINANCE_RATIO", 0.0))
    entropy = _clamp01(l1.get("NORMALIZED_FAMILY_ENTROPY", 0.0))
    leakage = _clamp01(1.0 - coverage)
    contradiction_pressure = _clamp01(l5.get("CONTRADICTION_PRESSURE_SCORE", 0.0))
    stability = _clamp01(l6.get("GLOBAL_STABILITY_SCORE", 1.0 - entropy))
    shadow_deviation = _clamp01(l3.get("SHADOW_DEVIATION_SCORE", 0.0))
    tier = int(l7.get("TRUST_TIER", 0))
    trust_tier = f"T{min(3, max(0, tier))}"
    return {
        "coverage": round(coverage, 6),
        "dominance": round(dominance, 6),
        "entropy": round(entropy, 6),
        "leakage": round(leakage, 6),
        "contradiction_pressure": round(contradiction_pressure, 6),
        "stability": round(stability, 6),
        "shadow_deviation": round(shadow_deviation, 6),
        "trust_tier": trust_tier,
    }


def _band_from_si(si: dict[str, Any]) -> str:
    """Band from SI_metrics per spec B.9: spiky | fragmented | coherent | stable."""
    tt = si.get("trust_tier", "T2")
    if tt == "T0":
        return "spiky"
    entropy = si.get("entropy", 0.0)
    dominance = si.get("dominance", 0.0)
    leakage = si.get("leakage", 0.0)
    if entropy > 0.6 and dominance < 0.4:
        return "fragmented"
    if dominance > 0.55 and leakage < 0.15 and entropy < 0.35:
        return "coherent"
    return "stable"


def _decision_code_from_l7(l7: dict[str, Any]) -> str:
    """Map L7 DECISION_STATUS_CODE to R1–R4 decision_code string. Ref: R1_R4_BAND_DECISION_CODE_MAPPING."""
    code = int(l7.get("DECISION_STATUS_CODE", 0))
    if code == 0:
        return "OK"
    if code == 75:
        return "GAMMA_DRIFT"  # profile conformance
    if code == 10:
        return "SIGMA_FAIL_LEAK"
    if code == 20:
        return "SIGMA_FAIL_ENTROPY"
    if code in (30, 40, 50, 60, 70):
        return "GAMMA_DRIFT"
    return "GAMMA_DRIFT"


def build_unit(
    unit_id: str,
    level: str,
    parent_id: str | None,
    token_count: int,
    hits: list[int],
    l1: dict[str, Any],
    l2: dict[str, Any],
    l3: dict[str, Any],
    l4: dict[str, Any],
    l5: dict[str, Any],
    l6: dict[str, Any],
    l7: dict[str, Any],
    F: int = 288,
    A: int = 12,
    top_n: int | None = None,
) -> dict[str, Any]:
    """Build a Unit dict conforming to schema/Unit.schema.json from L1–L7 and hits."""
    if top_n is None:
        top_n = get_top_n()
    si = _si_metrics_from_layers(l1, l3, l5, l6, l7)
    top_families = _top_families_from_hits(hits, top_n, F)
    top_areas = _top_areas_from_hits(hits, F, A, top_n=12)
    band = _band_from_si(si)
    decision_code = _decision_code_from_l7(l7)
    return {
        "unit_id": unit_id,
        "level": level,
        "parent_id": parent_id,
        "token_count": token_count,
        "top_areas": top_areas,
        "top_families": top_families,
        "SI_metrics": si,
        "flags": {"band": band, "decision_code": decision_code},
    }
