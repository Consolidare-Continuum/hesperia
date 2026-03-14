# Shipping reflection audit v1

**Status:** Active  
**Purpose:** Reduce reverse-engineering friction. Check that shipped artifacts (binary, image, help text, schema, package content) do not leak internal model. This is redistribution friction, not absolute security.

---

## 1. Strings scan on binary and image (S7-T1)

Run on the **shipped** CLI binary and (if feasible) inside the API image filesystem:

**Forbidden leaked terms:** sphere, hex, topology, bridge, layer, area11, family240 (and variants: area 11, 288 families, side_id, propagation path, etc.).

**Procedure:**

- **CLI binary:** `strings dist/hesperia-cli.bin | grep -iE 'sphere|hex|topology|bridge|layer|area11|family240|side_id|288 families'`  
  **Expected:** No matches (or only in obfuscated/minimal form). Nuitka and stripping reduce string leakage; any remaining must be reviewed.

- **API image:** Export image filesystem or run a container and inspect:  
  `docker run --rm hesperia-api:latest find /app -type f -name '*.py' -exec strings {} \; 2>/dev/null | grep -iE 'sphere|hex|topology|bridge|layer|area11|family240'`  
  **Expected:** No matches in user-facing paths; internal code may contain terms but must not appear in response bodies or logs.

Record results: PASS if no forbidden terms in binary string table or in API response/log paths. FAIL if any term appears in a way that teaches the model.

---

## 2. Help text and schema scan (S7-T2)

Same rule as CLI text audit (SHIPPING_CLI_TEXT_AUDIT_v1):

- **CLI help:** `./hesperia-cli.bin --help` and each subcommand `--help`. Grep for forbidden terms. **Expected:** PASS (no sphere, hex, layers, bridge, topology, reserve).
- **API OpenAPI/docs:** If Swagger or ReDoc is enabled, inspect description and example values. **Expected:** No internal vocabulary.
- **Public schema:** assets/public/public_output_schema.json and any schema shipped in the bundle. **Expected:** No property names or descriptions that reveal topology (hex, side_id, 12 areas, 288 families, layer count, bridge).

Record: PASS if all help and schema text is public-safe. FAIL if any reflective term appears.

---

## 3. Package content inspection (S7-T3)

Inspect the **release bundle** (hesperia-eval/ or the zip/tarball):

- **No accidental source:** No full repo clone; no docs/internal, legacy/, or tests/ in the bundle.
- **No specs:** No internal registries (MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY) or specs history.
- **Only sealed entry points:** Advertised commands are analyze, compare, batch-analyze, serve. No scripts named run_l1_l2, run_e2e_all, etc. as primary entry points.

Record: PASS if package contains only binary, image tar, examples, public schema, quickstart, limitations, checksums. FAIL if internal docs or source tree included.

---

## 4. Reflection test (S7-T4)

**Question:** Can a reviewer infer the larger model from command names, strings, outputs, docs, schemas, or image layout?

| Channel | What reviewer could try | Mitigation / Expected |
|---------|-------------------------|------------------------|
| **Command names** | Infer pipeline from "analyze", "compare", "batch-analyze". | Product-shaped; no "L1", "layer", "sphere". PASS if only these four. |
| **Strings in binary** | Extract strings to find formulas or structure. | Nuitka + strip; no obvious topology strings. PASS if scan (1) clean. |
| **Outputs** | Infer 12 areas or 288 families from response shape. | Projection: 10 macro-domains, 240 policy families; no reserved indices. PASS if outputs match public schema. |
| **Docs** | Read quickstart or bundled governance. | No internal method; only usage and limitations. PASS if no layer/topology description. |
| **Schemas** | Infer geometry from property names. | public_output_schema uses macro_domain_vector, policy_family_counts. PASS if no side_id, hex, area_id. |
| **Image layout** | Inspect filesystem in container. | Only /app with runtime, core, lexicon, assets. No docs/internal. PASS if layout minimal. |

**Result:** Document each channel as PASS or FAIL. Overall: PASS if a reviewer cannot reconstruct the internal model (sphere, hex grid, layer count, bridge logic, propagation method) from the shipped artifact alone.

**Done when:** Major reconstruction channels are blocked or reduced to low-value hints (no high-value leak from commands, outputs, strings, docs, schemas, or image layout).

---

## 5. What this will and will not achieve

**It will:**

- Stop casual inspection.
- Prevent straightforward source reading (binary + no source in bundle).
- Keep product review focused on outputs.
- Make reconstruction of the bigger model materially harder.

**It will not:**

- Make reverse engineering impossible.
- Stop a highly motivated expert from learning something from behavior.
- Protect secrets if you ship rich debug traces or revealing strings.

Sealing work (projection, vocabulary, boundary checks) matters more than the compiler choice. This audit verifies that the shipped artifact does not undo that sealing.

---

## 6. Deliverable

This document is the **SHIPPING_REFLECTION_AUDIT_v1** deliverable. Run the procedures above before release; record PASS/FAIL per section; remediate any FAIL before shipping.
