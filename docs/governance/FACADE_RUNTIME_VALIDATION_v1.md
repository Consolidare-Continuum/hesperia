# FACADE RUNTIME VALIDATION v1

**Status:** Active  
**Purpose:** Verify that the public runtime is fully operable through service façades only. No direct internal imports in public paths; outputs projected; audit manifests safe.

---

## 1. Validation scope

- **Entry points:** All public runners in ENTRYPOINT_CLASSIFICATION_v1 (run_l1_through_l9, run_reference_pipeline, run_l1_l2, run_l1_l2_l3, run_sphere_math_values, run_sphere_math_100_sentences, run_e2e_all for the service-based flows).
- **Imports:** tools/check_import_boundary.py must pass (zero violations in non-excluded files).
- **Outputs:** All file writes go through runtime.artifact_writer; public writes use apply_public_projection.
- **Audit:** Public audit manifest and evidence traces contain only public-safe keys (no internal layer ids, topology, or formula ids).

---

## 2. Dry-run checklist (from façades only)

Execute the following using **only** the listed commands (no direct Python imports of core.layers, sphere.pipeline, core.attribution from the runner process):

| Step | Command / action | Expected |
|------|------------------|----------|
| 1 | `python3 -m runtime.pipeline.run_l1_through_l9 --text "justice fairness" --out /tmp/out.json` | Exit 0; /tmp/out.json exists; content has no side_id / internal topology keys in plain form; L7/L9 present in projected form. |
| 2 | `python3 -m runtime.runners.run_reference_pipeline --text "justice" --out /tmp/ref.json` | Exit 0; output projected. |
| 3 | `python3 -m runtime.pipeline.run_l1_l2 --out /tmp/l2.json` | Exit 0; L1/L2 only in output. |
| 4 | `python3 -m runtime.pipeline.run_l1_l2_l3 --out /tmp/l3.json` | Exit 0; L1_B, L2_B, L3 (or projected equivalents) in output. |
| 5 | `python3 -m runtime.pipeline.run_sphere_math_values --out /tmp/values.json` | Exit 0; single JSON with projected structure. |
| 6 | `python3 -m runtime.pipeline.run_sphere_math_100_sentences --limit 2 --out /tmp/batch.json` | Exit 0; list of projected results. |
| 7 | If run_e2e_all is used: run with limited scope (e.g. one E2E flow) | No direct sphere.pipeline or core.layers import in stack; domain_metrics flow uses analysis_service. |

---

## 3. Checks during dry-run

- **No direct internal imports in public runtime:** Run `python3 tools/check_import_boundary.py`; must pass.
- **Outputs remain projected:** Spot-check output JSON for absence of reserved terms (side_id, hex, area_id, family_id, 12-area counts in keys).
- **Audit manifests remain safe:** If a run produces an audit manifest, it must match public_audit_manifest.schema.json and contain no internal layer ids or topology.
- **No extra artifacts:** In public_runtime mode, no internal layer dumps or bridge traces written.
- **Help/docs/schema non-reflective:** Public-facing help text and docs do not describe internal pipeline stages or layer count.

---

## 4. Done condition

Public runtime is fully operable through façades only. All of the above steps pass; execution paths do not reveal the method; reflection test (REFLECTION_RESISTANCE_TEST_v1) updated for execution-path coverage.
