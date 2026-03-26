# Clinical / TFP input_signal execution_flow — residual gaps (v0.1 note)

**Scope:** Maps user-facing “still missing” items to repo reality after softmax/cap/negation/session-relative curves and entropy confidence (session topology + `session_parser`).

| # | Topic | Status in repo | Next step (when prioritized) |
|---|--------|----------------|--------------------------------|
| 1 | Cross-area competition | **Partially addressed:** per-segment `share` or **`softmax`** before named curves (`area_competition`); raw `segments[].areas` unchanged. | Tune `softmax_temperature`; optional hard winner-take-most. |
| 2 | Trigger saturation | **Partially addressed:** `per_concept_score_cap` and optional `use_log1p_concept_scores` in `activate_concepts` / `analyze_session`; topology enables cap by default. | Calibrate cap per domain pack. |
| 3 | Negation | **Minimal:** RU `не`/`нет`/`ни` in ±`negation_window` tokens dampens **token** and **tuple-phrase** hits; string n-gram path in `analyze_session` still without scope. | Scoped clausal negation; polarity tags on Dict-A entries. |
| 4 | Subject / session baseline | **Partially addressed:** `area_curves_session_relative` = curve − session mean; not cross-patient z-norm. | Corpus or patient priors; z-score optional flag. |
| 5 | Transition cost / state machine | **Open:** `state_sequence` is argmax per segment; no penalty on jumps. | Hidden Markov / temporal regularizer on dominant area; or smooth logits before argmax. |
| 6 | Hierarchy consistency | **Largely already:** `activate_concepts` rolls concept→family→area by sum; no shortcut path in that function. | Audit propagation and enhanced paths for drift; schema validators on outputs. |
| 7 | Confidence | **Partial:** `segment_dominance_confidence` (entropy after competition). Not trigger-count / multi-input_signal agreement. | Fuse marker counts, family agreement, DLCR if present. |
| 8 | Gold segments & error surface | **Open:** no bundled 10–20 labeled segments for coefficient search. | Add `tests/gold/clinical_topology_segments_v1.yaml` + loss hook in tools. |
| 9 | Hex stabilization | **Open:** topology path is still text→markers→concepts→areas for segments; hex microstructure is separate artifact. | Optional `concept_scores → hex → area` branch behind flag. |
| 10 | Affect vs behavior vs cognition | **Open:** Dict-B lacks required `signal_type` for split aggregation. | Extend `concept_nodes` + aggregate A4 from affect-tagged concepts only. |
| 11 | Token-density / verbosity | **Partially addressed:** `analyze_session(..., evidence_volume_normalize=True)` scales **every** marker coefficient by `1/sqrt(token_count)` before aggregation; topology enables by default. | Optional per-100-token reporting; matched-token-only denominator variant. |
| 12 | Speaker-role contamination | **Open:** single stream unless dialogue path uses `analyze_session_speaker_aware` elsewhere; topology segments do not split patient/therapist. | Wire speaker channels into `09_` or separate artifacts (`patient_scores`, `therapist_scores`, dyadic layer). |
| 13 | Quotation / reported speech | **Open:** no utterance `mode` tags. | NLP layer: `self_report` / `reported_speech` / `third_party` / … + downweight indirect for state head. |
| 14 | Fantasy vs action | **Open:** no `action_status` (imagined vs completed). | Parser or Dict-A cues + separate aggregation for impulsivity/agency. |
| 15 | Temporal reference collapse | **Open:** segments treat all text as “present.” | `time_ref` tags; downweight distant_past for “current escalation” curves. |
| 16 | Question–answer asymmetry | **Open:** short confirmations not de-weighted vs therapist frame. | Dialogue pairing + “short reply to therapist prompt” flag → reduce autonomous coefficient. |
| 17 | Structural ambiguity | **Open:** one marker → one concept hard map. | Multi-candidate concepts + `ambiguity_penalty` + local resolver. |
| 18 | Opposing evidence / cancellation | **Open:** mostly additive evidence. | Counterweights (e.g. planning vs chaos; mentalization vs primitive defense). |
| 19 | Defense inference depth | **Open:** `defense_timeline` is still lexically driven. | Require multi-input_signal / cross-segment agreement before high-confidence defense labels. |
| 20 | Technique vs diagnosis separation | **Open:** shared competitive area space. | Separate output heads (state / defense / technique / dyadic) per §20. |
| 21 | Session edge artifacts | **Open:** no positional weighting. | `position_weight` taper on first/last k segments. |
| 22 | Repetition / thematic memory | **Open:** segment-local only. | Rolling `persistent_theme_score` with decay + recurrence stats. |

**Related code:** `research/clinical_tfp/session_topology.py`, `hesperia/nlp/session_parser.py`, `hesperia/ontology/dictA/loader.py` (`confidence_type`).

**Calibration index:** [TFP_CALIBRATION_KNOBS_v0_1.md](../../specs/TFP_CALIBRATION_KNOBS_v0_1.md) — bundle keys, knobs, API notes.
