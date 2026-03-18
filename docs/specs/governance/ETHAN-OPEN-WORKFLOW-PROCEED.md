# Ethan — open workflow proceed (Hesperia)

**2026-03-18 — Phase 2 shipped**

| Spec ref | Implementation |
|----------|----------------|
| §A.6 Phase 2, **H4** | `f_f` update: injection \(\hat X_f\), intra-area mean, area feedback, \(-\beta_{pf} p_f\) |
| **H5** | `p_family`: area TRIZ signal spread per family-in-area, decay, \(\rho_f\) bleed |
| **H6 coupling** | Area injection = `area_hit_weight`·hit-12 + (1−w)·normalize(\(\sum_{f\in a} f_f\)) |
| L6–L9 | Reuses `step_phase1` after L5 |

**Env:** `HESPERIA_FIELD_DYNAMICS=1` and `HESPERIA_FIELD_DYNAMICS_PHASE2=1` for E2E artifact fields `dynamics_phase: 2`, `family_mass_by_area`, `family_pressure_by_area`.

**2026-03-18 — Phase 3 shipped**

| Item | Implementation |
|------|----------------|
| L4 active subgraph | **Family-proxy** cells (hit-hot families, **cap** / env `HESPERIA_FIELD_DYNAMICS_HEX_CAP`), induced chain adjacency **within area** |
| H2/H3 proxy | `hex_x`, `hex_p` sparse dicts; TRIZ area signal → hex `p` |
| Downstream | `hex_hit_blend`: L5/L6 injections mix hit vs hex-field aggregate |

**Env:** `HESPERIA_FIELD_DYNAMICS_PHASE3=1` (+ `FIELD_DYNAMICS=1`). Stack `L4+L5+L6` or `L4+L6`.

**2026-03-18 — Phase 4 shipped**

| Item | Implementation |
|------|----------------|
| L8 §H8 proxy | Consecutive **active family-proxy** runs per area → Mass, Density, Radius, **Gravity**, **Velocity** vs `l8_cluster_mass_prev` |
| Coupling | **`gravity_epsilon`** biases area + family injections; family uses 0.85× ε |
| Fronts | **`l8_fronts_per_area`** (chain \|Δx\| > `tau_front`) |
| No PHASE3 | **Ephemeral** hex from hits (`ephemeral_cap`) for clusters only |

**Env:** `HESPERIA_FIELD_DYNAMICS_PHASE4=1`. Artifact: `l8_clusters`, `dominant_l8_cluster`.

**2026-03-18 — Ξ proxy (L3 → L7 drive)**

| Item | Implementation |
|------|----------------|
| TRIZ topology → tension | `xi_proxy.py`: `xi_proxy_global`, per-area profile from row scores / `area_a` / `area_b` |
| L7 boost | `apply_xi_to_contradiction_signal` in `e2e_bridge` **after** base `c_sig`, **before** Phase 3→2→1 |
| Env | `HESPERIA_FIELD_DYNAMICS_XI=1` (default), `HESPERIA_FIELD_DYNAMICS_XI_SCALE` (default 0.14) |
| Close-out | [REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md](REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md) |

**A.6 phases 1–4 + Ξ proxy shipped.** Next: full-graph **Ξ** from KME, or true hex-lattice H7/H8 when `Z_ih` wired.
