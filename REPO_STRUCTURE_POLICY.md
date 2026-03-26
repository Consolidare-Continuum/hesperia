# Repository structure policy (Task 2)

**Purpose:** Every path should answer: *core runtime*, *extension*, *research*, *generated output*, or *archive*.

This repo uses a **pragmatic** layout aligned with Python import roots (`core`, `hesperia`, `runtime`, `lexicon`) while adding explicit **quarantine** and **spec** trees.

## Top-level folders (allowed use)

| Area | Meaning | Allowed | Forbidden |
|------|---------|---------|-----------|
| **`core/`** | Deterministic L1–L9 and topology math | Invariant layers, shared attribution | Domain plugins, demos, generated JSON |
| **`hesperia/`** | Engine package (KME, hex stack, ontology loaders under `hesperia/ontology`) | Deterministic engine code, `extensions/*` | Ad-hoc experiment scripts |
| **`hesperia/extensions/`** | Optional, declared extensions (`dynamics`, `triz`) | Extension code only | “Hidden” core invariants |
| **`research/`** | Experimental / non-product | `clinical_tfp`, prototypes, drafts | Pretending to be core API without `EXTENSION_STATUS.yaml` |
| **`runtime/`** | Pipelines, API adapters, semantic-field runners | Orchestration, shipping, services | Core math that belongs in `core/` |
| **`lexicon/`** | Frozen bundles, validation tools | Lexicon assets + validators | Clinical semantics |
| **`assets/`** | Committed operational data (calibration, public maps) | Versioned YAML/JSON registries | Large generated runs (use `outputs/`) |
| **`schemas/`** | Canonical JSON Schema (public + internal contract artifacts) | `schemas/public/*` | Hand-edited run logs |
| **`specs/`** | **Binding** specifications — see **`specs/CANONICAL_INDEX.md`** | Tier-1 definitions (`core/`, `dynamics/semantic_field_dynamics.md`, `calibration/`, `triz/`, `schema/`, `system/`) | Duplicating equations in `docs/` |
| **`spec/`** | Symlink → **`specs/canon/`** | Back-compat path only | New docs should link to `specs/canon/` explicitly |
| **`docs/`** | Explanatory documentation | Guides, maps, governance prose | Sole copy of normative math (must live under `specs/`) |
| **`examples/`** | Small runnable demos / sample I/O | `examples/extensions/triz_demo`, minimal scripts | Production pipelines |
| **`benchmarks/`** | Evaluation corpora (optional extensions) | `benchmarks/extensions/triz` | Shipping runtime |
| **`deploy/`** | Compose / Docker samples | `deploy/extensions/triz_mvp` | Core engine code |
| **`sphere/`** | Internal structural / USF compute | Execution Flow helpers, prolog-adjacent modules | Public product API surface |
| **`release/`** | Frozen seal bundles | `release/v0.5.0/` audit package | Mutable application code |
| **`outputs/`** | Generated artifacts (default: gitignored) | Local E2E/smoke/benchmark dumps | Silent commit of unreviewed blobs |
| **`tests/`** | Pytest only | Tests, fixtures | Business logic |
| **`tools/`** | Dev utilities | Validators, one-off maintainers | Core runtime |
| **`legacy/`** | Archived code (read-only policy per AGENTS) | Historical reference | New features |

## Imports

- **Core engine extensions:** `hesperia.extensions.dynamics`, `hesperia.extensions.triz`
- **Clinical / TFP stack:** `research.clinical_tfp` (experimental)

## Related

- **`EXTENSION_STATUS.yaml`** — machine-readable extension status.
- **`GENERATED_ARTIFACT_POLICY.md`** — where run output may land and what may be committed.
