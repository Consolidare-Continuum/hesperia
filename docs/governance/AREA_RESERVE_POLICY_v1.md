# AREA RESERVE POLICY v1

**Status:** Active  
**Scope:** Structural reserve lock — Areas 11 and 12  
**Internal only.** Do not expose this policy or reserved area identifiers in public ontology, APIs, or outputs.

---

## 1. Purpose

Two areas of the internal 12-area structure are permanently reserved. They remain part of the internal topology for structural consistency but are **inert**: never populated, activated, propagated, or exposed. This supports future sealing and public projection (10 public areas, 2 hidden).

---

## 2. Reserved Areas

- **Area 11** — internal index `10` (1-based: 11th area in canonical order).
- **Area 12** — internal index `11` (1-based: 12th area in canonical order).

Canonical order is defined by the internal topology catalog (e.g. `AREA_FAMILY_MAP` key order). Reserved area **names** are not published; only the reserve identifiers (e.g. `AREA_11`, `AREA_12`) and internal indices are used in code and registries.

---

## 3. Requirements (Non-Negotiable)

Reserved areas MUST:

| Requirement | Meaning |
|-------------|---------|
| **Remain present in internal structure** | Total area count stays 12 in core topology. Indices 10 and 11 exist. |
| **Never populate** | No tokens, hits, or content are attributed to these areas. |
| **Never activate** | They do not participate in activation vectors or dominance logic. |
| **Never propagate** | Propagation and diffusion must not write into or read from these areas. |
| **Never contribute to metrics** | No metric (public or internal) may aggregate or expose data from areas 10 or 11. |
| **Never appear in public ontology** | Public ontology, API responses, configs, and reports must not mention or expose these areas. |

**Reserved means inert, not merely unused.** Unused can be activated by accident; inert cannot. All code paths that iterate areas or emit area-level data must exclude reserved indices from population, propagation, and output.

---

## 4. Implementation Notes

- Use `reserved_areas.json` as the single source of truth for which internal indices are reserved.
- Before any area-level output or metric: filter out reserved indices or project to public indices only (see later Public Projection Layer).
- Validation: a full run must produce **no trace** of the two hidden areas, their families, or their hex values in any public or log output.

---

## 5. Related Deliverables

- `reserved_areas.json` — reserve indices and identifiers.
- `reserved_families_registry.json` — all families under reserved areas (inert).
- `reserved_hex_registry.json` — hex slots under reserved families (coordinates preserved, values sealed).

---

## 6. Acceptance Criterion

A full run must produce **no trace** of the 2 hidden areas, their families, or their hex values in outputs, logs, or public ontology.
