# HC-01 — B↔A validation envelope

**Status:** MVP schema + gold fixtures landed. Wire to resolver pipeline in a follow-up PR.

## Alignment

- **Resolver contract:** `schemas/lexical_concept/resolver_output.schema.json` supplies span-level `candidate_concepts`, scores, `winning_reason_codes`, `rule_trace`.
- **Validation envelope:** `schemas/lexical_concept/ba_validation_envelope.schema.json` aggregates **per (concept_id, segment_id)** support from link types (exact / alias / fuzzy) and applies policy thresholds (config in calibration bundle — not hardcoded here).

## Gold fixtures

| Fixture | Path |
|--------|------|
| Valid mixed support | `tests/fixtures/ba_validation/seg_001.json` |
| Reject fuzzy-only | `tests/fixtures/ba_validation/seg_002.json` |
| Anchor-heavy | `tests/fixtures/ba_validation/seg_003.json` |

`SIGNED: Noah (task HC-01) | provenance envelope MVP | 2026-03-27 | Hesperia repo`
