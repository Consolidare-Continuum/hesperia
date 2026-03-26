# Semantic dynamics operator (H_total) — canonical spec

**Status:** production contract for Hesperia Engine Dynamics.  
**Not** a physics model: a **fixed, release-pinned, deterministic operator** over the concept index.

**Mainline policy:** sealed product wording avoids medical/clinical vocabulary; structure and code live in-repo. See `docs/governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md`.

---

## 0. Purpose

Replace isolated per-segment scoring with **state evolution**: segment `t` updates carried concept state `ψ_t` using a sparse `H_total`, bounded nonlinearities, and audited normalization.

---

## 1. Definition

### 1.1 Discrete operator

For concept indices `i, j` (off-diagonal):

\[
H_{total}[i][j] = W_{couple}[i][j] - W_{inhibit}[i][j]
\]

- \(W_{couple}\): nonnegative semantic affinity (compiled).
- \(W_{inhibit}\): nonnegative competitive suppression (compiled).
- **Diagonal:** self-retention / persistence (not “raw energy”): `diagonal[c]` ∈ typical band **0.35–0.75**.

### 1.2 Composition

\[
H_{total} = H_{self} + H_{coupling} - H_{inhibition}
\]

Off-diagonal edges store **precomputed** `value = coupling - inhibition` so runtime stays simple and deterministic.

### 1.3 Representation

- **Sparse edge list** + **diagonal map** — never ship dense matrix JSON.
- **Symmetric:** each unordered pair `{a,b}` appears once; `value` is the final weight.
- **Bounded** in \([-1, 1]\) (see `build_rules`).
- **Fixed per release** — not rebuilt from runtime text.

---

## 2. Data specification

### 2.1 File

`assets/data/engine_dynamics_v060/semantic_dynamics/h_total_concepts.json`

### 2.2 Shape (illustrative)

```json
{
  "version": "v060",
  "matrix_id": "h_total_concepts",
  "space": "concept_id",
  "description": "Deterministic bounded semantic propagation operator over concept activations.",
  "build_rules": {
    "symmetric": true,
    "bounded_min": -1.0,
    "bounded_max": 1.0,
    "default_missing_edge": 0.0,
    "diagonal_semantics": "self_retention",
    "off_diagonal_positive": "semantic_coupling",
    "off_diagonal_negative": "competitive_inhibition"
  },
  "normalization": {
    "row_balance_target": 1.0,
    "clip_abs_value": 1.0,
    "post_build_symmetrize": true
  },
  "concept_index": ["C0001", "C0002"],
  "diagonal": { "C0001": 0.60, "C0002": 0.55 },
  "edges": [
    {
      "a": "C0001",
      "b": "C0002",
      "coupling": 0.30,
      "inhibition": 0.00,
      "value": 0.30,
      "reason": "same_family"
    }
  ],
  "provenance": {
    "sources": ["…"],
    "build_method": "deterministic_rule_compilation",
    "notes": "…"
  }
}
```

**Mainline pin:** `python3 tools/build_h_total_concepts.py --install` — `dict_b_seed.jsonl` + `semantic_dynamics/area_inhibition_matrix_main_v1.json` (no TFP).  
**TFP / calibration:** `python3 tools/build_h_total_concepts.py --use-tfp-inputs --install` — coordinate with Grace boundary.

**Validate:** `python3 tools/validate_h_total_concepts.py`

### 2.3 JSON Schema

`schemas/semantic_dynamics/h_total_concepts.schema.json`

### 2.4 Field semantics

| Field | Meaning |
| --- | --- |
| `concept_index` | Ordered universe of concept IDs for `ψ` |
| `diagonal[c]` | Self-retention: how much activation carries from the previous step (typ. 0.35–0.75) |
| `edges[].coupling` | Nonnegative affinity component (audit) |
| `edges[].inhibition` | Nonnegative suppression component (audit) |
| `edges[].value` | **Precomputed** `coupling - inhibition` at runtime (no re-derive) |
| `edges[].reason` | Traceability token |
| `build_rules` | Symmetry, bounds |
| `normalization` | Offline build metadata |
| `provenance` | Source paths + build method |

---

## 3. Build rules (deterministic only)

Implemented in `tools/build_h_total_concepts.py` (constants + `compile_h_total`).

| Component | Rule (summary) |
| --- | --- |
| Diagonal | Base + specificity bonus; clamp to band |
| Coupling | Same family, same area / different family, anchor proximity; clamp |
| Inhibition | Area matrix × specificity factor; clamp |
| Edge value | `round(coupling - inhibition, 6)` |
| Symmetry | One edge per pair; stored value is already symmetric |

---

## 4. Runtime algorithm

**Component:** `hesperia/nlp/semantic_state_update.py`

One segment:

1. **Raw:** \(\psi^{raw} = H_{total}\psi_{prev} + \alpha e_t\)  
   - Diagonal: `diag[i] * psi_prev[i]`  
   - Off-diagonal: sparse `edges` (symmetric multiply)  
   - Evidence: `e_t` aligned to `concept_index`
2. **Saturate:** `sat(x) = sign(x)·(1 - exp(-k|x|))`, default `k = 1.2`
3. **Prune:** `|ψ| < ε → 0`, default `ε = 0.03`
4. **Normalize:** L1 on absolute values, `norm = max(Σ|ψ_i|, 1.0)`

Recommended defaults: `α = 0.7`, `k = 1.2`, `ε = 0.03`.

API: `propagate_state`, `update_semantic_state` (returns `psi_next` + per-segment audit).

---

## 5. Execution Flow integration (Hesperia)

**Insertion:** after **stabilized** concept evidence `e_t`, **before** hex feedback / area softmax cascade.

**Component:** `hesperia/nlp/tfp_activation.py` — `build_invariant_tfp_activation`

1. Raw markers → **stabilized** `stabilized_pre_hex` (= `e_t` in concept space)
2. If `semantic_dynamics.operator_enabled`: load `H_total` → `update_semantic_state(psi_prev, stabilized_pre_hex, …)` → `psi_next` → `merge_propagated_with_evidence_off_index` → **`concepts_into_hex`**
3. Hex feedback on **`concepts_into_hex`**
4. Family/area aggregation from post-hex concepts; area inhibition; softmax

**Pre-hex** family/area summaries use **`concepts_into_hex`** so masses match propagated `ψ` when the operator is on.

**Calibration:** `assets/data/engine_dynamics_v060/tfp/tfp_signal_calibration_v2.json` → `semantic_dynamics`: `operator_enabled`, `h_total_relative_path`, `alpha`, `sat_k`, `prune_eps`.

**Session:** `psi_prev` / topology — `research/clinical_tfp/session_topology.py` when enabled.

**Outputs:** `activation["semantic_state"]`, `activation["psi_concepts"]` when operator runs.

---

## 6. Area extraction (structural target)

Target formulation (concept → area weights, then softmax):

\[
\text{area\_score}[a] = \sum_{c} \max(\psi[c], 0) \cdot \mathrm{weight}(c \to a)
\]

Current execution_flow: area masses are derived via concept→area aggregation on the **propagated** concept vector feeding hex when semantic state is enabled (see §5). Full softmax-from-`ψ`-only tuning is a later calibration pass.

---

## 7. Audit

### 7.1 Per segment (`semantic_state`)

| Field | Description |
| --- | --- |
| `operator_applied` | bool |
| `alpha`, `sat_k`, `prune_eps` | scalars |
| `nonzero_concepts_before` | count on raw pre-saturate |
| `nonzero_concepts_after` | count after prune+normalize |
| `state_l1_abs` | \(\sum|\psi|\) after normalize |
| `top_concepts` | top entries by \(|\psi|\) |

### 7.2 Session / topology (`semantic_dynamics_audit`)

From `build_semantic_dynamics_session_audit`: `h_total_loaded`, `matrix_id`, `version`, `source_path`, `concept_count`, `edge_count`, `symmetric_check_passed`, `bounded_check_passed`.

---

## 8. Constraints

**Must:** deterministic; fixed per release; sparse; auditable; no runtime text rebuild; no randomness in operator construction.

**Must not:** dense full matrix JSON; per-segment rebuild of `H_total`; unconstrained row-sum drift; all-to-all edges.

---

## 9. Optional (offline only)

**Eigenmodes:** `h_total_eigenmodes.json` — leading modes, diagnostics, calibration — **not** required for runtime v1.

---

## 10. Phased rollout

1. Concept-level one-step update per segment (**implemented**).
2. Telemetry: stability, continuity vs raw evidence.
3. Offline eigenmode extraction.
4. Optional family-level operator (separate spec).

---

## 11. Deliverables (repo)

| Artifact | Role |
| --- | --- |
| `h_total_concepts.json` | Compiled operator (mainline or TFP path) |
| `semantic_state_update.py` | Load, propagate, audit |
| `tfp_activation.py` | Gated insertion + `psi_concepts` |
| `tools/build_h_total_concepts.py` | Offline compiler |
| `tools/validate_h_total_concepts.py` | Schema + symmetry + bounds |
| `schemas/semantic_dynamics/h_total_concepts.schema.json` | Strict shape |

---

## 12. Acceptance criteria

- Operator off: behavior unchanged (defaults).
- Operator on: adjacent segments couple through `ψ`; audit fields populated; `H_total` validates.
- Long-segment inflation reduced vs raw scoring (measured in calibration harness).

---

## 13. Failure modes

| Symptom | Likely cause |
| --- | --- |
| Explosion | missing saturation / bad bounds |
| Dead state | diagonal too low |
| Sticky concepts | diagonal too high |
| No competition | weak inhibition in compiled edges |
| Chaos / drift | asymmetric or text-dependent `H_total` |

---

## 14. Tooling (commands)

```bash
python3 tools/build_h_total_concepts.py --dry-run
python3 tools/build_h_total_concepts.py --install
python3 tools/validate_h_total_concepts.py
```

---

*Ethan — semantic dynamics operator — Hesperia Engine Dynamics*
