# Hesperia TFP — yielded parameters (table)

**Authority:** Ethan (governance). **Narrative (brain repo):** `operational/assignments/reports/GRACE-HESPERIA-TFP-YIELDED-PARAMETERS-2026-04-07.md`. **Asset paths:** Hesperia product repo.

## Clinical / process ↔ outputs (reference)

| Concept | Yielded where |
|---------|---------------|
| Iteration | Per-request scores; no multi-turn index in default `tfp_profile`. |
| Session | `input.signals`; not full transcript in `tfp_vector`/`tfp_profile`. |
| Client perspective | `areas`/`families`/`concept_hits` from one text slice. |
| Therapist perspective | Not in default `tfp_profile`/`tfp_conflicts`. |
| Interference | `interaction_loop` strings; structured loops if API supplies timeline. |
| Shift | No dedicated field. |

## Engine context — general (post-aggregation)

| Path | Type | Calibratable |
|------|------|--------------|
| `areas` | dict[str,float] | indirect (dict pack, lexical) |
| `families` | dict[str,float] | indirect |
| `metrics` | dict | per module |
| `signals.tfp_conflicts` | list[str] | indirect |
| `modules.<name>` | dict | per module contract |
| `input.text` | str | N/A |
| `input.signals` | list | N/A |
| `meta.trace` | list | N/A |
| `meta.execution_graph` | dict | N/A |
| `meta.hash_*` | str | N/A |

## `modules["tfp.v1"]` (TFP module)

| Key | Type | Calibratable |
|-----|------|--------------|
| `tfp_vector` | dict label→float | indirect (dict pack); labels via module config |
| `tfp_profile.dominant` | str|null | indirect |
| `tfp_profile.confidence` | float | indirect |
| `tfp_profile.stage` | enum str | indirect; thresholds in code |
| `tfp_profile.affect_intensity` | float 0–1 | code regex/tokens |
| `tfp_profile.confidence_scores` | nested dict | indirect; formula in code |
| `tfp_conflicts` | list[str] | indirect; 0.4 cutoff in code |

## Invariant activation bundle (`build_invariant_tfp_activation`)

| Key | Type | Calibratable |
|-----|------|--------------|
| `concepts` | dict | signal_calibration + dict map |
| `families` | dict | same |
| `areas` | dict (prob on AREA_IDS) | signal_calibration + inhibition + anchors |
| `areas_raw` | dict | same |
| `areas_inhibited` | dict | inhibition matrix |
| `areas_final` | dict | softmax temperature in JSON |
| `areas_pre_hex` | dict | dict + hex |
| `families_pre_hex` / `families_post_hex` | dict | hex params in JSON |
| `concept_weights_*` | dict | concept_cap, log norm, segment norm |
| `hex_activation_raw` / `hex_activation_post` | dict | hex_decay, hex_smoothing_alpha, anchors |
| `hex_feedback_delta` | dict | same |
| `invariant_activation` | dict meta | version ids from JSON |
| `propagation_trace` | list | sphere embedding optional |
| `families_propagated` / `areas_propagated` | dict | optional |
| `propagation_trace_error` | str | optional |

## Calibration artifacts (asset-level)

| Artifact | Calibratable | Feeds |
|----------|--------------|-------|
| `assets/calibration/dicts/<pack>/dict_a.jsonl` | yes | concept_hits, scores |
| `assets/calibration/dicts/<pack>/dict_b.jsonl` | yes | family/area metadata |
| `assets/data/engine_dynamics_v060/semantic_dynamics/signal_calibration_v2.json` | yes | invariant path numerics |
| `area_inhibition_matrix_*.json` (via calibration pointer) | yes | areas pre-softmax |
| `assets/data/engine_dynamics_v060/anchors/concept_hex_anchors_tfp.json` | yes | hex feedback |
| `TFPModule` YAML `labels` | yes | tfp_vector keys |
| `detect_tfp_stage` thresholds | code only | tfp_profile.stage |
| `estimate_affect_intensity` patterns | code only | affect_intensity |
| `detect_interaction_loops` thresholds | code only | tfp_conflicts |
| `classify_intervention` patterns | code only | loop records when wired |

## Footnote — `iteration_segment_openai_v1` export (2026-04-07)

The Django **HTML** layer (`output_views`) builds a frozen **`iteration_segment_openai_v1`** JSON for OpenAI export: **`parameters`** (iteration-level keys aligned with this table when the engine supplies them), **`sentences`**, **`audit`**, and **`messages`**. Schema: Hesperia `output_views/schemas/iteration_segment_openai_v1.schema.json`; glossary: Hesperia `docs/output_views/FIELD_GLOSSARY.md`. Brain UX spec: `governance/SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md` (cursor repo).

`SIGNED: Ethan (governance) | Hesperia TFP yielded table | 2026-04-07 | brain repo root`
