<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA v0.5 — Dict A Dense Projection (Operational Spec)

**Superseded by:** [OPERATIONAL_SPEC_v0_6.md](OPERATIONAL_SPEC_v0_6.md) (v0.6 full release). Retained for history.

**Status:** Build-time + runtime integration.
**Build v0.5 Dict A:** **FAIL** (count: 1). Retained only for experience gained; do not treat as production path.
**Goal:** Replace sparse Dict A lookup with deterministic 288-family dense projection.

## 1. Objective

- **From:** token → single family hit (or NONE).
- **To:** token → 288-dimensional attribution vector.
- **Guarantees:** No semantic vacuum; no dominant-family ties by absence; deterministic; backward compatible 6-key contract.

## 2. Scope

- **Included:** Family anchor spec, embedding + centroid freeze pipeline, deterministic projection engine, integration into `run_attribution_pipeline`, 6-key output unchanged.
- **Excluded:** Dict B changes, GPT wiring, nginx/auth.

## 3. Artifacts

| Artifact | Purpose |
|----------|--------|
| `hesperia_lex/curated/FAMILY_ANCHORS_v0_5.json` | 288 families: label, positive (5–20), negative (3–10). Skeleton from script; replace with curated before freeze. |
| `hesperia_lex/scripts/build_family_anchors_skeleton_v05.py` | Generate skeleton from `invariant_catalog.AREA_FAMILY_MAP`. |
| `sphere_rag/build_family_centroids_v05.py` | Build: embed anchors → normalized centroids → `FAMILY_CENTROIDS_v0_5.json` + SHA256. |
| `hesperia_lex/frozen/FAMILY_CENTROIDS_v0_5.json` | Per-family positive/negative centroid vectors (frozen). |
| `sphere_rag/dense_projection_v05.py` | `project_token(token)` → 288-dim; cosine pos_sim − neg_sim, clamp [-1,1]. |
| `sphere_rag/attribution_v05.py` | Dense path: sentence_vector = mean(sum project_token); dominant = argmax(abs); weighted seed. |
| `sphere_rag/verify_dense_projection_v05.py` | Determinism: fixed sentence × 10 runs, assert identical within 1e-9. |

## 4. Model and Build

- **Model:** `sentence-transformers/all-mpnet-base-v2`.
- **Revision:** Set `HESPERIA_V05_MODEL_REVISION` for freeze (commit/tag).
- **Build:** From `CLIENTS/hesperia`: `PYTHONPATH=. .venv_v040_build/bin/python sphere_rag/build_family_centroids_v05.py` (or `.venv_v040/bin/python`). Requires `sentence-transformers` + PyTorch (see `requirements_v040.txt` / `requirements-build-embeddings.txt`).
- **Runtime:** Load centroids only; embed token at runtime. No anchor embedding at runtime. Dense mode requires `hesperia_lex/frozen/FAMILY_CENTROIDS_v0_5.json` to exist.

## 5. Runtime Mode

- **Env:** `HESPERIA_ATTRIBUTION_MODE=dense` (default) or `sparse`.
- **Default:** dense. Sparse = fallback to v0.3.3 Dict A/B pipeline.

## 6. Contract

- **Output:** Same 6 keys: dominant_area, dominant_family, governance, loopability, tension_energy, obstacle_score.
- **Extended:** total_tokens, matched_tokens (= total in dense), attribution_coverage (= 1.0 in dense), meanAltitude_global, seed_size.
- **Seed:** Weighted by family mass (abs(sentence_vector[f]) > eps); 1500 sides per contributing family.

## 7. Success Criteria

- Calibration: 0 semantic vacuum, coverage ≈ 1.0, dominant_family varies by domain, shadow deltas measurable (once core math uses seed/traversal), determinism holds.

## 8. Live API checks (production)

**Runbook:** [RUNBOOK__v05_dense_live_proof.md](RUNBOOK__v05_dense_live_proof.md)

1. **Prove chroma venv:** Run the two one-liners (sentence_transformers+torch; centroids exists, len 288). If either fails: (A) pip install into chroma venv, or (B) point service ExecStart at build venv. Don’t keep two half-working envs.
2. **Prove dense via public API:** Two curls with Bearer — unknown token and former-vacuum sentence. Both must return **200**. If 400, dense is not live.
3. **Shadow:** Do not run shadow comparisons until core consumes family_vector; see [TASK__wire_family_vector_into_core_shadow_perturbs.md](TASK__wire_family_vector_into_core_shadow_perturbs.md).

## 9. Why sparse “missed” words (v0.4.x)

Sparse did not miss because “words aren’t in the language”. It missed because:
- Sparse path matches only **explicit lexical surfaces** in Dict A / surface map.
- “trust” hits when the surface map points to a Dict A key; “cooperation” misses when that surface (or map entry) is absent.
- Dict A is a frozen keyed structure, not a general English dictionary.
- Dense fixes this by **projecting any token** into the 288-family space; no surface map required for coverage.
