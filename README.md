# Hesperia

Deterministic semantic engine: text → attribution → layers L1–L9 → reading scales R1–R4 → operational outputs. Single version **v0.5** end-to-end.

---

## Version and status

| Item | Value |
|------|--------|
| **Version** | v0.5 |
| **Status** | Reference architecture: deterministic `core` + orchestrated `runtime`. Version suffixes stripped from active modules; legacy versioned tools live under `legacy/deprecated/`. |
| **Active stack** | `core/`, `runtime/`, `lexicon/` |

---

## Repository layout

```text
hesperia/
├── core/                    # Deterministic computation
│   ├── attribution/         # Tokenize, attribute, structural + v06 paths
│   ├── contracts/          # Layer I/O contracts
│   ├── layers/             # layer_1 … layer_9
│   ├── math/               # core_math, dict_b, core_math_legacy
│   ├── policy/             # Interpretation policy
│   ├── propagation/        # Guard pipeline, R1–R4, output contracts
│   ├── stability/          # Stability deltas
│   └── topology/           # Invariant catalog, family/area
├── runtime/
│   ├── api/                # HTTP API (e.g. uvicorn)
│   ├── dossier/            # HSD schema, writer, index
│   ├── pipeline/           # analyze, run_* entrypoints, batch
│   ├── provenance/         # Run manifest, engine provenance
│   └── runners/            # Reference pipeline CLI
├── lexicon/
│   ├── curated/            # Dict A/B sources, family spec
│   ├── frozen/             # Built/frozen dicts, v06
│   ├── build/              # Build definitions
│   └── validation/         # validate_lexical, etc.
├── tools/
│   ├── calibration/        # Calibration data (e.g. 100 sentences)
│   ├── diagnostics/        # Checksum/operational checks
│   └── scripts/            # Service/deploy configs
├── assets/
│   ├── artifacts/          # All produced outputs (e2e, layer_runs, …)
│   ├── models/
│   └── data/
├── tests/                   # Pytest unit + integration + e2e
├── docs/                    # Architecture, specs, boot
└── legacy/                  # Archive + deprecated (not on boot path)
```

---

## Elements

### Core

- **Attribution**  
  Normalize → tokenize → attribute (Dict A / Dict B). Structural path: `core.attribution.structural` (`load_dict_a`, `load_dict_b`, `attribute`, `run_attribution_pipeline`). Optional v06 path via `core.attribution.attribution` and shared helpers in `attribution_shared`.

- **Layers 1–9**  
  L1 (topology/tokens) → L2 (propagation) → L3 (shadow) → L4 (retrieval) → L5 (shortfall) → L6 (metrics) → L7 (decision/trust) → L8 (interpretation) → L9 (branding). Contract: `LayerInput` → layer `run()` → result + diagnostics. Registry: `runtime.pipeline.layer_registry`.

- **Propagation**  
  Guard pipeline (sigma/gamma), output contracts (6-key minimal result), R1–R4 segmenters, unit builder, ESM defaults, safeguard state machine, invariant enforcer.

- **Math**  
  `core_math`: config, analyze, fusion; `dict_b`: family-vector pipeline; `core_math_legacy`: legacy 22_SPEC reference (optional).

- **Topology**  
  Invariant catalog (families, areas, sides), forward mapping, validation.

### Runtime

- **Pipeline**  
  `analyze`: single entry for “text → 6-key + extended (attribution, dict_b, optional R1–R4)”.  
  `run_l1_through_l9`: full L1–L9 for one text; optional `--write-dossier`, `--validate-dossier`, `--profile`, `--policy-mode`.  
  `run_e2e_all`: runs all flows and writes planned e2e artifacts.  
  `run_e2e_sentence`, `run_r1_r4_pipeline`, `run_sphere_math_values`, `run_sphere_math_100_sentences`, `run_l1_l2`, `run_l1_l2_l3`, `batch_runner`, `reading_scales`.

- **API**  
  `uvicorn runtime.api.main:app` for HTTP (e.g. `/health`, analyze endpoint).

- **Dossier**  
  HSD schema (HSD_v1.0), writer, index, validation.

### Lexicon

- **curated**  
  Dict A/B sources, family spec, optional surface map.
- **frozen**  
  Built dicts (e.g. B0/B1, A_CORE_STAR_MAP), v06 dir (`dict_a_v06.jsonl`, `family_prior_v06.json`).
- **validation**  
  `validate_lexical.py` and related; versioned validators moved to `legacy/deprecated/lexicon_validation/`.

### Tools

- **calibration**  
  Data (e.g. `calibration_100_sentences.json`) used by sphere_math_100 and e2e. Versioned calibration scripts → `legacy/deprecated/tools/calibration/`.
- **diagnostics**  
  Checksum/operational scripts; versioned ones → `legacy/deprecated/tools/diagnostics/`.
- **scripts**  
  Service/config (e.g. nginx, systemd).

---

## Outcomes and outputs

### E2E (unified run)

One command produces all planned e2e artifacts under `assets/artifacts/e2e/`:

```bash
python3 -m runtime.pipeline.run_e2e_all
```

Optional: `--out-dir PATH`, `--text "..."`.

| Output file | Flow | Description |
|-------------|------|-------------|
| `run_output_e2e_sentence.json` | analyze | 6-key result + attribution + dict_b + R1–R4 units & book_profile |
| `run_output_e2e_l1_l9.json` | L1–L9 | Full layer stack (L1…L9 + diagnostics) for one text |
| `run_output_e2e_r1_r4.json` | R1–R4 | Units + book_profile (scale deltas, structural signature) |
| `run_output_e2e_sphere_math_values.json` | Sphere math | L1–L9 values for single text (no commentary) |
| `run_output_e2e_sphere_math_100.json` | Sphere math 100 | L1–L9 for first N calibration sentences |

No calibration of result values; outputs assert existence and shape only.

### Other pipeline outputs

- **L1–L9 only**  
  `python3 -m runtime.pipeline.run_l1_through_l9 --out /path/out.json`  
  Writes JSON with `L1`…`L9`, `diagnostics`, `run`; optional dossier write/validate.

- **Single-sentence analyze**  
  `python3 -m runtime.pipeline.run_e2e_sentence [--text "…"] [--out path.json]`  
  Same as e2e sentence flow; default out: `assets/artifacts/e2e/run_output_e2e_sentence.json`.

- **R1–R4 only**  
  `python3 -m runtime.pipeline.run_r1_r4_pipeline [--text "…" \| --file path] [--out-dir dir] [--levels R1,R2,R3,R4]`  
  Writes `units.json`, `book_profile.json` (and optional JSONL) under `--out-dir`.

- **Sphere math**  
  `run_sphere_math_values.py` → one JSON (L1–L9 values).  
  `run_sphere_math_100_sentences.py` → JSON for N sentences (`--sentences`, `--limit`).

- **Artifacts layout**  
  All generated outputs under `assets/artifacts/`: `e2e/`, `layer_runs/`, `calibration/`, `lex/` (see `assets/artifacts/README.md`).

---

## Commands (quick reference)

| Action | Command |
|--------|---------|
| E2E (all flows, 5 outputs) | `python3 -m runtime.pipeline.run_e2e_all` |
| L1–L9 pipeline | `python3 -m runtime.pipeline.run_l1_through_l9 [--out path.json]` |
| Analyze (library) | `from runtime.pipeline.analyze import analyze` |
| API server | `python3 -m uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000` |
| Full test suite | `python3 -m pytest tests/ -q` |
| E2E tests only | `python3 -m pytest tests/test_e2e_flows.py -v` |
| Lexical validation | `python3 lexicon/validation/validate_lexical.py` |

---

## Tests

- **Location**  
  `tests/`: unit, integration, e2e (e.g. pipeline execution, attribution, guard pipeline, invariant, adversarial, dossier, batch, e2e flows).

- **E2E flows**  
  `tests/test_e2e_flows.py`: one test per flow (analyze sentence, L1–L9, R1–R4, sphere_math_values, sphere_math_100) plus one that runs `run_e2e_all` and checks all planned artifacts exist.

- **Run**  
  `python3 -m pytest tests/ -v` (optionally `--ignore=tests/energy_invariants_stress.py`).

---

## Governance and docs

- **Agent rules**  
  `AGENTS.md`: layout, v0.5, no legacy paths in active work, path/command hygiene.

- **Architecture**  
  `docs/architecture/` (e.g. ENGINE_BOUNDARIES.md, SYSTEM_OVERVIEW.md).

- **Specs / boot**  
  `docs/specs/`, `docs/boot/`.

- **Legacy**  
  `legacy/`: archive and deprecated (versioned calibration, validation, build scripts). Do not modify unless doing explicit archival work.

---

## Data flow (high level)

```text
lexicon (curated/frozen) ──► core/attribution (structural or v06)
                                    │
                                    ▼
core/layers L1→…→L9  ◄── contracts, topology, math, propagation
                                    │
                                    ▼
runtime/pipeline (analyze, run_*, batch) ──► artifacts (e2e, layer_runs, …)
                                    │
                                    ▼
runtime/api (optional) ──► HTTP responses
```
