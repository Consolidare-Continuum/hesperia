# Gena terminology filter — main engine clarity set

Date: 2026-03-26  
Scope: apply a strict naming filter that separates definition, execution, topology, and measurement.

## Canonical split

- `SCHEMA` -> static system definition (ontology, areas, families, mappings).
- `ENGINE` -> executable core (execution flow, operators, checks, artifacts).
- `CONFIG` -> runtime parameterization (profiles, thresholds, env toggles).

Use: `HESPERIA ENGINE with SCHEMA vX and CONFIG profile Y`.

## Connectivity vs distance

- `TOPOLOGY` -> who connects to who.
- `METRIC` -> how strong/how far.
- `EMBEDDING` -> coordinates (only when explicitly present).

## Mechanism words

- `DIFFUSION` -> spreading over graph.
- `AGGREGATION` -> combining values.
- `TRANSFER` -> directed movement.

## Time words

- `TRANSITIONS` -> state-to-state movement.
- `TRAJECTORY` -> ordered transition sequence.
- `STABILITY` -> behavior metrics across time.

## Lexical/semantic words

- `TOKEN` -> raw word/phrase.
- `LEMMA` -> normalized lexical unit.
- `CONCEPT_ID` -> canonical semantic node.
- `ALIAS` -> lexical surface mapping to `CONCEPT_ID`.

## Mapping verbs

- `PROJECTION` -> TOKEN/LEMMA -> CONCEPT_ID.
- `ASSIGNMENT` -> CONCEPT_ID -> FAMILY.
- `AGGREGATION` -> FAMILY -> AREA.

## Metric typing (no generic score)

- `WEIGHT` -> static importance.
- `INTENSITY` -> input_signal magnitude.
- `ENERGY` -> coupling/system energy.
- `CONFIDENCE` -> reliability estimate.

## State typing

- `VECTOR` -> numerical representation.
- `ACTIVATION` -> per-node value.
- `SNAPSHOT` -> full system state.

## Output key clarity (non-breaking aliases now)

- keep `dominant_area`
- keep `dominant_family`
- `governance` alias -> `constraint_status`
- `loopability` alias -> `structural_recurrence`
- keep `tension_energy`
- `obstacle_score` alias -> `resistance_index`

Policy: existing keys remain for compatibility; aliases are canonical in new docs and consumers.

## Hard disambiguation set (protocol-level)

- `INPUT_SIGNAL` -> token-origin contribution before graph propagation.
- `ACTIVATION` -> per-node value after local update.
- `FLOW` -> propagated influence over links.

- `STATIC_WEIGHT` -> dictionary/lexicon static importance.
- `EDGE_WEIGHT` -> topology link strength.
- `COEFFICIENT` -> equation/config_param scalar.

- `COUPLING` -> symmetric relation.
- `INFLUENCE` -> directional effect.
- `CONFLICT` -> opposing coupling.

- `COMPETITION` -> node competition step.
- `SUPPRESSION` -> explicit reduction operator.
- `DAMPING` -> global stabilization.

- `VECTOR` -> raw vector.
- `NORMALIZED_VECTOR` -> sum-normalized vector.
- `PROFILE` -> interpreted profile readout.

- `DOMINANT` -> `argmax(VECTOR)`.
- `STABLE_DOMINANT` -> dominant persists across scale windows.

- `VARIANCE` -> fluctuation.
- `DRIFT` -> directional change.
- `CONSISTENCY` -> persistence.
- `STABILITY` -> derived composite metric only.

- `CYCLE` -> graph cycle.
- `RECURRENCE` -> repeated activation.
- `LOOPABILITY` -> recurrence probability.

- `TENSION_ENERGY` -> opposing-domain energy.
- `ACTIVATION_ENERGY` -> summed activation magnitude.
- `SYSTEM_ENERGY` -> global system energy metric.

- `CONSTRAINTS` -> hard rules (`Σ`).
- `INVARIANTS` -> dynamic rules (`Γ`).
- `POLICY` -> interpretation rules (`Θ`).

- `VIOLATION` -> hard rule break.
- `ANOMALY` -> unusual but admissible.
- `DEVIATION` -> measured difference.

- `VALIDATION` -> correctness check.
- `MEASUREMENT` -> metric extraction.
- `BENCHMARK` -> comparative evaluation.

- `INPUT_CONTEXT` -> local textual input_context.
- `EXTERNAL_CONTEXT` -> non-local external input_context.
- `STRUCTURAL_CONTEXT` -> position in system topology.

- `SEGMENT_SC1`, `SEGMENT_SC2`, `SEGMENT_SC3`, `SEGMENT_SC4` -> scale-bound segment types.

Acceptance rule: each term must map to one meaning, one scope, and one level (`STAGE`/`DOMAIN`/`SCALE`/`METRIC`).

## Extended disambiguation (execution + product vocabulary)

- `EXECUTION_FLOW` -> ordered `STAGE` sequence.
- `ORCHESTRATION` -> triggering/control mode (batch, API, parallel).

- Use explicit verbs only:
  - `TRANSFORM` -> data change
  - `COMPUTE` -> metric calculation
  - `EVALUATE` -> rule application

- Output typing:
  - `OUTPUT_VECTOR` -> raw computed values
  - `SUMMARY` -> final compact output
  - `DIAGNOSTICS` -> extended measurement outputs

- Replace overloaded nouns:
  - `METRIC` (not metric)
  - `ATTRIBUTE` (static property)
  - `CONSTANT`, `CONFIG_PARAM`, `COEFFICIENT` (not config_param)
  - `RAW_TEXT`, `TOKEN_STREAM`, `SEGMENT_SET` (not raw_text)

- Output reliability split:
  - `DETERMINISM` -> same raw_text gives same output
  - `CONSISTENCY` -> cross-scale agreement only
  - `ROBUSTNESS` -> noise resistance

- Temporal behavior split:
  - `DRIFT` -> directional change across scale
  - `OSCILLATION` -> back-and-forth pattern
  - `NOISE` -> random variance

- Replace `alignment`:
  - `MATCHING` -> lexical mapping
  - `FIT` -> projection quality
  - `CORRESPONDENCE` -> structural relation

- `semantic` allowed only for explicit lexical-vs-semantic contrast; otherwise prefer typed noun (`VECTOR`, `PROFILE`, `CONCEPT_ID`, etc.).

- Replace generic nouns:
  - `MEASUREMENT` / `INTERPRETATION` / `DIAGNOSTIC` (not measurement)
  - `ENGINE` / `ARCHITECTURE` / `PRODUCT` (not system)
  - `COMPONENT` / `SERVICE` / `BLOCK` (not component)
  - `TOPOLOGY` / `HIERARCHY` / `STRUCTURE` (only for whole-system reference)

Sanity gate: every term must answer exactly one axis:

- what runs -> `STAGE` / `EXECUTION_FLOW`
- what exists -> `DOMAIN` / `COMPONENT`
- what is measured -> `METRIC` / `VECTOR`
- what is observed -> `SCALE`

SIGNED: Main Developer (Gena) | terminology filter adoption | 2026-03-26 | engine clarity
