# AGENT GUIDELINES — HESPERIA (Post-Refactor)

This repository is in the Reference Architecture state. Agents must align all work with the current top-level layout and avoid legacy-era paths.

## Canonical Top-Level Structure

Active repository structure:

- `core/`
- `runtime/`
- `lexicon/`
- `tools/`
- `assets/`
- `tests/`
- `docs/`
- `legacy/`

Do not use or reintroduce old roots such as `sphere_rag/`, `hesperia_lex/`, `scripts/`, `api/`, `governance/`, or `project/` as active top-level architecture.

## Responsibilities

- `core/`
  - Deterministic computation layers.
  - `layer_1` through `layer_9`.
  - Topology, math, propagation.

- `runtime/`
  - Execution pipelines.
  - Runtime orchestration.
  - API server.

- `lexicon/`
  - Dictionary systems.
  - Lexical validation tooling.

- `tools/`
  - Developer utilities.
  - Diagnostics.
  - Data generation and operational helpers.

- `assets/`
  - Runtime/static artifacts and data resources.

- `tests/`
  - Pytest unit and integration suites.

- `docs/`
  - Specs.
  - Architecture documentation.
  - Governance rules that remain active documentation.

- `legacy/`
  - Archived historical code and references.
  - Not part of the active execution stack.

## Active Execution Stack

Treat the following as the active runtime stack:

- `runtime/`
- `core/`
- `lexicon/`

## Legacy Safety Rule

Agents must never modify code under `legacy/` unless explicitly instructed to perform archival maintenance.

## Path/Command Hygiene

- Keep examples and commands aligned to active modules.
- Use `python3 -m runtime.pipeline.run_l1_through_l9` for the L1→L9 pipeline entrypoint.
- Keep pytest references pointed at `tests/`.

## Scope

These rules apply to the full repository rooted at this directory.
