# Ethan — open workflow proceed (Hesperia)

**2026-03-18 — Phase 2 shipped**

| Spec ref | Implementation |
|----------|----------------|
| §A.6 Phase 2, **H4** | `f_f` update: injection \(\hat X_f\), intra-area mean, area feedback, \(-\beta_{pf} p_f\) |
| **H5** | `p_family`: area TRIZ signal spread per family-in-area, decay, \(\rho_f\) bleed |
| **H6 coupling** | Area injection = `area_hit_weight`·hit-12 + (1−w)·normalize(\(\sum_{f\in a} f_f\)) |
| L6–L9 | Reuses `step_phase1` after L5 |

**Env:** `HESPERIA_FIELD_DYNAMICS=1` and `HESPERIA_FIELD_DYNAMICS_PHASE2=1` for E2E artifact fields `dynamics_phase: 2`, `family_mass_by_area`, `family_pressure_by_area`.

**2026-03-18 — Phase 3 shipped**

| Item | Implementation |
|------|----------------|
| L4 active subgraph | **Family-proxy** cells (hit-hot families, **cap** / env `HESPERIA_FIELD_DYNAMICS_HEX_CAP`), induced chain adjacency **within area** |
| H2/H3 proxy | `hex_x`, `hex_p` sparse dicts; TRIZ area signal → hex `p` |
| Downstream | `hex_hit_blend`: L5/L6 injections mix hit vs hex-field aggregate |

**Env:** `HESPERIA_FIELD_DYNAMICS_PHASE3=1` (+ `FIELD_DYNAMICS=1`). Stack `L4+L5+L6` or `L4+L6`.

**2026-03-18 — Phase 4 shipped**

| Item | Implementation |
|------|----------------|
| L8 §H8 proxy | Consecutive **active family-proxy** runs per area → Mass, Density, Radius, **Gravity**, **Velocity** vs `l8_cluster_mass_prev` |
| Coupling | **`gravity_epsilon`** biases area + family injections; family uses 0.85× ε |
| Fronts | **`l8_fronts_per_area`** (chain \|Δx\| > `tau_front`) |
| No PHASE3 | **Ephemeral** hex from hits (`ephemeral_cap`) for clusters only |

**Env:** `HESPERIA_FIELD_DYNAMICS_PHASE4=1`. Artifact: `l8_clusters`, `dominant_l8_cluster`.

**2026-03-18 — Ξ proxy (L3 → L7 drive)**

| Item | Implementation |
|------|----------------|
| TRIZ topology → tension | `xi_proxy.py`: `xi_proxy_global`, per-area profile from row scores / `area_a` / `area_b` |
| L7 boost | `apply_xi_to_contradiction_signal` in `e2e_bridge` **after** base `c_sig`, **before** Phase 3→2→1 |
| Env | `HESPERIA_FIELD_DYNAMICS_XI=1` (default), `HESPERIA_FIELD_DYNAMICS_XI_SCALE` (default 0.14) |
| Close-out | [REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md](REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md) |

**A.6 phases 1–4 + Ξ proxy shipped.** Next: true hex-lattice **H7/H8** when `Z_ih` wired.

---

**2026-03-20 — Full-graph Ξ from KME (optional)**

| Item | Implementation |
|------|----------------|
| KME tension profile | `xi_proxy_from_kme_active_graph`: node mass per area + cross-area edge stress from clinical `ActiveGraph` + `build_concept_to_area_family()` |
| Blend with TRIZ Ξ | `apply_xi_to_contradiction_signal(..., kme_active_graph=..., concept_to_area_family=...)`; weight `HESPERIA_FIELD_DYNAMICS_XI_KME_WEIGHT` (default 0.55) |
| E2E wiring | `fetch_triz_contradiction_rows` returns `(rows, meta, ag)`; `e2e_bridge.run_field_dynamics_e2e_artifact` passes graph when KME Ξ enabled |
| Env | **`HESPERIA_FIELD_DYNAMICS_XI_KME=1`** enables full-graph Ξ (default **0** — no change to sealed default dynamics). **`HESPERIA_FIELD_DYNAMICS_XI_KME_WEIGHT`** in `[0,1]` blends TRIZ vs KME profiles when both exist |
| No TRIZ rows | With `XI_KME=1` and non-empty `ag`, Ξ boost still applies from graph alone |
| Artifact meta | `xi_kme_global`, `xi_kme_blended`, `xi_kme_weight`, `xi_triz_global` on contradiction step |

---

**2026-03-20 — DLCR v0.6.0 integration (20 tasks, CLOSED)**

| Item | Location |
|------|----------|
| **INT-001..INT-020** | [ETHAN-DLCR-INTEGRATION-20-v0_6_0.md](ETHAN-DLCR-INTEGRATION-20-v0_6_0.md) (**CLOSED**) |
| **Operator runbook** | [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md) |

**Shipped:** Canon § fragments + 72k phased-scale spec, `schemas/lexical_concept/README.md` + `definitions.json`, `assets/version_registry.yaml` dlcr pin, `run_dlcr_pipeline`, optional structural / dynamics / sealed hooks, `HESPERIA_E2E_DLCR` → `run_output_e2e_dlcr.json`, capability matrix `dlcr_pipeline`, `HESPERIA_TFP_DLCR` → `session_dlcr_bundles`, experimental `test_dlcr_benchmark_sessions.py`, `benchmark_sessions.yaml` optional `expected.dlcr`.

---

`[2026-03-20] ethan PO-02 status=done note=Option #2 formal closure: analyze lexical_evidence_dlcr adds evidence_spans (≤24, resolver_output keys, no audit) + schema fragment.`

**TFP RU DLCR — Codex stack (RAW vs ACTIVE, v060)**

| Item | Location |
|------|----------|
| **BUILD__DICT…RU_TFP__V060** implementation + calibration | [ETHAN-TFP-RU-CODEX-STACK.md](ETHAN-TFP-RU-CODEX-STACK.md) · `tools/build_ru_tfp_dictionary_stack.py` |

**TFP RU DLCR dictionaries — 12-task build (PARTIAL)**

| Item | Location |
|------|----------|
| **TASK 1–12** status, tools, merge order, version freeze | [ETHAN-TFP-RU-DICT-12TASKS.md](ETHAN-TFP-RU-DICT-12TASKS.md) |

**TFP testing grounds — runnable dictionary delimitation (OPEN)**

| Item | Location |
|------|----------|
| **Planes A/B/C** (frozen 288 vs ontology YAML vs DLCR JSONL) | [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md) |
| **Fix (2026-03-20)** | `load_family_embedding_tfp()` now resolves `specs/canon/family_embedding_tfp.yaml` (was only `hesperia/spec/…`, usually missing). |

**Post-integration options → 30-task matrix (IN PROGRESS)**

| Item | Location |
|------|----------|
| **PO-01..PO-30** | [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md) — **implementation snapshot** in-file |

Codex-style columns: **option #**, **integration target**, **modules**, **difficulty**, **expected gain**, **dependencies**, **acceptance test**. **PO-02** (option **#2**) — **`lexical_evidence_dlcr`** on `analyze` includes bounded **`evidence_spans`** aligned to **`resolver_output.schema.json`** (+ fragment schema). **PO-11/12** landed as **`HESPERIA_CONCEPT_EVIDENCE_GUARD`** (`observe` \| `strict`); full-stack default unchanged when unset.
