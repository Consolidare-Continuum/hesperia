# Projection → serialization chain v1

**Status:** Mandatory  
**Purpose:** The projection layer is the single most critical component. All serialization must follow one chain; no component may bypass it.

---

## Rule

**All serialization must pass through:**

```
projection  →  schema_guard  →  serializer
```

- **Projection:** Internal structure is mapped to public-safe form (e.g. `apply_public_projection`, `sanitize_public_trace`). Internal keys, coordinates, and topology are stripped or renamed.
- **Schema guard:** `validate_against_public_schema(output)` runs before serialization. Fails if any key in the output tree contains a forbidden substring (would leak internal architecture).
- **Serializer:** JSON (or other) output with deterministic ordering (e.g. `sort_keys=True`). No raw internal structures may be written in public mode.

No component may bypass this chain (e.g. writing raw layer output, dumping internal dicts, or skipping schema_guard).

---

## Enforcement

- Public entry points (CLI, API) call the service façade; the service returns projected data; CLI/API call `validate_against_public_schema` then serialize.
- Central artifact writer (`runtime/artifact_writer`) applies projection before write and uses deterministic JSON.
- Any new code path that emits public-facing output must use the same chain. Code review and sealing scan help catch bypasses.

---

## Components

| Step | Component / location | Responsibility |
|------|-------------------|----------------|
| Projection | `core/projection` | Map internal → public; strip reserved areas, internal keys, geometry language. |
| Schema guard | `runtime/shipping/schema_guard` | Walk full output tree; raise if any key is forbidden. |
| Serializer | CLI/API + `artifact_writer` | `json.dumps(..., sort_keys=True)` or equivalent; no internal-only writes in public mode. |

---

*See public_projection_layer.py, schema_guard.py, cli_main.py, api_main.py, artifact_writer.*
