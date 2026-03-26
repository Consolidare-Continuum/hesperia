# HESPERIA SEALED RUNTIME BASELINE v1

**Status:** Baseline defined  
**Purpose:** First truly sealed runtime package. Operable, calibratable, auditable, and non-reflective.

---

## 1. Exposed Interfaces Only

Public runtime and API consumers may use only the following:

### Service façades (core.services)

- **run_structural_analysis(text, assets_root, calibration_profile_id, report_profile_id, policy_mode)** — Run structural measurement; returns projected summary only.
- **build_public_report(analysis_result, report_profile_id, public_metric_profile_id)** — Build public report from projected summary.
- **export_public_artifacts(report, output_path)** — Write report JSON (public-safe).
- **run_calibration_review(...)** — Calibration review; returns public-safe summary only.

### Projection (core.projection)

- **apply_public_projection(payload)** — Apply public projection before any external output.
- **project_public_metrics(internal_metrics)** — Map internal metrics to public subset.
- **sanitize_public_trace(trace)** — Sanitize trace for public emission.

### Public manifest (runtime.public_reports)

- **write_public_audit_manifest(manifest, output_path)** — Write non-revealing audit manifest.

### Entry points (runtime.execution_flow)

- **run_l1_through_l9** — CLI; output is projected.
- **run_e2e_all** — E2E flows; all outputs projected.
- **Dossier write** — Via write_dossier_json; payload projected.

---

## 2. Not Exposed

- Raw L1–L9 layer modules or outputs.
- core.math.* (formulas, dependency graph).
- core.domain.bridge internals (hit-to-node, relation synthesis).
- core.topology (invariant_catalog, reserve internals) except via projection/reserve_loader for filtering.
- Execution Flow stage order, transformation chain, or bridge doctrine.
- Internal docs (docs/internal/), MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY.

---

## 3. Artifacts Included in Baseline

- docs/governance/*.md (policies)
- docs/internal/*.md (internal only; exclude from public package if shipping)
- assets/public/*.json (public schemas, ontology map, metric profiles, audit manifest schema)
- core/projection/*
- core/services/*
- runtime/public_reports/*
- tools/sealing_scan.py

---

## 4. Acceptance

The runtime package is **operable** (run measurement, get reports), **calibratable** (calibration profile, bounded knobs), **auditable** (audit manifest, checksum, evidence count), and **non-reflective** (no method, topology, or layer map exposed).
