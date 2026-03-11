# Version Policy

## Versioning Rules

- `v0.x` = research phase.
- `v1.x` = production engine.

## Current Baseline

- Current architecture baseline: **v0.4 reference architecture**.

## Governance Notes

- Structural and deterministic contracts in `core/` are version-governed.
- Runtime/API/tooling changes must preserve `core/` determinism unless accompanied by a versioned contract update.
- Lexicon artifact evolution in `lexicon/` must remain reproducible and validation-backed.
