# Historical reference (pre-refactor)

# HESPERIA v0.3.2 — implementation report (Gena)

**Date**: 2026-02-23
**Spec**: 26_SPEC__v0_3_2_Repo_State_Accurate.txt
**Status**: Implemented as required; gaps documented.

---

## 1. Implemented as required

| Spec section | Requirement | Implementation |
|--------------|-------------|----------------|
| **§1** | Non-negotiable constants (12/24/250/6, 432k sides, indexing) | `invariant_catalog.py`: frozen; single source. `invariant_enforcer` + `shadow_layer` + `lexical_loader` use it. |
| **§2.1** | Minimal operational result: exactly 6 keys, int 0..11 and 0..287, finite floats | `output_contracts_v032.to_minimal_operational_result()`; used by serve_v032 after `run_api()`. |
| **§2.2** | Minimal error result: exactly 3 keys (error, message, code) | `output_contracts_v032.make_error_result()`; used on 400/413/500. |
| **§5** | Guard discipline: no API path returns minimal result without Σ | `run_api()` and `run_api_with_guards()` both call Sigma; `serve_v032` uses `run_api()` only. No bypass. |
| **§6** | GET /health, POST /hesperia/analyze, OPTIONS | `serve_v032.py`: GET /health → `{"ok":true,"service":"hesperia","version":"0.3.2"}`; POST /hesperia/analyze → 6-key or error; OPTIONS for CORS. Entry: `run_simulation.py serve [port]`. |
| **§7.1** | Fix README mismatch | README rewritten: lists actual modules; notes missing geometry.py, semantic_engine.py, metrics.py, phase_engine.py. |
| **§7.2** | Minimal runnable entry point; /health and /hesperia/analyze | `run_simulation.py` full \| chroma \| serve; `serve_v032.py` implements HTTP API. |
| **§7.3** | Deterministic tests; Σ enforcement; bounds | test_invariant_v03, test_guard_pipeline_v031, test_adversarial_v03, hesperia_v03_core_math.py test. |
| **§7.4** | Document versioning | `RELEASE_NOTES__v0_3_2.txt` added. |

---

## 2. Gaps (documented, not blocking v0.3.2 spine)

- **Text → (dominant Area, dominant Family)** (pipeline Step 1): Attribution (Dictionary A/B → seed sides) not wired into POST /hesperia/analyze. Request body `{"text":"..."}` accepted; server runs deterministic core only. Same 6-key contract will apply when attribution is added.
- **Steps 0–2**: Normalize/tokenize/length-cap and region seed from attribution not in server path. Length cap (10k) applied to request body size only.
- **Shadow in HTTP path**: shadow_layer.py exists and is integrable; server returns base-plane result only. Shadow is first-class in codebase, not yet in the single-call analyze endpoint.

---

## 3. Files added or changed

- **Added**: `26_SPEC__v0_3_2_Repo_State_Accurate.txt` (normative spec)
- **Added**: `sphere_rag/output_contracts_v032.py` (6-key + error contracts)
- **Added**: `sphere_rag/serve_v032.py` (HTTP server)
- **Added**: `RELEASE_NOTES__v0_3_2.txt`
- **Added**: `governance/GENA-V032-IMPLEMENTATION-REPORT.md` (this file)
- **Updated**: `sphere_rag/README.md` (repo-accurate module list)
- **Updated**: `sphere_rag/run_simulation.py` (added `serve` mode)

---

## 4. Verification

- `run_api()` → `to_minimal_operational_result()` yields exactly 6 keys; dominant_area ∈ [0,11], dominant_family ∈ [0,287]; governance/loopability ∈ [0,1]; tension_energy/obstacle_score ≥ 0.
- Error result: 3 keys only.
- No path returns minimal result without Sigma (run_api and serve both enforce).

**SIGNED: Developer (Gena) | v0.3.2 implementation report | 2026-02-23 | CLIENTS/hesperia**
