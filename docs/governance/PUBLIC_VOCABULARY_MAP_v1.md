# PUBLIC VOCABULARY MAP v1

**Status:** Active  
**Scope:** Replace architecture-revealing language with neutral external language.  
**Rule:** Public docs, configs, outputs, schemas, logs, and API fields must use only public-safe terms.

---

## 1. Purpose

Internal geometry and topology must not be inferable from public-facing artifacts. This map defines the **minimum mapping set** from internal terms to public-safe terms. Any text or field that may be read by external users or operators must use the public-safe column only.

---

## 2. Minimum Mapping Set

| Internal term | Public-safe term |
|---------------|-------------------|
| sphere | structural space |
| hex / hexagon / cell | structural node |
| area | macro-domain |
| family | policy family |
| coordinate | structural position |
| side_id | internal relation id *(or omit entirely)* |
| 3D vector | directional structural signal |
| topology / geometry | relation structure |
| propagation surface | relation spread |
| domain distance | structural distance |
| area lattice | relation structure |
| coordinate map | structural position map |
| vector sphere | structural space *(avoid "vector" in public if possible)* |

---

## 3. Usage Rules

- **Public docs:** Use only public-safe terms. Do not use internal terms even in examples intended for external readers.
- **Configs:** Field names and descriptions must use public-safe terms. No "area", "hex", "side_id", "sphere" in user-facing config keys or help text.
- **Outputs:** JSON keys, report column headers, and log messages visible to operators must use public-safe terms.
- **Schemas:** Public JSON schemas and API response schemas must define fields with public-safe names and descriptions.
- **Logs:** Log lines that may be shipped or shown to external/operator use must not contain internal vocabulary.

---

## 4. Acceptance Criterion

A search across the **public-facing tree** (docs, configs, API surface, report schemas, operator logs) must yield **no** geometry-revealing vocabulary except in documents explicitly marked **internal-only**.

---

## 5. Related

- **VOCABULARY_SEPARATION_POLICY_v1.md** — Defines three vocabulary classes (internal, protected engineering, public) and forbidden crossovers.
- **public_projection_layer** — Enforces remapping of internal indices and labels to public-safe form before any external output.
