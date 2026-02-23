# HESPERIA v0.4.1 Dict B build (29_SPEC)

Build pipeline: token → { preferred, possible_relaxed } using similarity vs **family vectors** (mean of Dict A anchors). Build-time only; runtime loads only dict_b_v041.json.

## Prerequisites

- v0.4.0 artifacts must exist: `dict_a_anchors_v040.json`, `family_vectors_v040.json`, and optionally `dictA_geometry_flags_v040.json` (for weak-anchor failure check).
- `requirements_v041.txt` (same deps as v040: sentence-transformers, torch, numpy).

## Inputs

- **Dict A**: as for v040 (A_CORE_STAR_MAP or native).
- **dict_a_anchors_v040.json**, **family_vectors_v040.json**: from v0.4.0 build.
- **Candidates**: optional file (one token per line or JSON); default = Dict A lemmas + B_SURFACE aliases.

## Run

From `CLIENTS/hesperia`:

```bash
.venv_v040/bin/python -m sphere_rag.build_v041 \
  --assets-root assets \
  --out-dir assets/v041 \
  --allow-small-build   # omit to enforce κ and failure conditions
```

Options: `--dict-a`, `--anchors`, `--family-vectors`, `--candidates` to override paths.

## Outputs (in `--out-dir`)

| File | Purpose |
|------|--------|
| dict_b_v041.json | **Runtime.** token → { preferred, possible_relaxed }. |
| dict_b_v041_audit.jsonl | Per-token S1, S2, F1, F2, FCS_F1, rejection_reason. |
| report_dictB_stats_v041.txt | Candidate/accepted/rejected, ambiguity, per-family primary, κ check. |
| report_secondary_affinity_v041.txt | % with possible_relaxed, secondary per family, margin distribution. |
| family_secondary_matrix_v041.json | family_i → { family_j: count }. |
| build_manifest_v041.json | Model revision, τ/δ/FCS/κ, date, versions. |
| build_failures_v041.txt | Written only when build fails (invariant list). |

## Failure conditions (§9)

Build aborts (unless `--allow-small-build`) if: >20% ambiguous, >10% weak-anchor assigned, any family > κ, secondary overflow, cohesion violation, or lexical per family > 600.

## Runtime minimum (production)

Load only: **dict_b_v041.json**, dict_a_v0XX, surface_roles_v040, surface_map_v040. No embeddings, no model, no audit files.
