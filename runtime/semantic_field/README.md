<!--
HESPERIA — RAD
-->

# Semantic field runtime

Executes **`hesperia.extensions.dynamics.equations`** from JSON config and writes measurable outputs (family field, area projection, timeline, energy trajectories).

## Ontology-driven matrices

If the config includes **`ontology`** (`family_ids`, `relations`, `contradictions`, `resistance_priors`), **W_F, C_F, R** are built by **`hesperia.extensions.dynamics.matrix_builders`** ([FIELD_MATRIX_BUILDERS_v1](../../specs/dynamics/FIELD_MATRIX_BUILDERS_v1.md)). Documents may use **`source_family_id`**. Example: `runtime/configs/semantic_field_ontology_example.json`. Calibration runner uses the same resolution.

```bash
python3 -m runtime.semantic_field.run_semantic_field \
  --config runtime/configs/semantic_field_ontology_example.json \
  --output out/semantic_field_ontology_run.json
```

## Usage

From repository root:

```bash
python3 -m runtime.semantic_field.run_semantic_field \
  --config runtime/configs/semantic_field_example.json \
  --output out/semantic_field_run.json
```

## Config

| Key | Role |
|-----|------|
| `family_count` | Must equal `area_count` × `families_per_area` (e.g. 288 = 12×24) |
| `adjacency_matrix` | Full fc×fc non-negative weights **or** `adjacency_mode`: `"canonical_ring"` |
| `resistance_vector` | Length fc, or a single number (broadcast) |
| `contradiction_matrix` | fc×fc **or** `"contradiction_zero": true` |
| `initial_field` | Length fc **or** `initial_mode`: `"uniform"` |
| `ontology` | Optional: builds matrices from relations/contradictions/priors (see spec) |
| `documents` | `source_vector` **or** `source_family_index` **or** `source_family_id` (with ontology) |
| `alpha`, `beta`, `gamma`, `delta` | Dynamics (required) |
| `mu`, `dt`, `epsilon`, `tau`, `clip_mode` | Optional |
| `time_now` | Optional reference time for document decay |
| `max_steps` | Cap for `run_until_convergence` (default 50) |

## Output

- `family_field_final`, `area_field_final`
- `timeline` (per-step JSON from `FieldStepResult`)
- `energy_prev_trajectory`, `energy_next_trajectory`

## Field calibration (HCI grid search)

**HSPR Calibration Index (HCI):** one bounded score \([0,1]\) for stable, source-aligned, low-contradiction fields. Spec: [specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md](../../specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md).

```bash
python3 -m runtime.semantic_field.run_field_calibration \
  --config runtime/configs/field_calibration_example.json \
  --output out/run_output_e2e_field_calibration.json
```

Emits three deterministic JSON artifacts next to the base path:

| File | Content |
|------|---------|
| `run_output_e2e_field_calibration.json` | Full report: `best`, `top_k`, interpretation; optional `all_results` |
| `run_output_e2e_field_calibration_best.json` | Best candidate, HCI, components, convergence, `field_final`, `area_field_final` |
| `run_output_e2e_field_calibration_topk.json` | Ranked top-k summary rows |

Config mirrors `run_semantic_field` for matrices (`adjacency_matrix` or `adjacency_mode`, etc.). Set `"include_all_results": true` to embed every grid evaluation (large).

---

## Pipeline (target wire)

Document → Dict A → Dict B → family activation → **this runner** → KME / TRIZ (still to integrate).

## Still to add

- Matrix builders from ontology (family adjacency, contradiction graph, resistance priors)
- Full pipeline integration
- Calibration layer for α, β, γ, δ from corpora

See [specs/dynamics/semantic_field_dynamics.md](../../specs/dynamics/semantic_field_dynamics.md).
