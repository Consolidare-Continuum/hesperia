# Ethan — open workflow proceed (Hesperia)

**2026-03-18 — Phase 2 shipped**

| Spec ref | Implementation |
|----------|----------------|
| §A.6 Phase 2, **H4** | `f_f` update: injection \(\hat X_f\), intra-area mean, area feedback, \(-\beta_{pf} p_f\) |
| **H5** | `p_family`: area TRIZ input_signal spread per family-in-area, decay, \(\rho_f\) bleed |
| **H6 coupling** | Area injection = `area_hit_weight`·hit-12 + (1−w)·normalize(\(\sum_{f\in a} f_f\)) |
| L6–L9 | Reuses `step_phase1` after L5 |

**Env:** `HESPERIA_FIELD_DYNAMICS=1` and `HESPERIA_FIELD_DYNAMICS_PHASE2=1` for E2E artifact fields `dynamics_phase: 2`, `family_mass_by_area`, `family_pressure_by_area`.

**2026-03-18 — Phase 3 shipped**

| Item | Implementation |
|------|----------------|
| L4 active subgraph | **Family-proxy** cells (hit-hot families, **cap** / env `HESPERIA_FIELD_DYNAMICS_HEX_CAP`), induced chain adjacency **within area** |
| H2/H3 proxy | `hex_x`, `hex_p` sparse dicts; TRIZ area input_signal → hex `p` |
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
| Blend with TRIZ Ξ | `apply_xi_to_contradiction_signal(..., kme_active_graph=..., concept_to_area_family=...)`; coefficient `HESPERIA_FIELD_DYNAMICS_XI_KME_WEIGHT` (default 0.55) |
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

Codex-style columns: **option #**, **integration target**, **modules**, **difficulty**, **expected gain**, **dependencies**, **acceptance test**. **PO-02** (option **#2**) — **`lexical_evidence_dlcr`** on `analyze` includes bounded **`evidence_spans`** aligned to **`resolver_output.schema.json`** (+ fragment schema). **PO-11/12** landed as **`HESPERIA_CONCEPT_EVIDENCE_GUARD** (`observe` \| `strict`); full-stack default unchanged when unset.

---

**Vocabulary R / Tier / F vs repo topology (OPEN — planning)**

| Item | Location |
|------|----------|
| **R1–R10 / Tier 0–11 / F0–F10** — **Grace + team task:** [TASK-GRACE-VOCABULARY-R-TIER-F-MIGRATION.md](TASK-GRACE-VOCABULARY-R-TIER-F-MIGRATION.md) · inventory [ETHAN-VOCABULARY-MIGRATION-INVENTORY.md](ETHAN-VOCABULARY-MIGRATION-INVENTORY.md) · plan [ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md](ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md) · hub [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md) |

---

**Mainline v0.5.1 — lexical / concept / H_total carryover (OPEN)**

**Policy:** [ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md) · **Map:** [HESPERIA_v0_5_ENGINE_DYNAMICS.md](../../HESPERIA_v0_5_ENGINE_DYNAMICS.md) §8 · **Spec hooks:** [CANONICAL_INDEX.md](../../../specs/CANONICAL_INDEX.md) (v0.5.1 implementation anchors) · **H_total:** [semantic_dynamics_operator_spec.md](../../semantic_dynamics_operator_spec.md)

| ID | Task | Acceptance (minimal) |
|----|------|------------------------|
| **ML-01** | **Neutral component surface:** add `hesperia.nlp.concept_activation` (or equivalent) re-exporting invariant path from `tfp_activation` + docstring “lexical → concept evidence”; keep `tfp_activation` as compat alias. | No behavior change; grep/docs point new name; import graph or AGENTS note updated if required by CI. |
| **ML-02** | **Calibration pack naming (docs + optional file aliases):** document `tfp_signal_calibration_v2.json` as **lexical–area competition calibration**; optional duplicate read path under neutral filename (no duplicate truth). | Docs + loader note; single authoritative file unless dual-path explicitly tested. |
| **ML-03** | **`H_total` compiler:** implement `tools/build_h_total_concepts.py` deterministic build from Dict B + anchors + suppression per [semantic_dynamics_operator_spec.md](../../semantic_dynamics_operator_spec.md); output `h_total_concepts.json` for full `concept_index`. | **DONE** 2026-03-26 — mainline pin: `dict_b_seed.jsonl` + `area_inhibition_matrix_main_v1.json` → `assets/.../semantic_dynamics/h_total_concepts.json` (10 concepts, 45 edges); `tools/validate_h_total_concepts.py` PASS; `tests/experimental/clinical_tfp/test_semantic_state_update.py` PASS. |
| **ML-04** | **Enable semantic operator in calibration** after ML-03: set `semantic_dynamics.operator_enabled` + regression tests on golden segments (non-clinical fixtures). | Invariant + semantic tests green; audit fields present in segment output. |
| **ML-05** | **Thread segmentation in a neutral runner:** ensure `run_e2e_all` or a named internal step can invoke windowed `analyze_session` + `psi_prev` without `research.clinical_tfp` imports on shipping allowlist. | CI step or documented command; forbidden-import check still passes. |
| **ML-06** | **`run_e2e_product` smoke (optional):** one path lexical → concept → (optional H when enabled) → projection boundary; no clinical fixtures. | Product E2E still default minimal; extended flag or env documented. |
| **ML-07** | **Speaker-aware → mainline docs:** describe `analyze_session_speaker_aware` as **multi-channel / role-weighted** lexical evidence only in `HESPERIA_v0_5` or lexicon docs; no care-setting vocabulary in canon. | **DONE** 2026-03-26 — `HESPERIA_v0_5_ENGINE_DYNAMICS.md` §8 + `hesperia/nlp/session_parser.py` docstring. |
| **ML-08** | **Refactor `run_tfp_file_pipeline`:** extract shared session analyze + topology assembly; clinical-only stages (`detect_tfp_stage`, etc.) behind flags or research imports; optional rename when bundle is domain-neutral. | Same artifacts when TFP flags on; topology clearer in code review. |
| **ML-09** | **Neutral phase mapping (if needed):** if product requires discrete phases, add `hesperia.*` enum + mapper from area vector — **do not** re-export `research.clinical_tfp.stage_detection` to shipping. | New component + tests; no clinical strings in public schema. |
| **ML-10** | **Promote specs to Tier-1 (optional):** migrate stabilized lexical/concept-state paragraphs into `specs/canon/` + row in [CANONICAL_INDEX.md](../../../specs/CANONICAL_INDEX.md) when wording is frozen. | Version bump + seal checklist entry. |

**Proceed order (suggested):** ML-01 (docs/surface) → ML-03 → ML-04 → ML-05 → ML-08; ML-06/ML-07/ML-09 as product asks; ML-02/ML-10 when naming and canon freeze align.

---

**TASK GEO-01 — Repo-wide geometry vocabulary → operational terms (OPEN, scope-gated)**

| Item | Location / tool |
|------|------------------|
| **Full spec + Hesperia §0 gate (hex/sphere canon identifiers)** | [ETHAN-GEOMETRY-DECONTAMINATION-TASK.md](ETHAN-GEOMETRY-DECONTAMINATION-TASK.md) |
| **Script** | `tools/refactor_strip_geometry.py` — **dry-run default**; `--apply` defaults to **`docs/` + `specs/`** only; **`--whole-repo-apply`** requires `HESPERIA_GEOMETRY_REFACTOR_WHOLE_REPO_CONFIRM=1` |
| **Dry-run report** | `python3 tools/refactor_strip_geometry.py` → `outputs/geometry_refactor_report.json` |
| **Residual scan** | `python3 tools/refactor_strip_geometry.py --validate` → `outputs/geometry_validation_report.json` |
| **Acceptance** | Phased: prose/specs first; code + component paths only after architecture sign-off + seal plan; zero unintended replacements in frozen trees; commit message states scope |

**Objective (summary):** Word-boundary replacement map (hex→unit, sphere→domain, geometry→topology, …) with exclusions for `assets/`, `legacy/`, `release/`, `outputs/`, etc.; **not** a blind rename of sealed engine identifiers without §0 review.

---

**TASK GEO-02 — API schema cleanup + product-safe docs rewrite (OPEN, compatibility-first)**

| Item | Location / tool |
|------|------------------|
| **Full task spec (phase 2)** | [ETHAN-API-SCHEMA-DOCS-CLEANUP-TASK.md](ETHAN-API-SCHEMA-DOCS-CLEANUP-TASK.md) |
| **Script A (schemas/API)** | `tools/api_schema_cleanup.py` (to create): dry-run / `--apply` / `--validate` |
| **Script B (docs rewrite)** | `tools/rewrite_docs_product_safe.py` (to create): dry-run / `--apply` / `--validate` |
| **Alias compatibility layer** | `hesperia/io/schema_aliases.py` (to create/extend): legacy raw_text aliases + optional compat output |
| **Required reports** | `api_schema_cleanup_report.json`, `api_schema_rename_map.json`, `api_schema_validation_report.json`, `docs_rewrite_report.json`, `docs_rewrite_validation_report.json`, `docs_internal_marking_report.json` |
| **Final summary artifact** | `geometry_decontamination_phase2_summary.md` |
| **Acceptance** | Public schema/docs cleaned in approved scope, backward compatibility for major keys, validation reports green with explicit residual exceptions |

**Objective (summary):** remove geometry-leaking language from public/dev API schema surfaces and rewrite docs into operational product-safe wording, while preserving runtime behavior and client compatibility.
