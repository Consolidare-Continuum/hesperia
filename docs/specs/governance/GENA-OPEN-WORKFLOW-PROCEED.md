<!--
Gena — open workflow proceed log (Hesperia).
-->

# Gena proceed — open workflow (Hesperia)

**Full integration analysis (TRIZ → dynamics, what’s new, env, artifact):**  
→ **[GENA-DYNAMICS-INTEGRATION-ANALYSIS.md](GENA-DYNAMICS-INTEGRATION-ANALYSIS.md)**

---

## 2026-03-18 — TRIZ → dynamics wiring (baseline)

| Item | Action |
|------|--------|
| TRIZ → L7 vector | `triz_signal.py`: **`contradiction_signal_12_from_con_rows`**; **`fetch_triz_contradiction_rows`** (session → clinical graph → `run_triz_analysis_complete`). |
| E2E orchestration | **`e2e_bridge.run_field_dynamics_e2e_artifact`**: single **`c_sig`** into Phase 3 / 2 / 1. |
| Skip TRIZ | **`HESPERIA_FIELD_DYNAMICS_TRIZ=0`** — fast CI, hit-only injection. |
| Calibration | **`assets/calibration/dynamics_parameter_registry.yaml`** |
| VARIABLE_CATALOG | Dynamics env table (TRIZ, XI, phases, hex cap, state path). |

---

## 2026-03-18 — New: Ξ proxy + observability on artifact

| Item | Action |
|------|--------|
| Ξ proxy | **`xi_proxy.apply_xi_to_contradiction_signal`** after base `c_sig`, before phases; **`HESPERIA_FIELD_DYNAMICS_XI`**, **`XI_SCALE`**. |
| Artifact | **`triz_contradiction_meta`**: `xi_proxy_global`, `xi_scale`; **`contradiction_signal_12`** = post-Ξ drive. |
| Registry | v0.5 **`xi_scale`** parameter. |
| Tests | `tests/test_field_dynamics_triz_signal.py`, `tests/test_field_dynamics_xi_proxy.py`. |

---

## Next (open)

| Item | Owner |
|------|-------|
| Full-graph Ξ from KME (not only TRIZ rows) | Ethan + impl |
| Observability / structured logs for TRIZ→dynamics | Product |
| RAG §4.6 (other clone) | As tasked |
