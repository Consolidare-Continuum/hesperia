# REPO PATH MIGRATION PLAN v1

**Status:** Active  
**Purpose:** Real separation so public package/export surface no longer cohabits with clearly internal reflective modules. First pass moved or reclassified.

---

## 1. Priority Candidates (Reflective → Internal)

| Candidate | Current location | Target / reclassification |
|-----------|------------------|---------------------------|
| Math layer modules | core/layers/layer_1.py … layer_9.py | Keep in core/layers; **reclassify** as internal-only. No move; document as sealed. |
| Pipeline orchestration | sphere/pipeline/pipeline_runner.py | Internal. Entry from runtime must go via core.services.analysis_service. |
| Bridge helpers | core/domain/bridge.py, hesperia/engine/kme/bridge.py | Internal. No public import. |
| Topology helpers | core/topology/invariant_catalog.py | Internal. reserve_loader used only behind projection. |
| Debug writers | (any future layer-dump writers) | Must live under internal_debug guard; write via write_internal_json only. |
| Spec-heavy docs | docs/specs/history, docs/specs/schema (internal-facing) | **Exclude from release bundle.** docs/internal/ and docs/specs/ (selected) = internal. |

---

## 2. First Pass Actions

- **core/layers, core/math, core/domain (bridge), core/topology:** Marked as internal in PACKAGE_BOUNDARY_POLICY. No physical move; import boundary enforced for runtime/api, runtime/public_reports, runtime/artifact_writer.
- **runtime/pipeline:** Runners (run_sphere_math_values, run_l1_l2, run_l1_l2_l3, run_reference_pipeline) **patched** to use central artifact writer and projection. They still call core.layers directly; migration to core.services.analysis_service is **next pass** so pipeline entry points become thin wrappers that call the façade.
- **docs/internal/:** Already created; MATH_LAYER_REGISTRY and PIPELINE_LAYER_REGISTRY live here. **Excluded from release bundle** (see RELEASE_CONTENT_POLICY).
- **docs/governance/:** Policies stay in repo; **release bundle** may include a subset (public-facing policies only) or exclude governance from distributed package per RELEASE_CONTENT_POLICY.

---

## 3. Done Condition

Public package/export surface no longer cohabits with clearly internal reflective modules: internal modules are documented and import-checked; pipeline runners use central writer and projection; internal docs are excluded from release.
