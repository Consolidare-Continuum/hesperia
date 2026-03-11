# Engine Boundaries

## Core (`core/`)
- Deterministic engine only.
- No API server concerns.
- No deployment/runtime orchestration concerns.
- No mutable operational scripting concerns.

## Runtime (`runtime/`)
- Pipeline orchestration and service entry points.
- Calls `core/` as a library.
- Must not redefine deterministic math/logic present in `core/`.

## Lexicon (`lexicon/`)
- Language infrastructure and lexical assets.
- Build/validation for lexical artifacts.
- Supplies inputs consumed by runtime/core.

## Tools (`tools/`)
- Operational commands for calibration, diagnostics, and scripts.
- Must not become a dependency for deterministic core execution paths.

## Assets (`assets/`)
- Data/model/artifact storage only.
- No executable orchestration logic.

## Legacy (`legacy/`)
- Deprecated modules, PoC experiments, and superseded scripts.
- Not part of active boot path.
