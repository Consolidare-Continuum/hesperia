<!--
HESPERIA — Reference Architecture Definition (RAD)
Grace-led team task — implement Ethan semantic field dynamics spec (current).
-->

# Task: Grace + team — implement Ethan dynamics spec (L0–L10, phased)

**Added:** 2026-03-18 · **Status:** OPEN — **first tranche RECEIVED by Grace (2026-03-18)** — see §Grace receipt below. Further scope: full-graph Ξ, L10 public slice, true hex closure \(Z_{ih}\).  
**Purpose:** Coordinate a **single implementation program** aligned with **[ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md)** (v3, “today’s” canonical target): stateful discrete-time dynamics **on top of** the existing measurement pipeline — **without** replacing L1–L9 propagation or KME/TRIZ.

**Owners**

| Role | Responsibility |
|------|----------------|
| **Grace** | Sprint boundaries, acceptance criteria per phase, triage vs [GRACE_TRIAGE_REPORT.md](../triage/GRACE_TRIAGE_REPORT.md), unblock cross-module deps |
| **Ethan (spec)** | Clarifications on H0–H9 vs extended IDs, L-layer ordering, public projection (L10) |
| **Implementation** | Code + tests + deterministic replay |
| **Calibration steward** | Class B parameter registry seeding per [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md); path: `assets/calibration/dynamics_parameter_registry.yaml` (when live) |

**Hard rules (non-negotiable)**

1. **Topology:** [TOPOLOGY_INVARIANTS.md](../../TOPOLOGY_INVARIANTS.md) — 12 areas, 72k operational hex budget; **no full 72k update per step** until product explicitly requires Phase D (Ethan Part B §9).  
2. **Public surface:** L10 — **strip reserved internals**; same doctrine as static projection.  
3. **Phasing:** Enable **one Ethan phase at a time** (§A.6); static single-document run = **one dynamics step** or degenerate state.  
4. **Determinism:** Same inputs + same prior `State(t)` + same Θ ⇒ identical `State(t+1)` (replay tests).

---

## Progress

| Date | Note |
|------|------|
| 2026-03-18 | **Phase 1 core:** `hesperia.extensions.dynamics` — `FieldDynamicsState`, `Phase1Theta`, `step_phase1()` (L6+L7+L9 + L2 stub). Icosahedral diffusion via `sphere.topology`. Tests: `tests/test_field_dynamics_phase1.py`. Opt-in: `HESPERIA_FIELD_DYNAMICS=1` (helper `field_dynamics_enabled()`). |
| 2026-03-18 | **E2E wire:** With flag set, `run_e2e_all` writes `run_output_e2e_field_dynamics.json` + persists `field_dynamics_state.json` in out-dir. See `docs/E2E_RUN_ORDER.md` step 10. |
| 2026-03-18 | **Gena:** TRIZ → `contradiction_signal_12`; registry + VARIABLE_CATALOG. |
| 2026-03-18 | **Ethan proceed:** **Phase 2** — `step_phase2`, `Phase2Theta`, `f_f`/`p_family` (288), L6 blend; **`HESPERIA_FIELD_DYNAMICS_PHASE2=1`**. |
| 2026-03-18 | **Phase 3** — L4 family-proxy hex, **`PHASE3`**. |
| 2026-03-18 | **Phase 4** — L8 clusters, gravity coupling, fronts, **`PHASE4`**. **A.6 stack complete.** |
| 2026-03-18 | **Ξ proxy** — `xi_proxy.py` + E2E bridge; **`HESPERIA_FIELD_DYNAMICS_XI`** / **`XI_SCALE`**; [REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md](REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md). |
| 2026-03-18 | **Gena:** integration analysis — [GENA-DYNAMICS-INTEGRATION-ANALYSIS.md](GENA-DYNAMICS-INTEGRATION-ANALYSIS.md); proceed log updated. |

---

## Grace receipt — Ethan + Gena (done to this checkpoint)

**Received by Grace:** **2026-03-18**

| Source | Accepted as delivered |
|--------|------------------------|
| **Ethan / implementation** | A.6 **Phases 1–4** in `hesperia.extensions.dynamics`; E2E optional artifact; state persistence; **Ξ proxy** (TRIZ-row tension → boosted L7 drive); [REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md](REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md); [ETHAN-OPEN-WORKFLOW-PROCEED.md](ETHAN-OPEN-WORKFLOW-PROCEED.md); [DYNAMICS_EQUATION_INDEX.md](../DYNAMICS_EQUATION_INDEX.md) updated. |
| **Gena** | TRIZ → `contradiction_signal_12` + `fetch_triz_contradiction_rows`; wiring in `e2e_bridge`; **VARIABLE_CATALOG** + calibration registry (incl. **xi_scale**); [GENA-DYNAMICS-INTEGRATION-ANALYSIS.md](GENA-DYNAMICS-INTEGRATION-ANALYSIS.md); [GENA-OPEN-WORKFLOW-PROCEED.md](GENA-OPEN-WORKFLOW-PROCEED.md). |

**Grace notes:** Hard rules (topology cap, determinism, flag-gated E2E) respected. **Explicit non-goals for this tranche:** full-graph Ξ from KME; full 72k hex; L10 production API projection — remain **next program items**, not blockers on receipt.

**Formal check:** [../triage/GRACE_CHECK_AGAINST_TASKED.md](../triage/GRACE_CHECK_AGAINST_TASKED.md) (updated to match this receipt).

---

## 0. Preconditions (team kickoff)

| # | Deliverable | Owner |
|---|-------------|-------|
| 0.1 | Read **Ethan v3** Part A + Part B §9–§13 | All |
| 0.2 | **[DYNAMICS_EQUATION_INDEX.md](../DYNAMICS_EQUATION_INDEX.md)** — maintained alongside code (update if equations move) | Ethan + impl lead |
| 0.3 | Module home agreed: e.g. `hesperia/extensions/dynamics/` (or `core/` subpackage) — **new**, no legacy edits | Grace + impl |
| 0.4 | Stub **registry** path documented; expand from [dynamics_parameter_registry.example.yaml](../calibration/dynamics_parameter_registry.example.yaml) as phases land | Calibration steward |

---

## Phase 1 — Minimal closed loop (Ethan §A.6 Phase 1)

**Wire:** L0 (time / batch) + **L2** concept state + **L6** area state + **L7** area contradiction \(p_a\) + **L9** guards/stability.

**Implementation goals**

- **State container:** versioned struct (e.g. `FieldDynamicsState`: `t`, `c_i` or summary, `a_a`, `p_a`, optional Stab).  
- **Step API:** `step(state, pipeline_snapshot_or_injection, theta) -> state'` where injection can be **current run activations** mapped to concepts/areas.  
- **Integration point:** After a normal Hesperia run, **one** dynamics update; persist state only where product requires (file/DB optional in Phase 1 — in-memory + JSON fixture tests sufficient).  
- **L9:** boundedness, no NaN, stability metric (compact **H9**-style delta on `a_a`).  
- **Tests:** golden vectors: 2–3 timesteps, fixed Θ, bit-identical state serialization.

**Grace acceptance:** Phase 1 merged only if tests pass and **no** change to default E2E behavior unless `HESPERIA_FIELD_DYNAMICS=1` (or equivalent flag) is documented.

---

## Phase 2 — Family layer (Ethan Phase 2)

**Wire:** **L5** — family field \(f_f\), family contradiction \(p_f\), coupling to L6/L7.

**Goals:** \(\hat{X}_f\) from compressed path first (family aggregates from **existing** placement, not full hex); wire compact **H4, H5** (family + family \(p\)).

**Grace acceptance:** Family state dimensions match **288 families** (operational + reserved policy per topology); public export still obeys L10.

---

## Phase 3 — Active hex subgraph (Ethan Phase 3 / Part B Phase C)

**Wire:** **L4** — \(x_h\), \(p_h\) on **active hex set only** (Ethan §9): closure over activated concepts via \(Z_{ih}\), not full grid.

**Goals:** Adjacency \(H_{hk}\) on active subgraph; hex diffusion and contradiction pockets; optional **extended H7** (gradient/front) on active set only.

**Grace acceptance:** Worst-case active set size **capped** by config; performance benchmark documented.

---

## Phase 4 — Cluster / L8 (Ethan Phase 4)

**Wire:** **L8** — hex-native cluster gravity, narrative attractors, fronts (extended **H8**).

**Goals:** Build on Phase 3 hex state; deterministic cluster IDs or stable ordering for tests.

**Grace acceptance:** Product-facing narrative optional; core is **reproducible** metrics.

---

## Cross-cutting workstreams (parallel, low conflict)

| Stream | Work |
|--------|------|
| **L10 schema** | Time-aware JSON fields: `state_t`, `delta_t`, windows (Ethan §A.3 L10) |
| **L3** | Feed \(\Xi\) / graph tension into L7/L9 where Phase 1 already uses **H8**-style scalars |
| **TRIZ** | L7 resolution term \(R_a\) — real TRIZ signals from `hesperia/extensions/triz` when Phase 1–2 touch contradiction |
| **Docs** | Update [HESPERIA_VARIABLE_CATALOG.md](../../HESPERIA_VARIABLE_CATALOG.md), [E2E_RUN_ORDER.md](../../E2E_RUN_ORDER.md) when dynamics artifact ships |

---

## Deliverables summary

1. **Phase 1** — state + step + L2/L6/L7/L9 + tests + feature flag.  
2. **Phase 2** — family dynamics + tests.  
3. **Phase 3** — active-hex L4 + tests + perf cap.  
4. **Phase 4** — L8 cluster metrics + tests.  
5. **Ongoing** — `DYNAMICS_EQUATION_INDEX.md` + calibration registry growth.  
6. **Close-out report** — [REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md](REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md) (phases 1–4 + Ξ proxy, Θ, gaps).

---

## References

| Doc | Use |
|-----|-----|
| [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) | Source of truth |
| [DYNAMICS_EQUATION_INDEX.md](../DYNAMICS_EQUATION_INDEX.md) | H0–H9 ↔ extended ↔ phases |
| [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) | Class A/B/C, scenarios |
| [HESPERIA_DEPENDENCY_GRAPH.md](../../HESPERIA_DEPENDENCY_GRAPH.md) | Where static pipeline lives |
| [GRACE_TRIAGE_REPORT.md](../triage/GRACE_TRIAGE_REPORT.md) | Prior triage decisions |
| [TRIAGE_TASK_GRACE.md](../TRIAGE_TASK_GRACE.md) | Corpus scope |

---

**Grace check (tasked vs delivered):** [../triage/GRACE_CHECK_AGAINST_TASKED.md](../triage/GRACE_CHECK_AGAINST_TASKED.md)

---

*Grace task — team implementation of Ethan dynamics spec (2026-03-18).*
