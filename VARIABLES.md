# VARIABLES

Canonical variable index for HESPERIA.

This file now covers two scopes:

1. **Runtime/environment variables** used by executable code and deploy units.
2. **Specification/academic variables** used in numbered specs and `ACADEMIC.md` so readers can map formulas to implementation intent.

> Note: The spec/academic section is a consolidated glossary for the active v1/v0.x documentation line (10/11/12/13/16/19/21/40/42 + `ACADEMIC.md`).

---

## 1) Runtime environment variables (code + deploy)

| Variable | Purpose | Default / Example | Used by |
|---|---|---|---|
| `CHROMA_SERVER_URL` | Base URL for Chroma retrieval server. | `http://127.0.0.1:8002` | `api/analyze.py`, `deploy/hesperia-api.service` |
| `HESPERIA_DATA_DIR` | Base directory for local Hesperia data assets consumed by scripts and API flows. | Fallback to repo data paths when unset. Deploy example: `/data/workspaces/atomic-commit-hesperia` | `api/analyze.py`, `scripts/context_rag.py`, `scripts/ingest_hesperia_families.py`, `scripts/matrix_run.py`, `deploy/hesperia-api.service` |
| `PYTHONPATH` | Python import search path; used to include cursor workspace modules and local repo package roots. | Set dynamically by helpers or explicitly in service unit. | `api/analyze.py`, `scripts/context_rag.py`, `deploy/hesperia-api.service` |
| `OPENAI_API_KEY` | API key for OpenAI-powered statement extraction/classification utilities. | No embedded default; must come from environment. | `statements/extract_statements.py`, `statements/classify_statements.py` |

### Runtime notes

- Do **not** hardcode secrets in tracked files.
- Prefer shell export, gitignored `.env`, or deployment-level environment injection.

---

## 2) Canonical structural constants (spec + academic)

These constants define the frozen lattice geometry and are treated as invariants under Σ guard discipline.

| Variable | Meaning |
|---|---|
| `AREAS` / `AREA_COUNT` | Number of macro-areas on the semantic ring (12). |
| `FAMILIES_PER_AREA` | Number of families per area (24). |
| `TOTAL_FAMILIES` | Global number of families (288). |
| `HEXES_PER_FAMILY` | Number of hexes per family (250). |
| `SIDES_PER_HEX` | Number of sides per hex (6). |
| `TOTAL_HEXES` | Global hex count derived from family and per-family hex cardinality. |
| `TOTAL_SIDES` | Global side count derived from total hexes and 6-sided topology. |
| `AREA_RING_ORDER` | Fixed clockwise area order used by traversal and indexing. |

---

## 3) Coordinate and indexing variables (spec + geometry)

| Variable | Meaning |
|---|---|
| `areaId` | 0-based area index on ring. |
| `familyLocal` | Family index inside an area (0..23). |
| `familyGlobal` / `globalId` | Family index in full lattice (0..287). |
| `hexIndex` | Hex index inside a family (0..249). |
| `sideIndex` | Side index inside a hex (0..5). |
| `sideId` | Globally unique side identifier (bijective with full side coordinate tuple). |
| `SideCoord` labels (`Axx-Fyy-Hzzz-Sk`) | Human-readable coordinate label format used in API outputs/diagnostics. |

---

## 4) Semantic attribution and activation variables

| Variable | Meaning |
|---|---|
| `d_f(s)` / `d_f` | Base family activation from statement `s`. |
| `alpha[i]` | Raw area mass before normalization. |
| `A_vec[i]` | Normalized area activation vector. |
| `F_vec` | Family-level activation vector. |
| `C_f` | Accumulated family contribution during traversal/pass. |
| `w_pk` | Per-pass/per-step weighting factor for accumulation. |
| `tau[s]` | Side-level semantic intensity / occupancy variable. |
| `coveragePhi` | Coverage metric over reached semantic structure. |

---

## 5) Loopability, traversal, and novelty variables

| Variable | Meaning |
|---|---|
| `L_full` | Full loopability score (aggregate traversal viability). |
| `L_F` | Family novelty loop component. |
| `L_S` | Statement novelty loop component. |
| `G_F[p]` | Family novelty gain at traversal pass `p`. |
| `G_S[p]` | Statement novelty gain at traversal pass `p`. |
| `TAU_FAMILY` | Family activation threshold for novelty crossing. |
| `obstacleScore` | Traversal obstacle indicator / stop pressure. |
| `maxPasses` | Max traversal loops/passes allowed by policy run. |
| `stepBudget` | Max traversal steps for one execution. |

---

## 6) Axis, tension, and stability-control variables

| Variable | Meaning |
|---|---|
| `B[k]` / `AxisVector.B` | Six-axis bipolar diagnostic vector derived from area activations. |
| `tensionEnergy` | Scalar tension/polarity energy measure for semantic opposition. |
| `coherence` | Structural/semantic coherence indicator across region/traversal. |
| `fragmentation` | Dispersion/fragmentation indicator for region dynamics. |
| `polarization` | Polarization strength over opposite axes/areas. |
| `entropyMetric` | Entropy-like concentration/disorder measure for area/family distributions. |
| `drift` / `driftRate` | Temporal semantic drift metric across iterations. |

---

## 7) Governance and decision variables

| Variable | Meaning |
|---|---|
| `decisionIntegrity` | Governance score combining evidence/stability/consistency terms. |
| `strategicScore` | Strategy/action score combining action, coherence, saturation, evidence terms. |
| `evidenceQuality` | Trust quality of supporting evidence used in final decisioning. |
| `causalCoherence` | Causal consistency metric in reasoning chain. |
| `scaleConsistency` | Cross-scale consistency factor in governance equation. |
| `temporalStability` | Stability factor over time/iterations. |
| `contradictionScore` | Contradiction penalty term in governance equation. |
| `saturation` | Saturation penalty term in strategy equation. |
| `actionScore` | Base action utility term used in strategy composition. |

---

## 8) Guard-layer state variables (ΣΓΘ policy surface)

| Variable | Meaning |
|---|---|
| `SIGMA_OK` | Static invariant pass/fail state before runtime traversal. |
| `GAMMA_OK` | Runtime invariant pass/fail state during traversal dynamics. |
| `THETA_OK` | Governance publishability pass/fail state for release/output. |
| `structureHash` | Structural fingerprint for topology/indexing contract. |
| `configHash` | Configuration fingerprint for governance immutability checks. |
| `ingestionContractHash` | Ingestion schema/version contract fingerprint. |
| `failureMode` | Guard consequence mode (`HALT`, `ROLLBACK`, `CORRECT`, `REQUIRE_REVIEW`). |

---

## 9) Academic hashtag aliases (from `ACADEMIC.md`)

The following aliases are intentionally duplicated in the academic glossary to keep naming stable across natural-language docs:

- `#AREAS`
- `#FAMILIES_PER_AREA`
- `#TOTAL_FAMILIES`
- `#HEXES_PER_FAMILY`
- `#SIDES_PER_HEX`
- `#sideId`
- `#tau_s`
- `#loopability`
- `#tensionEnergy`

Use these tags when writing explanatory docs so formal variables and prose stay aligned.
