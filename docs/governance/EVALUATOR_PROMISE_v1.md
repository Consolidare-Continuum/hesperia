# Evaluator promise v1

**Status:** Active  
**Purpose:** Document what the evaluator bundle guarantees. Helps external reviewers understand the intended boundary.

---

## Guarantees

The HESPERIA evaluator bundle guarantees:

1. **Reproducible CLI and API**  
   Same commands and endpoints, same inputs → same behavior. The sealed runtime is built from a single path (`./release_sealed_runtime.sh`) and passes the release gate.

2. **Deterministic outputs**  
   Output JSON uses sorted keys and stable serialization. Same raw_text produces identical output across runs (no nondeterminism in structural measurement or serialization).

3. **No exposure of internal model mechanics**  
   No internal geometry, layer count, topology, propagation details, or reserved structure appears in outputs, help text, errors, or schemas. The projection layer and schema guard enforce this.

4. **Stable schema**  
   The public output schema has a `schema_version`. Incompatible output changes require a schema version bump and are documented. Evaluators can rely on a stable contract for the duration of a given schema version.

---

## Intended boundary

- **Visible:** Structural measurement as a product capability; evidence and metrics in public vocabulary; version and build info; health and rate limits.
- **Not visible:** Internal computation layers, topology, dictionary construction, propagation algorithm, reserved areas/families, or any implementation detail that would allow reconstruction of the method.

---

*See SHIPPING_PATH_POLICY_v1.md, PUBLIC_API_SURFACE_FREEZE_v1.md, and EVALUATOR_GUIDE.md.*
