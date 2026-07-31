# Topology invariants — the canon matrix

This is the single documented source of truth for Hesperia's canon matrix: 12 areas × 24 families
= 288 families, plus the hex/side geometry built on top of them. Five files already cite this
document as authoritative (`core/topology/invariant_catalog.py`, `core/hexmap/topology.py`,
`core/projection/public_projection_layer.py`, and two release-audit scripts) — this file is what
they were pointing at.

## Canonical source

**`core/topology/invariant_catalog.py`** is the single canonical source for these constants.
Its own docstring says it plainly: *"HESPERIA v0.3 — canonical ontology and geometry lock...
Frozen constants only. No dynamic generation. No auto-correction."* Every module that needs
`AREAS`, `FAMILIES_PER_AREA`, `TOTAL_FAMILIES`, `CANONICAL_AREA_SET`, or `AREA_FAMILY_MAP` must
import them from there — never redefine a local literal copy. See "Do not duplicate" below.

## Geometry constants

| Name | Value | Meaning |
|---|---|---|
| `AREAS` | 12 | Top-level areas |
| `FAMILIES_PER_AREA` | 24 | Families per area |
| `TOTAL_FAMILIES` | 288 | `AREAS * FAMILIES_PER_AREA` |
| `HEXES_PER_FAMILY` | 250 | Hex cells per family |
| `SIDES_PER_HEX` | 6 | Sides per hex cell |
| `TOTAL_HEXES` | 72,000 | `TOTAL_FAMILIES * HEXES_PER_FAMILY` |
| `TOTAL_SIDES` | 432,000 | `TOTAL_HEXES * SIDES_PER_HEX` |
| `SIDES_PER_FAMILY` | 1,500 | `HEXES_PER_FAMILY * SIDES_PER_HEX` |
| `SIDES_PER_AREA` | 36,000 | `FAMILIES_PER_AREA * SIDES_PER_FAMILY` |

## The 12 canonical areas

`CANONICAL_AREA_SET`: **GOOD, CARE, ORDER, CONTROL, INDIFFERENCE, HARM, DESTRUCTION, CHAOS,
FREEDOM, TRUTH, CREATION, DECEIT**.

Each area holds 24 named families (`AREA_FAMILY_MAP`, reproduced here so a reader doesn't need to
open the source to see the shape — but the source is still authoritative if these two ever drift).
**As of 2026-07-30, family names are sourced from the sphereV genesis book-corpus taxonomy** — see
[genesis_taxonomy_provenance.md](foundations/genesis_taxonomy_provenance.md) for where this came
from and why. Area order was kept as sealed in 0.7.0; only the family names within each area
changed.

- **GOOD**: Altruism, Protection, Healing, Mercy, Generosity, Mentorship, Community, Hospitality,
  Forgiveness, Integrity, Gratitude, Stewardship, Solidarity, Rehabilitation, Inclusion, Fairness,
  Conservation, Education, Mediation, Service, Safety, Trust, Compassion, Courage.
- **CARE**: Compassion, Nursing, Comfort, Inclusion, Medication, Preservation, Protection,
  Support, Accessibility, Attendance, De-escalation, Mediation, Restore, Shelter, Help,
  Hospitality, Security, Stewardship, Volunteerism, Aid, Mentoring, Kindness, Responsibility,
  Guardianship.
- **ORDER**: Standard, Schedule, Governance, Access, Quality, Documentation, Change, Response,
  Risk, Roles, Versioning, Backups, Budgeting, Compliance, Protocol, Checklists, Metrics,
  Playbooks, Workflows, Symmetry, Capacity, Directives, Escalation, Review.
- **CONTROL**: Safeguards, Takedowns, Isolation, Entitlements, Inspection, Permit, Monitoring,
  Revocation, Gatekeeping, Centralization, Price-controls, Curfews, Hierarchy, Quarantine,
  Listing, Blocklist, Moderation, Statutes, Oversight, Safety, Regulation, Supervise, Register,
  Directing.
- **INDIFFERENCE**: Neglect, Ostracism, Dodging, Dehumanization, Bystanding, Callousness,
  Withholding, Buckpassing, Neutrality, Ghosting, Stonewalling, Tokenism, Cynicism, Burnout,
  Complacency, Apathy, Stalling, Exclusion, Detachment, Ignorance, Dumping, Negation, Dispassion,
  Nonchalance.
- **HARM**: Violence, Exploitation, Corruption, Betrayal, Negligence, Oppression, Sabotage,
  Fraud, Defamation, Addiction-harms, Pollution, Waste, Harassment, Hatred, Vengeance, Coercion,
  Intimidation, Injury, Predation, Hazard, Dereliction, Cronyism, Ruthlessness, Vandalism.
- **DESTRUCTION**: Decommissioning, Strike, Refusal, Pruning, Culling, Removal, Dismantling,
  Erasure, Neutralization, Demolition, Invasion, Destroying, Death, Aggression, Eradication,
  Damage, Shred, Unlearning, Collapse, Devastation, Splitting, Partition, Decay, Recalls.
- **CHAOS**: Swarming, Drift, Ideation, Divergence, Disruption, Anomaly, Emergence, Volatility,
  Strife, Outliers, Discord, Subversion, Hijacking, Turmoil, Commotion, Mutation, Instigation,
  Manias, Randomness, Madness, Instability, Confusion, Entropy, Disorder.
- **FREEDOM**: Autonomy, Consent, Openness, Exit, Entry, Expression, Privacy, Mobility,
  Permissionless, Association, Liberties, Sandbox-testing, Experimentation, Representation,
  Choice, Interoperability, Transparency, Decentralization, Pluralism, Tolerance, Whistleblowing,
  Laws, Rights, Fair.
- **TRUTH**: Evidence, Measurement, Reproducibility, Transparency, Auditability, Citation,
  Calibration, Openness, Review, Clarity, Fallibilism, Verification, Signal, Validation,
  Versioning, Explainability, Groundtruth, Traceability, Definitions, Taxonomy, Testing,
  Methodology, Consensus, Uncertainty.
- **DECEIT**: Lies, Propaganda, Falsehood, Concealment, Forgery, Invalid, Scapegoating,
  Gaslighting, Unbalance, Pseudostatistics, Plagiarism, Clickbait, Trickery, Scams, Mendacity,
  Imposture, Subterfuge, Conspiracism, Mislabeling, Duplicity, Fraudulence, Misattribution,
  Chicanery, Hoaxes.
- **CREATION**: Invention, Design, Craft, Cultivation, Engineering, Composition,
  Music-and-rhythm, Writing, Entrepreneurship, Fusion, Toolmaking, Discovery, Integration,
  Prototyping, Refactoring, Synthesis, Pattern-language, User-experience, Renovation, Production,
  Growth, Art, Researching, Collaboration.

## Operational split (10+2)

Per `invariant_catalog.py`'s own docstring: areas 0–9 (240 families) are **public/operational**;
areas 10 and 11 (48 families) are **reserved service areas**, stateless. Family index `f` belongs
to area `f // FAMILIES_PER_AREA` — arithmetic, not a separate lookup table.

## Enforcement

This isn't just documentation — `core/propagation/invariant_enforcer.py` (`check_geometry`)
actively enforces these values on its call path, and `invariant_catalog.py` itself asserts
`len(CANONICAL_AREA_SET) == AREAS` and validates every `AREA_FAMILY_MAP` entry has exactly 24
families at import time.

## Do not duplicate

Any module needing these constants must import them:

```python
from core.topology.invariant_catalog import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES
```

Files already doing this correctly (use as reference examples):
`core/propagation/invariant_enforcer.py`, `core/propagation/shadow_layer.py`,
`core/attribution/structural.py`, `core/attribution/attribution_shared.py`,
`hesperia/engine/hex_topology_authority.py`, `hesperia/engine/hex_matrix_builders.py`.

As of the 2026-07-30 consolidation pass, roughly 20 other files had drifted into hardcoding their
own literal copies of these constants instead of importing them. That drift has been fixed by
replacing each local literal with an aliased import from this module (see
`docs/archive/ARCHIVE-MANIFEST.md` and git history for the file list) — if you find a new
hardcoded copy, that's regression, not a new legitimate pattern.

## Related

- `core/topology/invariant_catalog.py` — the canonical module itself (`forward`/`inverse`
  bijection helpers, `validate_side_id`, `validate_coord`).
- [foundations/attribution_layer.md](foundations/attribution_layer.md) — which attribution module
  is live and how it uses this matrix.
- [foundations/parameter_rationale_and_theory.md](foundations/parameter_rationale_and_theory.md) —
  why the constants have these values/ranges.
