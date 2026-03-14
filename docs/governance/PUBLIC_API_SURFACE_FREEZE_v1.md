# Public API surface freeze v1

**Status:** Frozen  
**Purpose:** The following commands and endpoints must remain stable for evaluators. Changes require a **surface version bump**.

---

## CLI (stable)

| Command / flag | Description |
|----------------|-------------|
| **analyze** | Run structural analysis on one text. |
| **compare** | Compare two texts (structural emphasis and confidence). |
| **batch-analyze** | Run structural analysis on multiple texts. |
| **--version** | Show runtime version, commit, and build info. |

No other CLI commands or flags are part of the frozen public surface. Adding, removing, or changing the behavior of these requires a surface version increment (e.g. 1.0 → 1.1) and release notes.

---

## API (stable)

| Method | Path | Description |
|--------|------|-------------|
| **POST** | **/analyze** | Body: `{"text": "..."}`. Returns analysis JSON. |
| **POST** | **/compare** | Body: `{"text1": "...", "text2": "..."}`. Returns comparison JSON. |
| **POST** | **/batch-analyze** | Body: `{"texts": ["...", ...]}`. Max 100 texts. Returns list of analysis results. |
| **GET** | **/health** | Liveness. Returns `{"status": "ok"}`. |
| **GET** | **/version** | Returns `{"version", "commit", "build"}`. |

No other HTTP endpoints are part of the frozen public surface. Adding, removing, or changing request/response shape for these requires a surface version bump and release notes.

---

## Version bump rule

- **Compatible** changes (e.g. additional optional fields, clarifications) may use patch version.
- **Incompatible** changes (removed or renamed fields, changed semantics, new required fields) require at least a minor surface version bump and must be documented.

---

*See SHIPPING_SURFACE_POLICY_v1.md, SHIPPING_SURFACE_FREEZE_v1.md, and EVALUATOR_GUIDE.md.*
