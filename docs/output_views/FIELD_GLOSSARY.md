# iteration_segment_openai_v1 — field glossary (human labels)

**Schema:** `output_views/schemas/iteration_segment_openai_v1.schema.json`  
**Authority:** brain `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md`

| JSON path | Meaning |
|-----------|---------|
| `schema_version` | Segment JSON format version (e.g. `1.0.0`). |
| `prompt_pack_id` | Which prompt templates were used for `messages` (e.g. `kernberg_iteration_review_v1`). Bump when prompts change. |
| `meta.run_timestamp_utc` | When the parent analyze run was produced (ISO-8601 UTC). |
| `meta.source_file` | Display name or basename of input artifact (no secrets). |
| `meta.source_label` | Optional human label for the run. |
| `meta.modules_executed` | Hesperia module names that contributed. |
| `meta.module_versions` | Semver or hash per module. |
| `meta.calibration_dict_pack` | Optional pointer to calibration pack used. |
| `meta.trace` | Optional engine trace (opaque to UI in v1). |
| `meta.disclaimer_footer` | Non-clinical disclosure string (UI + export). |
| `iteration.iteration_id` | Stable id for this iteration within the session. |
| `iteration.order` | Monotonic index for charts (0..n-1). |
| `iteration.t_start_ms` / `t_end_ms` | Optional timing window for graphs. |
| `iteration.wall_clock_iso` | Optional wall time for this iteration. |
| `parameters` | Engine output for this iteration (areas, families, tfp_profile, …). |
| `sentences` | Ordered sentence spans with `id`, `text`, `order`. |
| `audit` | Attribution / corpus slice for inspection (may be empty in MVP). |
| `messages` | OpenAI Chat-style `role` + `content` (system + user minimum). |

`SIGNED: Gena | Hesperia output_views | 2026-04-07 | T05`
