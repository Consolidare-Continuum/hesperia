# Operational checklist (pre–survival run)

Casual check of active tree (excluding `legacy/`, `archive/`) to confirm everything is wired and runnable.

**Date:** 2026-03-14  
**Scope:** core, runtime, sphere, hesperia, lexicon, tools (no legacy/archive)

---

## 1. Entry points & imports

| Check | Status |
|-------|--------|
| `runtime.pipeline.run_e2e_all` | OK |
| `runtime.pipeline.run_l1_through_l9` | OK |
| `runtime.pipeline.analyze` | OK |
| `runtime.pipeline.r1_r4_pipeline` | OK |
| `runtime.services.analysis_service` | OK (moved from core; see below) |
| `core.projection` | OK |
| `sphere.pipeline.pipeline_runner` | OK |
| `sphere.pipeline.layer_registry` | OK |
| `core.layers` (L1–L9) | OK |
| `core.attribution.structural` | OK |
| `hesperia.engine.kme` | OK |
| `runtime.shipping.schema_guard` | OK |
| `runtime.artifact_writer.writer` | OK |
| All core layers (layer_1 … layer_9) | OK |
| Sphere engines (propagation, shadow, logic, interpretation, usf, dynamism, guards, metrics, geometry) | OK |

---

## 2. Architecture boundaries

| Rule | Status |
|------|--------|
| core does not import sphere | OK (analysis_service moved to runtime) |
| core does not import runtime | OK |
| sphere does not import runtime | OK |

**Change made:** `core/services/analysis_service.py` was the only core module importing sphere. It was moved to `runtime/services/analysis_service.py`. All callers (run_l1_through_l9, run_e2e_all, shipping CLI/API, runners, tests) now use `runtime.services.analysis_service`. Core no longer depends on sphere.

---

## 3. KME / domain wiring

| Item | Status |
|------|--------|
| `core.domain` re-exports from `hesperia.engine.kme` | OK |
| `sphere.pipeline.pipeline_runner` uses `core.domain.bridge`, `loader`, `pipeline`, `models` for domain_metrics | OK |
| Tests use `core.domain` for domain tests | OK |

---

## 4. Shipping & sealed surface

| Item | Status |
|------|--------|
| `runtime/shipping/cli_main.py` (analyze, compare, batch-analyze) | OK, uses `runtime.services.analysis_service` |
| `runtime/shipping/api_main.py` | OK, uses `runtime.services.analysis_service` |
| `runtime/shipping/schema_guard` | OK |
| `runtime/shipping/version_info.py` | OK (generated) |

---

## 5. Tests

| Suite | Result |
|-------|--------|
| Full test suite (`pytest tests/`) | 378 passed |
| Architecture (`test_layer_dependencies`) | 3 passed |
| E2E flows (`test_e2e_flows`) | 7 passed |
| Sealed runtime regression (`test_sealed_runtime_regression`) | 7 passed |

---

## 6. E2E runner

| Check | Status |
|-------|--------|
| `python3 -m runtime.pipeline.run_e2e_all` | OK, **19** baseline JSON under `assets/artifacts/e2e/` (+ optional field dynamics); `docs/E2E_RUN_ORDER.md`, `E2E_OUTPUTS.md` |

---

## 7. File areas (casual)

- **core/** — Layers 1–9, attribution, contracts, domain (KME re-exports), math, policy, projection, propagation, services (report only), stability, topology. No sphere/runtime imports.
- **runtime/** — Pipeline runners, shipping CLI/API, artifact_writer, dossier, provenance, **services** (analysis_service). Imports sphere and core as intended.
- **sphere/** — Pipeline runner, layer registry, propagation, shadow, logic, interpretation, USF, dynamism, guards, metrics, geometry, prolog_logic, diagnostics. Imports core only.
- **hesperia/engine/kme/** — Primitives, derived, fingerprint, profiling, validation, pipeline, loader, bridge, etc. Used via core.domain and sphere pipeline (domain_metrics).
- **lexicon/** — Build and validation scripts; not on hot path of run_e2e_all.
- **tools/** — Diagnostics, domain_constants_extract, sealing_scan, visualization; not required for e2e.

---

## Summary

- All critical imports and entry points load.
- Architecture boundaries hold: runtime → sphere → core; no core → sphere.
- E2E runner and full test suite pass.
- One structural fix applied: analysis service moved from core to runtime so the layer rule is satisfied and the stack is ready for the survival run.
