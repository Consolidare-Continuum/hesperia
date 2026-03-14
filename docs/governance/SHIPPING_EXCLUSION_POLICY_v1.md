# SHIPPING EXCLUSION POLICY v1

**Status:** Active  
**Purpose:** Define what the shipped runtime must **never** contain. Applies to both the Linux CLI binary (Nuitka) and the Linux API container (Docker). Build and packaging must enforce these exclusions.

---

## 1. Mandatory exclusions

The following must **never** be included in the shipped runtime (binary or container image).

| Category | Must exclude | Reason |
|----------|--------------|--------|
| **Internal docs** | docs/internal/ (MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY, internal-only specs) | Reveals layer count, transformation chain, method. |
| **Specs history** | docs/archive/specs_history/, draft governance that describes internal geometry or formulas | Teaches the model; not for operators. |
| **Debug scripts** | Any script or entry point whose purpose is to dump layer state, propagation path, bridge internals, or raw traces | Debug is not part of shipping surface. |
| **Topology helpers** | core/topology/invariant_catalog (or any module that exports AREA_FAMILY_MAP, CANONICAL_AREA_SET, area/family counts to public callers) | Reveals internal structure. reserve_loader may be included only in a form used by projection filtering and not exposed to CLI/API. |
| **Internal registries** | docs/internal/*.md registries, assets/reserve/*.json (or ship only as opaque data with no schema that reveals 12 areas, 288 families, reserved indices) | Reveals structural counts and reserve layout. |
| **Raw dictionaries** | Unprojected Dict A / Dict B or internal dictionary build artifacts that expose family placement, ontology construction | Internal ontology doctrine. |
| **Calibration builders** | Tools or scripts that build or edit calibration/dictionaries with access to internal topology, family geometry, or placement logic | Operator calibration is bounded; builders are internal. |
| **Non-public entry points** | Any CLI command or API route other than **analyze**, **compare**, **batch-analyze**, **serve** (per SHIPPING_SURFACE_POLICY_v1) | Only the four commands are the shipping surface. |

---

## 2. Explicit exclusion list (paths / patterns)

Use this list in packaging and Docker multi-stage builds to exclude from the final artifact:

```
# Docs and specs
docs/internal/
docs/archive/specs_history/
*.internal.md

# Internal registries and reserve layout (or ship as opaque-only)
docs/internal/
assets/reserve/   # or include with no schema/doc that reveals structure

# Debug and dev-only
tools/sealing_scan.py
tools/check_import_boundary.py
**/debug_*.py
**/*_dump_*.py
**/run_e2e_*.py
**/run_l1_l2.py
**/run_l1_l2_l3.py
**/run_sphere_math*.py
**/run_reference_pipeline.py
**/run_corpus_benchmark.py
**/batch_runner.py
**/r1_r4_pipeline.py
**/reading_scales.py
**/analyze.py

# Topology and internal implementation (do not ship as public API)
# (core/topology, core/layers, core/math, core/domain may be compiled in but not exposed as entry points or docs)
legacy/
tests/
```

Entry points **analyze**, **compare**, **batch-analyze**, **serve** are implemented by thin wrappers that call only core.services and core.projection; the above runner scripts are development entry points and are excluded from the **shipped** CLI surface (see SHIPPING_SURFACE_POLICY_v1).

---

## 3. What may be included (minimal surface)

- **Runtime:** Code paths that implement the four commands (analyze, compare, batch-analyze, serve) and that use only core.services, core.projection, runtime.artifact_writer.
- **Core surface:** core/services, core/projection, core/topology/reserve_loader (for projection only; no export of topology names to user).
- **Assets:** assets/public/ (public_ontology_map, public_output_schema, public_metric_profiles, public_audit_manifest.schema).
- **Governance subset:** Only public-facing governance docs (e.g. PUBLIC_VOCABULARY_MAP, PUBLIC_PIPELINE_NARRATIVE, PUBLIC_AUDIT_POLICY) if bundled for operator reference; no internal registries or specs history.
- **No:** internal docs, specs history, debug scripts, topology helpers (as public API), internal registries (as readable specs), raw dictionaries, calibration builders, non-public entry points.

---

## 4. Enforcement

- **Nuitka build:** Include only the modules required for the four commands; exclude the paths above from the compiled bundle.
- **Docker multi-stage:** Copy only the sealed runtime tree; do not COPY docs/internal, assets/reserve (or copy reserve as data-only with no schema), legacy, tests, or dev runner scripts. Final image has no internal docs or debug tooling.
- **CI / release checklist:** Before tagging a release, confirm exclusion list is applied and that the shipped artifact does not contain any of the mandatory exclusions.

---

## 5. Done condition

The shipped runtime (CLI binary and API container) contains none of the excluded categories. Build and packaging enforce the exclusion policy.
