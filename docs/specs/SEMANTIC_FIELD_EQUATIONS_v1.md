<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# SEMANTIC_FIELD_EQUATIONS_v1

**Status:** Draft for lock-in (normative family-field core)  
**Scope:** Canonical semantic field dynamics for HESPERIA  
**Layer:** Family-field core with area projection  
**Implementation:** **`hesperia.engine.field_dynamics.equations`** (canonical step/energy/observables; explicit `L_F`, `R_F`, `C`) · `semantic_field_v1` (calibration JSON, E2E bundle, stub matrices **dev-only**) · `assets/calibration/semantic_field_equations_v1.json`

**Purpose:** Unify propagation, resistance, contradiction pressure, source injection, stability, and observables into one closed mathematical specification.

**Related:** [FIELD_MATRIX_BUILDERS_v1.md](FIELD_MATRIX_BUILDERS_v1.md) · [HSPR_CALIBRATION_INDEX_v1.md](HSPR_CALIBRATION_INDEX_v1.md) (HCI grid calibration) · [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) (L0–L10 wire) · [DYNAMICS_EQUATION_INDEX.md](DYNAMICS_EQUATION_INDEX.md) · [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) · [TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md)

---

## 1. Purpose

This specification defines the canonical semantic field equations for HESPERIA.

HESPERIA operates on a bounded semantic topology. Documents inject activation into the topology as source vectors. The field then evolves under:

- diffusion across adjacency,
- resistance/inertia,
- contradiction pressure,
- temporal source weighting,
- bounded convergence.

This spec provides one formal model to align:

- field_dynamics
- propagation
- topology
- KME
- TRIZ
- E2E outputs
- calibration

This document is **normative** for the semantic field layer described herein.

---

## 2. Structural domain

### 2.1 Topology

Let:

- `Areas = 12`
- `FamiliesPerArea = 24`
- `FamilyCount = 288`

Define the family-level semantic graph:

- \( G_F = (V_F, E_F) \)
- \( |V_F| = 288 \)

Each family belongs to exactly one area.

Let:

- \( \mathcal{A}(m) \in \{1,\dots,12\} \) denote the area of family \(m\) (implementation: 0-based indices 0..11)

The area graph is the 12-node icosahedral adjacency graph and acts as the macro-topology.  
The family graph is the true field substrate.

---

## 3. State variables

### 3.1 Family field state

The canonical field state is the family activation vector:

\[
\mathbf{F}(t) \in \mathbb{R}^{288}
\]

where \(F_m(t)\) is the activation of family \(m\) at time \(t\).

By default, runtime uses bounded activation:

\[
F_m(t) \in [0,1]
\]

unless a specific experimental mode explicitly allows unbounded values.

### 3.2 Area projection

\[
A_i(t) = \sum_{m : \mathcal{A}(m)=i} F_m(t)
\qquad
\mathbf{A}(t) \in \mathbb{R}^{12}
\]

Area state is a **projection**, not the primary dynamic substrate.

### 3.3 Document source vectors

Each document \(d\) maps to \(\mathbf{S}^{(d)} \in \mathbb{R}^{288}\), \(S_m^{(d)} \ge 0\).

\[
\mathbf{S}(t) = \sum_{d \in \mathcal{D}(t)} w_d(t)\mathbf{S}^{(d)}
\]

---

## 4. Core matrices

- \(W_F\): symmetric weighted family adjacency, sparse, \(W_{mn} \ge 0\)
- \(L_F = D_F - W_F\) (Laplacian)
- \(R_F = \mathrm{diag}(r_1,\dots,r_{288})\), \(r_m \ge 0\)
- \(C\): symmetric contradiction, \(C_{mn} \ge 0\), \(C_{mm}=0\)

---

## 5. Continuous-time equation

\[
\frac{d\mathbf{F}}{dt}
=
-\alpha L_F \mathbf{F}
-\beta R_F \mathbf{F}
-\gamma \big(\mathbf{F}\odot (C\mathbf{F})\big)
+\delta \mathbf{S}(t)
\]

---

## 6. Discrete runtime (Euler + clip)

\[
\mathbf{F}_{t+1}
=
\mathbf{F}_t
+
\Delta t
\left(
-\alpha L_F \mathbf{F}_t
-\beta R_F \mathbf{F}_t
-\gamma \big(\mathbf{F}_t \odot (C\mathbf{F}_t)\big)
+\delta \mathbf{S}_t
\right)
\]

Production: \(\mathbf{F}_{t+1} \leftarrow \mathrm{clip}(\mathbf{F}_{t+1}, 0, 1)\).

---

## 7. Energy (linearized contradiction form)

\[
E(\mathbf{F})
=
\frac{\alpha}{2}\mathbf{F}^T L_F \mathbf{F}
+
\frac{\beta}{2}\mathbf{F}^T R_F \mathbf{F}
+
\frac{\gamma}{2}\mathbf{F}^T C \mathbf{F}
-
\delta \mathbf{S}^T \mathbf{F}
\]

Nonlinear runtime contradiction term remains energy-inspired.

---

## 8. Temporal document weights

\[
w_d(t) = q_d \exp(-\mu (t - t_d))
\]

---

## 9. Stability

- Numerical: \(\|\mathbf{F}_{t+1} - \mathbf{F}_t\|_2 < \varepsilon\)
- Contradiction: \(\|\mathbf{P}(\mathbf{F}_t)\|_1 < \tau\), \(\mathbf{P} = \mathbf{F}\odot(C\mathbf{F})\)

---

## 10. Observables

| Symbol | Definition |
|--------|------------|
| \(v_t\) | \(\|\mathbf{F}_{t+1}-\mathbf{F}_t\|_2/\Delta t\) |
| \(K_t\) | \(\mathbf{F}_t^T C \mathbf{F}_t\) |
| \(D_t\) | \(\mathbf{F}_t^T L_F \mathbf{F}_t\) |
| \(R_t^{\mathrm{load}}\) | \(\mathbf{F}_t^T R_F \mathbf{F}_t\) |
| \(Q_t\) | \(\mathbf{S}_t^T \mathbf{F}_t\) |
| \(\Sigma_t\) | \(1/(1+\|\mathbf{F}_{t+1}-\mathbf{F}_t\|_2)\) |
| \(\mathbf{A}_t\) | \(\Pi(\mathbf{F}_t)\) |

---

## 11. Production-safe constraints

1. \(\mathbf{F} \in [0,1]^{288}\) in production-safe mode.  
2. \(\mathbf{S} \ge 0\) unless signed-source experimental.  
3. \(C_{mm}=0\).  
4. \(L_F\) from sparse non-negative \(W_F\).  
5. Area projection derived from family field only.  
6. Parameters from calibration registry.

---

## 12. Required E2E outputs

`field_state`, `field_state_next`, `field_energy`, `field_observables`, `field_stability`, `field_area_projection`, `field_source_vector`, `field_timeline` (multi-step).

---

## 13. Minimum implementation contract

- build family adjacency / Laplacian / resistance / contradiction / source  
- step field one timestep · compute energy · observables · convergence · area aggregate  

---

## 14. Out of scope v1

Second-order dynamics, stochastic jumps, signed activations (default), non-Euler integrators, adaptive dt, learned \(C\), auto-fitting loops, tensor interactions, full hex-level canonical dynamics.

---

## 15. Thesis

HESPERIA semantic field dynamics are a bounded family-level field on a fixed semantic graph, driven by document sources, governed by diffusion, resistance, contradiction pressure, and convergence, with area outputs by deterministic projection.
