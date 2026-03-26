# Family weights sparsification v0.5.2

**Component:** `hesperia.extensions.triz.family_weights_sparsify_v052`  
**CLI:** `python3 tools/sparsify_family_weights_v052.py`

## Inputs

| File | Role |
|------|------|
| `family_weights.json` | Full symmetric family–family matrix (repo: often `family_contradiction_matrix.json`) |
| `concept_clusters.json` | `{ "clusters": [ { "cluster_id", "concepts" \| "families" }, … ] }` |

## Output

**`family_weights_sparse_v052.json`** — `edges[]` with `weight`, `effective_weight` (= `weight * log(1 + cluster_cooccurrence)` when overlap &gt; 0), `active_for_contradiction` (`weight >= 0.4`), stats, optional `matrix_sparse` (`--include-matrix` on CLI).

Execution Flow disk artifact omits `matrix_sparse` (`matrix_sparse_omitted: true`) to save size.

## Rules (summary)

- Top‑K = **8** per node with **union** keep (either endpoint ranks the other in top‑K), then per‑node degree cap at K by dropping weakest incidents.
- Drop weights **&lt; 0.25**; forbid **0.2** and **0.5** (recalculated bands).
- Cap **≤ 0.9**; structured bands for same‑area / cross‑area (cluster‑gated) / predefined strong.
- Cluster scale **×0.5** if no shared cluster; locality multipliers **1.0 / 0.8 / 0.5** by graph distance (same family / same area / cross area).
- Row‑sum normalization target **2.5–4.5**; promotions from the **top‑K pruned pool** only.
- §9 density checks apply when `node_count ≥ 30` and `edge_count ≥ 20` (uniformity when `edge_count ≥ 30`).

## Integration

`run_topology_triz_activation` writes **`concept_clusters.json`** and **`family_weights_sparse_v052.json`**, and drives **contradictions** from sparse weights (cross‑area off‑graph dropped; same‑area off‑graph uses a weak mapped prior, never 0.2/0.5).

See also: `docs/specs/TRIZ_TOPOLOGY_ACTIVATION_PIPELINE_v1.md`.
