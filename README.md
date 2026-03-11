# Hesperia Reference Architecture

Current baseline: **v0.4 reference architecture**.

**Version**: v0.4.x (reference architecture baseline)
**Status**: canonical structure with deterministic `core` + orchestrated `runtime`.

## Repository Layout

```text
hesperia/
  core/
    layers/
    attribution/
    topology/
    math/
    propagation/

  runtime/
    runners/
    api/
    pipeline/

  lexicon/
    curated/
    frozen/
    build/
    validation/

  tools/
    scripts/
    calibration/
    diagnostics/

  assets/
    models/
    artifacts/
    data/

  tests/

  docs/
    architecture/
    specs/
    boot/

  legacy/
```

## Architecture Diagram

```text
lexicon/*  --->  core/*  --->  runtime/pipeline  --->  runtime/api
                   ^                |
                   |                v
               assets/* <--- tools/calibration + tools/diagnostics

legacy/* is isolated from the active boot path.
```

## Deterministic Boot Paths

- L1-L9 pipeline:
`python3 -m runtime.pipeline.run_l1_through_l9 --out /tmp/l1_l9.json`

- Analyze pipeline (library call):
`from runtime.pipeline.analyze import analyze`

- API service:
`python3 -m uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000`

## Test and Validation

- Python test suite:
`python3 -m pytest -q`

- Lexical validation scripts:
`python3 lexicon/validation/validate_lexical.py`

## Governance

- Architecture boundaries: `docs/architecture/ENGINE_BOUNDARIES.md`
- System model: `docs/architecture/SYSTEM_OVERVIEW.md`
- Version governance: `VERSION_POLICY.md`
