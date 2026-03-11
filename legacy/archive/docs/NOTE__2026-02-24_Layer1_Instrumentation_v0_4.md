# Note — 2026-02-24 Math day: Layer-1 and Layer-2 instrumentation

**Session**: Math day; Cursor take-off.

**Added**:
- **34_SPEC__V0_4_Layer1_Instrumentation_25_Variables_v1_0.txt** — canonical Layer-1 for v0.4.x baseline.
  - Contract: first layer only variables that are deterministic, reproducible, input-bound; no probabilistic semantics, no LLM weighting, no shadow deviation.
  - 25 variables defined (TOTAL_TOKENS … STRUCTURAL_STABILITY_INDEX).
  - Auxiliary: `computeGini`, `secondMax`, altitude variance (per-family decomposition when no per-token altitudes).
  - Java-style pseudocode §6 in same spec.

- **35_SPEC__V0_4_Layer2_Geometric_Traversal_25_Variables_v1_0.txt** — canonical Layer-2 for v0.4.x baseline.
  - Contract: must not reinterpret meaning; measure movement inside geometry only. No semantics, no books, no shadow deviation; only traversal math on frozen topology.
  - Prerequisites: pre-frozen family adjacency graph, area structure, depth limit D, Layer-1 dominant family.
  - 25 variables (TRAVERSAL_START_FAMILY … GEOMETRIC_STABILITY_INDEX); BFS-based; clustering, centrality, loop count, boundary crossings.
  - Java-style pseudocode §6 including BFS with parent tracking, induced subgraph edges, computeClustering.

- **36_SPEC__V0_4_Layer3_Shadow_Divergence_25_Variables_v1_0.txt** — Layer-3 shadow divergence.
  - Contract: measure divergence between baseline (B) and shadow (S) only; no semantics, no books; deterministic; SHADOW_ACCEPTABILITY_GATE.
  - 25 variables: SHADOW_ENABLED through SHADOW_ACCEPTABILITY_GATE; deltas on Layer-1/Layer-2; VISITED_JACCARD, VISITED_SYMMETRIC_DIFFERENCE_RATIO, HIT_VECTOR_COSINE_SIMILARITY, TOP_K_OVERLAP_RATIO; SHADOW_DEVIATION_SCORE (0.35/0.35/0.30); gate = deviation ≤ max && |CROSS_AREA_RATIO_DELTA| ≤ max && (area flip allowed or not changed).
  - Config: SHADOW_MAX_DEVIATION, SHADOW_MAX_CROSS_AREA_DELTA, SHADOW_ALLOW_AREA_FLIP. Java-style §6.

- **37_SPEC__V0_4_Layer4_Book_Evidence_25_Variables_v1_0.txt** — Layer-4 book intersection & evidence.
  - Contract: not "book says I'm right"; given structural decision, did deterministic retrieval return evidence whose frozen labels intersect activated region and is store intact? No semantic authority (21_SPEC, 22_SPEC §13).
  - 25 variables: RETRIEVAL_MODE_ID, TOP_K, retrieved counts/shortfalls, unique books, duplicate ratios, family/area match, TOP_K_FAMILY_COVERAGE, EVIDENCE_ENTROPY/GINI, RANK_WEIGHTED_ALIGNMENT, HIT_EVIDENCE_OVERLAP B/S, EVIDENCE_JACCARD_BS, BOOKSET_JACCARD_BS, EVIDENCE_SHIFT_SCORE, INTEGRITY_CHECK_PASS_RATIO, EVIDENCE_SUPPORT_INDEX_BASELINE (0.45/0.35/0.20), EVIDENCE_ACCEPTABILITY_GATE.
  - Config: MAX_SHORTFALL, MIN_SUPPORT, MAX_DUP_BOOK_CONC. Java-style §6.

- **38_SPEC__V0_4_Layer5_Counter_Evidence_Trig_Reality_25_Variables_v1_0.txt** — Layer-5 counter-evidence + trig reality.
  - 5A (12): R_pos, R_neg, antiFamilies; ANTI_REGION_SIZE, RETRIEVED_COUNT_NEG, NEG_SHORTFALL, NEG_UNIQUE_BOOKS, NEG_DUPLICATE_BOOK_RATIO, NEG_AREA_MATCH_RATIO, POS_NEG_BOOKSET/JACCARD_CHUNK_JACCARD, POS_SUPPORT_INDEX, NEG_SUPPORT_INDEX, CONTRADICTION_PRESSURE_SCORE (0.55/0.25/0.20), REALITY_GATE_COUNTER_EVIDENCE.
  - 5B (13): DOT_SYMMETRY_RESIDUAL, DOT_SELF_NONNEG_RESIDUAL, NORM_CONSISTENCY_RESIDUAL, COSI_CLAMP_VIOLATION_COUNT, ANGLE_RANGE_VIOLATION_COUNT, LAW_OF_COSINES_RESIDUAL, SIN_COS_IDENTITY_RESIDUAL, ROTATION_NORM_PRESERVATION_RESIDUAL, ORTHONORMALITY_RESIDUAL_FROBENIUS, TRIANGLE_INEQUALITY_VIOLATION_COUNT, METRIC_SYMMETRY/IDENTITY_RESIDUAL, REALITY_GATE_TRIG. Prove geometry = real math; no fake precision.

- **39_SPEC__V0_4_Layer6_Conceptual_Math_Dynamic_Function_25_Variables_v1_0.txt** — Layer-6 conceptual math & dynamic function.
  - Engine as function x → y(x); E(x); perturbation ε. I Functional response (5): INPUT_PERTURBATION_RESPONSE, DOMINANT_FAMILY_STABILITY, COVERAGE_GRADIENT, ENTROPY_GRADIENT, STABILITY_RADIUS. II Second order (3): SECOND_ORDER_RESPONSE, DOMINANCE_CURVATURE, ENTROPY_CURVATURE. III Matrix (4): HIT_VECTOR_RANK, PC1_ENERGY_RATIO, CONDITION_NUMBER, SPECTRAL_GAP. IV Depth growth (4): DEPTH_GROWTH_RATIO, FIBONACCI_DEVIATION_SCORE, EXPONENTIAL_FIT_ERROR, POWER_LAW_FIT_ERROR. V Newtonian (3): POTENTIAL_GRADIENT, ESCAPE_ENERGY_THRESHOLD, FORCE_ANALOG_MAGNITUDE. VI Functional (6): MONOTONICITY_CHECK, FIXED_POINT, FUNCTIONAL_CYCLE, LYAPUNOV_ESTIMATE, GLOBAL_STABILITY_SCORE, CONCEPTUAL_COHERENCE_INDEX. Real systems analysis.

- **40_SPEC__V0_4_Layer7_Cross_Layer_Interactions_Limits_Aggregates_25_Variables_v1_0.txt** — Layer-7 cross-layer interactions, limits, aggregates.
  - A Consistency (10): CONSIST_COVERAGE_MIN_GATE, CONSIST_ATTRIBUTION_MASS_EQUALITY, CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED, CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL, CONSIST_AREA_MAPPING, CONSIST_EVIDENCE_INTEGRITY_HARD, CONSIST_SHADOW_DELTA_ONLY_IF_SHADOW, CONSIST_TRIG_REQUIRED_FOR_ANGLE_METRICS, CONSIST_COUNTER_EVIDENCE_VALID, CONSIST_STABILITY_REGIME_VALID. B Limits (8): TRUST_TIER, MAX_ALLOWABLE_*, SHADOW_WITHIN_LIMITS, CONTRADICTION_WITHIN_LIMITS, AREA_LEAKAGE_WITHIN_LIMITS, MAX_CHAOS_LEVEL. C Alignment (4): STRUCTURE_EVIDENCE_ALIGNMENT, SHADOW_EVIDENCE_ALIGNMENT_DELTA, SHADOW_JUSTIFICATION_SCORE, CONTRADICTION_ADJUSTED_SUPPORT. D Aggregates (3): SYSTEM_CONFIDENCE_SCORE, DECISION_STATUS_CODE, OUTPUT_TRUST_TAG. Canonical operational outputs.

- **41_SPEC__V0_4_Layer8_Units_Normalization_I18n_25_Variables_v1_0.txt** — Layer-8 units, normalization, i18n.
  - A (5): UnitType, ScalePolicy enums; EPS, clamp, rounding. B (8): ratioToPct, ratioToU1000, pctToU1000, u1000ToPct, radToDeg, signedDeltaToU1000, scoreToU1000, logBoundedToU1000. C (12): SI_* report units (L1–L7): SI_TOTAL_TOKENS_COUNT, SI_COVERAGE/DOMINANCE/ENTROPY, SI_GEOMETRIC_STABILITY, SI_AREA_LEAKAGE, SI_SHADOW_DEVIATION, SI_EVIDENCE_SUPPORT, SI_CONTRADICTION_PRESSURE, SI_TRIG_REALITY_FLAG, SI_GLOBAL_STABILITY, SI_SYSTEM_CONFIDENCE (PCT + U1000). Practical contract: raw, unitType, pct, u1000, policy.

- **42_SPEC__V0_4_Layer9_Human_Reference_Brand_Treatment_25_Variables_v1_0.txt** — Layer-9 human reference & brand.
  - A Bands (6): BAND_0_CRITICAL..BAND_5_EXCELLENT. B Direction (4): directionalScoreHighGood/lowGood, AREA_CONTAINMENT_U1000, CONSISTENCY_U1000. C Pillars (6): PILLAR_INPUT_QUALITY, GEOMETRY, EVIDENCE, CONSISTENCY, STABILITY, GOVERNANCE. D Brand words (5): BRAND_WORD_TRUST, EVIDENCE, CONTRADICTION, GEOMETRY, SHADOW. E Action flags (4): ACTION_REQUIRE_MORE_INPUT, REQUIRE_EVIDENCE_REBUILD, REQUIRE_GOVERNANCE_REVIEW, ALLOW_HUMAN_SUMMARY.

**Updated**:
- **22_SPEC__V0_3_Core_Math_Contract_v1_0.md** — §17 references 34–42_SPEC.
- **DOC_INDEX.md** — 34–42_SPEC under Core System Specs.
- **README.md** — Layer-1–9 in entry points table.

**Definitions frozen**:
- Layer-1: F, A, FAMILIES_PER_AREA, N, hits[f], altitudeSum[f], altitude ∈ [0,1]. Observes attribution; does not replace resolution.
- Layer-2: adjacency[f], area[f], MAX_ALLOWED_DEPTH, Layer-1 outputs. Measures geometry response to signal propagation; no interpretation.
- Layer-3: B and S runs; Layer-1/Layer-2 outputs for both; governance params. Compares runs; gate for shadow acceptability.
- Layer-4: R_B, R_S (retrieval chunks); chunk.bookId, chunk.familyId, chunk.chunkId; areaOf(familyId); checksumOK(c); MAX_SHORTFALL, MIN_SUPPORT, MAX_DUP_BOOK_CONC. Structural intersection and integrity only; no books vote.
- Layer-5: 5A — R_pos (= R_B), R_neg, antiFamilies; POS_SUPPORT_INDEX from Layer-4; MAX_CONTRADICTION. 5B — v,w, dot, norm, angle; EPS; optional a,b,c,γ, R, d(x,y). Trig/metric sanity only.
- Layer-6: x, y(x), E(x), ε; dominance/coverage/entropy from Layer-1; mass_at_depth from Layer-2; covariance over runs; finite-difference derivatives and curvature; rank, eigenvalues, fit errors; stability radius and escape energy; Lyapunov estimate. Real systems analysis.
- Layer-7: L1–L6 outputs; visited_B; FPA; EVIDENCE_SUPPORT_INDEX_SHADOW (when shadow enabled); MIN_COVERAGE_RATIO, EPS_INT, SHADOW_MAX_DEVIATION, MAX_CONTRADICTION, MAX_CROSS_AREA_RATIO, MAX_LYAPUNOV, HIGH_CONF, MED_CONF. Consistency gates, limits, alignment, DECISION_STATUS_CODE, SYSTEM_CONFIDENCE_SCORE, OUTPUT_TRUST_TAG.
- Layer-8: UnitType, ScalePolicy enums; EPS, clamp, rounding; ratioToPct, ratioToU1000, pctToU1000, u1000ToPct, radToDeg, signedDeltaToU1000, scoreToU1000, logBoundedToU1000; SI_* report units for L1–L7 (COUNT, PCT, U1000, BOOLEAN). Practical contract: raw, unitType, pct, u1000, policy.
- Layer-9: U1000 bands (critical/weak/fair/good/strong/excellent); directionalScoreHighGood/lowGood; AREA_CONTAINMENT_U1000, CONSISTENCY_U1000; pillars (INPUT_QUALITY, GEOMETRY, EVIDENCE, CONSISTENCY, STABILITY, GOVERNANCE); BRAND_WORD_* (TRUST, EVIDENCE, CONTRADICTION, GEOMETRY, SHADOW); ACTION_* flags (REQUIRE_MORE_INPUT, REQUIRE_EVIDENCE_REBUILD, REQUIRE_GOVERNANCE_REVIEW, ALLOW_HUMAN_SUMMARY).
**L1–L9 predefined defaults:** `LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt` and `layer_1_9_predefined_defaults_v1_0.json` list all inputs required before calculation (topology F/A/FPA, eps, L2–L7 config). System normal state, born with state. Cursor/code can compute any L1–L9 formula using Dict A/B frozen state + this list; no need to ask for thresholds.
