# Shipping public text scan v1

**Status:** Active  
**Purpose:** Check CLI help, API docs, public schema, examples, README for forbidden terms. Public-facing text must stay product-only.

---

## 1. Surfaces to scan

| Surface | Location | Check |
|---------|----------|--------|
| **CLI help** | Output of hesperia-cli.bin --help and each subcommand --help | No sphere, hex, topology, bridge, layer, family reserve, area counts. |
| **API docs** | OpenAPI/Swagger description, endpoint descriptions, example values | Same. |
| **Public schema** | assets/public/public_output_schema.json (and any schema in bundle) | No property names or descriptions that reveal topology (hex, side_id, 12 areas, 288 families). |
| **Examples** | examples/*.json, examples/README.md | No internal vocabulary in keys or comments. |
| **README / quickstart** | release/README.md, any quickstart in bundle | No internal method description; only usage and limitations. |

---

## 2. Procedure

1. Capture CLI help to a file; grep for forbidden terms.
2. If API serves /openapi.json or /docs, capture and grep.
3. Open public_output_schema.json and examples; grep for forbidden terms.
4. Open release/README.md and quickstart; grep for forbidden terms.

Forbidden pattern (same as elsewhere): sphere, hex, topology, bridge, layer, family reserve, 12 areas, 288 families, side_id, propagation path, bridge nodes.

---

## 3. Done condition

**Done when:** Public-facing text stays product-only (no reflective terms in help, API docs, schema, examples, README).
