# Hesperia (prod)

Runnable product. Documentation and context: https://github.com/igareosh/hesperia

Current architecture authority:

- `core.domain` is the canonical shared KME/domain computation layer.
- `core.runtime` is the canonical generic runtime module layer.
- `hesperia.engine.kme` and `hesperia.modules.core` / `metrics.base` / `topology.core` remain compatibility import surfaces.
- `hesperia.modules.tfp` remains the domain extension.

| Line | Tag |
|------|-----|
| Rollback (2026-05-18) | `hesperia/rollback-line-20260518` |
| Dev-ready (this) | `hesperia/dev-ready-line-20260518` |
