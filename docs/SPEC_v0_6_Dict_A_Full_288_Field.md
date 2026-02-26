# Build Dict A v0.6 — Full 288-Family Field Model

**Status:** Normative
**Version:** v0.6.0
**Replaces:** v0.5 (failed)
**Mode:** Build-time deterministic generation
**Runtime:** Immutable artifact

## 1. OBJECTIVE

Redesign Dict A as a calibrated 288-dimensional semantic field.

Each token MUST yield:

- A mathematically valid probability distribution over all 288 families.
- Strong-signal metrics.
- Deterministic reproducibility.
- Calibrated comparability across families.

No sparse mapping. No heuristic patching. No multi-family first-entry hacks.

## 2. REQUIRED INPUTS

- **Frozen family specification (288 families):** label, core_definition, positive_axis, negative_axis, central_examples.
- **Embedding model:** sentence-transformers/all-mpnet-base-v2; fixed revision hash; CPU mode; deterministic inference; normalized embeddings.
- **Token source:** Canonical vocabulary list (existing pipeline source: Dict A keys or explicit vocab file).

## 3. BUILD PIPELINE

1. **Step 1 — Build family anchors:** For each family f, construct anchor_text from spec, embed once → A_f, normalize. Fail if not 288.
2. **Step 2 — Embed all tokens:** For each token t, embed → E_t, normalize. No dropout; deterministic.
3. **Step 3 — Raw similarity matrix:** sim_f(t) = cosine(E_t, A_f).
4. **Step 4 — Family-wise calibration:** μ_f, σ_f over tokens; z_f(t) = (sim_f(t) - μ_f) / σ_f. Fail if any σ_f ≈ 0.
5. **Step 5 — Temperature softmax:** τ = 0.35; w_f(t) = exp(z_f(t)/τ) / Z. Fail on NaN or sum deviation > 1e-6.
6. **Step 6 — Strong signal metrics:** margin_1_2, mass_top8, entropy, gini; strong_flag if margin_1_2 ≥ 0.06, mass_top8 ≥ 0.55, entropy ≤ 3.6.

## 4. ARTIFACTS

- **assets/v060/dict_a_v060.jsonl** — One JSON object per line: token, topk (K=32), metrics (margin_1_2, mass_top8, entropy, gini, strong).
- **assets/v060/family_prior_v060.json** — Normalized frequency of family as argmax across tokens (for runtime tail model).
- **assets/v060/dict_a_v060.sha256** — SHA256 of dict_a_v060.jsonl.

## 5. TAIL PRIOR MODEL (RUNTIME COMPACT MODE B)

tail_mass = 1 − Σ(topk weights). For families not in topk: w_f_runtime = tail_mass × π_f_normalized_excluding_topk.

## 6. VALIDATION

**validate_dict_a_v060.py** — Verifies: exactly 288 anchors (from family spec), no negative weights, no NaN. Reports: % strong tokens, family dominance histogram, entropy distribution. Hard-fail on structural violations, σ_f collapse, missing families. Do NOT fail on low strong percentage — only warn.

## 7. SUCCESS CRITERIA

v0.6 is structurally successful if:

- Artifact builds deterministically.
- Calibration stabilizes dominance distribution.
- ≥ 20% tokens classified strong (domain-dependent; warning if below).
- No single family dominates > 25% tokens unless justified.

## 8. IMPLEMENTATION

| Component | Path |
|-----------|------|
| Family spec skeleton | hesperia_lex/scripts/build_family_spec_v060.py → hesperia_lex/curated/FAMILY_SPEC_v0_6.json |
| Build pipeline | sphere_rag/build_dict_a_v060.py |
| Validator | sphere_rag/validate_dict_a_v060.py |

Run from **CLIENTS/hesperia**:

```bash
# 1. Generate family spec (skeleton; curate FAMILY_SPEC_v0_6.json as needed)
PYTHONPATH=. python3 hesperia_lex/scripts/build_family_spec_v060.py

# 2. Build Dict A v0.6 (vocab from Dict A keys if --vocab not set). Use venv with sentence-transformers + PyTorch (e.g. .venv_v040_build).
PYTHONPATH=. python3 sphere_rag/build_dict_a_v060.py [--vocab path] [--assets path] [--out-dir path]

# 3. Validate
PYTHONPATH=. python3 sphere_rag/validate_dict_a_v060.py [--dict-a path] [--report path]
```

**Note:** Build requires `sentence-transformers` and PyTorch in a clean env (CPU). If the system has conflicting TensorFlow/transformers backends, use the project build venv (e.g. `.venv_v040_build/bin/python`).
