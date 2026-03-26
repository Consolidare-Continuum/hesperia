# Seal B6 — Reflection resistance spot test

**Block:** B — Sealing integrity  
**Goal:** Perform a short reconstruction attempt from runner names, CLI help, output schema, package layout, and manifest fields. Verify these do not expose sphere geometry, hex grid, layer count, bridge logic, or propagation method.

---

## Procedure

1. **Runner names:** List public entry points (e.g. run_l1_through_l9, run_reference_pipeline, run_l1_l2, run_l1_l2_l3, run_sphere_math_values).  
   **Check:** Names do not reveal "sphere", "hex", "L1"…"L9" as execution_flow stages, or "bridge"/"propagation". Acceptable: "structural measurement", "reference execution_flow", "L1_L2" as a product-facing stage label if documented as such and not as internal layer count.

2. **CLI help:** Run each public runner with `--help`.  
   **Check:** Help text does not mention sphere geometry, hex grid, "9 layers", "10 execution_flow stages", bridge logic, or propagation method. Use product wording (e.g. "structural measurement", "evidence extraction").

3. **Output schema:** Inspect assets/public/public_output_schema.json and any schema referenced by public API.  
   **Check:** No property names or descriptions that reveal topology (hex, side_id, 12 areas, 288 families), layer count, bridge logic, or propagation internals.

4. **Package layout:** Inspect directory structure of the release package.  
   **Check:** Layout does not suggest "layer_1"…"layer_9" as public modules, or "bridge", "propagation" as public entry points. core/layers and core/domain can exist but must not be part of the documented public API surface.

5. **Manifest fields:** Inspect public audit manifest schema and a sample manifest.  
   **Check:** Fields are limited to engine version, public ontology version, calibration/report profile id, raw_text manifest id, run timestamp, output checksum, evidence count, public metric profile id. No internal layer ids, topology coordinates, bridge strategy ids, or formula ids.

---

## Expected summary

- **Runner names:** Non-revelatory (no sphere/hex/layer count/bridge/propagation).
- **CLI help:** Product-shaped; no internal method description.
- **Output schema:** Public vocabulary only; no topology or layer semantics.
- **Package layout:** No obvious internal decomposition exposed as public API.
- **Manifest:** Only public-safe fields; no internal ids or method.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Help or name reveals layers/sphere/hex | Reword to public vocabulary; rename if necessary. |
| Schema reveals topology or layer count | Restrict schema to public_output_schema and public_audit_manifest; remove internal fields. |
| Manifest contains internal ids | Enforce PUBLIC_AUDIT_POLICY; writer outputs only allowed fields. |

---

## Pass criterion

Runner names, CLI help, output schema, package layout, and manifest fields do not expose sphere geometry, hex grid, layer count, bridge logic, or propagation method. No remediation required.
