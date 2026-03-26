# Semantic dynamics operator (H_total)

## Purpose

Define a deterministic semantic propagation operator `H_total` over concept activations so segment processing becomes a **state machine**: each segment updates a carried concept state `ψ` using fixed sparse structure, bounded nonlinearities, and audited normalization — instead of treating each window as an isolated score pile.

`H_total` is **not** a physics model. It is a **fixed, release-pinned, deterministic operator** over the concept index.

**Mainline policy:** canonical product documentation and shipping surfaces do not carry medical or clinical vocabulary; only structural implementation is in scope. See `docs/governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md`.

## Core definition

### Operator (one segment step)

Let `ψ_t` be concept state after segment `t`, and `e_t` be stabilized concept evidence for the current segment (same space as pre-hex concept weights in the invariant lexical activation path).

\[
\psi_{t+1} = \mathrm{Normalize}\Big(\mathrm{Prune}_\varepsilon\big(\mathrm{Saturate}(H_{total}\psi_t + \alpha e_t)\big)\Big)
\]

- `H_total ψ_t`: sparse multiply — diagonal self-retention plus undirected edge weights (symmetric).
- `α`: evidence injection coefficient (default `0.7`).
- `Saturate`: `sat(x) = sign(x) · (1 - exp(-k|x|))` with default `k = 1.2`.
- `Prune_ε`: `|x| < ε → 0` (default `ε = 0.03`).
- `Normalize`: L1 on absolute values with floor `norm = max(Σ|ψ_i|, 1.0)` (no naive signed-sum normalization).

### Matrix construction (offline)

\[
H_{total} = H_{self} + H_{coupling} - H_{inhibition}
\]

Stored as **sparse edge list** plus **diagonal map** (never ship dense JSON).

Constraints:

- symmetric (each unordered pair appears once; `value` is the final compiled weight)
- bounded per `build_rules.bounded_min` / `bounded_max` (default `[-1, 1]`)
- sparse, deterministic, fixed per release
- must not be rebuilt from runtime text

## Data specification

### File

`assets/data/engine_dynamics_v060/semantic_dynamics/h_total_concepts.json`

**Build (mainline):** `python3 tools/build_h_total_concepts.py --install` — compiles from `dict_b/dict_b_seed.jsonl` + `semantic_dynamics/area_inhibition_matrix_main_v1.json` (no TFP). Validate: `python3 tools/validate_h_total_concepts.py`. Re-pin after Dict B or inhibition matrix changes.

### JSON Schema

`schemas/semantic_dynamics/h_total_concepts.schema.json`

### Field semantics

| Field | Meaning |
| --- | --- |
| `concept_index` | Ordered universe of concept IDs for `ψ` |
| `diagonal[c]` | Self-retention / persistence for `c` (typical tuning band ~0.35–0.75) |
| `edges[].coupling` | Nonnegative compiled affinity component (audit) |
| `edges[].inhibition` | Nonnegative compiled suppression component (audit) |
| `edges[].value` | **Precomputed** `coupling - inhibition` used at runtime (deterministic, no re-derive) |
| `edges[].reason` | Traceability token for governance review |
| `build_rules` | Symmetry, bounds, defaults |
| `normalization` | Offline build normalization metadata |
| `provenance` | Sources and build method |

## Runtime integration (Hesperia)

### Module

`hesperia/nlp/semantic_state_update.py`

- `load_h_total`, `propagate_state`, `update_semantic_state`
- `merge_propagated_with_evidence_off_index` — concepts **in** `concept_index` use propagated `ψ`; others keep stabilized evidence for hex (so unknown IDs are not silently dropped).

### Calibration switch

`assets/data/engine_dynamics_v060/tfp/tfp_signal_calibration_v2.json` → `semantic_dynamics`:

- `operator_enabled` — default **`false`** until a production `h_total` covers the active concept universe.
- `h_total_relative_path` — relative to `assets/data/engine_dynamics_v060/`.
- `alpha`, `sat_k`, `prune_eps` — segment update hyperparameters.

### Pipeline position

Invariant TFP path in `hesperia/nlp/tfp_activation.py`:

1. Raw concept sums → **stabilized** evidence `e_t`
2. If `semantic_dynamics.operator_enabled`: **semantic state update** → merged concept vector **then** hex feedback
3. Hex feedback → family/area aggregation → inhibition → softmax

Session topology (`research/clinical_tfp/session_topology.py`) threads `psi_prev` across windows when the operator is enabled and adds `semantic_dynamics_audit` to the topology payload.

## Audit

### Per segment (`semantic_state`)

When the operator runs successfully, activation output includes `semantic_state` with:

- `operator_applied`, `alpha`, `sat_k`, `prune_eps`
- nonzero counts before saturation vs after prune
- `state_l1_abs`, `top_concepts`

### Session / topology (`semantic_dynamics_audit`)

When enabled, `run_session_topology` may include:

- `h_total_loaded`, `matrix_id`, `version`, `source_path`
- `concept_count`, `edge_count`
- `symmetric_check_passed`, `bounded_check_passed`

## Tooling

**Offline build (`tools/build_h_total_concepts.py`):**

- **Default (mainline):** `dict_b_seed.jsonl` + `semantic_dynamics/area_inhibition_matrix_main_v1.json` → writes `outputs/semantic_dynamics/h_total_concepts.json`. Does **not** read `dict_b_tfp.jsonl` or `tfp/`.
- **TFP inputs (operator-only):** pass **`--use-tfp-inputs`** to use `dict_b_tfp.jsonl` + `tfp/area_inhibition_matrix_tfp.json`. Coordinate with Grace boundary while calibration runs.

```bash
python3 tools/build_h_total_concepts.py --dry-run
python3 tools/build_h_total_concepts.py
python3 tools/validate_h_total_concepts.py outputs/semantic_dynamics/h_total_concepts.json
```

Validate structure, bounds, and symmetry (schema optional if `jsonschema` installed):

```bash
python3 tools/validate_h_total_concepts.py
python3 tools/validate_h_total_concepts.py --no-schema
```

## Optional offline artifact

Leading eigenmodes of `H_total` may be shipped as `h_total_eigenmodes.json` for diagnostics and calibration review — **not** required for runtime v1.

## Failure modes

| Symptom | Likely cause |
| --- | --- |
| Explosion | missing saturation / bad bounds |
| Dead state | diagonal too low |
| Sticky concepts | diagonal too high |
| No competition | inhibition too weak in compiled edges |
| Nondeterminism / drift | asymmetric or text-dependent rebuild of `H_total` |

## Phased rollout

1. Operator at concept level, one step per segment (implemented).
2. Audit stability and continuity vs raw evidence (telemetry).
3. Offline eigenmode extraction.
4. Optional family-level operator (separate spec).
