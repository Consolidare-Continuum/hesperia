# HESPERIA post-seal consistency report v1

**Purpose:** Summary of the Consistency Verification Program (Block A — Functional integrity, Block B — Sealing integrity, Block C — Performance sanity). Run before any release tag.

**Expected outcome (when Phases 1–5 are correctly implemented):**

- Functional consistency: **PASS**
- Seal integrity: **PASS**
- Runtime boundary: **PASS**

At that point the engine can be considered **sealed and operationally consistent**.

---

## 1. Block A — Functional integrity

| Check | Document | Summary | Notes |
|-------|----------|--------|------|
| A1 | [CONSISTENCY_A1_BASELINE_STABILITY.md](CONSISTENCY_A1_BASELINE_STABILITY.md) | ☐ PASS / ☐ FAIL | Triple run of `run_structural_analysis()`; identical projected outputs and checksums. |
| A2 | [CONSISTENCY_A2_RUNNER_SERVICE_EQUIVALENCE.md](CONSISTENCY_A2_RUNNER_SERVICE_EQUIVALENCE.md) | ☐ PASS / ☐ FAIL | Runners vs direct service; projected output and metric equivalence. |
| A3 | [CONSISTENCY_A3_STAGE_LIMITED_RUNS.md](CONSISTENCY_A3_STAGE_LIMITED_RUNS.md) | ☐ PASS / ☐ FAIL | L1_L2, L1_L2_L3, full; domain_metrics only when enabled. |
| A4 | [CONSISTENCY_A4_BATCH_SINGLE_EQUIVALENCE.md](CONSISTENCY_A4_BATCH_SINGLE_EQUIVALENCE.md) | ☐ PASS / ☐ FAIL | `batch([text])[0]` equals `run_structural_analysis(text)`. |
| A5 | [CONSISTENCY_A5_DOMAIN_METRIC_SWITCH.md](CONSISTENCY_A5_DOMAIN_METRIC_SWITCH.md) | ☐ PASS / ☐ FAIL | domain_metrics absent when disabled, present when enabled; projection applied. |

**Block A summary:** ☐ PASS (all A1–A5 pass) / ☐ FAIL

---

## 2. Block B — Sealing integrity

| Check | Document | Summary | Notes |
|-------|----------|--------|------|
| B1 | [SEAL_B1_PROJECTION_VERIFICATION.md](SEAL_B1_PROJECTION_VERIFICATION.md) | ☐ PASS / ☐ FAIL | No forbidden terms in JSON, logs, manifests, stdout. |
| B2 | [SEAL_B2_RESERVED_STRUCTURE_TEST.md](SEAL_B2_RESERVED_STRUCTURE_TEST.md) | ☐ PASS / ☐ FAIL | No area 10/11, families 240–287, side IDs 360000–431999 in output. |
| B3 | [SEAL_B3_IMPORT_BOUNDARY_CHECK.md](SEAL_B3_IMPORT_BOUNDARY_CHECK.md) | ☐ PASS / ☐ FAIL | `check_import_boundary.py` exit 0; excluded files recorded. |
| B4 | [SEAL_B4_WRITER_ENFORCEMENT.md](SEAL_B4_WRITER_ENFORCEMENT.md) | ☐ PASS / ☐ FAIL | public_runtime blocks internal writes; write_public_json applies projection. |
| B5 | [SEAL_B5_RELEASE_PACKAGE_CHECK.md](SEAL_B5_RELEASE_PACKAGE_CHECK.md) | ☐ PASS / ☐ FAIL | Bundle excludes internal docs/registries; includes runtime, services, projection, assets/public. |
| B6 | [SEAL_B6_REFLECTION_SPOT_TEST.md](SEAL_B6_REFLECTION_SPOT_TEST.md) | ☐ PASS / ☐ FAIL | Runner names, CLI help, schema, layout, manifest non-revelatory. |

**Block B summary:** ☐ PASS (all B1–B6 pass) / ☐ FAIL

---

## 3. Block C — Performance sanity

| Check | Document | Summary | Notes |
|-------|----------|--------|------|
| C1 | [PERF_C1_SINGLE_TEXT.md](PERF_C1_SINGLE_TEXT.md) | ☐ PASS / ☐ FAIL | Single-text latency and memory recorded; within expected bounds. |
| C2 | [PERF_C2_BATCH_RUN.md](PERF_C2_BATCH_RUN.md) | ☐ PASS / ☐ FAIL | Batch (e.g. 100) linear scaling; no memory leak; writer not bottleneck. |

**Block C summary:** ☐ PASS (C1–C2 pass) / ☐ FAIL

---

## 4. Overall summary

| Category | Summary |
|----------|--------|
| Functional consistency (A) | ☐ PASS / ☐ FAIL |
| Seal integrity (B) | ☐ PASS / ☐ FAIL |
| Runtime boundary (B3, B4) | ☐ PASS / ☐ FAIL |
| Performance (C) | ☐ PASS / ☐ FAIL |

**System passes the consistency program when:** All functional tests (A) produce stable outputs; service and runner outputs match; no internal terms in outputs/logs (B); import boundary check passes (B3); public mode blocks internal writes (B4); release bundle excludes internal artifacts (B5); performance within bounds (C).

---

## 5. Remediation list

*(Use when one or more checks fail. Add rows as needed.)*

| Check | Failure | Remediation |
|-------|---------|-------------|
| (example) | A1: outputs differ on triple run | Eliminate nondeterminism (e.g. dict iteration, random seed). |
| | | |
| | | |

---

## 6. How to run the program

1. **Block A:** Execute procedures in CONSISTENCY_A1 through A5 (scripts or manual steps); record pass/fail and any notes.
2. **Block B:** Execute SEAL_B1 through B6 (artifact inspection, `tools/check_import_boundary.py`, writer tests, package build inspection, reflection spot test); record pass/fail.
3. **Block C:** Run PERF_C1 and C2; record runtime/memory and scaling; set pass/fail.
4. **Fill this report:** Update summary cells and Block/Overall summaries; add remediation items for any failure.
5. **Release gate:** Do not create release tag until Overall summary is PASS for A, B, and (as policy) C.

---

*Document version: v1. Part of HESPERIA Consistency Verification Program.*
