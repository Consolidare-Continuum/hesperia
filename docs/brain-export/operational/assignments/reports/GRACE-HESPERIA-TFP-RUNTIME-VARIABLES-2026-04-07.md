# Grace — Hesperia variables that change outcomes when the TFP module runs

**Root table (Ethan):** `HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md` (repo root).  
**Date:** 2026-04-07  
**Scope:** Environment variables and closely related runtime switches that can change `tfp_vector`, `tfp_profile`, `tfp_conflicts`, or the upstream `concept_hits` / `family_scores` / `area_scores` / `input.text` / `normalized_tokens` the module consumes.  
**Sources:** `hesperia/modules/tfp/v1.py` → `hesperia.engine.calculus.compute_tfp_bundle`, `hesperia/engine/lexical_concept/pipeline.py`, `runtime/shipping/env_guard.py` `ALLOWED_HESPERIA_ENV`, `docs/governance/TFP_ENV_FLAGS_V1.md`, `docs/governance/RUNTIME_ENV_VARS_v1.md`, `docs/HESPERIA_TFP_MODULE_DICTS.md`.

---

## Clinical / process concepts vs code (iteration, session, perspectives, interference, shift)

- **Iteration:** In sealed `TFPModule.project`, `detect_interaction_loops` is called with a **synthetic two-step timeline** (the same areas/families repeated), so “iteration” there is a **minimal dyad for loop heuristics**, not a stored client-turn index. Multi-step aggregation helpers such as `stage_from_timeline` exist under `hesperia.modules.tfp.math_v1` but are **not** invoked by `project()`.
- **Session:** Request-scoped engine `ctx` is the session boundary for one API call; **E2E / smoke** can attach dialog DLCR sidecars when `HESPERIA_TFP_DLCR` is truthy (`run_e2e_all.py`), which can change downstream structure before or alongside TFP in those pipelines only.
- **Client iterations perspective:** Lexical resolution and concept hits are driven by **one combined `input.text`** (plus optional role stripping via `HESPERIA_CLINICAL_STRIP_ROLES`); there is **no** separate env for “client-only” vs “therapist-only” slices in the sealed module path.
- **Therapist iterations perspective:** `detect_interaction_loops(..., therapist_utterances=...)` and `classify_intervention` can label therapist **intervention type** per window, but **`TFPModule.project` does not pass therapist lines**, so therapist perspective **does not** alter outputs unless a **custom caller** wires a richer timeline.
- **Interference / answer of iteration (client–therapist):** Engine-side “interference” is approximated by **interaction_loop** conflict tags and **intervention_type** / **projective_identification_signal** inside loop records when a real timeline + therapist utterances are supplied; the default module path mostly reflects **accusation + escalation** on the duplicated slice.
- **Shift (client → therapist → client):** **Not** modeled as a named environment variable; capturing shift requires **explicit multi-turn context** assembled by the integration layer (and optionally therapist utterance indices), not the TFP env surface alone.

---

## General values (Hesperia-wide; affect TFP when they change lexical input, scores, caps, or pipeline branches)

**Dictionary and asset resolution**

- **HESPERIA_CALIB_DICT_VERSION** — Selects the calibration dict pack directory under `assets/calibration/dicts/<version>/`, changing which Dict A/B rows feed concept resolution and thus family/area scores feeding TFP.
- **HESPERIA_ASSETS_ROOT** — Overrides the repo root used to resolve bundled assets (including dicts), changing which files load if paths differ.
- **HESPERIA_PRODUCTION_MATRICES_DIR** — Overrides where production matrices load from when the pipeline uses matrix-backed stages that touch the same run.
- **HESPERIA_PCH_DIR** — Overrides PCH (precompiled hints) directory when PCH-backed paths participate in the run.
- **HESPERIA_V06_MODEL_REVISION** — Version/revision pin used in version reporting and consistency checks; mismatches can fail gates or change declared model lineage alongside outputs.

**Input text and token shaping**

- **HESPERIA_MAX_INPUT_CHARS** — Caps accepted request body / default text length, truncating or bounding what lexical and TFP layers see.
- **HESPERIA_CLINICAL_STRIP_ROLES** — When enabled, strips role-marked segments from clinical text before policy/DLCR, changing tokens and resolutions.
- **HESPERIA_DLCR_POLICY_MODE** — Selects lexical DLCR policy mode (with default path in `analysis_input.py`), affecting tokenization and resolution behavior.

**Lexical / DLCR resolution (directly changes `concept_hits` and derived scores)**

- **HESPERIA_DLCR_STOPWORDS** — Extra stopword list for DLCR-style filtering, shrinking or shifting which spans resolve.
- **HESPERIA_DLCR_DOMAIN_WHITELIST** — Restricts allowed domain tokens/phrases for resolution.
- **HESPERIA_DLCR_REJECT_TINY_FRAGMENTS** — When truthy, rejects tiny fragments from consideration, changing hits.
- **HESPERIA_DLCR_MIN_TOKEN_LEN** — Minimum token length for resolution candidates.
- **HESPERIA_DLCR_MIN_RESOLVE_SCORE** — Floor for accepting a lexical resolve score (primary path).
- **HESPERIA_DLCR_MIN_RESOLVE_SCORE_C** — Additional floor used for Dict C-related resolution path in pipeline (when active).
- **HESPERIA_DLCR_TOKEN_TOPK** — How many top candidates per token/span are kept for mass aggregation into concept weights.
- **HESPERIA_DLCR_DEBUG_TOKEN_WEIGHTS** — Enables debug weight diagnostics (can change logging and, in debug paths, which branches execute).
- **HESPERIA_DLCR_DOMAIN_PACK** — Selects domain pack for DLCR policy loading in lexical policy.
- **HESPERIA_DLCR_STRUCTURAL** — Requests structural DLCR attachment subject to product capabilities (`capabilities.py`).

**Dict A merge / gates**

- **HESPERIA_DICT_A_CONFIDENCE_THRESHOLD** — Drops Dict A rows below this confidence when merging.
- **HESPERIA_DICT_A_MAX_SYNONYMS_PER_CONCEPT** — Caps synonyms per concept during Dict A merge.
- **HESPERIA_DICT_A_MAX_ACCEPTED** — Caps how many accepted Dict A rows are used (pipeline enforces max).
- **HESPERIA_CB1_LEXICAL_GATE** — Enables optional pre-resolve lexical rejection (`core.lexical_gate`); **not** currently in `env_guard.py` allowlist (strict unknown-env mode may reject).
- **HESPERIA_CB1_CONCEPT_GATE** — Enables optional high-level TFP single-token concept rejection helper; **not** currently in `env_guard.py` allowlist.

**Concept dictionary (CD) executor**

- **HESPERIA_CD_ENABLED** / **HESPERIA_CD_DISABLE** — Toggle CD annotation path on/off (mutually constrained in pipeline).
- **HESPERIA_CD_JSONL** — Override path to CD JSONL when set.
- **HESPERIA_CD_PHASE** — Selects CD phase integer used by the CD merge path.

**Sealed stack / sidecars**

- **HESPERIA_SEALED_DLCR_SIDECAR** — Attaches sealed multiscale DLCR sidecar behavior when enabled in `sealed_multiscale_stack.py`.

**Field dynamics and semantic field (full-stack / E2E paths that also run TFP)**

- **HESPERIA_FIELD_DYNAMICS** — Master switch for field dynamics phase 1 integration.
- **HESPERIA_FIELD_DYNAMICS_PHASE2** / **HESPERIA_FIELD_DYNAMICS_PHASE3** / **HESPERIA_FIELD_DYNAMICS_PHASE4** — Enable specific dynamics phases.
- **HESPERIA_FIELD_DYNAMICS_HEX_CAP** — Caps hex-related dynamics outputs when phase 3 reads it.
- **HESPERIA_FIELD_DYNAMICS_DLCR** — Merges DLCR into dynamics bridge behavior in `e2e_bridge.py`.
- **HESPERIA_FIELD_DYNAMICS_TRIZ** — Disables TRIZ branch in dynamics bridge when set off.
- **HESPERIA_FIELD_DYNAMICS_XI** / **HESPERIA_FIELD_DYNAMICS_XI_SCALE** / **HESPERIA_FIELD_DYNAMICS_XI_KME** / **HESPERIA_FIELD_DYNAMICS_XI_KME_WEIGHT** — Tune ξ / KME proxy behavior in `xi_proxy.py`.
- **HESPERIA_FIELD_DYNAMICS_STATE_PATH** — Overrides persisted dynamics state path when used.
- **HESPERIA_CONCEPT_EVIDENCE_GUARD** — Sets concept evidence guard mode in dynamics E2E bridge.

**E2E and product pipeline harness (when those scripts exercise TFP)**

- **HESPERIA_E2E_RUN_ID** — Stable id for E2E runs (artifact naming, reproducibility metadata).
- **HESPERIA_E2E_DLCR** — Enables DLCR segments in E2E flows.
- **HESPERIA_TFP_DLCR** — When truthy, TFP smoke/E2E attaches `session_dlcr_bundles` per TFP governance.
- **HESPERIA_E2E_MULTISCALE** — Enables multiscale branch in `run_e2e_all.py`.
- **HESPERIA_E2E_CALIBRATION_BATCH_N** — Batch size for calibration steps inside E2E.
- **HESPERIA_SEALED_E2E_TRIZ** — TRIZ toggle for sealed E2E slice.
- **HESPERIA_SEMANTIC_FIELD_EQUATIONS_V1** / **HESPERIA_SEMANTIC_FIELD_V1_STEPS** / **HESPERIA_SEMANTIC_FIELD_STUB_MATRICES** — Control semantic field equation/stub behavior when those phases run.
- **HESPERIA_MAIN_ENGINE_TEXT** — Default utterance for `run_main_engine_workflow.py` when no file input.
- **HESPERIA_PRODUCT_E2E_TEXT** / **HESPERIA_PRODUCT_E2E_OUT** — Default text and output path for product E2E driver.
- **HESPERIA_ANALYZE_DLCR_EVIDENCE** — Recorded into TFP file pipeline manifest in `run_tfp_file_pipeline.py` (traceability / side paths).

**Shipping / API bounds (change what reaches the engine)**

- **HESPERIA_RATE_LIMIT** — Limits requests per minute (can change which inputs are processed).
- **HESPERIA_API_HOST** / **HESPERIA_API_PORT** — Bind address (operational, not math).
- **HESPERIA_REQUIRE_SYSTEM_SEAL** — Enforces system seal at shipping startup.
- **HESPERIA_SHIPPING_ENV_STRICT** — Unknown `HESPERIA_*` keys fail closed at startup when truthy.
- **HESPERIA_SCHEMA_SHA256** / **HESPERIA_PUBLIC_SCHEMA_STRICT_KEYS** — Schema validation strictness on public payloads.
- **HESPERIA_RUNTIME_MODE** — Runtime mode string for artifact writer and behavior flags.
- **HESPERIA_PRODUCT_SURFACE** — Strict product API surface (hides optional routes including some DLCR-capable paths unless paired with capabilities).
- **HESPERIA_EXPOSE_TRIZ** / **HESPERIA_EXPOSE_VERSION** — Expose optional HTTP routes when product surface allows.
- **HESPERIA_LICENSE_SKIP** / **HESPERIA_LICENSE_REQUIRED** / **HESPERIA_LICENSE_TOKEN** / **HESPERIA_LICENSE_FILE** / **HESPERIA_LICENSE_EXPIRY** — License gating for shipping API startup.
- **HESPERIA_MACHINE_BINDING** / **HESPERIA_MACHINE_ID** — Machine-bound license checks.

**Core math reference (`core/math/core_math.py` load_config env overrides; affects outputs only if that math path is on the same run)**

- **HESPERIA_ALPHA** — Overrides fusion blend weight alpha in guard reference config.
- **HESPERIA_ETA** — Overrides centroid activation threshold eta.
- **HESPERIA_LAMBDA** — Overrides traversal lambda.
- **HESPERIA_DECAY** — Overrides traversal decay.
- **HESPERIA_DELTA_GAP** — Overrides ambiguity delta_gap.
- **HESPERIA_K_GUARD** / **HESPERIA_K_DISP** / **HESPERIA_K_SHADOW_PERTURB** — Override penalty/perturbation coefficients.

**Calibration tooling (rebuild / offline calibration; indirect on TFP until dicts change)**

- **HESPERIA_DICT_CALIB_OFFLINE** / **HESPERIA_DICT_CALIB_WORKERS** — Offline mode and worker count for dict calibration tools.
- **HESPERIA_CALIB_LINKS_FUZZY** / **HESPERIA_CALIB_LINKS_SKIP_FUZZY** — Fuzzy link generation toggles for calibration link builder.
- **HESPERIA_CALIB_MOCK_OPENAI** / **HESPERIA_CALIB_OPENAI_MODEL** / **HESPERIA_CALIB_MAX_OUTPUT_TOKENS** / **HESPERIA_CALIB_USE_MAX_COMPLETION_TOKENS** / **HESPERIA_CALIB_NORMALIZE_INPUT_TEXT_CAP** — OpenAI-backed calibration tool behavior.

**Other allowlisted names (metadata, gates, or adjacent products; typically do not change sealed TFP math per request)**

- **HESPERIA_BUILD_ID** / **HESPERIA_BUILD_TIMESTAMP** / **HESPERIA_RELEASE_BUILD_TIMESTAMP** / **HESPERIA_GIT_COMMIT** / **HESPERIA_VERSION** — Build and provenance stamps (affect reporting, not `compute_tfp_bundle` formulas).
- **HESPERIA_API_KEY** / **HESPERIA_API_KEY_NEXT** / **HESPERIA_API_INSTRUMENTATION** — Dev API auth and instrumentation.
- **HESPERIA_LEXICAL_WRITE_ALLOWED** — Allows lexical write paths in control guard (safety for mutating pipelines).
- **HESPERIA_SPHERE_PIPELINE_DEV** — Sphere pipeline dev gate in `pipeline_runner.py`.
- **HESPERIA_ATTRIBUTION_MODE** — Attribution mode string in `analyze.py` trace paths.

**Test / gate-only readers (change pass/fail or fixtures, not production sealed formulas)**

- **HESPERIA_STRICT_DETERMINISM** — Env determinism test gate.
- **HESPERIA_SKIP_TFP_V1_LAYOUT_TEST** — Skips layout test when set.
- **HESPERIA_METRICS_MIN_LEXICAL_ACCEPTED_SUM** / **HESPERIA_METRICS_MIN_PER_TEXT_NON_EMPTY_RATIO** / **HESPERIA_METRICS_MIN_LOWEST_PER_TEXT_ACCEPTED** — Metrics gate thresholds in `check_metrics_gate.py`.
- **HESPERIA_REL_REAL_UNMAPPED_RATE_MAX** / **HESPERIA_CD_DELTA_REL_K** / **HESPERIA_CD_DELTA_ABS_CAP** / **HESPERIA_UNMAPPED_RATE_MAX** — REL/ENF and unmapped gate tests.

**Non-allowlist readers (compliance gap if strict mode on)**

- **HESPERIA_REPO** — Repo root for some PG-SA snapshot scripts only.
- **HESPERIA_LEGACY_RESEARCH_CORPUS** — Legacy corpus guard in dict calibration env defaults.

**Non-`HESPERIA_*` but used in TFP smoke**

- **PYTHONHASHSEED** — Set to `0` in `tools/run_tfp_env_precheck.sh` for deterministic hashing.
- **HESPERIA_PHASE_C_SMOKE_MAX_SEC** / **HESPERIA_PHASE_C_LATENCY_RATIO_MAX** — Wall-clock and latency ratio caps in `tools/run_tfp_phase_c_smoke.sh` (orchestration only).

---

## TFP-specific module values (`HESPERIA_TFP_*` and direct TFP tooling)

- **HESPERIA_TFP_MODULE_SEALED** — When `1`/`true`, warns on `TFPModule.project`; when `block`, raises on `project` (see `hesperia/modules/tfp/seal.py` and `VERSION.yaml` seal flags).
- **HESPERIA_TFP_MODULE_DATA_ROOT** — Reserved optional loader root for module data; runtime still defaults to `assets/` until loader ADR is implemented.
- **HESPERIA_TFP_PIPELINE_RUN_ID** — Stable id for TFP file/bundle pipelines (`run_tfp_file_pipeline.py`, `gena_tfp_bundle_run.py`).
- **HESPERIA_TFP_GOLD_BUNDLE_DIR** — Override directory for gold bundle comparisons in benchmarks/CI.
- **HESPERIA_TFP_DLCR** — Truthy attaches session DLCR bundles in TFP-class E2E/smoke paths (see `TFP_ENV_FLAGS_V1.md`).
- **HESPERIA_TFP4_ROOT** — Legacy corpus root for `tfp4_*` ingest CLI tools (offline corpus operations).

**Module instance config (not an environment variable):** `TFPModule.configure({"labels": [...]})` sets the **label bucket names** used to fold family scores into `tfp_vector`; changing labels changes the vector keys and normalization.

---

## Cross-references

- **Yielded outputs table (repo root):** `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md`.  
- **Yielded outputs narrative:** `operational/assignments/reports/GRACE-HESPERIA-TFP-YIELDED-PARAMETERS-2026-04-07.md`.  
- Allowlist policy: `hesperia/docs/governance/TFP_ENV_FLAGS_V1.md`, `hesperia/runtime/shipping/env_guard.py`.  
- Human grouping: `hesperia/docs/governance/RUNTIME_ENV_VARS_v1.md`.  
- Dict resolution: `hesperia/docs/governance/TFP_RESOLUTION_CONTRACT.md`, `hesperia/docs/HESPERIA_TFP_MODULE_DICTS.md`.

`SIGNED: Grace (triage) | Hesperia TFP runtime catalog | 2026-04-07 | GRACE-HESPERIA-TFP-RUNTIME-VARIABLES`
