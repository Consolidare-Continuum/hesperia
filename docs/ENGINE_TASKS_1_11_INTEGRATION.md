<!--
HESPERIA — Engine Dynamics
Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
-->

# Engine tasks 1–11 — integration map

Single **wiring index**: what each task delivers, where it lives, how it is verified, and how **Task 11** (system seal) references it.

**Authoritative GO/NO-GO:** `python3 -m tools.system_seal.run_system_seal` → `hesperia.system.system_seal.run_system_seal_gate`.  
**Release bundle:** `python3 tools/release/build_release_audit_v0_5_1.py` writes `release/v0.5.1/system_seal.json` (and full audit tree) and fails if the gate is not `PASS`. Historical v0.5.0: `build_release_audit_v0_5_0.py` → `release/v0.5.0/`.

**Full repo E2E pipe (artifacts + yields):** `python3 -m runtime.pipeline.run_e2e_full_stack` — `run_e2e_all` + product JSON + physics validation + system seal + `run_output_e2e_full_stack_manifest.json` (see `docs/E2E_RUN_ORDER.md`).

| Task | Scope | Primary artifacts / modules | Seal check key (see `system_seal.json`) |
|------|--------|-----------------------------|----------------------------------------|
| **1** | Canonical product pipeline | `runtime.services.analysis_service` → sealed stack → `project_to_public`; `run_e2e_product` | `pipeline` |
| **2** | Hex-causal product signals | `hesperia.engine.product_signals`, sealed path uses hex tensors | `hex_dependency` |
| **3** | Production matrices | `hesperia.engine.matrix_loader`, `assets/matrices/**`, manifest | `production_matrices` |
| **4** | Governed **P_CH** (sparse concept→hex) | `hesperia.engine.pch_loader`, `pch_builder`, `assets/matrices/pch/` | `pch` |
| **5** | Energy-consistent dynamics | `hesperia.engine.energy`, `hex_dynamics`, `hesperia.extensions.dynamics.equations` | `energy` |
| **6** | Concept registry & **A_concept** | `hesperia/ontology/concepts_registry.yaml`, `concept_registry.py`, `e2e_bridge` | `concept` |
| **7** | Hex topology authority | `assets/topology/hex_topology_v1.json`, `hex_topology_authority.py` | `topology` |
| **8** | Calibration protocol & profiles | `specs/calibration_protocol.md`, `assets/calibration/profiles_v1.json`, `VERSION.yaml` `defaults.calibration_profile` | `calibration` |
| **9** | Physics validation harness | `tests/physics_validation/`, `specs/validation_thresholds.json`, `python3 -m tests.physics_validation.run_all` | `validation` |
| **10** | Public schema discipline | `runtime.shipping.schema_guard`, optional `HESPERIA_PUBLIC_SCHEMA_STRICT_KEYS` | `product_truth` (sample analyze + schema + envelope keys) |
| **11** | System seal + release/API hooks | `tools/system_seal/`, `build_release_audit_v0_5_0.py`, `HESPERIA_REQUIRE_SYSTEM_SEAL` | (aggregate `status`) |

## Environment notes

- **Do not** set `HESPERIA_SEMANTIC_FIELD_STUB_MATRICES=1` when running the full system seal or release audit (production matrices must load).
- **Dev-only** uniform hex injection: `HESPERIA_PCH_UNIFORM_INJECTION_DEV=1` (forbidden for production claims).
- **API startup:** optional `HESPERIA_REQUIRE_SYSTEM_SEAL=1` runs the gate when creating the shipping app (`runtime.shipping.api_main`).

## Related docs

- [AGENTS.md](../AGENTS.md) — repo contract + command hygiene  
- [HESPERIA_v0_5_ENGINE_DYNAMICS.md](HESPERIA_v0_5_ENGINE_DYNAMICS.md) — spec ↔ engine master index  
- [tools/system_seal/README.md](../tools/system_seal/README.md) — seal CLI and check list  
- [tests/physics_validation/README.md](../tests/physics_validation/README.md) — Task 9 runner  
