# Hesperia (prod)

Runnable product. Documentation and context: https://github.com/igareosh/hesperia

Current architecture authority:

- `core.domain` is the canonical shared KME/domain computation layer.
- `core.runtime` is the canonical generic runtime module layer.
- `hesperia.engine.kme` remains a narrowed compatibility package surface, with protected legacy bridge behavior.
- former `hesperia.modules.core` / `metrics.base` / `topology.core` shim files were removed after convergence to `core.runtime.*`.
- `hesperia.modules.tfp` remains the domain extension.

| Line | Tag |
|------|-----|
| Rollback (2026-05-18) | `hesperia/rollback-line-20260518` |
| Dev-ready (this) | `hesperia/dev-ready-line-20260518` |
