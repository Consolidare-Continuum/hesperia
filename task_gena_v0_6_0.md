# Task Gena Workflow — DLCR-HP v0.6.0

Status: Execution-ready  
Scope: Deterministic Lexical-Concept Resolution + Hex Projection (DLCR-HP)  
Ticket range: `DLCR-001` to `DLCR-020`

## Objective

Deliver a deterministic, auditable execution_flow:

`text -> normalization -> lexical evidence -> concept resolution -> hex projection -> hex dynamics -> family/area aggregation -> outputs`

This plan expands the 12 normative tasks from `task.txt` into 20 Cursor-run tasks, including 3 line-relaxing safety tasks (compatibility, observability, release hardening).

## Delivery rules

- Determinism first: same raw_text + same resources => same output.
- No direct word-to-family default path.
- Every decision path must be auditable.
- Resource changes must trigger regression checks.
- Public output must derive from internal-rich output (not separate semantic path).

## Systems to use

- Runtime/core stack: `core/`, `runtime/`, `schemas/`, `tests/`, `tools/`.
- Validation/testing: schema validation + `pytest`.
- CI/gates: regression checker and release integration.
- Resource assets: `assets/data/engine_dynamics_v060/`.

## Model policy

- Primary engine path: deterministic rules only.
- Optional model usage: offline assistant for lexicon drafting only.
- Prohibited as primary resolver: non-auditable black-box disambiguation.

---

## Execution board (20 tasks)

### `DLCR-001` Create master DLCR spec
- **Size:** M
- **Depends on:** none
- **Artifacts:**
  - `specs/canon/lexical_concept/SPEC__DLCR_HP_Master_v0_6_0.md`
  - `specs/canon/lexical_concept/README.md`
- **Acceptance:**
  - Master spec exists and reflects L0-L6 chain.
  - Hard prohibitions and deterministic rules are explicit.

### `DLCR-002` Register DLCR in canonical index
- **Size:** S
- **Depends on:** `DLCR-001`
- **Artifacts:**
  - `specs/CANONICAL_INDEX.md` update
- **Acceptance:**
  - Canonical index links DLCR spec pack.
  - Naming aligns with repository conventions.

### `DLCR-003` Add Dict A schema
- **Size:** M
- **Depends on:** `DLCR-001`
- **Artifacts:**
  - `schemas/lexical_concept/dict_a.schema.json`
- **Acceptance:**
  - Requires `entry_id`, `surface_form`, `normalized_form`, `match_type`, `candidate_concept_ids`, `priority`, `version`.
  - Supports phrase-first entries and negative patterns.

### `DLCR-004` Implement Dict A validator CLI + tests
- **Size:** M
- **Depends on:** `DLCR-003`
- **Artifacts:**
  - `tools/validate_dict_a.py`
  - `tests/lexical_concept/test_dict_a_schema.py`
- **Acceptance:**
  - Valid packs pass with exit code 0.
  - Invalid packs fail with actionable messages.

### `DLCR-005` Add Dict B schema
- **Size:** M
- **Depends on:** `DLCR-001`
- **Artifacts:**
  - `schemas/lexical_concept/dict_b.schema.json`
- **Acceptance:**
  - Requires `concept_id`, `preferred_label`, `definition`, `family_ids`, `area_ids`, `specificity_rank`, `status`, `version`.
  - Supports anchors and disambiguation clues.

### `DLCR-006` Implement Dict B validator CLI + tests
- **Size:** M
- **Depends on:** `DLCR-005`
- **Artifacts:**
  - `tools/validate_dict_b_dlcr.py`
  - `tests/lexical_concept/test_dict_b_schema.py`
- **Acceptance:**
  - Invalid linkages (missing family/area) are detected.
  - Deprecated/blocked statuses validate correctly.

### `DLCR-007` Add resolver output schema
- **Size:** M
- **Depends on:** `DLCR-001`
- **Artifacts:**
  - `schemas/lexical_concept/resolver_output.schema.json`
- **Acceptance:**
  - Per-span fields include source offsets, candidates, winner, score breakdown, rule trace, unresolved reason.

### `DLCR-008` Add run metadata schema
- **Size:** S
- **Depends on:** `DLCR-007`
- **Artifacts:**
  - `schemas/lexical_concept/run_metadata.schema.json`
- **Acceptance:**
  - Emits engine/resource versions, mode, deterministic signature.

### `DLCR-009` Implement normalization component (L0)
- **Size:** L
- **Depends on:** `DLCR-001`
- **Artifacts:**
  - `core/lexical/normalization.py`
  - `core/lexical/__init__.py` (if needed)
- **Acceptance:**
  - Deterministic canonicalization for case/punctuation/token spans.
  - Original->normalized offset mapping is preserved.

### `DLCR-010` Add normalization golden tests
- **Size:** M
- **Depends on:** `DLCR-009`
- **Artifacts:**
  - `tests/lexical_concept/test_normalization.py`
  - `assets/data/engine_dynamics_v060/baselines/normalization_golden.json`
- **Acceptance:**
  - Golden snapshots remain stable across runs.
  - Drift appears as explicit test diffs.

### `DLCR-011` Implement phrase-first matcher (L1)
- **Size:** L
- **Depends on:** `DLCR-003`, `DLCR-009`
- **Artifacts:**
  - `core/lexical/matcher.py`
- **Acceptance:**
  - Longest-span precedence works.
  - Overlap resolution is deterministic.

### `DLCR-012` Add matcher conflict/negative tests
- **Size:** M
- **Depends on:** `DLCR-011`
- **Artifacts:**
  - `tests/lexical_concept/test_matcher.py`
  - fixtures under `tests/fixtures/lexical_concept/`
- **Acceptance:**
  - Negative patterns block known false positives.
  - Rejected hits are retained in trace.

### `DLCR-013` Implement deterministic resolver core (L2)
- **Size:** L
- **Depends on:** `DLCR-005`, `DLCR-011`
- **Artifacts:**
  - `core/resolver/resolver.py`
  - `core/resolver/score_rules.py`
  - `core/resolver/tiebreaks.py`
- **Acceptance:**
  - Score formula is fixed and versioned.
  - Tie-break order is stable and test-covered.

### `DLCR-014` Add resolver trace + schema validation tests
- **Size:** M
- **Depends on:** `DLCR-007`, `DLCR-013`
- **Artifacts:**
  - `tests/lexical_concept/test_resolver.py`
  - `tests/lexical_concept/test_resolver_output_schema.py`
- **Acceptance:**
  - Resolver output validates against schema.
  - Candidate competition and winner reasons are present.

### `DLCR-015` Build initial concept pack (bounded domain)
- **Size:** L
- **Depends on:** `DLCR-004`, `DLCR-006`
- **Artifacts:**
  - `assets/data/engine_dynamics_v060/dict_a/*.jsonl`
  - `assets/data/engine_dynamics_v060/dict_b/*.jsonl`
  - `assets/data/engine_dynamics_v060/corpora/gold_spans.jsonl`
- **Acceptance:**
  - 100-300 concepts with lexical variants and exclusions.
  - Pack passes both validators.

### `DLCR-016` Implement concept->hex projection (L3)
- **Size:** L
- **Depends on:** `DLCR-013`, `DLCR-015`
- **Artifacts:**
  - `core/hexmap/anchor_registry.py`
  - `core/hexmap/projection.py`
  - `assets/data/engine_dynamics_v060/anchors/concept_hex_anchors.json`
- **Acceptance:**
  - Resolved concept IDs map to deterministic anchors/footprints.
  - Missing anchors surface degradation markers.

### `DLCR-017` Implement hex dynamics primitives (L4)
- **Size:** L
- **Depends on:** `DLCR-016`
- **Artifacts:**
  - `core/hexmap/dynamics.py`
  - `tests/lexical_concept/test_hex_dynamics.py`
- **Acceptance:**
  - Spread/decay/reinforcement are deterministic.
  - Concentration/dispersion/drift features are produced.

### `DLCR-018` Implement hex->family/area adapter (L5)
- **Size:** M
- **Depends on:** `DLCR-017`
- **Artifacts:**
  - `core/hexmap/aggregate.py`
  - `tests/lexical_concept/test_aggregation.py`
- **Acceptance:**
  - Family and area vectors derive from hex state.
  - No raw lexical shortcut in default path.

### `DLCR-019` Add compatibility fallback + degradation flags (relax line)
- **Size:** M
- **Depends on:** `DLCR-018`
- **Artifacts:**
  - runtime service integration updates
  - tests for default-off fallback behavior
- **Acceptance:**
  - Fallback is explicitly marked and non-default.
  - Outputs include degradation flags when fallback used.

### `DLCR-020` Add regression gate + CI/release integration (relax line)
- **Size:** L
- **Depends on:** `DLCR-010`, `DLCR-014`, `DLCR-018`, `DLCR-019`
- **Artifacts:**
  - `tools/check_dlcr_regression.py`
  - CI workflow update
  - release audit/checklist integration notes
  - optional `tools/dlcr_trace_report.py` (observability relax task)
- **Acceptance:**
  - Silent semantic drift is blocked in CI.
  - Release checklist includes DLCR gate status.
  - Trace report supports fast operator debugging.

---

## Dependency summary

Primary chain:

`001 -> 002`  
`001 -> 003 -> 004`  
`001 -> 005 -> 006`  
`001 -> 007 -> 008`  
`001 -> 009 -> 010`  
`003 + 009 -> 011 -> 012`  
`005 + 011 -> 013 -> 014`  
`004 + 006 -> 015`  
`013 + 015 -> 016 -> 017 -> 018 -> 019`  
`010 + 014 + 018 + 019 -> 020`

## Suggested execution waves

- **Wave A (Spec + Schemas):** `001-008`
- **Wave B (Core semantics):** `009-014`
- **Wave C (Data + Hex path):** `015-018`
- **Wave D (Relax + Gates):** `019-020`

## Mapping back to original 12

- Original 1-12 are covered by `DLCR-001` through `DLCR-018`.
- Three relaxed additions:
  - compatibility/degradation (`DLCR-019`)
  - observability trace reporting (`DLCR-020`, optional sub-artifact)
  - release hardening (`DLCR-020`)

## Definition of done (v0.6.0 first ship)

- Default path no longer does direct word->family activation.
- Dict A/Dict B/resolver schemas are validated and versioned.
- Normalization/matcher/resolver are deterministic and audited.
- Concept pack + anchors exist and pass tests.
- Hex projection/dynamics/aggregation produce stable structural outputs.
- Regression gate prevents silent drift.
- Compatibility fallback exists but is explicit and non-default.

