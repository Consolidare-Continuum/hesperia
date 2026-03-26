# Seal B3 — Import boundary enforcement

**Block:** B — Sealing integrity  
**Goal:** Confirm that the import boundary check passes (exit code 0, no violations). Record excluded files and justification.

---

## Procedure

1. **Execute:** From repo root, run  
   `python3 tools/check_import_boundary.py`  
   (or `python3 tools/check_import_boundary.py --repo /path/to/hesperia`).

2. **Confirm:**
   - **Exit code = 0.** Non-zero indicates at least one violation in public runtime paths.
   - **No violations reported.** Output should state "Import boundary check: no violations" (or equivalent).

3. **Record excluded files:** The checker skips files listed in `EXCLUDED_FILES` (see tools/check_import_boundary.py). Document them and justification:

   | File | Justification |
   |------|----------------|
   | runtime/execution_flow/analyze.py | Internal-review; uses core.attribution, core.math, core.propagation; not yet migrated to service. |
   | runtime/execution_flow/r1_r4_pipeline.py | Internal-review; uses core.attribution, core.layers, core.propagation. |
   | runtime/execution_flow/batch_runner.py | Internal-review; uses core.layers.load_defaults; internal flows. |
   | runtime/execution_flow/reading_scales.py | Internal-review; uses core.layers; calibration tooling. |
   | runtime/execution_flow/run_corpus_benchmark.py | Internal-review; benchmark only; uses sphere.execution_flow. |

   These must **not** be advertised as public entry points (see ENTRYPOINT_CLASSIFICATION_v1).

---

## Expected summary

- **Exit code = 0.**
- **No violations** in non-excluded public runtime paths (runtime/api, runtime/execution_flow, runtime/public_reports, runtime/artifact_writer, runtime/runners).
- Excluded files documented with justification; excluded list kept minimal and reviewed for any new public entry points.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Exit code non-zero | Fix violating imports: replace with core.services or core.projection; or move component to internal/excluded and document. |
| New public runner imports internal | Migrate runner to use analysis_service (or other façade) only; re-run check. |

---

## Pass criterion

`python3 tools/check_import_boundary.py` exits 0 with no violations. Excluded files and justification recorded. No remediation required.
