# Hesperia TFP — runtime variables (table)

**Authority:** Ethan (governance). **SSoT allowlist (Hesperia repo):** `hesperia/runtime/shipping/env_guard.py`. **Narrative (brain repo):** `operational/assignments/reports/GRACE-HESPERIA-TFP-RUNTIME-VARIABLES-2026-04-07.md`.

## Clinical / process ↔ engine (reference)

| Concept | In sealed TFP path |
|---------|-------------------|
| Iteration | Synthetic 2-step timeline for `detect_interaction_loops`; no turn index in `tfp_profile`. |
| Session | Request `ctx`; DLCR bundles only if E2E/smoke + `HESPERIA_TFP_DLCR`. |
| Client perspective | Single `input.text` (+ optional role strip) drives lexical → scores. |
| Therapist perspective | No therapist utterances passed into `TFPModule.project` by default. |
| Interference | `interaction_loop` in `tfp_conflicts`; rich loop records need caller-supplied timeline. |
| Shift (C→T→C) | No dedicated output field; compare runs or upper layer. |

## `ALLOWED_HESPERIA_ENV` (107)

| Variable | Bucket | Can change TFP slice | Role |
|----------|--------|----------------------|------|
| `HESPERIA_ALPHA` | core_math | yes | fusion α override |
| `HESPERIA_ANALYZE_DLCR_EVIDENCE` | tfp_tool | e2e | file pipeline manifest flag |
| `HESPERIA_API_HOST` | shipping | no | bind host |
| `HESPERIA_API_INSTRUMENTATION` | dev_api | no | dev logging |
| `HESPERIA_API_KEY` | dev_api | no | bearer auth |
| `HESPERIA_API_KEY_NEXT` | dev_api | no | bearer auth rotate |
| `HESPERIA_API_PORT` | shipping | no | bind port |
| `HESPERIA_ASSETS_ROOT` | assets | yes | asset root override |
| `HESPERIA_ATTRIBUTION_MODE` | analyze | no | attribution mode |
| `HESPERIA_BUILD_ID` | provenance | no | build id stamp |
| `HESPERIA_BUILD_TIMESTAMP` | provenance | no | build time stamp |
| `HESPERIA_CALIB_DICT_VERSION` | dict | yes | dict pack dir |
| `HESPERIA_CALIB_LINKS_FUZZY` | calib_tool | indirect | link builder fuzzy |
| `HESPERIA_CALIB_LINKS_SKIP_FUZZY` | calib_tool | indirect | link builder skip fuzzy |
| `HESPERIA_CALIB_MAX_OUTPUT_TOKENS` | calib_tool | indirect | OpenAI calib cap |
| `HESPERIA_CALIB_MOCK_OPENAI` | calib_tool | indirect | mock OpenAI calib |
| `HESPERIA_CALIB_NORMALIZE_INPUT_TEXT_CAP` | calib_tool | indirect | normalize cap |
| `HESPERIA_CALIB_OPENAI_MODEL` | calib_tool | indirect | calib model |
| `HESPERIA_CALIB_USE_MAX_COMPLETION_TOKENS` | calib_tool | indirect | token API flag |
| `HESPERIA_CD_DISABLE` | cd | yes | CD off |
| `HESPERIA_CD_ENABLED` | cd | yes | CD on |
| `HESPERIA_CD_JSONL` | cd | yes | CD jsonl path |
| `HESPERIA_CD_PHASE` | cd | yes | CD phase int |
| `HESPERIA_CLINICAL_STRIP_ROLES` | lexical | yes | strip role lines |
| `HESPERIA_CONCEPT_EVIDENCE_GUARD` | dynamics | e2e | evidence guard mode |
| `HESPERIA_DECAY` | core_math | yes | traversal decay |
| `HESPERIA_DELTA_GAP` | core_math | yes | ambiguity gap |
| `HESPERIA_DICT_A_CONFIDENCE_THRESHOLD` | dict | yes | Dict A floor |
| `HESPERIA_DICT_A_MAX_ACCEPTED` | dict | yes | Dict A cap |
| `HESPERIA_DICT_A_MAX_SYNONYMS_PER_CONCEPT` | dict | yes | synonym cap |
| `HESPERIA_DICT_CALIB_OFFLINE` | calib_tool | indirect | offline calib |
| `HESPERIA_DICT_CALIB_WORKERS` | calib_tool | indirect | calib workers |
| `HESPERIA_DLCR_DEBUG_TOKEN_WEIGHTS` | lexical | yes | DLCR debug |
| `HESPERIA_DLCR_DOMAIN_PACK` | lexical | yes | domain pack |
| `HESPERIA_DLCR_DOMAIN_WHITELIST` | lexical | yes | domain whitelist |
| `HESPERIA_DLCR_MIN_RESOLVE_SCORE` | lexical | yes | resolve floor |
| `HESPERIA_DLCR_MIN_TOKEN_LEN` | lexical | yes | min token len |
| `HESPERIA_DLCR_POLICY_MODE` | lexical | yes | DLCR policy |
| `HESPERIA_DLCR_REJECT_TINY_FRAGMENTS` | lexical | yes | reject tiny |
| `HESPERIA_DLCR_STOPWORDS` | lexical | yes | extra stopwords |
| `HESPERIA_DLCR_STRUCTURAL` | lexical | yes | structural DLCR req |
| `HESPERIA_DLCR_TOKEN_TOPK` | lexical | yes | candidate top-K |
| `HESPERIA_E2E_CALIBRATION_BATCH_N` | e2e | e2e | E2E calib batch |
| `HESPERIA_E2E_DLCR` | e2e | e2e | E2E DLCR |
| `HESPERIA_E2E_MULTISCALE` | e2e | e2e | E2E multiscale |
| `HESPERIA_E2E_RUN_ID` | e2e | e2e | E2E run id |
| `HESPERIA_ETA` | core_math | yes | centroid η |
| `HESPERIA_EXPOSE_TRIZ` | shipping | no | expose TRIZ route |
| `HESPERIA_EXPOSE_VERSION` | shipping | no | expose /version |
| `HESPERIA_FIELD_DYNAMICS` | dynamics | e2e | dynamics master |
| `HESPERIA_FIELD_DYNAMICS_DLCR` | dynamics | e2e | dynamics+DLCR |
| `HESPERIA_FIELD_DYNAMICS_HEX_CAP` | dynamics | e2e | hex cap |
| `HESPERIA_FIELD_DYNAMICS_PHASE2` | dynamics | e2e | phase 2 |
| `HESPERIA_FIELD_DYNAMICS_PHASE3` | dynamics | e2e | phase 3 |
| `HESPERIA_FIELD_DYNAMICS_PHASE4` | dynamics | e2e | phase 4 |
| `HESPERIA_FIELD_DYNAMICS_STATE_PATH` | dynamics | e2e | state path |
| `HESPERIA_FIELD_DYNAMICS_TRIZ` | dynamics | e2e | TRIZ in bridge |
| `HESPERIA_FIELD_DYNAMICS_XI` | dynamics | e2e | ξ switch |
| `HESPERIA_FIELD_DYNAMICS_XI_KME` | dynamics | e2e | ξ KME |
| `HESPERIA_FIELD_DYNAMICS_XI_KME_WEIGHT` | dynamics | e2e | KME weight |
| `HESPERIA_FIELD_DYNAMICS_XI_SCALE` | dynamics | e2e | ξ scale |
| `HESPERIA_GIT_COMMIT` | provenance | no | git commit stamp |
| `HESPERIA_K_DISP` | core_math | yes | k_disp penalty |
| `HESPERIA_K_GUARD` | core_math | yes | k_guard penalty |
| `HESPERIA_K_SHADOW_PERTURB` | core_math | yes | shadow perturb |
| `HESPERIA_LAMBDA` | core_math | yes | traversal λ |
| `HESPERIA_LEXICAL_WRITE_ALLOWED` | control | no | lexical write guard |
| `HESPERIA_LICENSE_EXPIRY` | license | no | license expiry |
| `HESPERIA_LICENSE_FILE` | license | no | license file path |
| `HESPERIA_LICENSE_REQUIRED` | license | no | require license |
| `HESPERIA_LICENSE_SKIP` | license | no | skip license |
| `HESPERIA_LICENSE_TOKEN` | license | no | license token |
| `HESPERIA_MACHINE_BINDING` | license | no | machine bind |
| `HESPERIA_MACHINE_ID` | license | no | machine id |
| `HESPERIA_MAIN_ENGINE_OUT` | e2e | e2e | main engine out path |
| `HESPERIA_MAIN_ENGINE_TEXT` | e2e | e2e | default main text |
| `HESPERIA_MAX_INPUT_CHARS` | shipping | yes | input cap |
| `HESPERIA_NOONE2_ROOT` | ingest | indirect | noone2 corpus root |
| `HESPERIA_NOONE_ROOT` | ingest | indirect | noone corpus root |
| `HESPERIA_OPENAI_MODEL` | tools | indirect | default OpenAI model (`gpt-4o-mini`) |
| `HESPERIA_PCH_DIR` | assets | yes | PCH dir override |
| `HESPERIA_PCH_UNIFORM_INJECTION_DEV` | dev | no | PCH dev inject |
| `HESPERIA_PRODUCTION_MATRICES_DIR` | assets | yes | matrices dir |
| `HESPERIA_PRODUCT_E2E_OUT` | e2e | e2e | product E2E out |
| `HESPERIA_PRODUCT_E2E_TEXT` | e2e | e2e | product E2E text |
| `HESPERIA_PRODUCT_SURFACE` | shipping | yes | strict product surface |
| `HESPERIA_PUBLIC_SCHEMA_STRICT_KEYS` | shipping | no | strict JSON keys |
| `HESPERIA_RATE_LIMIT` | shipping | no | RPM limit |
| `HESPERIA_RELEASE_BUILD_TIMESTAMP` | provenance | no | release seal ts |
| `HESPERIA_REQUIRE_SYSTEM_SEAL` | shipping | no | require system seal |
| `HESPERIA_RUNTIME_MODE` | shipping | no | runtime mode string |
| `HESPERIA_SCHEMA_SHA256` | shipping | no | schema SHA check |
| `HESPERIA_SEALED_DLCR_SIDECAR` | stack | yes | sealed DLCR sidecar |
| `HESPERIA_SEALED_E2E_TRIZ` | e2e | e2e | sealed E2E TRIZ |
| `HESPERIA_SEMANTIC_FIELD_EQUATIONS_V1` | e2e | e2e | semantic field eq |
| `HESPERIA_SEMANTIC_FIELD_STUB_MATRICES` | seal | e2e | stub matrices |
| `HESPERIA_SEMANTIC_FIELD_V1_STEPS` | e2e | e2e | semantic field steps |
| `HESPERIA_SHIPPING_ENV_STRICT` | shipping | no | strict unknown env |
| `HESPERIA_SPHERE_PIPELINE_DEV` | sphere | no | sphere dev gate |
| `HESPERIA_TFP4_ROOT` | tfp_tool | indirect | tfp4 ingest root |
| `HESPERIA_TFP_DLCR` | tfp | e2e | TFP session DLCR |
| `HESPERIA_TFP_GOLD_BUNDLE_DIR` | tfp_tool | gate | gold bundle dir |
| `HESPERIA_TFP_MODULE_DATA_ROOT` | tfp | indirect | module data root |
| `HESPERIA_TFP_MODULE_SEALED` | tfp | no | seal warn/block project |
| `HESPERIA_TFP_PIPELINE_RUN_ID` | tfp_tool | no | pipeline run id |
| `HESPERIA_V06_MODEL_REVISION` | version | gate | model revision pin |
| `HESPERIA_VERSION` | provenance | no | version string |

## Read in code, not in `env_guard` allowlist

| Variable | Bucket | Can change TFP slice | Note |
|----------|--------|----------------------|------|
| `HESPERIA_CB1_LEXICAL_GATE` | lexical | yes | optional lexical gate; not in allowlist |
| `HESPERIA_CB1_CONCEPT_GATE` | lexical | yes | optional TFP concept gate; not in allowlist |
| `HESPERIA_DLCR_MIN_RESOLVE_SCORE_C` | lexical | yes | Dict C resolve floor; not in allowlist |
| `HESPERIA_REPO` | tool | no | Hesperia repo path (tooling) |
| `HESPERIA_LEGACY_RESEARCH_CORPUS` | calib_tool | indirect | legacy corpus guard |
| `HESPERIA_STRICT_DETERMINISM` | test | gate | determinism pytest |
| `HESPERIA_SKIP_TFP_V1_LAYOUT_TEST` | test | gate | skip layout test |
| `HESPERIA_METRICS_MIN_LEXICAL_ACCEPTED_SUM` | test | gate | metrics gate |
| `HESPERIA_METRICS_MIN_PER_TEXT_NON_EMPTY_RATIO` | test | gate | metrics gate |
| `HESPERIA_METRICS_MIN_LOWEST_PER_TEXT_ACCEPTED` | test | gate | metrics gate |
| `HESPERIA_REL_REAL_UNMAPPED_RATE_MAX` | test | gate | REL ENF test |
| `HESPERIA_CD_DELTA_REL_K` | test | gate | CD delta test |
| `HESPERIA_CD_DELTA_ABS_CAP` | test | gate | CD delta test |
| `HESPERIA_UNMAPPED_RATE_MAX` | test | gate | unmapped gate |
| `PYTHONHASHSEED` | smoke | gate | TFP precheck hash seed |
| `HESPERIA_PHASE_C_SMOKE_MAX_SEC` | smoke | gate | phase C wall cap |
| `HESPERIA_PHASE_C_LATENCY_RATIO_MAX` | smoke | gate | phase C ratio cap |

## Module config (not env)

| Key | Scope | Role |
|-----|-------|------|
| `labels` | TFP | `TFPModule.configure`; `tfp_vector` bucket names |

`SIGNED: Ethan (governance) | Hesperia TFP runtime table | 2026-04-07 | brain repo root`
