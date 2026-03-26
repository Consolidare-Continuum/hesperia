---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CORE-SYSTEM-ARCH
---

# Core system architecture — canonical execution_flow

## 1. Multiscale chain (binding order)

Data flows **concept → hex → family → area** for **structural (Engine Dynamics v0.5)** claims:

| Stage | State | Canonical spec |
|-------|--------|----------------|
| Concept | activation vector **A** (Dict-A scope) | §2 |
| Hex | **H** ∈ ℝ^Nh | [hex_microphysics_canon.md](hex_microphysics_canon.md) |
| Family | **F** ∈ ℝ^Nf, Nf=288 | [family_aggregation.md](family_aggregation.md) + [semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md) |
| Area | **A_area** ∈ ℝ^Na, Na=12 internal | [area_aggregation.md](area_aggregation.md) |

**Option A (canonical):** after microphysics, **F = P_HF H** (or weighted bridge in family_aggregation). **Option B** (coupled hex–family) is reserved and must be explicitly labeled non-baseline.

## 2. Layer responsibilities

- **Concept:** non-negative evidence mass per concept; deterministic aggregation from lexicon / attribution (`core/`, `hesperia.nlp`, `hesperia.ontology`).
- **Hex:** local diffusion, contradiction lift from **C_F**, resistance **R_H**, injection **S_H** = **P_CH A** when structural path is claimed.
- **Family:** semantic field on **G_F** (family graph); **single** dynamics definition in [semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md).
- **Area:** sum of family masses per area; no independent dynamics on areas (projection only).

## 3. Allowed data-flow directions

- **Forward:** concept → hex → family → area → product observables / HSPR / public projection.
- **Forbidden as silent default:** introducing a parallel **F** not reconciled with **P_HF H** when Option A is claimed (drift observable **G_F** per hex microphysics spec).

## 4. Structural constraints

- Topology: **12-node icosahedral** area graph; **10+2** operational vs reserved — see `docs/TOPOLOGY_INVARIANTS.md`.
- **Determinism:** fixed inputs, fixed calibration IDs, fixed registry → identical outputs (Task 1 `VERSION.yaml` trace).

## 5. Product observables

Hex-level narrative metrics (hotspot, propagation, density, etc.) are defined in [product_observables.md](product_observables.md). **Innovation scalar I** is defined only in [../triz/innovation_metrics.md](../triz/innovation_metrics.md).

## 6. Non-binding documentation

`docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`, `docs/HESPERIA_SYSTEM_AWARENESS.md`, and `specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md` **explain** wiring; they **must not** introduce equations absent from Tier-1 specs in `specs/core/`, `specs/dynamics/`, `specs/calibration/`, `specs/triz/`, `specs/schema/`, `specs/system/`.
