# Seal B1 — Projection verification

**Block:** B — Sealing integrity  
**Goal:** Confirm that public runners and emitted artifacts do not contain internal architecture terms. Inspect JSON outputs, logs, manifests, stdout.

---

## Forbidden terms (must be absent)

Ensure **absence** of the following in any emitted artifact (JSON outputs, logs, manifests, stdout) from public runners:

| Term / pattern | Reason |
|----------------|--------|
| hex | Geometry-revealing |
| sphere | Geometry-revealing |
| side_id | Internal coordinate |
| topology | Internal structure |
| 12 areas | Internal count |
| 288 families | Internal count |
| coordinates | Internal geometry |
| 3D vectors | Geometry-revealing |
| propagation path | Internal method |
| bridge nodes | Bridge internals |

(Aligned with SEALING_SCAN_RULES_v1 and PUBLIC_VOCABULARY_MAP.)

---

## Procedure

1. **Run public runners** with fixed raw_text (e.g. default text):
   - `python3 -m runtime.pipeline.run_l1_through_l9 --text "justice fairness" --out /tmp/b1_out.json`
   - `python3 -m runtime.runners.run_reference_pipeline --text "justice" --out /tmp/b1_ref.json`
   - `python3 -m runtime.pipeline.run_l1_l2 --out /tmp/b1_l2.json`
   - `python3 -m runtime.pipeline.run_l1_l2_l3 --out /tmp/b1_l3.json`
   - `python3 -m runtime.pipeline.run_sphere_math_values --out /tmp/b1_vals.json`

2. **Inspect:**
   - **JSON outputs:** Open each output file; search (case-insensitive) for: `hex`, `sphere`, `side_id`, `topology`, `12 areas`, `288 families`, `coordinates`, `3D`, `propagation path`, `bridge nodes`. None should appear as key names or in string values that expose internal structure.
   - **Logs:** If runners write to stderr, capture and search the same terms.
   - **Manifests:** If an audit manifest is written, open it and search for the same terms.
   - **Stdout:** Capture stdout (e.g. JSON printed by runners); search the same terms.

3. **Pass:** No forbidden term appears in any of the above from public runner execution.

---

## Expected summary

- No key or value in emitted JSON/logs/manifests/stdout reveals internal geometry, topology, layer count, or bridge logic.
- Public vocabulary (e.g. macro_domain, policy_family, structural space) may appear; internal terms must not.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Forbidden term in output JSON | Fix projection or writer to strip/remap; ensure all writes go through projection. |
| Forbidden term in logs/stdout | Remove or redact from runner print statements; use public vocabulary only. |
| Forbidden term in manifest | Restrict manifest to public_audit_manifest.schema; no internal fields. |

---

## Pass criterion

All inspected artifacts (JSON, logs, manifests, stdout) are free of the listed forbidden terms. No remediation required.
