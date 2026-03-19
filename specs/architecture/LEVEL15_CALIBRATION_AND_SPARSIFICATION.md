# LEVEL 15 — Calibration and sparsification

Reproducibility and control of propagation weights, relation weights, graph density, and fingerprint format.

## 1. Propagation weights (graph calibration)

**File:** `specs/canon/propagation_weights.yaml`  
**Loader:** `sphere.topology.propagation_weights_loader.load_propagation_weights()`

- **zone_weights:** center_to_inner, inner_to_middle, middle_to_inner, middle_to_outer, outer_to_middle.
- **bridge_weight:** cross-area bridge coefficient.
- **decay_factor:** optional per-hop decay (default 1.0).
- **concept_to_family_multiplier:** optional scaling (default 1.0).

Used in `sphere.topology.activation_propagation`: `propagate_within_area` and `propagate_across_bridges` take optional `weights`; `propagate_activation` loads from spec when `weights=None`.

## 2. Concept relation weights

**File:** `specs/canon/concept_relation_weights.yaml`

- **relation_weights:** activates=1.0, co_occurs_with=0.7, expresses=0.6, defends_against=0.5, opposes=-0.6, etc.
- **default_weight:** for unknown relation types (0.5).

Used in `hesperia.engine.kme.clinical_bridge.build_concept_relation_edges`: edge weight = base_weight × abs(relation_weight). Negative weights (e.g. opposes) affect conflict index (CI) interpretation.

## 3. Graph sparsification

**Constants in** `hesperia.engine.kme.clinical_bridge`:

- **TOP_K_CONCEPTS:** 60 — keep only top 60 concepts by score before building graph.
- **TOP_K_FAMILIES:** 30 — keep only top 30 families.
- **MIN_EDGE_WEIGHT:** 0.05 — drop edges below this after merge.

Reduces noise and keeps KME metrics stable on dense sessions.

## 4. Stable fingerprint format

**File:** `specs/canon/clinical_fingerprint_schema.yaml`

- **primitive_metrics:** 6 (LD, COH, NC, PR, PV, CI).
- **derived_metrics:** 35.
- **fingerprint_vector:** 41 (primitives + derived).
- **vector_hash:** sha256.

Ensures version compatibility for distance and trajectory.

## 5. Cross-session fingerprint distance

**Module:** `hesperia.engine.kme.fingerprint_distance`

- **cosine_distance(a, b):** 1 - cosine_similarity; range [0, 2].
- **euclidean_distance(a, b):** L2 between 41-dim vectors.
- **wasserstein_distance(a, b):** 1D Earth Mover's distance (CDF difference).
- **fingerprint_distance(a, b, metric="cosine"|"euclidean"|"wasserstein"):** single entry point.

Use for: patient similarity, therapy progress, cluster detection.

## 6. Visualization

**Module:** `hesperia.visualization.session_graph`

- **export_graph_gexf(graph, path):** write hierarchical graph to GEXF.
- **export_graph_graphml(graph, path):** write to GraphML.
- **plot_activation_heatmap(data, path):** heatmap from segment/area or area→values; saves if matplotlib and path given.
- **plot_area_trajectory(state_sequence, path):** A2 → A3 → A4 style plot.

## 7. Transcript ingestion

**Module:** `hesperia.nlp.transcript_parser`

- **parse_speaker_turns(text):** list of Turn(speaker, text, turn_index); detects "Пациент:", "Терапевт:", "Patient:", "Therapist:".
- **segment_by_speaker(text):** {"patient": [...], "therapist": [...]}.
- **get_patient_text_only(text):** concatenated patient turns for analysis.

Improves detection when input is turn-segmented TFP transcripts.

## 8. Speaker-aware session parsing (LEVEL 15)

**Module:** `hesperia.nlp.session_structure` + `hesperia.nlp.session_parser`

- **Utterance(speaker, text, tokens):** single turn; `speaker` is `"patient"` or `"therapist"`.
- **parse_session_dialogue(text):** split by "Patient:" / "Therapist:" lines; unlabeled lines default to patient. Each utterance gets tokenize + normalize → `tokens`.
- **analyze_session_speaker_aware(text, ...):** pipeline: parse_session_dialogue → tokenize per utterance → detect_markers → speaker-weighted activation → optional propagation.
- **Weights:** patient markers = 1.0 (mental dynamics), therapist markers = 0.5 (intervention). Constants: `PATIENT_MARKER_WEIGHT`, `THERAPIST_MARKER_WEIGHT`.
- **Result shape:** `areas`, `families`, `concepts` (combined weighted) + `speaker_activation`: `{ "patient": { areas, families, concepts }, "therapist": { ... } }`.

Pipeline: text → parse_session_dialogue → tokenize → detect_markers → speaker-weighted activation → propagation → Clinical ActiveGraph → KME. Prepares for transference/countertransference/role induction.
