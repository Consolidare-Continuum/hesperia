# SPEC: Deterministic Lexical-Concept Resolution + Hex Projection

Version: `v0.6.0-draft1`  
Status: Proposed (canonical draft)  
ID: `HES-SPEC-DLCR-HP`

## Purpose

Define a deterministic subsystem that converts raw text into audited concept
evidence before any family or area activation.

Required chain:

`text -> normalization -> lexical evidence -> concept resolution -> hex projection -> hex dynamics -> family/area aggregation -> interpretation`

Forbidden default shortcut:

`text -> family guess`

## Core invariants

1. Same raw_text + same resources => same output.
2. Phrase-first matching, then token fallback.
3. Resolver decisions are auditable per span.
4. Concept IDs activate hex first; family/area are projections.
5. Resource changes must be regression-tested.

## Layer stack (normative)

- L0 Raw_text Normalization
- L1 Lexical Evidence (Dict A)
- L2 Concept Resolution (Dict B + tie-breaks)
- L3 Hex Projection
- L4 Hex Dynamics
- L5 Structural Aggregation (hex->family->area)
- L6 Interpretation / reporting

## Dict roles

- Dict A proposes candidates from lexical evidence.
- Dict B defines concept identity and structural linkage.
- Dict A must not directly classify family or area.

## Output classes

- Internal-rich audit output (full trace, candidate scores, winner reasons).
- Public-safe output (deterministic summary derived from internal output).

## Required schema set

- `schemas/lexical_concept/dict_a.schema.json`
- `schemas/lexical_concept/dict_b.schema.json`
- `schemas/lexical_concept/resolver_output.schema.json`
- `schemas/lexical_concept/run_metadata.schema.json`

## Acceptance for first ship

- No default direct word->family path.
- Dict A/B resources validate.
- Resolver output validates and contains per-span trace.
- Concept evidence maps to hex before family/area aggregation.
- Regression gate blocks silent semantic drift.

