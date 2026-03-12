<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# R1–R4 integration contract

**Purpose:** Contract for integrating the R1–R4 reading-scale pipeline (Units, BookProfile) with analyze, context_rag, API, and guards. **Owner:** Ethan (I1). **Refs:** [TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md](../governance/TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md), [SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md).

---

## 1. Entry points

| Entry point | Module | Function | Inputs | Outputs |
|-------------|--------|----------|--------|---------|
| Full pipeline | `sphere_rag.r1_r4_pipeline` | `run_full_pipeline(text, book_id=..., levels=...)` | text, book_id, dict_a/dict_b/assets_root (optional), levels (R1,R2,R3,R4) | (units: list[Unit], book_profile: BookProfile) |
| Pipeline to JSON | `sphere_rag.r1_r4_pipeline` | `run_full_pipeline_to_json(text, book_id=..., levels=..., out_units=, out_profile=, validate=)` | same + optional paths, validate flag | {"units", "book_profile", optional "validation"} |
| R1-only | `sphere_rag.r1_r4_pipeline` | `run_r1_pipeline(text, book_id=...)` | text, book_id, optional dict_a/dict_b/assets_root | (units, book_profile) |
| CLI | `sphere_rag.run_r1_r4_pipeline` | — | `--text`, `--file`, `--book-id`, `--levels`, `--out-dir`, `--validate` | Writes units.json, book_profile.json |

All outputs are JSON-serializable and conform to Part C schemas (Unit, BookProfile, SI_metrics). Validate with `--validate` (requires jsonschema) or `_validate_units_and_profile`.

---

## 2. Inputs / outputs summary

- **Inputs:** `text` (string), `book_id` (string, default `"book"`), optional `levels` (subset of R1,R2,R3,R4), optional dict_a/dict_b/assets_root for attribution.
- **Outputs:** `units` (list of Unit dicts), `book_profile` (BookProfile dict: book_id, level_averages, scale_deltas, turning_points, structural_signature). Optional validation result when `validate=True`.
- **Attribution (surface + Dict B):** Pipeline loads Dict B and surface map from the **same** `assets_root` (e.g. `hesperia_lex/curated`); `load_dict_b_v033(assets_root=assets)` and surface map use that root so token resolution (surface → structural key) and Dict B fallback share the same lex tree. This avoids token_count 0 and ensures all L1–L9 variables and SI_metrics appear on run. R1-only path (`run_r1_pipeline`) also loads and passes surface_map.

---

## 3. Where R1–R4 may be consumed

### 3.1 analyze (`sphere_rag/analyze.py`, `analyze_v033`)

- **Wired (I2):** When `r1_r4=True`, analyze runs the R1–R4 pipeline and attaches `extended["r1_r4"] = {"units": [...], "book_profile": {...}}`. On pipeline failure, `extended["r1_r4"] = {"error": str, "units": [], "book_profile": None}`.
- **Parameters:** `analyze(..., r1_r4=False, r1_r4_book_id="book", r1_r4_levels=None)`. `r1_r4_levels` defaults to `["R1","R2","R3","R4"]` when r1_r4 is True.
- **Runbook:** Call `minimal, extended = analyze(text, r1_r4=True)`; then `extended.get("r1_r4", {}).get("units")` and `extended["r1_r4"]["book_profile"]` (if no error).

### 3.2 context_rag (if present)

- **Current:** Context packet is built from matrix_run, Chroma, etc.; no BookProfile.
- **Integration (optional):** If context_rag is extended to include reading-scale summary, add an optional block (e.g. `reading_scale` or `book_profile`) with level_averages or structural_signature. **Not wired by default.** — task I3.

### 3.3 API (`api/main.py`)

- **Wired (I3):** POST /hesperia/analyze returns **two outputs:** `result` (6-key minimal) and `extended` (total_tokens, family_vector, dict_b, etc.). Request body may include `r1_r4: true`; when set, the R1–R4 pipeline runs and `extended.r1_r4` is populated with `{ units, book_profile }` (or `{ error, units, book_profile }` on failure).
- **Response shape:** `{ "result": { dominant_area, dominant_family, governance, loopability, tension_energy, obstacle_score }, "extended": { total_tokens, ... optional r1_r4 } }`.

---

## 4. Guard integration (Σ/Γ/Θ)

- **Unit.flags.decision_code** and **SI_metrics** (trust_tier, band, leakage, entropy, etc.) are produced by the R1–R4 pipeline and are **reference-only** for the current guard pipeline (Sigma/Gamma/Theta in `guard_pipeline`, `core_math`). No automatic wiring: guard pipeline continues to use its existing inputs (traversal, area_hop_count, etc.).
- **Future wire:** If a later spec requires it, Unit-level or BookProfile-level signals (e.g. any Unit with decision_code != OK, or SI_metrics breach) can be fed into a guard layer or gate. Contract: document that decision_code and SI_metrics are available on each Unit and in level_averages for use by guards when wiring is approved.

---

## 5. Optional wiring tasks (Grace-assigned)

| Task | Owner | Description | Status |
|------|--------|-------------|--------|
| I2 | Gena | Wire R1–R4 into analyze: optional flag/mode to run pipeline and attach units/book_profile to result. | **Done:** `analyze(..., r1_r4=True, r1_r4_book_id=..., r1_r4_levels=...)` → `extended["r1_r4"]`. |
| I3 | Gena | API / context_rag: optional response field or context block for BookProfile/level_averages. | **Done:** API returns `{ result, extended }`; body `r1_r4: true` adds `extended.r1_r4`. |

**Default:** R1–R4 off unless body `r1_r4: true`. API always returns `{ result, extended }`; second output is `extended`.

---

**SIGNED: Architecture (Ethan) | R1–R4 integration contract | 2026-02-27 | docs**
