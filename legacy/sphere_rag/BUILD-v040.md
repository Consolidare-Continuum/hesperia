# HESPERIA v0.4.0 build (28_SPEC)

Build pipeline: Dict A → anchor embeddings → Dict B → surface (roles + map). Build-time only; runtime uses frozen artifacts.

## One-time setup

1. **Dependencies** (recommend venv for clean env):
   ```bash
   cd CLIENTS/hesperia
   python3 -m venv .venv_v040
   .venv_v040/bin/pip install -r requirements_v040.txt
   ```
   Or install globally: `pip install -r requirements_v040.txt`

2. **Model** is downloaded automatically on first run: `sentence-transformers/all-mpnet-base-v2`.

## Inputs

- **Dict A**: default `A_CORE_STAR_MAP_v0_4_1_1.json` (v0.4.1.1 semantic, gates). v0.4.1 (`A_CORE_STAR_MAP_v1.json`) deprecated; use `--dict-a` to override.
- **Candidates**: optional file (one token per line or JSON list/dict keys). If omitted, build uses Dict A lemmas + B_SURFACE aliases.

## Run

From repo root or from `CLIENTS/hesperia`:

```bash
cd CLIENTS/hesperia
.venv_v040/bin/python -m sphere_rag.build_v040 \
  --assets-root hesperia_lex/curated \
  --out-dir assets/v040 \
  --mode balanced
```

For **tiny Dict A** (e.g. 3 lemmas) use `--allow-small-build` to skip κ and F_min_covered checks.

## Outputs (in `--out-dir`)

| File | Purpose |
|------|--------|
| `dict_a_anchors_v040.json` | Anchor embeddings (lemma, familyGlobal, altitude, embedding). |
| **§8A diagnostic** | |
| `dictA_family_affinity_v040.json` | Per-lemma: primary_family, primary_score, full_affinity_vector[288], top5_families, OSS. |
| `family_vectors_v040.json` | Per-family mean embedding vector (frozen). |
| `report_dictA_affinity_matrix_v040.txt` | OSS distribution, % ambiguous, top 20 weakest, FCS per family, CFL top pairs. |
| `report_family_geometry_v040.txt` | Inter-family similarity summary, most similar/isolated families, entropy. |
| `dictA_geometry_flags_v040.json` | weak_anchor, thin_families, family_overlap_pairs (QA flags). |
| `dict_b_v040.json` | Runtime Dict B: token → familyGlobal. |
| `dict_b_v040_audit.jsonl` | Per-token audit (scores, anchors, ambiguity). |
| `surface_roles_v040.json` | Per-family 1500 side roles (L/T/S/R). |
| `surface_map_v040.json` | side_id → token bucket. |
| `report_dictA_coverage_v040.txt` | Anchors per family, thin families. |
| `report_dictB_stats_v040.txt` | Accept/reject rates, similarity stats, imbalance. |
| `report_surface_stats_v040.txt` | Role quotas, per-hex constraints, bucket stats. |
| `build_manifest_v040.json` | Model revision, torch/python versions, τ/δ/κ, date. |

## Runtime (production)

Load only: `dict_b_v040.json`, `surface_roles_v040.json`, `surface_map_v040.json` (+ Dict A if needed). Do not load the embedding model at runtime.
