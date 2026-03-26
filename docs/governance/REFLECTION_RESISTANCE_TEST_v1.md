# REFLECTION RESISTANCE TEST v1

**Status:** Red-team checklist  
**Purpose:** Test whether the sealed bundle leaks. Do not test whether it works; test whether it leaks.

---

## 1. Question

**What can be inferred about the hidden model from names, outputs, docs, schemas, and logs?**

---

## 2. Reconstruction Paths to Test

| Path | What an adversary might try | Blocked? | Notes |
|------|-----------------------------|----------|--------|
| **Names in output keys** | Infer topology from field names (area, family, hex, side_id). | Yes | PUBLIC_VOCABULARY_MAP; projection remaps to macro_domain, policy_family. |
| **Output shape** | Infer 12 areas from length of a vector. | Yes | Public vector length 10; reserved excluded. |
| **Output shape** | Infer 288 families from length. | Yes | Public length 240. |
| **Docs** | Read execution_flow order or layer count. | Yes | PUBLIC_PIPELINE_NARRATIVE only; no L1–L9 in public docs. |
| **Schemas** | Infer geometry from schema property names or descriptions. | Yes | public_output_schema and public_audit_manifest only; no topology. |
| **Logs** | Find layer names or formula ids in stderr. | Review | Ensure no print of L1…L9 or internal vars in default path. |
| **Package layout** | Infer decomposition from directory structure (core/layers, core/math). | Mitigated | Release bundle may exclude or rename; or ship only runtime + core/projection + core/services. |
| **Bridge** | Infer hit-to-node or relation synthesis from any artifact. | Yes | BRIDGE_EXPOSURE_POLICY; no bridge output in public mode. |
| **Reserved structure** | Infer area 11/12 or families 240–287 from any output. | Yes | Projection and reserve_loader filter; no trace. |
| **Execution path** | Infer method from which modules runners import (core.layers, sphere.execution_flow). | Yes | Phase 5: runners are thin wrappers; only core.services and core.projection; check_import_boundary enforces. |
| **Runner names / CLI help** | Infer execution_flow stages from command names or --help text. | Yes | ENTRYPOINT_CLASSIFICATION; public entry points use product-shaped language; no “L1–L9” or “sphere” in public help. |
| **Import graph** | Inspect public runtime .py files for internal imports. | Yes | tools/check_import_boundary.py; CI fails on violation. |

---

## 3. Non-Critical / Accepted Leaks

- **Package layout** — If the sealed package still ships core/ with layers/math, a determined party could infer “there are layers and math modules.” Mitigation: exclude from bundle or ship a flattened package that only exposes runtime + projection + services. Accept as non-critical if the actual method (formulas, dependency graph, topology) is not in the bundle.
- **Version string** — “Engine version 1.0” does not reveal method.

---

## 4. Done Condition

All major reconstruction paths are documented and either **blocked** or **accepted as non-critical**. Red-team reflection test is run (or checklist executed); no unmitigated leak path remains.
