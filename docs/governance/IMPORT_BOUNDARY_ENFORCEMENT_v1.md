# IMPORT BOUNDARY ENFORCEMENT v1

**Status:** Active  
**Purpose:** Make façade-only imports technical, not cultural. Public runtime cannot directly import internal math/pipeline/bridge modules without failing checks.

---

## 1. Rule Set

### Public runtime zones (checked by tools/check_import_boundary.py)

- **runtime/api/** — API entry points.
- **runtime/pipeline/** — Runners must be thin wrappers over **core.services.analysis_service** only. Allowed: core.services, core.projection, runtime.artifact_writer, runtime.dossier, runtime.provenance, runtime.public_reports. **Forbidden:** core.layers, core.attribution, core.contracts.layer_contract, core.policy, core.stability, sphere.pipeline.pipeline_runner, sphere.pipeline.layer_registry, sphere.pipeline.pipeline_state, core.math.*, core.domain.bridge, core.topology.invariant_catalog.
- **runtime/runners/** — Same as pipeline (façade-only).
- **runtime/public_reports/** — May import core.projection, runtime.artifact_writer.
- **runtime/artifact_writer/** — May import core.projection.

### Excluded files (internal-review or not yet migrated)

The checker skips these paths; they still use internal modules and must not be exposed as public entry points (see ENTRYPOINT_CLASSIFICATION_v1.md):

- runtime/pipeline/analyze.py
- runtime/pipeline/r1_r4_pipeline.py
- runtime/pipeline/batch_runner.py
- runtime/pipeline/reading_scales.py
- runtime/pipeline/run_corpus_benchmark.py

### Allowed imports from public runtime

- core.projection (apply_public_projection, project_public_metrics, sanitize_public_trace)
- core.services (run_structural_analysis, build_public_report, export_public_artifacts, run_calibration_review)
- core.topology.reserve_loader (is_reserved_area, etc.) — only for use inside projection/code that does not expose topology
- runtime.artifact_writer
- runtime.public_reports
- runtime.dossier (which uses projection)
- runtime.provenance (run_manifest, etc.)

### Forbidden in public runtime

- `from core.layers import compute_L1` or any compute_L*
- `from core.math import ...` (except if math is used only inside a service that is not part of public runtime entry)
- `from core.domain.bridge import ...` (except inside sealed core or services)
- `from core.topology.invariant_catalog import AREAS, CANONICAL_AREA_SET, AREA_FAMILY_MAP` in any file under runtime/ that is an entry point or public-facing.

---

## 2. CI / Local Check

Run **tools/check_import_boundary.py** (or equivalent). It scans **runtime/api**, **runtime/pipeline**, **runtime/public_reports**, **runtime/artifact_writer**, **runtime/runners** for forbidden import patterns and exits non-zero if any are found. Excluded files (see above) are skipped. Boundary violations must be treated as **hard failures** in CI.

**Command (repo root):**
```bash
python3 tools/check_import_boundary.py
```
Or with explicit repo path: `python3 tools/check_import_boundary.py --repo /path/to/hesperia`.

**CI rule:** Add a job/step that runs the above; fail the build if exit code is non-zero. Do not merge if the check fails.

---

## 3. Done Condition

Public runtime cannot directly import internal math/pipeline/bridge modules without failing checks. CI fails on violation.
