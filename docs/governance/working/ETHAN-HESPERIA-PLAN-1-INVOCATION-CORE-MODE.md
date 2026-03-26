<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia Plan 1 — internal calibration invocation (Ethan)

**Purpose**: Define **one internal invocation** that runs **all** core-mode functions and scripts on the **existing matrix**, with **no books** and **no statements**, and logs **all outputs** (every variable, every summary) for **calibration** and **general sense of state**. **Owner**: Ethan. **Date**: 2026-02-18.

**Internal, not main spec.** This is an **internal function for calibration**. The runner outputs **its own results** (timestamped log dir with full JSON and run.log). It is **not** the main Hesperia product spec; the main spec is core mode MVP (mode, scope, output contract) and the product/release docs. Plan 1 exists so we can run everything in core mode in one go and inspect all variables and outputs — calibration and state visibility.

**Refs**: [ETHAN-HESPERIA-CORE-MODE-MVP.md](ETHAN-HESPERIA-CORE-MODE-MVP.md), [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md), [CONTEXT-RAG-PACKET-SCHEMA.md](CONTEXT-RAG-PACKET-SCHEMA.md).

---

## 1. Scope — core mode only (no books, no statements)

- **In scope**: matrix_run, context_rag (no retrieval), hesperia_logic (path/area/family only), apple_path_imprint, apple_involvements.
- **Out of scope**: `--query`, `--area_id`, `--family_name` (no retrieval); no statement_set; no books chunks. Matrix = existing CSV or Chroma layer=hesperia_families (read-only coordinates).

---

## 2. Plan 1 — single invocation sequence

One run that executes in order and **logs every output**:

| Step | Script / function | Invocation / raw_text | What to log |
|------|-------------------|--------------------|-------------|
| 1 | **matrix_run.py** | `--start 0 --direction 1 --steps 12` (default CSV; optional `--chroma`). From repo root. | Full JSON stdout: matrix_source, geometry, path_params, road_coordinates, border_passings, traversal_length, is_loop, loopability. All variables used inside (e.g. area_to_families keys, row counts) may be logged by runner. |
| 2 | **context_rag.py** | No `--query`, no `--area_id`, no `--family_name`. Same `--start 0 --direction 1 --steps 12`. Core mode = no retrieval block. | Full packet JSON: matrix_source, calculable (same shape as matrix_run), coherence_hints. No retrieval key. Log full packet and any intermediate (calculable_raw, coherence_hints build). |
| 3 | **hesperia_logic** | Path from step 1: `path = [(r["area_id"], r["global_id"]) for r in road_coordinates]`. Context: `state = {}`, no statement_set. Call `run_traversal_with_safeguard(path, input_context)`. | Full summary: status (OK or SAFEGUARD_STOP), state, path, steps_done; or safeguard payload (fail_count, fail_trace, obstacle_region). Log path length, input_context keys, and summary dict. |
| 4 | **apple_path_imprint** | Raw_text: matrix_run JSON from step 1 (stdin or temp file). `--run-id core_plan1`. | Stored file path; file contents (path list). Log run_id, store path, and the written path JSON. |
| 5 | **apple_involvements** | Raw_text: stored path from step 4 (e.g. `--path cluster/chroma-server/apple_paths/core_plan1.json`) or matrix_run JSON. | Full output: areas, families, area–family pairs, counts. Log full JSON and any text summary. |

---

## 3. Logging requirement — general sense of state

All outputs SHALL be written so that:

- **Every** script’s **stdout** (JSON or text) is captured.
- **Every** summary dict (matrix_run out, context_rag packet, hesperia_logic return, apple involvements) is logged in full (e.g. JSON).
- **Key variables** (path length, road_coordinates length, geometry constants, path_params, status, steps_done, fail_count if any) are visible in one place (e.g. a single run log or summary section).
- Logs are **timestamped** and **one directory per run** (e.g. `core_mode_logs/YYYY-MM-DD_THHMMSS/`) so we can compare runs and get a reproducible snapshot of state.

---

## 4. Runner script (recommended)

A single runner script **run_core_mode_invocation.py** (or equivalent) SHALL:

1. Run from **repo root** (or set REPO_ROOT / HESPERIA_DATA_DIR so matrix CSV is found).
2. Execute steps 1–5 in order; capture stdout/stderr and summary dicts.
3. Write to a **timestamped log dir**:
   - `matrix_run.json` — full matrix_run output.
   - `context_rag_packet.json` — full context_rag packet (core mode).
   - `hesperia_logic_result.json` — full return from run_traversal_with_safeguard.
   - `apple_path_stored.json` — path written by apple_path_imprint (or path to file).
   - `apple_involvements.json` — full apple_involvements output.
   - `run.log` — concatenated log: timestamp, step names, key variables (path length, status, steps_done, geometry.AREA_COUNT, etc.), and any stderr.
4. Use **existing matrix only** (CSV default; optional `--chroma` for run if Chroma available).
5. **No** `--query`, **no** `--area_id`, **no** `--family_name`; **no** statement_set; **no** books.

Invocation example (from repo root):

```bash
python cluster/chroma-server/run_core_mode_invocation.py [--chroma] [--log-dir PATH]
```

---

## 5. Success criteria

- One run produces one log dir with all five outputs (matrix_run, context_rag, hesperia_logic, apple imprint path, apple involvements).
- All variables and summary shapes listed in §2 are present in the logs.
- Core mode is respected: no retrieval, no statement_set, no books in any step.
- A human or agent can read the log dir and infer **current state** of matrix, path, calculable, coherence hints, logic summary, and apple path/involvements.

---

## 6. Summary

| Item | Statement |
|------|-----------|
| **Role** | Internal calibration harness; not the main product spec. Runner outputs its own results (log dir). |
| **Plan** | Plan 1 = one invocation that runs matrix_run → context_rag (core) → hesperia_logic (run_traversal_with_safeguard) → apple_path_imprint → apple_involvements on existing matrix. |
| **Mode** | Core only: no books, no statements, no retrieval. |
| **Logging** | All outputs and key variables to a timestamped log dir; full JSON for each step. |
| **Goal** | Calibration and general sense of state (reproducible, inspectable). |

---

**SIGNED: Architecture (Ethan) | Hesperia Plan 1 — internal calibration invocation, core mode | 2026-02-18 | governance**
