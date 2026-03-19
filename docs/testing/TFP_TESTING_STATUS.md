# TFP Testing — What’s Done So Far

Status of the TFP (Transference-Focused Psychotherapy) / Kernberg testing stack in HESPERIA. Use this with [TFP_KERNBERG_TESTING.md](TFP_KERNBERG_TESTING.md) for input/output and CLI, and [TASK_LIST_TFP_SESSION.md](TASK_LIST_TFP_SESSION.md) for the full task list.

---

## Pipeline (end-to-end)

Current flow for session text:

```
session text
  → text normalization (fillers, disfluency, punctuation)
  → speaker parsing (Patient:/Therapist: → Utterance with target)
  → dialogue structure (Turn, InteractionPair: patient → therapist → patient reaction)
  → tokenize → (optional) lemmatize → Dict-A markers + colloquial + phrase patterns + n-gram markers (2–5)
  → (optional) negation scope: drop markers from negated tokens
  → (optional) clinical stopwords filter
  → concept activation → family → area
  → (optional) propagation (topology)
  → activation_by_direction (patient_to_therapist, therapist_to_patient, patient_to_third)
  → transference detection (positive/negative, projective identification, idealization, devaluation)
  → temporal dynamics (utterance windows, activation timeline, escalation)
  → TFP stage (chaotic, defense_clarification, interpretation, integration)
  → intervention classification (clarification, confrontation, interpretation, limit_setting, support)
  → affect intensity [0..1], object representation tracking, affect–defense coupling
  → (optional) safety filter (minimum evidence threshold)
  → session summary + confidence + clinical report
  → (optional) Clinical ActiveGraph → KME metrics
  → (optional) activation_trace (explainability), session log (JSONL), graph persistence (JSON/GraphML)
```

---

## Implemented and test-covered

| Layer | Module(s) | Tests |
|-------|-----------|--------|
| Speaker parsing | `hesperia.nlp.session_structure` | `test_session_structure.py` |
| Russian enhancement (lemmatizer, colloquial, phrase patterns) | `hesperia.nlp.lemmatizer`, `phrase_detector`, `session_parser.analyze_session_enhanced` | `test_activation_enhanced.py` |
| Role direction (target, activation_by_direction) | `session_structure`, `session_parser.analyze_session_speaker_aware` | `test_role_direction_and_temporal.py` |
| Transference detection | `research.clinical_tfp.transference_detection` | `test_role_direction_and_temporal.py` |
| Temporal dynamics (windows, timeline, escalation) | `hesperia.nlp.temporal_dynamics` | `test_role_direction_and_temporal.py` |
| Stage detection | `research.clinical_tfp.stage_detection` | `test_role_direction_and_temporal.py` |
| Dialogue structure (Turn, InteractionPair) | `hesperia.nlp.dialogue_structure` | `test_operational_analytics.py` |
| Intervention classification | `research.clinical_tfp.intervention_classifier` | `test_operational_analytics.py` |
| Affect intensity | `research.clinical_tfp.affect_intensity` | `test_operational_analytics.py` |
| Object representation tracking | `research.clinical_tfp.object_representation_tracking` | `test_operational_analytics.py` |
| Interaction loops | `research.clinical_tfp.interaction_loop_detection` | `test_operational_analytics.py` |
| Affect–defense coupling | `research.clinical_tfp.affect_defense_coupling` | `test_operational_analytics.py` |
| Session summary | `research.clinical_tfp.session_summary` | `test_operational_analytics.py` |
| Text normalization | `hesperia.nlp.text_normalization` | `test_text_norm_negation_ngram.py` |
| Negation detection | `hesperia.nlp.negation` | `test_text_norm_negation_ngram.py` |
| N-gram markers (2–5) | `hesperia.nlp.ngram_markers` | `test_text_norm_negation_ngram.py` |
| Session segmentation | `hesperia.nlp.session_segmentation` | `test_text_norm_negation_ngram.py` |
| Activation calibration | `hesperia.engine.calibration.activation_calibration` | — |
| Config + stopwords | `hesperia.config`, `dictA_stopwords.yaml`, `load_stopwords` | — |
| Confidence scoring | `research.clinical_tfp.confidence_scoring` | — |
| Clinical report (readable) | `generate_clinical_report_readable` | — |
| Ontology registry | `hesperia.ontology.registry` | `test_governance_explainability_benchmark.py` |
| Explainability (activation_trace) | `hesperia.engine.explainability` | `test_governance_explainability_benchmark.py` |
| Session logging (JSONL) | `hesperia.logging.session_log` | `test_governance_explainability_benchmark.py` |
| Graph persistence | `hesperia.graph.graph_store` | `test_governance_explainability_benchmark.py` |
| Benchmark sessions | `tests/clinical/benchmark_sessions.yaml` | `test_governance_explainability_benchmark.py` (load + run one) |
| Safety (min evidence) | `research.clinical_tfp.safety_layer` | `test_governance_explainability_benchmark.py` |
| Corpus + experiments | `hesperia.corpus`, `hesperia.experiments` | — |

---

## How to run TFP-related tests

From repo root:

```bash
# Speaker-aware and role/temporal/transference/stage
pytest tests/nlp/test_session_structure.py tests/nlp/test_role_direction_and_temporal.py -v

# Russian enhancement (lemmatizer, colloquial, phrase patterns)
pytest tests/nlp/test_activation_enhanced.py -v

# Operational analytics (dialogue, intervention, affect, object, loops, coupling, summary)
pytest tests/clinical/test_operational_analytics.py -v

# Text norm, negation, n-grams, segmentation
pytest tests/nlp/test_text_norm_negation_ngram.py -v

# Governance, explainability, logging, graph, benchmark, safety, config
pytest tests/clinical/test_governance_explainability_benchmark.py -v
```

Single batch:

```bash
pytest tests/nlp/test_session_structure.py tests/nlp/test_role_direction_and_temporal.py tests/nlp/test_activation_enhanced.py tests/clinical/test_operational_analytics.py tests/nlp/test_text_norm_negation_ngram.py tests/clinical/test_governance_explainability_benchmark.py -v
```

---

## Not yet done / optional

- **Full pipeline wiring:** Normalization and negation are not yet plugged into the default `analyze_session_speaker_aware` path; they can be applied in a wrapper or a dedicated “TFP full” entrypoint.
- **Validation corpus:** Placeholder and process are in [VALIDATION_CORPUS.md](VALIDATION_CORPUS.md); 20–50 TFP transcripts still to be added for marker/relation/threshold tuning.
- **Performance layer:** Marker indexing, vectorized token lookup, graph caching are not implemented.
- **Neo4j:** Graph store supports JSON and GraphML only; Neo4j would be an extra backend.

---

## Quick smoke (speaker-aware + summary + report)

```python
from hesperia.nlp import parse_session_dialogue, analyze_session_speaker_aware
from research.clinical_tfp import build_session_summary, generate_clinical_report_readable

text = """Patient: Вы меня ненавидите.
Therapist: Что вы чувствуете?
Patient: Меня бесит это."""

activation = analyze_session_speaker_aware(text)
summary = build_session_summary(activation)
report = generate_clinical_report_readable(session_summary=summary)
print(report)
```

---

*Last updated: session that added the 20-task list and this status doc. For input formats and CLI/API, see [TFP_KERNBERG_TESTING.md](TFP_KERNBERG_TESTING.md).*
