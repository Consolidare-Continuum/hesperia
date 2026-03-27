# Consistency A2 — Runner/service equivalence

**Block:** A — Functional integrity  
**Goal:** Verify that all public runners produce results equivalent to a direct call to `analysis_service.run_structural_analysis()` (same projected output, metric vectors, evidence trace, manifest checksum).

---

## Procedure

1. **Canonical baseline:** Run  
   `analysis_service.run_structural_analysis(text, assets_root=assets, stages="full")`  
   and store as `service_out`. Use fixed text and assets (e.g. default text, repo `lexicon/curated`).

2. **Runner outputs:** For each runner, invoke it so that it processes the **same** raw_text text and write output to a file (or capture stdout). Parse the JSON output to get a dict.
   - **run_l1_through_l9:** `python3 -m runtime.pipeline.run_l1_through_l9 --text "<same_text>" --out /tmp/a2_l19.json` → load `/tmp/a2_l19.json`.
   - **run_reference_pipeline:** `python3 -m runtime.runners.run_reference_pipeline --text "<same_text>" --out /tmp/a2_ref.json` → load `/tmp/a2_ref.json`.
   - **run_l1_l2:** `python3 -m runtime.pipeline.run_l1_l2 --text "<same_text>" --out /tmp/a2_l2.json` → load; compare only L1/L2 and shared keys (runner is stage-limited).
   - **run_l1_l2_l3:** `python3 -m runtime.pipeline.run_l1_l2_l3 --text "<same_text>" --out /tmp/a2_l3.json` → load; compare L1_B, L2_B, L3 and shared keys.
   - **run_sphere_math_values:** `python3 -m runtime.pipeline.run_sphere_math_values --text "<same_text>" --out /tmp/a2_vals.json` → load; should match full service output structure for same raw_text.
   - **run_e2e_all:** Run with minimal scope (e.g. one E2E flow that runs structural measurement); extract the structural-measurement summary segment and compare to `service_out` for the same text.

3. **Equivalence rules:**
   - **Full runners (run_l1_through_l9, run_reference_pipeline, run_sphere_math_values):** Projected output (after normalizing key order / serialization) should equal `service_out` for the same text and options (no profile, full stages).
   - **Stage-limited (run_l1_l2, run_l1_l2_l3):** Only the present stages (L1, L2 or L1_B, L2_B, L3, etc.) and common top-level keys must match the corresponding subset of `service_out`; later stages need not exist.

4. **Compare:**
   - Projected output: same keys and values (allow float tolerance if needed).
   - Metric vectors: identical length and values.
   - Evidence trace: same structure and counts if present.
   - Manifest checksum: if runners produce an audit manifest, its checksum-related fields should match when raw_text and config are identical.

---

## Expected summary

- Each runner’s output is **equivalent** to the service output for the same raw_text (full runners: full equality; stage-limited: subset equality).
- No runner introduces extra keys or different projection.

---

## Failure interpretation

| Symptom | Likely cause |
|--------|---------------|
| Runner output differs from service | Runner using different code path, options, or not calling service; or writing pre-projection data. |
| Metric vectors differ | Different defaults, profile, or execution_flow path. |
| Manifest checksum differs | Different manifest construction or non-deterministic field. |

---

## Pass criterion

All listed runners produce output that matches (or is a valid subset of) the direct service invocation for the same raw_text. No remediation required.
