# TFP signal calibration knobs (v0.1)

**Purpose:** Single index of **weights / thresholds** that shape clinical session topology and Dict-A attribution, where they appear in bundle output, and how to **run** with overrides.

## Where values are recorded in a bundle

| Location | Contents |
|----------|-----------|
| `00_manifest.json` → **`tfp_signal_calibration`** | `session_topology_run_params`, `area_curve_map`, `curve_calibration_reference`, `dict_a_confidence_multiplier` |
| `09_session_topology.json` (top-level) | Same four keys + `sessions[]` |
| Per session → `session_topology` → **`curve_projection_meta`** | `engine_params`, `area_curve_map`, `lexical_controls`, `segment_dominance_confidence`, `calibration_reference_bands` |

**CLI override:** `python3 -m runtime.pipeline.run_tfp_file_pipeline … --topology-params-json path/to.json` merges a JSON **object** over `DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS` (see `research.clinical_tfp.session_topology`).

**Programmatic:** `run_pipeline(..., topology_run_params={"per_concept_score_cap": 12.0})`.

---

## Variables that require weighting / tuning

| Variable | Module | Role | Typical tuning |
|----------|--------|------|----------------|
| **`AREA_CURVE_MAP`** | `session_topology` | Named clinical axis → Hesperia area (1:1) | Clinical mapping review; version in git |
| **`area_competition`** | `run_session_topology` | `share` / `softmax` / `none` | Softmax sharpens dominant state |
| **`softmax_temperature`** | `run_session_topology` | Softmax sharpness | ↑ = softer competition |
| **`curve_smooth_alpha`** | `run_session_topology` | Adjacent-segment smoothing | 0.6–0.85 |
| **`curve_session_center`** | `run_session_topology` | Emit `area_curves_session_relative` | On for deviation-from-session-mean |
| **`per_concept_score_cap`** | `analyze_session` | Caps summed trigger weight per concept | 6–12 for verbose corpora |
| **`use_log1p_concept_scores`** | `analyze_session` | Alternative to cap | Mutually exclusive path vs cap |
| **`evidence_volume_normalize`** | `analyze_session` | `marker_weight × 1/sqrt(token_count)` | On to reduce verbosity bias |
| **`apply_token_negation`** | `analyze_session` | Dampen triggers near `не`/`нет`/`ни` | On/off; tune `negation_multiplier` |
| **`negation_window`** | `analyze_session` | Token window for negation | 2–3 |
| **`negation_multiplier`** | `analyze_session` | Factor when negation in window | 0.3–0.7 |
| **`CURVE_CALIBRATION_REFERENCE`** | `session_topology` | Operator bands 0.2 / 0.5 / 0.8 | Not auto-labels; tune dict weights to hit bands on gold |
| **`CONFIDENCE_TYPE_MULTIPLIER`** | `dictA/loader` | `strong` / `weak` on Dict-A entries | Edit YAML + multipliers in code |
| **Dict-A `weight`** | `lexical_markers.yaml` | Per-marker activation | Corpus calibration |
| **`normalize_scores`** | `activate_concepts` / `analyze_session` | Max-norm per layer | Usually true |

---

## API / runtime attribution (product vs research)

| Surface | Attribution |
|---------|-------------|
| **TFP file pipeline** (`run_tfp_file_pipeline`) | Research/testing bundle; parameters in `00_manifest.json` and `09_`. Not the sealed v0.5.1 public product proof. |
| **Shipping HTTP** (`runtime.shipping`) | Does **not** expose these knobs by default; analysis goes through `analysis_service` + projection. TFP topology is **not** the default product JSON. |
| **E2E** `run_output_e2e_session_topology.json` | Uses `run_session_topology(text)` with **library defaults** unless E2E is extended to pass params. |

**One-shot product API + calibration snapshot:** `PYTHONPATH=. python3 tools/tfp_api_calibration_one_shot.py -i <transcript.md> -o outputs/tfp_api_calibration_one_shot` runs **one** in-process `POST /analyze` (same handler as shipping) and writes `public_analyze_response.json` plus `tfp_signal_calibration.json` (same shape as `00_manifest.json` → `tfp_signal_calibration`). Use `--calibration-only` to emit only the sidecar.

For a future **API**, recommended pattern: optional `clinical_topology_options` object (subset of `session_topology_run_params`) validated against an allowlist; defaults = `DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS`.

---

## Related

- `docs/governance/working/CLINICAL_SIGNAL_PIPELINE_GAPS_v0_1.md` — roadmap for speaker split, time_ref, etc.
- `docs/HESPERIA_VARIABLE_CATALOG.md` — E2E variable index.
