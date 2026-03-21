# TRIZ topology activation pipeline v1

**Module:** `hesperia.extensions.triz.topology_activation_pipeline`  
**CLI:** `python3 tools/run_triz_topology_activation.py --topology-json … --out-dir … [--session-id …]`

## Purpose

Derive **contradiction signal from real segment-level concept co-activation** (`research.clinical_tfp.session_topology` shape: `segments[].concepts`), not from an empty TRIZ layer.

## Artifacts (per session)

Written **flat** in the run’s `--out-dir` as `12_<session_slug>_<artifact>.json` when `run_tfp_file_pipeline --with-topology` runs (unless `--skip-triz-activation`). The manifest’s `triz_activation` map still keys logical names (e.g. `concept_coactivation_graph.json`) to absolute paths of those files.

| Artifact (suffix) | Task |
|------|------|
| `concept_coactivation_graph.json` | Pairwise co-occurrence across segments, normalized weights |
| `family_contradiction_matrix.json` | Full dense family–family scaffold (input to v0.5.2) |
| `concept_clusters.json` | Clusters from TRIZ `innovation_clusters` or synthetic from coactivation |
| `family_weights_sparse_v052.json` | Sparsified, recalibrated weights + `active_for_contradiction` (see `FAMILY_WEIGHTS_SPARSIFY_v052.md`) |
| `concept_contradictions_raw.json` | `coactivation × family_conflict` |
| `concept_contradictions_classified.json` | `parameter_change` / `segmentation` / `counterbalance` / `dynamic_adaptation` |
| `triz_metrics_v1.json` | Counts, density, cross-area rate, mean score |
| `contradiction_hotspots.json` | Top families by summed contradiction |
| `innovation_clusters_enriched.json` | Clusters from optional `08` TRIZ + within-cluster pair scores |
| `triz_dynamics.json` | Velocity / spillover / narrative penetration (minimal formulas) |
| `cross_plane_audit.json` | **`TRIZ_DEAD_LAYER`** if `topology_activation > 0.5` and `contradiction_count == 0` |

## Pipeline gate (Task 10)

- With `--with-topology` and without `--skip-triz-activation`, the file pipeline writes the bundle and sets **`manifest.errors`** on failure.
- Exit code **3** if `TRIZ_DEAD_LAYER` or topology error blocks activation or an exception occurs while writing.

## Design rules

- Deterministic heuristics only (no ML).
- Predefined high-conflict family pairs live in code (`PREDEFINED_FAMILY_CONFLICTS`).
- Refine thresholds later; v1 **forces** non-zero contradictions whenever multiple concepts co-occur in segments.

## Related

- `hesperia.extensions.triz.pipeline` — classic graph TRIZ (`08_triz_complete.json`)
- `docs/governance/working/ETHAN-TFP-RUNNABLE-DICT-WIRING.md` — TFP file pipeline
