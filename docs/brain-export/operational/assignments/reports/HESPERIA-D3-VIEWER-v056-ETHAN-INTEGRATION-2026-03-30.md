# HESPERIA-D3-VIEWER v0.5.6 — Ethan integration and traceability (later scope)

## Frozen deliverable (this drop)

- **Path**: `hesperia/tools/inspection_viewer/` (`index.html`, `app.js`, `styles.css`, `data_loader.js`, `graph_builder.js`).
- **Input contract (single source of truth)**: `hesperia/outputs/inspection/session_trace.json` — schema locked in task spec; loader **fails fast** on structural invalidity; field-level gaps render as **missing** (no inference).
- **CB-1**: No scoring, recalculation, mutation of engine output, topology edits, hidden normalization, or node merging in the viewer.

## Local run (acceptance)

- **HTTP (recommended)**: Document root must be **`hesperia/`** so resolved URL `/outputs/inspection/session_trace.json` exists:
  - From repo: `hesperia/serve_viewer.sh` (or `cd hesperia && python3 -m http.server 8765`)
  - Viewer: `http://127.0.0.1:8765/tools/inspection_viewer/index.html`
- **404**: Serving from `tools/inspection_viewer/` makes `/outputs/...` wrong — always use **`hesperia/`** as document root.
- **Session 11-09 (engine aggregate report, not graph trace)**: `hesperia/outputs/reports/extended_corpus_report_v052_5_session_11_09.json` — URL when served: `/outputs/reports/extended_corpus_report_v052_5_session_11_09.json`. Graph viewer expects `session_trace` schema; this file is metrics-only until export exists.
- **file://**: Resolved path is correct on disk, but browsers often block `fetch`; use **Load file** and pick `hesperia/outputs/inspection/session_trace.json`.

## Full integration — word maps traceability (out of scope for v0.5.6)

**Objective**: Every visual element in the viewer maps 1:1 to engine-emitted trace fields; extend that to **per-token / per-dict-entry** lineage in lexical assets (dict_a / dict_c / dict_b / links) without recomputation in the UI.

**Phase 0 — Engine export (implemented on hesperia repo, not in cursor tree)**

1. **`tools/extended_corpus_report.py`** — flag **`--session-trace-dir PATH`**: same `run_dlcr_pipeline` passes used for metrics also emit `session_trace_*.json` (no second DLCR run). Per chunk: `session_trace_<corpus_stem>_chunk_NNN.json`; if exactly one chunk, also **`session_trace.json`**.
2. **`tools/session_trace_export.build_session_trace`**: maps `canonical_text`, `span_resolutions`, `concept_weights`, `area_activation` + `load_dlcr_concept_index` → D3 contract; **`areas[].label`** = Ethan RU topology line (`dlcr_display_labels.AREA_CODE_RU`); optional top-level **`terminology`** (viewer ignores).
3. Example (prichindel, repo `/data/hesperia/hesperia`):  
   `HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_5 python3 tools/extended_corpus_report.py --corpus tests/fixtures/tfp_calibration/session_11_09_2023_plain.txt --version v0_6_0_clr_v052_5 --chunk-words 600 --out outputs/reports/extended_corpus_report_v052_5_session_11_09.json --session-trace-dir outputs/inspection`  
   Copy or sync `outputs/inspection/session_trace*.json` into **cursor** `hesperia/outputs/inspection/` for the LAN static viewer (`hesperia/serve_viewer.sh`).

**Phase 1 — Traceability hooks**

1. **Word-map anchor**: For each match, optional `source_dict` + `source_key` (or line id) in JSON when engine has it — viewer displays as opaque strings (no resolution logic in UI).
2. **Validator**: CI check that export JSON validates against a machine schema (JSON Schema) matching the frozen contract.
3. **Regression**: Golden `session_trace.json` fixtures under `hesperia/outputs/inspection/fixtures/` for snapshot tests of loader + graph edge counts.

**Phase 2 — Product demo layer**

1. Host viewer behind static server on cluster (Abelard) or ship as zip; same read-only contract.
2. Optional: deep-link query `?trace=url` only if served with explicit CORS policy (no silent cross-origin inference).

**RACI sketch**: Ethan — contract freeze and gate severity; Gena — runtime/export; Noah — dict row ids and fixture corpora; Liam — CI schema gate; Grace — triage row when export lands in workflow.

---

SIGNED: Governance (Ethan) | Hesperia inspection viewer integration plan | 2026-03-30 | v0.5.6 viewer + later traceability phases
