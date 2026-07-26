# Grace workflow packet — Hesperia modularization T1–T10

Date: 2026-03-26  
Project: `hesperia`  
Scope: enforce deterministic semantic kernel + pluggable module layers.

## Task set

1. T1 Freeze Core Boundary — Owner: Marcus (review Liam)  
   Deliverable: `governance/core_boundary_policy.md` + CI boundary check  
   Acceptance: CI fails on violation; current tree passes.

2. T2 Hesperia Language Definitions — Owner: Gena  
   Deliverable: canonical `ctx`, `signal`, `result` definitions in `hesperia/engine/language.py` + schema docs  
   Acceptance: runtime entrypoints share same keys/types; no duplicate vocabularies.

3. T3 Signal Contract Enforcement — Owner: Daniel  
   Deliverable: ingress validator for `signal={family_id:int,strength:float,source:str|None}`  
   Acceptance: invalid signals hard-fail with deterministic error code.

4. T4 Module Interface Lock — Owner: Gena  
   Deliverable: base protocol/class with `name/version/requires/configure/load/preprocess/project/postprocess`  
   Acceptance: all registered modules conform; conformance tests pass.

5. T5 Pure Orchestration Runner — Owner: Liam  
   Deliverable: runner flow locked to `preprocess -> project -> engine.run -> postprocess`  
   Acceptance: no domain logic in runner; deterministic ordering tests pass.

6. T6 Domain Logic Extraction — Owner: Noah (paired with Gena)  
   Deliverable: dict/marker/interpretation logic moved from core to modules (`tfp`, `nlp`, etc.)  
   Acceptance: core has zero domain dictionaries/labels; module tests preserve behavior.

7. T7 Registry + Loader Hardening — Owner: Sophia  
   Deliverable: deterministic registry, dependency resolution, version checks, config loader  
   Acceptance: one-line load works from config; invalid order fails fast.

8. T8 Read-Only Engine Context — Owner: Ava  
   Deliverable: read-only `engine_context` wrapper + mutation guard  
   Acceptance: module writes to core context blocked and logged.

9. T9 Engine API Freeze — Owner: Ethan  
   Deliverable: `engine_api_v1` contract, compatibility policy, versioned tests  
   Acceptance: breaking changes require explicit API version bump; gate enforced.

10. T10 Modularity Governance Gates — Owner: Grace (triage) + Olivia (QA gates)  
    Deliverable: CI gate bundle (boundary checks, determinism hash stability, `ctx/signal/result` schema compliance, no module→core mutation)  
    Acceptance: release seal blocked unless all modular gates are green.

## Dependency order

`T1 -> T2 -> T3 -> T4 -> T5 -> T6 -> T7 -> T8 -> T9 -> T10`
Signed: Grace (Triage) | cursor workflow context | 2026-03-26 | hesperia modularization T1–T10
