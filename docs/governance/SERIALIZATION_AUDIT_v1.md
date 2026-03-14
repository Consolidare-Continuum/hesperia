# SERIALIZATION AUDIT v1

**Status:** Complete  
**Purpose:** Classify every writer. No writer remains unclassified. Mode and projection govern what may be written.

---

## 1. Classification

Each code path that writes JSON, dossier, stdout, logs, temp files, report files, calibration outputs, or debug outputs is classified as one of:

| Class | Meaning | Mode guard |
|-------|---------|------------|
| **internal-only** | Writes internal state (layer dumps, traces, bridge output). Must not run in public_runtime. | internal_debug or internal_review only |
| **public-safe** | Writes only projected or audit manifest content. Safe for public_runtime. | All modes |
| **needs-projection** | Writes pipeline/output that must pass through apply_public_projection before write. | public_runtime: must project first |
| **forbidden** | Must not be used in shipped code path (e.g. accidental dump of raw L1–L9). | Remove or guard |

---

## 2. Audited Writers

| Location | What it writes | Classification | Notes |
|----------|----------------|----------------|-------|
| runtime/dossier/dossier_writer.write_dossier_json | Dossier JSON | needs-projection | Applies apply_public_projection before write. |
| runtime/pipeline/run_l1_through_l9 | stdout, --out file, dossier | needs-projection | Output is projected before write. |
| runtime/pipeline/run_e2e_all | E2E artifact JSONs | needs-projection | Each write uses apply_public_projection. |
| runtime/pipeline/run_e2e_sentence, run_e2e_l1_l9, run_e2e_r1_r4, run_e2e_domain_metrics | JSON to assets | needs-projection | Projection applied. |
| runtime/pipeline/run_sphere_math_values, run_sphere_math_100_sentences | JSON | needs-projection | Patched: use runtime.artifact_writer; write_public_json in public mode, write_internal_json in internal mode. |
| runtime/pipeline/run_l1_l2, run_l1_l2_l3, runtime/runners/run_reference_pipeline | JSON to file, stdout | needs-projection | Patched: apply_public_projection + write_public_json for file; projected output to stdout. |
| runtime/artifact_writer.writer.write_public_json | JSON file | public-safe | Central gate; applies projection. |
| runtime/artifact_writer.writer.write_internal_json | JSON file | internal-only | No-op in public_runtime; writes only in internal_debug/internal_review. |
| runtime/public_reports/public_manifest_writer.write_public_audit_manifest | Audit manifest JSON | public-safe | Only allowed keys. |
| runtime/pipeline/run_l1_through_l9 print(j) | stdout | needs-projection | `out` is projected. |
| core/services/report_service.export_public_artifacts | Report JSON | public-safe | Input is already projected. |
| runtime/provenance/run_manifest.build_run_manifest | In-memory manifest | public-safe | Embedded in dossier (projected). |
| Any future L1–L9 raw dump, layer trace, bridge diagnostic | Internal artifacts | internal-only | Must be mode-guarded; see RUNTIME_MODE_POLICY. |
| Logging (if logs go to operator) | Log lines | needs-projection / public-safe | Must not contain internal layer names or topology. |

---

## 3. Rules

- **internal-only** writers must check runtime mode and only run when mode is internal_debug or internal_review.
- **needs-projection** writers must call apply_public_projection (or equivalent) before writing when mode is public_runtime.
- **public-safe** writers may write as-is; content must already conform to public vocabulary and no internal structure.
- **forbidden** writers must be removed or refactored so they are never invoked in public or shipped paths.

---

## 4. Acceptance Criterion

No writer remains unclassified. Every serialization path is either internal-only (guarded), public-safe, or needs-projection (and projection is applied). See RUNTIME_MODE_POLICY and INTERNAL_DEBUG_ISOLATION_POLICY.
