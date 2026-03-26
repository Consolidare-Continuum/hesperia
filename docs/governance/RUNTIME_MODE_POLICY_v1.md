# RUNTIME MODE POLICY v1

**Status:** Active  
**Purpose:** No writer writes unless its mode classification allows it. Internal layer outputs and traces must never be emitted in public mode.

---

## 1. Modes

| Mode | Purpose | Allowed writes |
|------|---------|----------------|
| **internal_debug** | Full development: traces, math intermediates, layer dumps, bridge diagnostics. | All: L1–L10 outputs, internal traces, bridge outputs, raw domain-state payloads, debug logs. |
| **internal_review** | Reduced internal: still internal semantics but no full dumps. | Curated internal artifacts; no raw layer serialization to external paths. |
| **public_runtime** | Normal operation for operators and API consumers. | Only projected outputs, public reports, public manifest, public evidence trace. No layer intermediates, no internal topology, no bridge internals. |

---

## 2. Rules

1. **Any writer** for the following **must be guarded by mode:**
   - L1–L10 raw outputs (per-layer JSON or intermediate state)
   - Internal traces (propagation path, adjacency path, layer-by-layer state)
   - Bridge outputs (hit-to-node, relation synthesis intermediates)
   - Raw domain-state payloads (unprojected area_vector, family_counts, side_id)

2. **public_runtime:** Only these may be written:
   - Raw_text manifest (opaque ids, no topology)
   - Calibration profile id / report profile id (bounded knobs only)
   - Public-safe evidence trace (per PUBLIC_EVIDENCE_TRACE_POLICY)
   - Public report / dossier (after projection)
   - Public audit manifest (version, checksum, evidence count — no layer ids, no coordinates)
   - Log lines that do not contain internal layer names, formulas, or topology

3. **internal_debug / internal_review:** May write to paths that are **excluded from public package** (e.g. under `internal/` or env-guarded). Never write internal artifacts to the same path as public artifacts without an explicit internal-only guard.

---

## 3. Enforcement

- **Serialization audit:** Every code path that writes JSON, dossier, stdout, logs, temp files, report files, calibration outputs, or debug outputs is classified (internal-only / public-safe / needs-projection / forbidden). See SERIALIZATION_AUDIT_v1.md.
- **Writers:** Before writing, check mode (e.g. env `HESPERIA_RUNTIME_MODE` or equivalent). If mode is `public_runtime`, only public writers and projection-backed writers may run.
- **Tests:** Verify mode separation: no shared code path allows public mode to emit internal debug state.

---

## 4. Acceptance Criterion

Public runtime cannot emit internal layer payloads (L1–L10 raw, internal traces, bridge outputs, raw domain-state) even by accident. All such writers are mode-guarded and classified.
