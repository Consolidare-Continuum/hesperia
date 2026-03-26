<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA (HSPR) — CONCEPTS (v1.0)

Purpose: capture the principles that currently govern how the HESPERIA
system is defined, implemented, and evaluated. These principles are
normative for the current repo state and should be treated as constraints
when extending specs or code.

## Scope
- Applies to the CLI core execution_flow (raw_text -> attribution -> geometry ->
  traversal/governance -> output).
- External APIs, services, or LLM wrappers are secondary; they must
  respect the core constraints defined here.

## Core Principles
- Deterministic attribution: word/statement mapping must be stable and
  reproducible without runtime LLM drift.
- Fixed semantic geometry: Areas, Families, hexes, sides, and indexing
  are fixed; only activations and truth weights vary.
- Canonical indexing: #sideId and coordinate mapping are single-source
  of truth; arrays are indexed by #sideId.
- Atomic truth slots: each side is the minimal unit of truth with
  #tau_s in [0,1].
- Evidence-weighted reasoning: regional metrics are functions of #tau_s
  and provenance; stronger evidence carries more weight.
- Temporal dynamics: truth weights and metrics may decay over time using
  explicit, declared functions.
- Governance as constraints: allow / require_correction / forbid flags
  constrain downstream actions and LLM behavior.
- Metrics-first transparency: outputs must surface metrics and rationale
  alongside decisions.
- Referential integrity: schema and geometry identifiers must remain
  consistent across data, code, and documentation.
- Observability: system outputs should be inspectable and auditable, not
  only narrative.
- Versioned evolution: stable specs should not be overwritten; changes
  are introduced as new versions.

## Integration Principles
- Spec alignment: geometry, indexing, attribution, and governance must
  follow the numbered specs.
- Schema alignment: database schema must reflect canonical geometry and
  index ranges.
- LLM separation: external LLMs consume HESPERIA outputs and are bounded
  by HESPERIA metrics, not vice versa.

## Non-Goals (Current State)
- No runtime learning that changes family/area mappings during inference.
- No replacement of the CLI core with microservices by default.
- No implicit changes to geometry or indexing without spec revisions.

## References
- `10_MASTER_SPEC__HESPERIA_v1_0.txt`
- `11_BLUEPRINT__HESPERIA_v4_7_full.txt`
- `12_SPEC__Semantic_Engine_v0_4.txt`
- `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
- `40_POLICY__Loopability_and_traversal.txt`
- `41_POLICY__Operational_additions_v0_1.txt`
- `15_SPEC__Data_and_Schema_v0_1.txt`
