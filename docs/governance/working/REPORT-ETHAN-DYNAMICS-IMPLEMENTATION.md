# Report — Ethan semantic field dynamics (implementation close-out)

**Date:** 2026-03-18 · **Spec:** [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) · **Task:** [TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md](TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md)

One-page summary of what shipped in-code vs A.6 phases and known gaps.

---

## Phase 1 — L6 / L7 / L9 (+ L2 stub)

| Item | Status |
|------|--------|
| Module | `hesperia.extensions.dynamics` — `FieldDynamicsState`, `Phase1Theta`, `step_phase1` |
| Topology | Icosahedral neighbor diffusion (`sphere.topology`) |
| Flag | `HESPERIA_FIELD_DYNAMICS=1` |
| Tests | `tests/test_field_dynamics_phase1.py` |
| Θ | `lambda_a`, `gamma_f`, `gamma_q`, `gamma_p`, `mu_a`, `delta_a`, `rho_a`, `lambda_c`, `alpha_in` (registry) |

---

## Phase 2 — L5 families + L6 blend

| Item | Status |
|------|--------|
| API | `step_phase2`, `Phase2Theta` — `f_f`, `p_family` (288), area blend |
| Flag | `HESPERIA_FIELD_DYNAMICS_PHASE2=1` |
| Tests | `tests/test_field_dynamics_phase2.py` |
| Θ | `lambda_f`, `beta_x`, `beta_intra`, `beta_area`, `beta_pf`, `mu_f`, `delta_f`, `rho_f`, `area_hit_weight` |

---

## Phase 3 — L4 family-proxy hex

| Item | Status |
|------|--------|
| API | `step_phase3` — sparse `hex_x` / `hex_p`, cap |
| Flag | `HESPERIA_FIELD_DYNAMICS_PHASE3=1`, `HESPERIA_FIELD_DYNAMICS_HEX_CAP` |
| Tests | `tests/test_field_dynamics_phase3.py` |
| Θ | `hex_cap`, `lambda_h`, `theta_c`, `theta_d`, `theta_p`, `mu_h`, `delta_h`, `rho_h`, `hex_hit_blend` |

---

## Phase 4 — L8 cluster proxy

| Item | Status |
|------|--------|
| API | `step_phase4` in `phase4.py` — clusters, gravity, fronts, ephemeral hex if no Phase 3 |
| Flag | `HESPERIA_FIELD_DYNAMICS_PHASE4=1` |
| Tests | `tests/test_field_dynamics_phase4.py` |
| Θ | `gravity_epsilon`, `tau_front`, `ephemeral_cap` |

---

## Cross-cutting: TRIZ → L7 + Ξ proxy (L3 → L7 drive)

| Item | Status |
|------|--------|
| TRIZ rows → `c_sig` | `triz_signal.py` → `e2e_bridge` |
| **Ξ proxy** | `xi_proxy.py`: tension scalar + per-area profile from row scores/areas; boosts `contradiction_signal_12` before phases |
| Flags | `HESPERIA_FIELD_DYNAMICS_TRIZ`, **`HESPERIA_FIELD_DYNAMICS_XI`**, **`HESPERIA_FIELD_DYNAMICS_XI_SCALE`** |
| Artifact meta | `xi_proxy_global`, `xi_scale` merged into `triz_contradiction_meta` |
| Tests | `tests/test_field_dynamics_xi_proxy.py`, `tests/test_field_dynamics_triz_signal.py` |

**Gap (explicit):** Full Ξ = Σ K_ij c_i c_j − ω Σ W_ij c_i c_j on graph state is **not** implemented; proxy is TRIZ-topology only.

---

## E2E artifact

| Item | Status |
|------|--------|
| Optional 10th JSON | `run_output_e2e_field_dynamics.json` when `HESPERIA_FIELD_DYNAMICS=1` |
| Order | [E2E_RUN_ORDER.md](../../E2E_RUN_ORDER.md) |
| Registry | `assets/calibration/dynamics_parameter_registry.yaml` (v0.5+ incl. `xi_scale`) |

---

## Known gaps (next tranche)

1. True hex-lattice **H7/H8** when `Z_ih` / full active closure is wired.  
2. Full **L3 Ξ** from KME/graph, not only TRIZ proxy.  
3. L10 time-aware public projection fields (schema pass).  
4. Calibration search / profiles per [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) (registry seeded, search tooling TBD).
