<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia Engine Dynamics

**Canonical release: v0.5.1** — deterministic multiscale semantic physics: **concept → hex → family → area → product signals → HSPR**, with a sealed **L1–L9** structural execution flow, **KME**, and optional **TRIZ** (not on the minimal product HTTP surface by default). Same input text and configuration yield the same output (no learning in the core path).

**Author:** Platonov Igor ([@igareosh](https://github.com/igareosh)) · [igareosh.com](https://igareosh.com)

---

## Status

| | |
| --- | --- |
| **Product line** | **Hesperia Engine Dynamics** (Engine Dynamics v0.5) |
| **Version authority** | Root [`VERSION.yaml`](VERSION.yaml) (and `hesperia/VERSION.yaml` real file copy, content-identical) + [`pyproject.toml`](pyproject.toml) `version` |
| **Sealed public surface** | Mandatory projection via [`hesperia.engine.projection`](hesperia/engine/projection/); see [`docs/PUBLIC_PRODUCT_SURFACE.md`](docs/PUBLIC_PRODUCT_SURFACE.md) |
| **Release audit** | [`release/v0.5.1/`](release/v0.5.1/) — `python3 tools/release/build_release_audit_v0_5_1.py` ([`final_gate_status.json`](release/v0.5.1/final_gate_status.json) → `sealed: true` on clean tree). Historical: [`release/v0.5.0/`](release/v0.5.0/). |
| **License** | **Restricted Research Disclosure** — inspection and reference only. See [`LEGAL_NOTICE.md`](LEGAL_NOTICE.md). |

---

## What you get

- **Structural measurement** — Lexicon-driven attribution → full **L1–L9** sphere execution_flow → **public-safe** JSON (macro domains, families, trust, evidence where applicable; no raw hex/adjacency/calibration dumps on product paths).
- **Reading scales (R1–R4)** — Optional segment-level and book-style profiles (internal / extended pipelines).
- **Dynamics & calibration** — Spec-driven; named profiles in `VERSION.yaml`. Research and clinical/TFP collateral are **out of the product image** boundary.
- **KME / TRIZ** — Available in-repo; TRIZ HTTP routes only when explicitly exposed (strict product surface disables them).

---

## Repository layout (active stack)

| Path | Role |
| --- | --- |
| [`core/`](core/) | Deterministic math, layers, attribution, contracts, propagation |
| [`hesperia/`](hesperia/) | Engine: **KME**, hex outputs, **projection** (`hesperia/engine/projection/`), extensions |
| [`runtime/`](runtime/) | Pipelines, **shipping API/CLI**, `analysis_service` façade, semantic-field runners |
| [`lexicon/`](lexicon/) | Dict A/B and lexical assets |
| [`schemas/`](schemas/) | Public JSON Schema (e.g. `schemas/public/public_output_schema.json`) |
| [`specs/`](specs/), [`spec/`](spec/) | Canonical specs and canon fragments |
| [`docs/`](docs/) | Architecture, governance, **Cursor / release** guides |
| [`tests/`](tests/) | Pytest (unit, integration, E2E) |
| [`tools/`](tools/) | Validators, seal inventory, **release audit** (`tools/release/`) |
| [`release/v0.5.1/`](release/v0.5.1/) | **Current** sealed audit bundle · [`release/v0.5.0/`](release/v0.5.0/) historical |
| [`legacy/`](legacy/) | Archive — **not** part of the active execution stack |

Policies: [`REPO_STRUCTURE_POLICY.md`](REPO_STRUCTURE_POLICY.md) · [`EXTENSION_STATUS.yaml`](EXTENSION_STATUS.yaml) · [`GENERATED_ARTIFACT_POLICY.md`](GENERATED_ARTIFACT_POLICY.md)

**Master index (v0.5):** [`docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`](docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md)

---

## Quick start

```bash
git clone <repo-url>
cd hesperia
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .    # installs console script: hesperia → runtime.shipping.cli_main
python3 tools/validate_version_consistency.py
python3 -m pytest tests/ -q --tb=no
```

**Full deterministic pipeline** (config + input file):

```bash
python3 -m hesperia.run --help
# e.g. python3 -m hesperia.run path/to/input.txt --config path/to/config.yaml [--out dossier.json]
```

**Dictionary / CD gates** (validators + smoke after lexical A is green): [`docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md`](docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md) — `tools/run_dict_release_gates.sh`, `tools/run_b_cd_wave_after_a.sh`.

---

## Sealed product CLI & API

**CLI** (mirrors shipping API semantics):

```bash
hesperia analyze --text "Your text here"
hesperia compare --text1 "..." --text2 "..."
hesperia batch --texts "a" "b"          # alias: batch-analyze
hesperia --version
```

**Shipping API** (Docker / production-style — no OpenAPI UI on app):

```bash
python3 -m uvicorn runtime.shipping.api_main:app --host 127.0.0.1 --port 8000
# POST /analyze, /compare, /batch (and /batch-analyze), GET /health
```

**Dev / GPT Actions API** (`runtime.api.main` — Bearer auth, OpenAPI at `/openapi.json`; **not** the shipping entrypoint):

| Surface | Routes |
| --- | --- |
| Structural (L1–L9, projected) | `POST /hesperia/analyze`, `/hesperia/compare`, `/hesperia/batch` |
| **T17 product profiles** | `POST /product/llm-audit`, `/product/tfp`, `/product/fingerprint` (same Bearer as above) |

```bash
python3 -m uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000
# Requires HESPERIA_API_KEY — see docs/governance/RUNTIME_ENV_VARS_v1.md
```

**Shipping** (`runtime.shipping.api_main`) exposes only `POST /analyze`, `/compare`, `/batch` (no `/hesperia/*` or `/product/*` prefix). Structural responses use **`run_structural_analysis`** → **`project_to_public`**. Full split: [`docs/PUBLIC_PRODUCT_SURFACE.md`](docs/PUBLIC_PRODUCT_SURFACE.md).

---

## Running execution flows

| Goal | Command |
| --- | --- |
| **Full internal E2E** (many artifacts) | `python3 -m runtime.pipeline.run_e2e_all` — order: [`docs/E2E_RUN_ORDER.md`](docs/E2E_RUN_ORDER.md) |
| **Product E2E** (minimal seal proof) | `python3 -m runtime.pipeline.run_e2e_product` |
| **L1–L9 single run** | `python3 -m runtime.pipeline.run_l1_through_l9 --out /path/out.json` |

Artifacts default under `assets/artifacts/e2e/` unless overridden.

---

## Release, seal, and GitHub sync

**Before claiming a sealed v0.5.1 or pushing release-audit changes:**

1. Follow [`docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md`](docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md) (same discipline).
2. Use [`docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md`](docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md) for **pre-push validation** and GitHub hygiene.
3. Regenerate audit (full pytest, **clean git tree**, fixed timestamp recommended):

   ```bash
   export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T18:00:00Z
   python3 tools/release/build_release_audit_v0_5_1.py
   ```

4. Confirm `release/v0.5.1/final_gate_status.json` → `"sealed": true` before `git tag v0.5.1`.

**Docker (product slice):** `Dockerfile.shipping` / `Dockerfile.product` — see [`release/README.md`](release/README.md).

---

## Contributing & Cursor workflow

- **Agent rules:** [`AGENTS.md`](AGENTS.md)
- **Pre-push / sync:** [`docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md`](docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md)
- **Open task queue (this repo):** [`docs/CURSOR_OPEN_WORKFLOW.md`](docs/CURSOR_OPEN_WORKFLOW.md)

For implementation or redistribution beyond inspection/reference, **explicit written permission** is required ([`LEGAL_NOTICE.md`](LEGAL_NOTICE.md)).

---

## Documentation map

| Topic | Doc |
| --- | --- |
| v0.5 engine index | [`docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`](docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md) |
| System / product awareness | [`docs/HESPERIA_SYSTEM_AWARENESS.md`](docs/HESPERIA_SYSTEM_AWARENESS.md) |
| Repository map | [`docs/HESPERIA_REPOSITORY_MAP.md`](docs/HESPERIA_REPOSITORY_MAP.md) |
| From scratch: run / build / deploy | [`docs/RUN_FROM_SCRATCH.md`](docs/RUN_FROM_SCRATCH.md), [`docs/BUILD_FROM_SCRATCH.md`](docs/BUILD_FROM_SCRATCH.md), [`docs/DEPLOY_FROM_SCRATCH.md`](docs/DEPLOY_FROM_SCRATCH.md) |
| Changelog | [`CHANGELOG.md`](CHANGELOG.md) |
| Evidence / fingerprint | [`docs/ARCHITECTURE_FINGERPRINT.txt`](docs/ARCHITECTURE_FINGERPRINT.txt) |

---

## Quick command reference

| Action | Command |
| --- | --- |
| Tests | `python3 -m pytest tests/ -q` |
| Version check | `python3 tools/validate_version_consistency.py` |
| Public surface audit | `python3 tools/audit_public_surface.py` |
| Full E2E | `python3 -m runtime.pipeline.run_e2e_all` |
| L1–L9 | `python3 -m runtime.pipeline.run_l1_through_l9 [--out path.json]` |

---

**Hesperia Engine Dynamics** · © 2026 Platonov Igor / igareosh.com · Restricted Research Disclosure
