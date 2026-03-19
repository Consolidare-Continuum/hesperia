<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# `assets/data/` — active operational inputs

- **`domain_constants.json`**, **`domain_graph.json`** (when present) — KME / domain metrics frozen inputs (see `hesperia.engine.kme.loader`, domain docs).
- **`B_SURFACE_LEX_FIELD_v1.json`** — lexical field artifact where used by tooling.
- **`engine_dynamics_v050/`** — calibration / prior bundle for engine dynamics (internal filenames may retain historical `v060` labels; **folder name** reflects Engine Dynamics v0.5 baseline, not repo chronology).

Historical frozen dumps (**`v040`**, **`v0413`**, **`v0414`**) were moved to **`legacy/assets/data/`** to keep the active tree small.
