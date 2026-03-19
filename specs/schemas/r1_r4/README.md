<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# R1–R4 JSON Schemas (2020-12)

Deterministic-friendly, guard-compatible validation for Reading-Scale Unit and Book Profile outputs. Validate pipeline outputs **before** any LLM or analyst consumes them.

| File | Validates |
|------|-----------|
| **SI_metrics.schema.json** | Reusable SI_metrics object (coverage, dominance, entropy, leakage, contradiction_pressure, stability, shadow_deviation, trust_tier). All metrics [0,1]; trust_tier ∈ {T0,T1,T2,T3}. |
| **Unit.schema.json** | R1–R4 unit: unit_id (pattern `^R[1-4]:.+`), level, parent_id, token_count, top_areas, top_families, SI_metrics, flags (band, decision_code). |
| **BookProfile.schema.json** | Composite: book_id, level_averages (SI_means [0,1], SI_variances [0,0.25]), scale_deltas (delta_expected fill 0.0 until H2 locked), turning_points, structural_signature. |

Spec: `docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md` Part C.
