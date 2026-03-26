# Seal B2 — Reserved structure verification

**Block:** B — Sealing integrity  
**Goal:** Verify that outputs never contain reserved internal structure: area indices 10 and 11, family indices 240–287, side IDs 360000–431999.

---

## Reserved ranges (must never appear in public output)

| Element | Forbidden in public output |
|---------|----------------------------|
| Area index 10 | Reserved (internal area 11). |
| Area index 11 | Reserved (internal area 12). |
| Family indices 240–287 | Reserved (families under the two hidden areas). |
| Side IDs 360000–431999 | Reserved hex/side range. |

(Per AREA_RESERVE_POLICY and reserve_loader; projection must filter these.)

---

## Procedure

1. **Inputs that activate multiple families:** Use raw_text text that triggers attribution across many families (e.g. longer text, or corpus sentences) so that the execution_flow processes a wide set of families and areas.

2. **Run public service:**  
   `run_structural_analysis(text, assets_root=assets, stages="full")`  
   and optionally runners that write full output (e.g. run_l1_through_l9, run_reference_pipeline).

3. **Inspect output (recursively over the full structure):**
   - **Area index 10 or 11:** Must not appear in any list or value (e.g. no `area_id: 10`, no vector index 10 in a 12-element area vector, no "area_10" in keys). Public projection must expose only 10 macro-domains (indices 0–9).
   - **Family 240–287:** Must not appear in any family index, count array beyond 240 elements, or key that encodes family id (e.g. no `family_id: 240`, no 288-element policy_family array in public output; public length 240).
   - **Side IDs 360000–431999:** Must not appear in any field (e.g. no `side_id`, no numeric value in that range in evidence or topology-related fields).

4. **Vectors/lists:** If output contains `macro_domain_vector` or `policy_family_counts`, lengths must be 10 and 240 respectively (or as defined in public_ontology_map). No 12-area or 288-family vectors in public output.

---

## Expected summary

- No area index 10 or 11 in any emitted artifact.
- No family index in 240–287.
- No side_id or numeric id in 360000–431999.
- Public vectors have public lengths (10 areas, 240 families).

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Area 10/11 or 12-area vector in output | Ensure projection uses project_public_areas / filter_reserved_structures; all writers use projected data. |
| Family 240–287 or 288-family vector | Apply project_public_families / filter; cap family counts at 240 in public. |
| Side ID in reserved range | Strip side_id from public trace; sanitize_public_trace must remove or remap. |

---

## Pass criterion

Outputs never contain reserved area indices (10, 11), reserved family indices (240–287), or reserved side IDs (360000–431999). No remediation required.
