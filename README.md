<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA

**Deterministic semantic engine.** Text in → attribution and layered analysis → reading scales and operational outputs. Config-driven, reproducible, no learning. The repository is in **Reference Architecture Definition (RAD) freeze**: one canonical snapshot, as-is.

**Author:** Platonov Igor ([@igareosh](https://github.com/igareosh)) · <https://igareosh.com>

---

## Status

| | |
| --- | --- |
| **State** | **RAD freeze** — architecture stable, boundaries enforced |
| **Proof** | [docs/ARCHITECTURE_FINGERPRINT.txt](docs/ARCHITECTURE_FINGERPRINT.txt) (SHA256 → commit → tag `HESPERIA_RAD_FREEZE` + OpenTimestamps) |
| **License** | Restricted Research Disclosure — inspection and reference only. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md). |

---

## Capabilities

The engine analyzes text deterministically and produces structured outputs:

- **Attribution** — Map text to a fixed conceptual space (lexicon-driven; no training). Tokens are attributed to families and areas; the result feeds all downstream layers.
- **Layered analysis** — A fixed pipeline (L1–L9) runs on attributed input: coverage and dominance, traversal and propagation, shadow comparison, retrieval and evidence, consistency and trust, then interpretation and branding. Each layer adds diagnostics; no learning, full reproducibility.
- **Reading scales (R1–R4)** — Segment text by sentence, paragraph, chapter, or full document and get per-segment metrics plus an aggregate book-style profile (scale deltas, structural signature).
- **Interpretation & fingerprint** — Structural state, tension and propagation summaries, event-style interpretation, and a Universal Structural Fingerprint (USF) for comparison or versioning. Optional logic and Prolog-style explanation outputs.
- **Guards & contracts** — Pipeline enforces invariants and output contracts; stability checks and safeguards keep outputs within defined bounds.

All behavior is config-driven (structure profile, policy mode, propagation and guard settings). Same input and config yield the same output.

---

## Use

- **Inspection and reference** — The repo is for study and technical evaluation. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md) for allowed use and restrictions.
- **Running pipelines** — Pass raw text (or a file) into the E2E flow or L1–L9 pipeline; artifacts are written to `assets/artifacts/` (e2e, layer runs, etc.). Use `--out` or `--out-dir` to choose paths.
- **API** — Run the HTTP server for health checks or to call the analyze endpoint (e.g. from another service). Responses are JSON.
- **Calibration and benchmarks** — Use the bundled calibration data and corpus/benchmark runners to reproduce runs or compare behavior; outputs are JSON/JSONL.
- **Validation** — Lexical validation (Dict A/B, family spec) and optional dossier validation ensure inputs and outputs match the expected schema.

For implementation, reproduction, or derivative use, explicit written permission from the author is required.

---

## What's in the repo

- **core/** — Deterministic computation (layers, attribution, contracts, policy, propagation).
- **runtime/** — Pipelines, API server, dossier, provenance.
- **lexicon/** — Dictionary systems (Dict A/B), build, validation.
- **tools/** — Calibration data, diagnostics, scripts.
- **assets/** — Artifacts (e2e outputs, layer runs, etc.).
- **tests/** — Pytest unit, integration, and e2e.
- **docs/** — Specs, architecture, governance.
- **legacy/** — Archive only; not part of the active stack.

---

## Run it

**Full E2E (all flows, 5 artifacts):**

```bash
python3 -m runtime.pipeline.run_e2e_all
```

Outputs under `assets/artifacts/e2e/`. Optional: `--out-dir PATH`, `--text "..."`.

**L1–L9 pipeline (single run):**

```bash
python3 -m runtime.pipeline.run_l1_through_l9 --out /path/out.json
```

**API server:**

```bash
python3 -m uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000
```

**Tests:**

```bash
python3 -m pytest tests/ -q
# E2E flows only:
python3 -m pytest tests/test_e2e_flows.py -v
```

---

## Quick reference

| Action | Command |
| --- | --- |
| E2E (all) | `python3 -m runtime.pipeline.run_e2e_all` |
| L1–L9 | `python3 -m runtime.pipeline.run_l1_through_l9 [--out path.json]` |
| API | `python3 -m uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000` |
| Tests | `python3 -m pytest tests/ -q` |

---

## Further reading

- **Evidence chain & timestamp** — [docs/ARCHITECTURE_FINGERPRINT.txt](docs/ARCHITECTURE_FINGERPRINT.txt)
- **Legal terms** — [LEGAL_NOTICE.md](LEGAL_NOTICE.md)
- **Architecture & specs** — [docs/](docs/) (system spec, boundaries, topology invariants, layer order, USF schema)
- **Agent/contributor rules** — [AGENTS.md](AGENTS.md)

---

HESPERIA RAD · © 2026 Platonov Igor / igareosh.com · Restricted Research Disclosure
