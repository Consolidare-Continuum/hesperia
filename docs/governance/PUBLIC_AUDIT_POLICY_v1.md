# PUBLIC AUDIT POLICY v1

**Status:** Active  
**Purpose:** Do not become a black box; show only safe accountability. A third party can verify run identity without learning the engine.

---

## 1. Public-Safe Audit Manifest May Include

| Field | Purpose |
|-------|---------|
| engine version | Reproducibility; which engine build. |
| public ontology version | Which public macro-domain / policy-family map. |
| calibration profile id | Which calibration was used. |
| report profile id | Which report template/profile. |
| input manifest id | Opaque reference to input (hash or id; no content). |
| run timestamp | When the run occurred. |
| output checksum | Integrity of the emitted output. |
| evidence count | How many evidence entries. |
| public metric profile id | Which metric subset (commercial / demo / analyst). |

---

## 2. Must Not Include

- Internal layer ids (L1–L9, L10).
- Internal topology coordinates (area index, family index, side_id, hex).
- Hidden area/family references (reserved areas 10–11, families 240–287).
- Internal formula ids or dependency graph.
- Bridge strategy ids or construction doctrine.

---

## 3. Schema

Public audit manifest shape is defined in **assets/public/public_audit_manifest.schema.json**. Every public run should produce a manifest that conforms to this schema and is written via **runtime/public_reports/public_manifest_writer.py** (or equivalent).

---

## 4. Acceptance Criterion

A third party can verify run identity (version, input ref, checksum, evidence count) without learning the engine’s method. No internal layer, topology, or formula is exposed in the manifest.
