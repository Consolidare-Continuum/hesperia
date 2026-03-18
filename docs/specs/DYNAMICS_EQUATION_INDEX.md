<!--
HESPERIA — RAD. Companion to ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md
-->

# Dynamics equation index (compact ↔ extended ↔ L-layer)

**Canonical spec:** [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) (v3). This file is the **single cheat sheet** for implementers.

**Family-field closed form (parallel spine):** [SEMANTIC_FIELD_EQUATIONS_v1.md](SEMANTIC_FIELD_EQUATIONS_v1.md) — single \(\mathbf{F}\in\mathbb{R}^{288}\) equation with \(L_F,R_F,C,\mathbf{S}\); calibration `assets/calibration/semantic_field_equations_v1.json`; module `hesperia.engine.field_dynamics.semantic_field_v1`.

---

## Compact wire (Part A §A.4) — implementation order

| ID | Name | Primary L-layers |
|----|------|------------------|
| **H0** | Input injection \(I_i\) | L0→L2 |
| **H1** | Concept \(c_i\) | L2 |
| **H2** | Hex field \(x_h\) | L4 |
| **H3** | Hex contradiction \(p_h\) | L4 |
| **H4** | Family \(f_f\) | L5 |
| **H5** | Family contradiction \(p_f\) | L5/L7 |
| **H6** | Area \(a_a\) | L6 |
| **H7** | Area contradiction \(p_a\) | L7 |
| **H8** | Global tension \(\Xi\) | L3/L8 |
| **H9** | Stability Stab | L9 |

---

## Extended lattice IDs (Part B §6, §13–14)

Use **extended** IDs when splitting **resolution**, **gradients**, **cluster gravity** into separate units.

| Ext | Role | Maps to compact A-row |
|-----|------|------------------------|
| H1 | Concept activation | **H1** |
| H2 | Hex activation | **H2** |
| H3 | Hex contradiction | **H3** |
| H4 | Family from hex | **H4** |
| H5 | Area propagation | **H6** (area state) |
| H6 | Resolution \(R_h,R_f,R_a\) | feeds **H3, H5, H7** |
| H7 | Gradient / front / turbulence | L4/L8 detail |
| H8 | Hex cluster gravity | L8 |
| H9 | \(\Xi\) + stability | **H8, H9** |

**Note:** Extended **H5** = area equation; compact **H5** = family **\(p_f\)**. Always disambiguate by **“compact H5”** vs **“extended H5 (area)”**.

---

## Phased implementation (Ethan §A.6)

| Phase | Layers enabled | Part B alignment |
|-------|----------------|------------------|
| **1** | L0, L2, L6, L7 (area \(p_a\)), L9 | ≈ compressed area + contradiction |
| **2** | + L5 **H4/H5** (`f_f`, \(p_f\)) + L6 blend **ĤF_a** | **Implemented:** `step_phase2`, env `HESPERIA_FIELD_DYNAMICS_PHASE2=1` |
| **3** | + L4 active subgraph (**family-proxy**, capped) | **`step_phase3`**, `PHASE3=1` |
| **4** | + L8 gravity, fronts, velocity | **`PHASE4=1`**, `phase4` module |
| **Ξ proxy** | TRIZ rows → tension scalar + per-area boost of **L7** `c_sig` before L4–L6 | **`xi_proxy.py`**, `HESPERIA_FIELD_DYNAMICS_XI` |

---

## Cross-ref

- **L0–L10 definitions:** Ethan §A.2–A.3  
- **Calibration knobs:** [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md)  
- **Dependency layers vs L:** [HESPERIA_DEPENDENCY_GRAPH.md](../HESPERIA_DEPENDENCY_GRAPH.md) (crosswalk)
