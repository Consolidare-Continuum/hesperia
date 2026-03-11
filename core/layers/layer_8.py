"""
HESPERIA v0.4.x Layer-8 units (41_SPEC). SI_* report units from L1..L7.
Single taxonomy: COUNT, RATIO, PERCENT, U1000, BOOLEAN. All 9 layers flow to i18n via L8→L9.
"""
from __future__ import annotations

def _clamp(v, lo, hi): return max(lo, min(hi, v))
def _ratio_to_pct(r): return _clamp(r, 0.0, 1.0) * 100.0
def _ratio_to_u1000(r): return round(_clamp(r, 0.0, 1.0) * 1000.0)

def compute_L8(l1, l2, l3, l4, l5, l6, l7):
    return {
        "UNIT_TYPE_ENUM": "COUNT,RATIO,PERCENT,U1000,RADIANS,SECONDS,BYTES,HASH,BOOLEAN,CODE",
        "SCALE_POLICY_ENUM": "RAW,CLAMP_0_1,CLAMP_0_100,CLAMP_0_1000,ZSCORE,LOG10",
        "EPSILON_POLICY": 1e-12,
        "CLAMP_POLICY": "max(lo,min(hi,v))",
        "ROUNDING_POLICY": "DECIMALS_RATIO=6,DECIMALS_PCT=2,DECIMALS_U1000=0",
        "SI_TOTAL_TOKENS_COUNT": int(l1["TOTAL_TOKENS"]),
        "SI_COVERAGE_PCT": _ratio_to_pct(l1["COVERAGE_RATIO"]),
        "SI_COVERAGE_U1000": _ratio_to_u1000(l1["COVERAGE_RATIO"]),
        "SI_DOMINANCE_PCT": _ratio_to_pct(l1["DOMINANCE_RATIO"]),
        "SI_DOMINANCE_U1000": _ratio_to_u1000(l1["DOMINANCE_RATIO"]),
        "SI_ENTROPY_U1000": _ratio_to_u1000(l1["NORMALIZED_FAMILY_ENTROPY"]),
        "SI_ENTROPY_PCT": _ratio_to_pct(l1["NORMALIZED_FAMILY_ENTROPY"]),
        "SI_GEOMETRIC_STABILITY_U1000": _ratio_to_u1000(l2["GEOMETRIC_STABILITY_INDEX"]),
        "SI_GEOMETRIC_STABILITY_PCT": _ratio_to_pct(l2["GEOMETRIC_STABILITY_INDEX"]),
        "SI_AREA_LEAKAGE_PCT": _ratio_to_pct(l2["CROSS_AREA_RATIO"]),
        "SI_AREA_LEAKAGE_U1000": _ratio_to_u1000(l2["CROSS_AREA_RATIO"]),
        "SI_SHADOW_DEVIATION_U1000": _ratio_to_u1000(_clamp(l3["SHADOW_DEVIATION_SCORE"], 0.0, 1.0)),
        "SI_SHADOW_DEVIATION_PCT": _ratio_to_pct(_clamp(l3["SHADOW_DEVIATION_SCORE"], 0.0, 1.0)),
        "SI_EVIDENCE_SUPPORT_U1000": _ratio_to_u1000(l4["EVIDENCE_SUPPORT_INDEX_BASELINE"]),
        "SI_EVIDENCE_SUPPORT_PCT": _ratio_to_pct(l4["EVIDENCE_SUPPORT_INDEX_BASELINE"]),
        "SI_CONTRADICTION_PRESSURE_U1000": _ratio_to_u1000(l5["CONTRADICTION_PRESSURE_SCORE"]),
        "SI_CONTRADICTION_PRESSURE_PCT": _ratio_to_pct(l5["CONTRADICTION_PRESSURE_SCORE"]),
        "SI_TRIG_REALITY_FLAG": l5["REALITY_GATE_TRIG"],
        "SI_GLOBAL_STABILITY_U1000": _ratio_to_u1000(l6["GLOBAL_STABILITY_SCORE"]),
        "SI_GLOBAL_STABILITY_PCT": _ratio_to_pct(l6["GLOBAL_STABILITY_SCORE"]),
        "SI_SYSTEM_CONFIDENCE_U1000": _ratio_to_u1000(l7["SYSTEM_CONFIDENCE_SCORE"]),
        "SI_SYSTEM_CONFIDENCE_PCT": _ratio_to_pct(l7["SYSTEM_CONFIDENCE_SCORE"]),
    }
