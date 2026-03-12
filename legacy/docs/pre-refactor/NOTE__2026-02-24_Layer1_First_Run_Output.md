<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Note — Layer-1 first run output

**Date**: 2026-02-24
**Script**: `sphere_rag/layers/layer_1.compute_L1` (34_SPEC).

## Run

- **Input**: Text `"justice lie fairness truth good order harm freedom"` → normalized, tokenized (8 tokens).
- **Attribution**: Dict A = `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json`, Dict B from frozen B0 (or {}).
- **Matched**: 3 tokens (justice, lie, fairness in Dict A); coverage 0.375.
- **Defaults**: `load_defaults()` → F=288, A=12, eps=1e-9.

## First output (25 variables)

| Variable | Value |
|----------|--------|
| TOTAL_TOKENS | 8 |
| ATTRIBUTED_TOKENS | 3 |
| COVERAGE_RATIO | 0.375 |
| UNIQUE_FAMILIES_HIT | 1 |
| FAMILY_ACTIVATION_DENSITY | 0.003472 |
| FAMILY_HIT_VECTOR_L1 | 3.0 |
| FAMILY_HIT_VECTOR_L2 | 3.0 |
| MAX_FAMILY_HITS | 3 |
| DOMINANT_FAMILY_ID | 0 |
| DOMINANT_AREA_ID | 0 |
| DOMINANCE_RATIO | 1.0 |
| MEAN_ALTITUDE_GLOBAL | 0.7 |
| MEAN_ALTITUDE_DOMINANT | 0.7 |
| ALTITUDE_VARIANCE_GLOBAL | 0.0 |
| FAMILY_ENTROPY | 0.0 |
| NORMALIZED_FAMILY_ENTROPY | 0.0 |
| GINI_COEFFICIENT | 0.993056 |
| UNIQUE_AREAS_HIT | 1 |
| AREA_SPREAD | 0.083333 |
| AREA_DOMINANCE_RATIO | 1.0 |
| SECONDARY_FAMILY_RATIO | 1.0 |
| SIGNAL_TO_NOISE_RATIO | 3e9 (effectively; remainder=0 so dominant/(eps)) |
| SPARSITY_INDEX | 0.996528 |
| TOKEN_REDUNDANCY_RATIO | 0.666667 |
| ALTITUDE_WEIGHTED_MASS | 2.1 |
| STRUCTURAL_STABILITY_INDEX | 1.0 |

## Notes

- All 3 attributed tokens landed in family 0 (one family) → DOMINANCE_RATIO 1.0, FAMILY_ENTROPY 0, STRUCTURAL_STABILITY_INDEX 1.0.
- SIGNAL_TO_NOISE_RATIO = MAX_FAMILY_HITS / (ATTRIBUTED - MAX_FAMILY_HITS + eps); when all mass in one family, denominator = eps, so value is very large; spec-compliant.
- First run successful; script and defaults OK.
