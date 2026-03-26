<!--
Ethan — DLCR-HP v0.6.0 integration into Hesperia + TFP testing environment.
Companion: task.txt §26–§28, task_gena_v0_6_0.md (baseline landed), specs/canon/lexical_concept/.
-->

# Ethan — 20 integration tasks (DLCR v0.6.0 → Hesperia + TFP)

**Status:** CLOSED (2026-03-20)  
**Scope:** Close gaps between **current DLCR baseline** (schemas, `core/lexical`, `core/resolver`, `core/hexmap`, seed assets, CI regression) and **normative `task.txt` / §28 first-ship**, including **TFP testing collateral** (`run_e2e_tfp_smoke`, `tests/experimental/clinical_tfp/`, `benchmark_sessions.yaml`).

**Closure:** Runbook [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md). INT-001–INT-020 delivered per board below (canon split, registry, schemas README, execution_flow/E2E/TFP/capability wiring, experimental benchmark test, docs).

**Non-goals:** Do not move TFP/clinical into canonical **product** surface without `EXTENSION_STATUS` + projection gate review; integration tasks below keep **experimental / testing** paths explicit.

---

## Dependency waves

| Wave | Tasks | Theme |
|------|-------|--------|
| **W1** | INT-001 — INT-004 | Canon + schemas completion |
| **W2** | INT-005 — INT-008 | 72k topology + data scale |
| **W3** | INT-009 — INT-012 | Runtime execution_flow + projection |
| **W4** | INT-013 — INT-016 | Field dynamics + multiscale bridge |
| **W5** | INT-017 — INT-020 | TFP env + CI + docs |

---

## Task board

### `INT-001` — Split master spec into §26 file set (canon)
- **Size:** M  
- **Depends on:** —  
- **Artifacts:** Under `specs/canon/lexical_concept/`: `SPEC__Dict_A_Schema_v0_6_0.md`, `SPEC__Dict_B_Schema_v0_6_0.md`, `SPEC__Normalization_v0_6_0.md`, `SPEC__Resolver_v0_6_0.md`, `SPEC__Hex_Projection_v0_6_0.md`, `SPEC__Hex_Dynamics_v0_6_0.md`, `SPEC__Audit_Output_v0_6_0.md`, `SPEC__Calibration_Regression_v0_6_0.md` (extract from `task.txt` / master).  
- **Acceptance:** Each file has Purpose, normative rules, acceptance bullets; `specs/CANONICAL_INDEX.md` lists new IDs or README index table.  
- **Systems:** `specs/canon/lexical_concept/README.md`

### `INT-002` — Version registry for DLCR resources
- **Size:** S  
- **Depends on:** INT-001  
- **Artifacts:** `assets/version_registry.yaml` (or `assets/data/engine_dynamics_v060/VERSION.yaml`) with `dict_a`, `dict_b`, `normalization`, `resolver_rules`, `hex_topology`, `aggregation` version pins.  
- **Acceptance:** `run_metadata.schema.json` example payload validates; docs cite registry path.

### `INT-003` — JSON Schema `$ref` hub for lexical_concept
- **Size:** S  
- **Depends on:** —  
- **Artifacts:** Optional `schemas/lexical_concept/README.md` + shared `definitions.json` if duplicate fields grow.  
- **Acceptance:** Validators still pass; no CI regression.

### `INT-004` — Capabilities / env surface for DLCR
- **Size:** M  
- **Depends on:** INT-002  
- **Artifacts:** `hesperia/system/capabilities.yaml` + `hesperia.system.capabilities` entries: `dlcr_enabled`, `dlcr_fallback`, `dlcr_xi_kme` (document coupling with existing dynamics env).  
- **Acceptance:** Shipping measurement rejects DLCR flags unless explicitly allowed (product boundary unchanged default-off).

### `INT-005` — Map symbolic hex IDs → engine hex index space
- **Size:** L  
- **Depends on:** INT-001 (hex projection spec)  
- **Artifacts:** `assets/data/engine_dynamics_v060/anchors/hex_index_map.json` + `core/hexmap/topology.py` (adjacency stub or link to `docs/TOPOLOGY_INVARIANTS.md` 12-area / family grid).  
- **Acceptance:** Deterministic `HX-*` → integer cell id or (area,family,local) triple; unit tests.

### `INT-006` — Align DLCR footprint with 72k substrate contract
- **Size:** L  
- **Depends on:** INT-005  
- **Artifacts:** Spec note + code: either **shard** into 72k addressing or **document** phased scale (bounded region → full grid).  
- **Acceptance:** No claim of “full 72k” in code comments unless implemented; gate doc updated.

### `INT-007` — Scale concept pack (100–300 concepts) for TFP-relevant domain
- **Size:** L  
- **Depends on:** INT-002  
- **Artifacts:** `assets/data/engine_dynamics_v060/dict_a/*.jsonl`, `dict_b/*.jsonl` expanded; `tools/validate_*` pass.  
- **Acceptance:** Line count + validator exit 0; subset linked to existing `hesperia/ontology/dictB` ids where possible.

### `INT-008` — Gold / ambiguity / overlap corpora (§24)
- **Size:** M  
- **Depends on:** INT-007  
- **Artifacts:** `assets/data/engine_dynamics_v060/corpora/*.jsonl`; extend `tools/check_dlcr_regression.py` to multi-corpus.  
- **Acceptance:** CI runs all corpora; failure messages name corpus + case id.

### `INT-009` — `core/sequence` — segmentation + trajectory (L4 spec)
- **Size:** L  
- **Depends on:** —  
- **Artifacts:** `core/sequence/segmentation.py`, `trajectory.py`; tests under `tests/lexical_concept/`.  
- **Acceptance:** Deterministic segment boundaries; trajectory features over segments (e.g. hex id sequence) JSON-serializable.

### `INT-010` — Single entry: `run_dlcr_pipeline(text, paths) -> internal_rich`
- **Size:** L  
- **Depends on:** INT-007, INT-009  
- **Artifacts:** `hesperia.engine.lexical_concept.execution_flow` or `runtime/execution_flow/run_dlcr.py` (package TBD in INT-001): L0→L6 orchestration, emits audit object matching `resolver_output` + hex summaries.  
- **Acceptance:** One function called from tests; deterministic given fixed assets.

### `INT-011` — Wire DLCR optional branch into `run_structural_analysis` (dev flag)
- **Size:** L  
- **Depends on:** INT-010, INT-004  
- **Artifacts:** `runtime/services/analysis_service.py`: when `HESPERIA_DLCR_STRUCTURAL=1` (or capability), attach **non-breaking** `dlcr_audit` sibling key **before** `project_to_public` (internal envelope), or merge via allowed internal builder only.  
- **Acceptance:** Default path unchanged (`HESPERIA_DLCR_STRUCTURAL` unset); schema tests for public output still pass.

### `INT-012` — Public projection slice for DLCR summaries
- **Size:** M  
- **Depends on:** INT-011  
- **Artifacts:** `hesperia.engine.projection` (or subset): map internal DLCR → **public-safe** deterministic fields; extend `schemas/public/...` only if Tier-1 approved.  
- **Acceptance:** Public output derived from internal; no second semantic path.

### `INT-013` — Bridge DLCR concept weights → field dynamics injection (optional)
- **Size:** L  
- **Depends on:** INT-010, INT-005  
- **Artifacts:** `hesperia.extensions.dynamics.e2e_bridge` or sibling: env `HESPERIA_FIELD_DYNAMICS_DLCR=1` blends DLCR family/area vector into hit injection **after** concept resolution (not raw tokens).  
- **Acceptance:** With flag off, bitwise/behavioral parity with current dynamics artifact; with flag on, meta records `dlcr_merged: true`.

### `INT-014` — Bridge DLCR → sealed multiscale stack (research flag)
- **Size:** L  
- **Depends on:** INT-010  
- **Artifacts:** `hesperia.engine.sealed_multiscale_stack` hook (env-gated): feed structural signals from DLCR hex/family rollup into allowed inputs only.  
- **Acceptance:** Default sealed E2E unchanged; gated test in `tests/experimental/` or env-marked test.

### `INT-015` — E2E artifact: `run_output_e2e_dlcr.json` (optional step)
- **Size:** M  
- **Depends on:** INT-010  
- **Artifacts:** `runtime/execution_flow/run_e2e_all.py`: new output when `HESPERIA_E2E_DLCR=1`; document in `docs/E2E_RUN_ORDER.md`, `assets/artifacts/e2e/E2E_OUTPUTS.md`.  
- **Acceptance:** Manifest lists file only when flag set; builder docs updated.

### `INT-016` — `run_e2e_capability_matrix` block for DLCR
- **Size:** S  
- **Depends on:** INT-010  
- **Artifacts:** `run_e2e_capability_matrix` `_put("dlcr_pipeline", ...)`.  
- **Acceptance:** Capability JSON contains `dlcr` key with run id / version stamps.

### `INT-017` — TFP smoke: per-session DLCR bundle
- **Size:** M  
- **Depends on:** INT-010  
- **Artifacts:** `run_e2e_tfp_smoke` adds `session_dlcr_bundles: [...]` when `HESPERIA_TFP_DLCR=1` (or same as INT-015).  
- **Acceptance:** Each smoke session id maps to resolver span count + hex summary + degradation flags list.

### `INT-018` — `tests/experimental/clinical_tfp` — DLCR regression tests
- **Size:** M  
- **Depends on:** INT-010, INT-008  
- **Artifacts:** `tests/experimental/clinical_tfp/test_dlcr_benchmark_sessions.py` reading `benchmark_sessions.yaml` + optional gold expectations file.  
- **Acceptance:** `pytest tests/experimental/clinical_tfp/test_dlcr_benchmark_sessions.py` passes; respects `check_forbidden_zone_imports` (research stays experimental).

### `INT-019` — Benchmark sessions: DLCR expected fields
- **Size:** S  
- **Depends on:** INT-018  
- **Artifacts:** Extend `tests/experimental/clinical_tfp/benchmark_sessions.yaml` with optional `expected.dlcr` (e.g. winning concepts, min span count).  
- **Acceptance:** At least one session has structured DLCR expectations; tests document tolerance (deterministic fuzzy bounds if needed).

### `INT-020` — Integration checklist + VARIABLE_CATALOG / operator runbook
- **Size:** S  
- **Depends on:** INT-001–INT-019 (rolling)  
- **Artifacts:** `docs/governance/working/ETHAN-DLCR-INTEGRATION-RUNBOOK.md` (env matrix, command list: `pytest …`, `python3 -m runtime.execution_flow.run_e2e_all`, validators); update `ETHAN-OPEN-WORKFLOW-PROCEED.md` closure criteria.  
- **Acceptance:** Operator can run TFP + DLCR from doc without reading this full 20-table.

---

## Environment variables (summary)

| Variable | Purpose |
|----------|---------|
| `HESPERIA_DLCR_STRUCTURAL` | Optional DLCR branch on structural measurement (INT-011) |
| `HESPERIA_E2E_DLCR` | Emit `run_output_e2e_dlcr.json` in full E2E (INT-015) |
| `HESPERIA_TFP_DLCR` | Attach DLCR bundles to TFP smoke artifact (INT-017) |
| `HESPERIA_FIELD_DYNAMICS_DLCR` | Blend DLCR into field dynamics injection (INT-013) |
| Existing `HESPERIA_FIELD_DYNAMICS_*` | Dynamics + Ξ / Ξ-KME (already wired) |

---

## Definition of done (integration track)

- §28 **first-ship** bullets satisfied on **default product path** where Tier-1 requires it; TFP/testing paths clearly flagged experimental.  
- `task.txt` §26 placement complete for code paths that exist; §24 corpora + CI multi-gate (INT-008).  
- TFP smoke + benchmark sessions can **observe** DLCR outputs under explicit env.  
- No `research.*` imports in `runtime/shipping` / forbidden trees (existing policy).

---

## Mapping to prior DLCR-001..020 baseline

The completed **Gena team10** tasks delivered the **scaffold**. This Ethan **INT-001..020** list is **integration + scale + product/TFP wiring** — not a duplicate of DLCR-001..020.
