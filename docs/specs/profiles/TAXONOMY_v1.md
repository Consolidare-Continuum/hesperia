<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# L1 Profile Taxonomy v1.0 (Canonical Set)

Profiles are grouped by **structural geometry intent**, not human function. Each canonical profile is a stable envelope across four axes: Concentration vs Distribution, Altitude Band, Domain Compression, Constraint Strictness.

## Taxonomy rule

A profile **must** declare (when it is part of the canonical set):

- **primary_axis** ∈ `{distribution, concentration, altitude, constraint, regression}`
- **strictness_level** ∈ `{soft, medium, hard}`

This prevents uncontrolled profile sprawl. Non-canonical or one-off profiles may omit these; canonical envelopes must include them.

## Categories and canonical envelopes

| Category | Axis | Canonical profile | Intent |
|----------|------|-------------------|--------|
| A | Distribution | UNIFORM_ENVELOPE | Maximal structural neutrality; baseline regression |
| A | Distribution | BROAD_ANALYSIS_ENVELOPE | Multi-area coverage; diagnostic / inspection |
| B | Concentration | FOCUSED_DOMAIN_ENVELOPE | Strong concentration in one macro domain; specialized segments |
| C | Altitude | LOW_ALTITUDE_ENVELOPE | Tactical / execution layer |
| C | Altitude | HIGH_ALTITUDE_ENVELOPE | Governance / policy / meta-structure |
| D | Constraint | HARD_BOUNDARY | Strict enforcement; CI gate / compliance |

## Minimal core set (frozen first)

For HESPERIA core, the following 6 are the canonical minimal set:

1. **UNIFORM_ENVELOPE** — baseline
2. **BROAD_ANALYSIS_ENVELOPE** — wide
3. **FOCUSED_DOMAIN_ENVELOPE** — narrow
4. **LOW_ALTITUDE_ENVELOPE** — tactical
5. **HIGH_ALTITUDE_ENVELOPE** — strategic
6. **HARD_BOUNDARY** — strict gate

File naming: `STRUCTURE_PROFILE__<envelope_name>__v1.json` (e.g. `STRUCTURE_PROFILE__UNIFORM_ENVELOPE__v1.json`).

## Envelope geometry (summary)

- **UNIFORM_ENVELOPE**: FEDV/AEDV uniform; no DENY; ALT_BAND (0, 1); no budget caps.
- **BROAD_ANALYSIS_ENVELOPE**: FEDV/AEDV moderately spread; MIN_AREA_SPREAD ≥ 0.40; MAX_FAMILY_DOMINANCE ≤ 0.30; ALT_BAND (0.4, 0.9).
- **FOCUSED_DOMAIN_ENVELOPE**: FEDV/AEDV concentrated in selected families/areas; MAX_FAMILY_DOMINANCE ≤ 0.60; MIN_AREA_SPREAD ≤ 0.20; moderate ALT_BAND.
- **LOW_ALTITUDE_ENVELOPE**: ALT_BAND (0, 0.4); optional MAX_AREA_DOMINANCE.
- **HIGH_ALTITUDE_ENVELOPE**: ALT_BAND (0.6, 1.0); DENY low-level operational families; moderate MIN_AREA_SPREAD.
- **HARD_BOUNDARY**: DENY_FAMILIES present; tight MAX_* / MIN_*; narrow ALT_BAND; high L7 MIN_PCS in use.

Layer-1 does not interpret `primary_axis` or `strictness_level`; they are metadata for governance and tooling.
