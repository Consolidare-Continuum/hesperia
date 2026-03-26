# Ethan — Main Engine conceptual math map (B)

Date: 2026-03-26  
Scope: Main engine only (`hesperia/engine`, `runtime/services`, `runtime/execution_flow`), no session/clinical research workflows.

## 1) Canonical executable path

`runtime.services.analysis_service.run_structural_analysis` ->
`hesperia.engine.multiscale_product_bridge.build_structural_internal_from_multiscale` ->
`hesperia.engine.sealed_multiscale_stack.run_sealed_multiscale_stack` ->
`hesperia.engine.projection.project_to_public`

This is the only path for main-engine conceptual math workflows.

## 2) Conceptual-math layers mapped to modules

- **L0 Raw_text normalization and lexical evidence**
  - `hesperia.engine.lexical_concept.execution_flow`
  - Role: deterministic marker-to-concept evidence extraction and stabilizing controls.

- **L1 Concept state to hex embedding**
  - `hesperia.engine.hex_matrix_builders`
  - `hesperia.engine.pch_loader`, `hesperia.engine.pch_builder`
  - Role: project concept activations into the hex substrate (`A_hex`).

- **L2 Local hex microphysics update**
  - `hesperia.engine.hex_dynamics`
  - `hesperia.engine.energy`
  - Role: one-step or controlled-step field evolution over hex rows with bounded energy behavior.

- **L3 Hex-to-family/area aggregation (readout only)**
  - `hesperia.engine.hex_family_bridge`
  - `hesperia.engine.sealed_multiscale_stack` (area roll-up)
  - Role: aggregate for readout/projection; not used as causal raw_text in input_signal formulas.

- **L4 Product input_signal operators (hex-causal)**
  - `hesperia.engine.product_signals`
  - `hesperia.engine.hspr_index`
  - Role: contradiction pressure, propagation strength, density, entropy, innovation, HSPR from `A_hex`.

- **L5 Observability / explainability / traces**
  - `hesperia.engine.output_trace`
  - `hesperia.engine.explainability`
  - `hesperia.engine.observables`
  - Role: auditable input_signal/state outputs and stable reporting payloads.

- **L6 Projection and schema enforcement**
  - `hesperia.engine.projection.public_projection`
  - `hesperia.engine.projection.schema_enforcer`
  - `hesperia.engine.projection.sanitizer`
  - Role: produce public-safe contracts from internal state.

- **L7 Release and anomaly gating**
  - `hesperia.engine.output_anomalies`
  - `hesperia.engine.calibration_release_gate`
  - Role: deterministic pass/fail checks and operational envelope signaling.

## 3) Core invariants for conceptual math workflows

- **I1 Hex-causal signals**: product input_signal formulas consume `A_hex` tensors, not pre-aggregated family vectors as causal source.
- **I2 Determinism**: same text + same assets + same profile => same payload hash for stable sections.
- **I3 Bounded outputs**: no NaN/Inf in hex state, signals, and projected payload.
- **I4 Schema closure**: public outputs must pass schema enforcement.
- **I5 Separation**: no research/clinical/session orchestration in canonical main-engine workflow.

## 4) Current gaps to close next

- Introduce a single main-engine workflow runner with deterministic double-run check and artifact manifest.
- Replace TFP-named gate semantics with engine-neutral gate profile naming.
- Add explicit invariant report artifact (`determinism`, `bounds`, `schema`) for each workflow run.

SIGNED: Engineer (Ethan) | main engine conceptual math map | 2026-03-26 | B mapping
