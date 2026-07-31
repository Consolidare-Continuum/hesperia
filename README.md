# Hesperia (prod)

**Copyright © 2026 CONSOLIDARE CONTINUUM S.R.L.** (IDNO 1026023120076) — All rights reserved. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md), [NOTICE](NOTICE), [LICENSE](LICENSE).

Runnable product. Documentation and context: https://github.com/igareosh/hesperia

Current architecture authority:

- `core.domain` is the canonical shared KME/domain computation layer.
- `core.runtime` is the canonical generic runtime module layer.
- `hesperia.engine.kme` remains a narrowed compatibility package surface, with protected legacy bridge behavior.
- former `hesperia.modules.core` / `metrics.base` / `topology.core` shim files were removed after convergence to `core.runtime.*`.
- `hesperia.modules.tfp` remains the domain extension.
- `core.topology.invariant_catalog` is the single canonical source for the canon matrix (12 areas × 24 families = 288) — see [docs/TOPOLOGY_INVARIANTS.md](docs/TOPOLOGY_INVARIANTS.md).
- `core.attribution` has two live modules (`attribution_shared.py`, sole path via `runtime/pipeline/analyze.py`; `structural.py`, r1_r4-only) — see [docs/foundations/attribution_layer.md](docs/foundations/attribution_layer.md). The former "v06" module (`attribution.py`, a synthetic-placeholder dictionary — no real vocabulary) was retired 2026-07-30. Core has no relation to any extension/module (TRIZ, TFP, clinical, or otherwise).
- Canon matrix family names sourced from the sphereV genesis book corpus (adopted 2026-07-30) — see [docs/foundations/genesis_taxonomy_provenance.md](docs/foundations/genesis_taxonomy_provenance.md).

| Line | Tag |
|------|-----|
| Rollback (2026-05-18) | `hesperia/rollback-line-20260518` |
| Dev-ready (this) | `hesperia/dev-ready-line-20260518` |
