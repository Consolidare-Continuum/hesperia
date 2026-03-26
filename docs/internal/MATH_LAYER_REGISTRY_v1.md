# MATH LAYER REGISTRY v1 (INTERNAL ONLY)

**Classification:** Internal. Do not expose publicly. Public artifacts must not contain a complete map of math-layer semantics.

---

## 1. Layer Overview

| Layer id | Role | Dependency inputs | Main outputs | Invariants | Failure modes |
|----------|------|-------------------|--------------|------------|---------------|
| L1 | Instrumentation + normative topology profile. Base metrics from matched (family, altitude); optional profile deviation. | total_tokens, matched list, F, A, eps; optional profile | COVERAGE_RATIO, DOMINANCE_RATIO, DOMINANT_*, ENTROPY, STRUCTURAL_*, PROFILE_* | Raw_text-bound; no shadow; altitude in [0,1] | Empty match → zero coverage; profile conformance failure → code 75 |
| L2 | Geometric traversal. Topology-bound reachability, cross-area ratio, clustering. | L1 (DOMINANT_*, etc.), hits, adjacency, area, F, A, MAX_DEPTH, eps | TOTAL_REACHABLE_NODES, CROSS_AREA_RATIO, GEOMETRIC_STABILITY_INDEX, VISITED_IDS, MASS_AT_DEPTH | Deterministic; ring/stub or real adjacency | Empty traversal when no hits; area leakage above threshold |
| L3 | Shadow divergence. Baseline vs shadow comparison. | L1_B, L2_B, hits_B, L1_S, L2_S, hits_S, F, A, governance params | SHADOW_DEVIATION_SCORE, CROSS_AREA_RATIO_DELTA, SHADOW_ACCEPTABILITY_GATE | B vs S same F,A | Shadow delta beyond limit; dominant area flip |
| L4 | Book evidence. Retrieval, family/area match, integrity, support index. | L1, L2, chunk data (bookId, familyId, chunkId), R_B, R_S | EVIDENCE_SUPPORT_INDEX_BASELINE, INTEGRITY_CHECK_PASS_RATIO, AREA_MATCH_RATIO_* | Chunk checksum; shortfall gate | Shortfall > MAX_SHORTFALL; integrity fail |
| L5 | Counter-evidence + trig reality. Contradiction pressure, reality gate. | L1, L2, L4, counter-evidence inputs | CONTRADICTION_PRESSURE_SCORE, REALITY_GATE_TRIG, REALITY_GATE_COUNTER_EVIDENCE | Trig required for angle metrics | Contradiction above limit; gate fail |
| L6 | Conceptual math & dynamic function. Sensitivity, curvature, Lyapunov, consistency. | L1, L2, MASS_AT_DEPTH | LYAPUNOV_ESTIMATE, GLOBAL_STABILITY_SCORE, sensitivity/curvature outputs | Numerical consistency | Lyapunov overflow; regime invalid |
| L7 | Cross-layer consistency. Gates, confidence, decision code, trust tag. | L1..L6 | CONSIST_* gates, SYSTEM_CONFIDENCE_SCORE, DECISION_STATUS_CODE, OUTPUT_TRUST_TAG, TRUST_TIER | All gates defined; code 75 reserved (profile conformance) | Profile conformance failure; coverage/area/shadow/contradiction/Lyapunov fail |
| L8 | SI units. Report units from L1..L7 (COUNT, RATIO, PERCENT, U1000, etc.). | L1..L7 | SI_* (COVERAGE_PCT, DOMINANCE_U1000, etc.) | Single taxonomy; clamp/round policy | N/A (derived) |
| L9 | Human reference & brand treatment. Bands, pillars, BRAND_WORD_*, ACTION_*. | L3, L4, L7, L8 | BAND_*_CRITICAL/WEAK/FAIR/GOOD/STRONG/EXCELLENT, PILLAR_*, BRAND_WORD_TRUST, ACTION_* | Final layer; i18n can wrap | N/A (presentation) |

---

## 2. Internal Use Only

- **Full formulas** — Not for public artifacts.
- **Full dependency chain** — Not for public artifacts.
- **Internal metric graph** — Not for public artifacts.
- **True layer names (L1–L9)** — May appear in internal docs and code; must not be exposed as the canonical “map” of the engine in public docs or schemas.

Public metric exposure is defined by PUBLIC_METRIC_EXPOSURE_POLICY and public_metric_profiles.json (curated subsets only).
