<!--
HESPERIA — Reference Architecture Definition (RAD)
-->

# Repository lifecycle map

Strict lifecycle classes for top-level material. Use this when deciding **imports**, **shipping**, and **deletion**.

| Class | Meaning | Examples |
|-------|---------|----------|
| **active** | Runtime-critical or binding; expected in CI and product paths | `runtime/`, `core/`, `hesperia/`, `specs/`, `schemas/`, `assets/` (current inputs), `tests/` (non-experimental) |
| **optional** | Extension or demo; gated by flags / capabilities | `hesperia.extensions.triz`, `benchmarks/extensions/triz`, `examples/extensions/triz_demo`, `deploy/extensions/triz_mvp`, `tools/triz` |
| **research** | Non-product; must not define binding behavior | `research/`, `research/reports/` |
| **experimental** | Tests/fixtures for research-backed features; not minimal product E2E | `tests/experimental/`, `tests/fixtures/clinical_tfp/` |
| **legacy** | Historical read-only quarantine | `legacy/` (includes `legacy/assets/data/`, `legacy/docs/…`) |
| **generated** | Local or CI outputs; not authoritative source | `outputs/`, `tmp/`, selected paths under `assets/artifacts/` per policy |

**Rule of thumb:** if it does not help **run · test · build · ship · govern** the current version, it should not sit in the **active** spine.
