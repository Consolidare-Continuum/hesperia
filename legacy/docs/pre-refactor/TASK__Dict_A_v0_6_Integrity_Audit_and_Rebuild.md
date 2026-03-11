# Historical reference (pre-refactor)

# TASK: Dict A v0.6 Integrity Audit + Clean Rebuild

**Status:** Mandatory
**Mode:** Deterministic
**Goal:** Confirm whether collapse is calibration failure or pipeline failure.

---

## PHASE 1 — Structural Integrity Audit (NO REBUILD YET)

**Script:** `sphere_rag/audit_dict_a_v060_runtime.py`

1. **Token-Level Variation** — 10 tokens (spec: altruism, power, trade, …). If all OOV, samples 10 in-dict tokens. Prints top 10 families, margin_1_2, entropy.
   **FAIL:** In-dict outputs identical → Case B (artifact/softmax collapse). All spec tokens OOV → vocabulary mismatch.

2. **Sentence-Level Raw Vector** — 3 sentences (social_cohesion, conflict_power, technical_systems). Prints 288-vector checksum and top 10 families.
   **FAIL:** Vectors identical → aggregation bug (Case A) or OOV-only (vocabulary mismatch).

3. **Calibration Statistics** — Requires `calibration_stats_v060.json` (build with `--save-calibration-stats`). Prints min/max/mean σ_f, count σ_f < 1e-6, histogram μ_f.
   **FAIL:** σ_f collapse → Case C (calibration broken).

**Decision tree:** A = aggregation bug; B = artifact/softmax collapse; C = calibration failed; vocabulary mismatch = build keys vs runtime tokenize (surface forms). Fix: use surface map at runtime (surface→lemma) so tokenize output resolves to dict keys.

---

## PHASE 2 — Clean Rebuild (ONLY IF NEEDED)

If calibration failure (Case C): rebuild with stability guards:

- τ = 0.5 (not 0.35)
- ε = 1e-6 added to σ_f
- Clip z_f to [-10, 10] before softmax

**Build:** `--stability-guards`
**Calibration stats:** `--save-calibration-stats` (for audit).

---

## PHASE 3 — Aggregation Sanity

Sentence-level family vector:

- **V_S = mean over tokens of w_f(token)**
- Normalize once (sum = 1), then compute dominance.
- Not: first token only, max over tokens, or re-softmax.

**Implementation:** `attribution_v06._sentence_vector_v060`: mean then normalize (sum=1). No re-softmax.

---

## PHASE 4 — Metric Validation

After rebuild and runtime fix (surface map):

- Run 100-sentence set.
- **Expected:** social_cohesion, conflict_power, economic_exchange, identity_culture, technical_systems show different dominant families where tokens hit dict; governance/loopability/tension vary.
- **Success:** Different domains produce different dominant families; metrics not identical; no single family >30% unless justified; entropy distribution non-flat.

---

## STRICT RULES

- Do NOT: adjust τ based on results, modify ontology, manually reassign families, inject domain heuristics.
- Fix: math or aggregation only. Runtime: surface map resolution (surface→lemma) is pipeline alignment, not ontology change.

---

## IMPLEMENTATION SUMMARY

| Item | Path / Command |
|------|----------------|
| Audit | `PYTHONPATH=. python3 sphere_rag/audit_dict_a_v060_runtime.py [--v060-dir path]` |
| Build (stability + stats) | `PYTHONPATH=. .venv_v040_build/bin/python sphere_rag/build_dict_a_v060.py --assets hesperia_lex/frozen --save-calibration-stats --stability-guards` |
| Surface map | Loaded in `attribution_v06` from `load_dict_a_surface_map_v033` (hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.json). Token lookup: key = surface_map.get(t, t). |
| Calibration run | `PYTHONPATH=. python3 scripts/run_calibration_v060.py` |

**Result (after surface map + stability rebuild):** 100/100 OK; 10 distinct dominant_area; 26 distinct dominant_family; 38 distinct governance values. Family 228 still dominates 60% of sentences (prior-heavy or skeleton spec); further differentiation requires curated FAMILY_SPEC_v0_6 or vocabulary expansion.
