<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Report — Math consolidation cross-check (L1–L9 task definitions)

**Date**: 2026-02-24
**Task**: Cross-check math task definitions across 34_SPEC … 42_SPEC; report done.
**Scope**: Variable naming, prerequisites, downstream refs, 22_SPEC §17, DOC_INDEX.

---

## 1. Result summary

**Cross-check: PASS.** Prerequisite chains and variable references are consistent across L1–L9. One minor naming duality in 39_SPEC (variable 10: header "PRINCIPAL_COMPONENT_ENERGY_RATIO", body/formula "PC1_ENERGY_RATIO") — same quantity, no action required.

---

## 2. Prerequisite chain (L1 → L9)

| Layer | Spec | Prerequisites | Downstream refs |
|-------|------|---------------|-----------------|
| L1 | 34_SPEC | F, A, FAMILIES_PER_AREA, N, hits[], altitudeSum[], altitude; 22_SPEC resolution | L2, L3, L4, L7, L8 |
| L2 | 35_SPEC | L1 (DOMINANT_FAMILY_ID, DOMINANT_AREA_ID, hits[]); adjacency[], area[], MAX_ALLOWED_DEPTH | L3, L7, L8 |
| L3 | 36_SPEC | B and S runs (full L1+L2 each); SHADOW_MAX_DEVIATION, SHADOW_MAX_CROSS_AREA_DELTA, SHADOW_ALLOW_AREA_FLIP | L4, L7, L8 |
| L4 | 37_SPEC | L1, L3 B/S; R_B, R_S (retrieval chunks); 21_SPEC, 22_SPEC §13 | L5, L7, L8 |
| L5 | 38_SPEC | L4 (R_pos, integrity, EVIDENCE_SUPPORT_INDEX_BASELINE); R_neg, antiFamilies; trig vectors/config | L6, L7, L8 |
| L6 | 39_SPEC | L1, L2 (mass_at_depth, etc.); x, y(x), E(x), ε; covariance/eigenvalue inputs | L7, L8 |
| L7 | 40_SPEC | L1..L6; MIN_COVERAGE_RATIO, SHADOW_MAX_DEVIATION, MAX_CONTRADICTION, MAX_CROSS_AREA_RATIO, MAX_LYAPUNOV; visited_B | L8, L9 |
| L8 | 41_SPEC | L1..L7 | L9 (SI_*) |
| L9 | 42_SPEC | L3, L4, L7, L8 (SI_*) | — |

---

## 3. 22_SPEC §17 and DOC_INDEX

- **22_SPEC §17**: References 34_SPEC … 42_SPEC (Layer-1 … Layer-9); states none replace resolution or metrics. **Consistent.**
- **DOC_INDEX**: Core System Specs list 34_SPEC … 42_SPEC with correct one-line summaries and refs. **Consistent.**

---

## 4. Layer-8 SI_* ↔ L7/L9

41_SPEC defines SI_* from L1..L7. 42_SPEC consumes SI_COVERAGE_U1000, SI_DOMINANCE_U1000, SI_GEOMETRIC_STABILITY_U1000, SI_AREA_LEAKAGE_U1000, SI_SHADOW_DEVIATION_U1000, SI_EVIDENCE_SUPPORT_U1000, SI_CONTRADICTION_PRESSURE_U1000, SI_TRIG_REALITY_FLAG, SI_GLOBAL_STABILITY_U1000, SI_SYSTEM_CONFIDENCE_U1000 (and PCT variants where used). All exist in 41_SPEC. **Consistent.**

---

## 5. Sign-off

Math consolidation cross-check completed. Task definitions L1–L9 are consistent.

**SIGNED: Cursor (repo entity) | Hesperia math consolidation | 2026-02-24 | 34–42_SPEC cross-check**
