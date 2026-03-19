# TFP Testing Session — Task List (17–20 items)

Session summary: tasks completed for TFP (Transference-Focused Psychotherapy) / Kernberg testing and clinical analytics in HESPERIA.

---

## 1. LEVEL 15 — Speaker-aware session parsing

- **Module:** `hesperia/nlp/session_structure.py`
- Utterance (speaker, text, tokens, target); `parse_session_dialogue(text)` with Patient:/Therapist: and default patient.
- **Tests:** `tests/nlp/test_session_structure.py`

## 2. Russian activation enhancement (dicts)

- **Modules:** `hesperia/nlp/lemmatizer.py`, `hesperia/nlp/phrase_detector.py`; **Data:** `dictA_colloquial.yaml`, `phrase_patterns.yaml`
- Lemmatization (pymorphy2), colloquial/affective markers (weight 1.2), phrase patterns (weight 1.5), `analyze_session_enhanced()`.
- **Tests:** `tests/nlp/test_activation_enhanced.py`

## 3. Dialogue role layer

- **Updates:** `session_structure.py` — `Target`, `infer_utterance_target(speaker, text, tokens)`; `session_parser` — `activation_by_direction`, `role_direction` (patient_to_therapist, therapist_to_patient, patient_to_third).
- **Tests:** `tests/nlp/test_role_direction_and_temporal.py`

## 4. Transference detection layer

- **Module:** `research/clinical_tfp/transference_detection.py`
- `detect_transference()`, `transference_summary()` — positive/negative transference, projective identification, idealization, devaluation, persecutory object.
- **Tests:** in `test_role_direction_and_temporal.py`

## 5. Temporal session dynamics

- **Module:** `hesperia/nlp/temporal_dynamics.py`
- `build_utterance_windows()`, `build_activation_timeline()`, `detect_escalation()` (utterance windows, activation timeline).
- **Tests:** in `test_role_direction_and_temporal.py`

## 6. TFP stage detection

- **Module:** `research/clinical_tfp/stage_detection.py`
- `detect_tfp_stage()`, `stage_from_timeline()` — chaotic, defense_clarification, interpretation, integration.
- **Tests:** in `test_role_direction_and_temporal.py`

## 7. Dialogue structure model

- **Module:** `hesperia/nlp/dialogue_structure.py`
- Turn, Response, InteractionPair (patient → therapist → patient reaction); `build_turns()`, `build_interaction_pairs()`.
- **Tests:** `tests/experimental/clinical_tfp/test_operational_analytics.py`

## 8. Therapist intervention classification

- **Module:** `research/clinical_tfp/intervention_classifier.py`
- `classify_intervention()` — clarification, confrontation, interpretation, limit_setting, support (Area 9).
- **Tests:** in `test_operational_analytics.py`

## 9. Affect intensity estimation

- **Module:** `research/clinical_tfp/affect_intensity.py`
- `estimate_affect_intensity(text, tokens)` → [0..1]; lexical + exclamation.
- **Tests:** in `test_operational_analytics.py`

## 10. Object representation tracking

- **Module:** `research/clinical_tfp/object_representation_tracking.py`
- `track_object_representations()` — therapist_representation, self_representation, third_objects (A2).
- **Tests:** in `test_operational_analytics.py`

## 11. Interaction loop detection

- **Module:** `research/clinical_tfp/interaction_loop_detection.py`
- `detect_interaction_loops(timeline, therapist_utterances)` — accusation → escalation, projective_identification_signal.
- **Tests:** in `test_operational_analytics.py`

## 12. Affect–defense coupling

- **Module:** `research/clinical_tfp/affect_defense_coupling.py`
- `couple_affect_defense()`, `infer_affect_from_areas()` — anger→splitting, shame→projection, etc. (A1, A3, A4).
- **Tests:** in `test_operational_analytics.py`

## 13. Session summary generator

- **Module:** `research/clinical_tfp/session_summary.py`
- `build_session_summary()`, `build_session_summary_with_timeline()` — dominant affects, defenses, object relations, transference indicators.
- **Tests:** in `test_operational_analytics.py`

## 14. Text normalization

- **Module:** `hesperia/nlp/text_normalization.py`
- Fillers removal, speech disfluency cleanup, punctuation normalization; `normalize_transcript_text()`.
- **Tests:** `tests/nlp/test_text_norm_negation_ngram.py`

## 15. Negation detection

- **Module:** `hesperia/nlp/negation.py`
- `find_negation_scopes()`, `get_negated_token_indices()` — avoid false activation (e.g. “я не злюсь”).
- **Tests:** in `test_text_norm_negation_ngram.py`

## 16. Multi-word marker detection (2–5 n-grams)

- **Module:** `hesperia/nlp/ngram_markers.py`
- `build_ngram_marker_index()`, `detect_ngram_markers()` — phrases like “мне кажется вы”, “вы специально”.
- **Tests:** in `test_text_norm_negation_ngram.py`

## 17. Activation calibration + config + stopwords

- **Modules:** `hesperia/engine/calibration/activation_calibration.py`, `specs/canon/activation_calibration.yaml`, `hesperia/ontology/dictA/dictA_stopwords.yaml`, `load_stopwords()`.
- **Tests:** smoke in session; calibration tests in `test_governance_explainability_benchmark.py`.

## 18. Session segmentation + confidence + clinical report

- **Modules:** `hesperia/nlp/session_segmentation.py`, `research/clinical_tfp/confidence_scoring.py`, `generate_clinical_report_readable()` in report_generator.
- **Tests:** in `test_text_norm_negation_ngram.py` and operational/benchmark tests.

## 19. Ontology governance + explainability + logging + corpus + experiments + graph + benchmark + safety

- **Ontology:** `hesperia/ontology/ontology_registry.yaml`, `registry.py` (versioning).
- **Explainability:** `hesperia/engine/explainability.py` (activation_trace: marker→concept→family→area).
- **Logging:** `hesperia/logging/session_log.py` (JSONL).
- **Corpus:** `hesperia/corpus/session_corpus.py` (manifest, metadata).
- **Experiments:** `hesperia/experiments/experiment_runner.py` (compare ontology versions).
- **Graph:** `hesperia/graph/graph_store.py` (JSON, GraphML).
- **Config:** `hesperia/config/clinical_config.yaml`, `config_loader.py`.
- **Benchmark:** `tests/experimental/clinical_tfp/benchmark_sessions.yaml`.
- **Safety:** `research/clinical_tfp/safety_layer.py` (minimum evidence threshold).
- **Tests:** `tests/experimental/clinical_tfp/test_governance_explainability_benchmark.py`.

## 20. Validation corpus and TFP testing docs

- **Doc:** `docs/testing/VALIDATION_CORPUS.md` — 20–50 TFP transcripts, marker/relation/threshold tuning.
- **Existing:** `docs/testing/TFP_KERNBERG_TESTING.md` — input format, CLI/API, output; extended by status doc below.

---

*Total: 20 task groups. See `docs/testing/TFP_TESTING_STATUS.md` for what’s done and how to run TFP testing.*
