# Hesperia

**Copyright © 2026 CONSOLIDARE CONTINUUM S.R.L.** (IDNO 1026023120076) — All rights reserved.  
**Proprietary.** Access only under company written agreement (NDA). See `LICENSE`, `NOTICE`, `LEGAL_NOTICE.md`, `docs/corporate/`.

Private company product repository of Societatea cu Răspundere Limitată „CONSOLIDARE CONTINUUM”.  
Sole shareholder / administrator / author-implementor: **Platonov Igor**.

---

## Product (sealed line)

Runnable product tree. Architecture authority:

- `core.domain` is the canonical shared KME/domain computation layer.
- `core.runtime` is the canonical generic runtime module layer.
- `hesperia.engine.kme` remains a narrowed compatibility package surface, with protected legacy bridge behavior.
- former `hesperia.modules.core` / `metrics.base` / `topology.core` shim files were removed after convergence to `core.runtime.*`.
- `hesperia.modules.tfp` remains the domain extension.

| Line | Tag |
|------|-----|
| Rollback (2026-05-18) | `hesperia/rollback-line-20260518` |
| Dev-ready | `hesperia/dev-ready-line-20260518` |

Upstream sealed tips are received from the Atomic-Commits-Team prod line under
company mirror discipline. **Do not** invent version bumps in this org repo.
