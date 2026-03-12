# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.3 — canonical ontology and geometry lock.
19_SPEC Release v0.3 Structural Enforcement.
Frozen constants only. No dynamic generation. No auto-correction.
Source: 16_SPEC Structural Invariants, 18_SPEC Indexing and Coordinates,
30_FAMILIES canonical.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Geometry constants (frozen)
# -----------------------------------------------------------------------------
AREAS = 12
FAMILIES_PER_AREA = 24
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6

TOTAL_FAMILIES = AREAS * FAMILIES_PER_AREA  # 288
TOTAL_HEXES = TOTAL_FAMILIES * HEXES_PER_FAMILY  # 72_000
TOTAL_SIDES = TOTAL_HEXES * SIDES_PER_HEX  # 432_000
SIDES_PER_FAMILY = HEXES_PER_FAMILY * SIDES_PER_HEX  # 1_500
SIDES_PER_AREA = FAMILIES_PER_AREA * SIDES_PER_FAMILY  # 36_000

# -----------------------------------------------------------------------------
# Canonical area set (12 names, ring order)
# -----------------------------------------------------------------------------
CANONICAL_AREA_SET: frozenset[str] = frozenset({
    "GOOD", "CARE", "ORDER", "CONTROL", "INDIFFERENCE", "HARM",
    "DESTRUCTION", "CHAOS", "FREEDOM", "TRUTH", "CREATION", "DECEIT",
})

# -----------------------------------------------------------------------------
# AREA_FAMILY_MAP: area name -> tuple of 24 family names (canonical order)
# -----------------------------------------------------------------------------
AREA_FAMILY_MAP: dict[str, tuple[str, ...]] = {
    "GOOD": (
        "Altruism", "Generosity", "Compassion", "Mercy", "Forgiveness", "Gratitude",
        "Integrity", "Reliability", "Courage", "Loyalty", "Solidarity", "Fairness",
        "Justice", "Respect", "Trust-building", "Service", "Stewardship", "Responsibility",
        "Reconciliation", "Inclusion", "Community-building", "Mentorship", "Protection", "Care-giving",
    ),
    "CARE": (
        "Nurturing", "Compassionate-response", "Comfort-and-soothing", "De-escalation",
        "Listening-and-attention", "Emotional-support", "Practical-assistance", "Shelter-and-safety-net",
        "Health-support", "Recovery-support", "Accessibility-support", "Inclusion-support",
        "Guardianship-and-trusteeship", "Ongoing-check-ins", "Hospitality-and-welcome", "Relational-repair",
        "Mentoring-and-guidance", "Community-care", "Volunteerism", "Protection-of-vulnerable",
        "Responsibility-taking", "Safeguarding-duties", "Restoration-care", "End-of-life-and-grief-care",
    ),
    "ORDER": (
        "Structure", "Stability", "Predictability", "Coordination", "Role-clarity", "Governance",
        "Compliance", "Procedures", "Protocols", "Standards", "Risk-management", "Capacity-planning",
        "Quality-assurance", "Documentation-discipline", "Record-keeping", "Scheduling",
        "Prioritization", "Escalation-paths", "Monitoring-routines", "Redundancy-and-backups",
        "Budget-discipline", "Access-structure", "Version-control", "Change-management",
    ),
    "CONTROL": (
        "Oversight", "Enforcement", "Gatekeeping", "Licensing", "Monitoring", "Takedowns-and-removals",
        "Quarantine-and-isolation", "Centralization", "Access-restrictions", "Permission-systems",
        "Revocation", "Sanctions", "Curfews-and-limits", "Price-and-rate-controls", "Censorship", "Moderation",
        "Blocklists-and-allowlists", "Inspection-and-audit", "Registration", "Supervision",
        "Statutory-rules", "Eligibility-criteria", "Priority-queues", "Safety-constraints",
    ),
    "INDIFFERENCE": (
        "Neglect", "Bystanding", "Callousness", "Withholding-help", "Buckpassing", "Ghosting-and-avoidance",
        "Stonewalling", "Tokenism", "Cynicism", "Burnout-numbness", "Complacency", "Apathy",
        "Stalling", "Exclusion", "Detachment", "Ignorance-maintained", "Information-dumping", "Dehumanization",
        "Nonchalance", "Fatalism", "Moral-disengagement", "Instrumentalization-of-people", "Indifference-to-risk", "Indifference-to-harm",
    ),
    "HARM": (
        "Violence", "Exploitation", "Corruption", "Betrayal", "Negligence", "Oppression",
        "Sabotage", "Fraud", "Defamation", "Harassment", "Hatred", "Vengeance",
        "Coercion", "Intimidation", "Injury", "Predation", "Hazard", "Ruthlessness",
        "Abuse of power", "Systemic harm", "Resource stripping", "Environmental harm", "Self-harm patterns", "Social breakdown",
    ),
    "DESTRUCTION": (
        "Decommissioning", "Pruning", "Culling", "Dismantling", "Disassembly", "Erasure-of-records",
        "Neutralization-of-threats", "Demolition", "Aggression", "Eradication", "Damage", "Collapse",
        "Devastation", "Shredding-and-wiping", "Partition-and-splitting", "Controlled-burns",
        "Sunsetting-systems", "Recall-and-withdrawal", "Unlearning-harmful-patterns", "Asset-stripping",
        "Sabotage-destruction", "Scorched-earth-actions", "Decay-and-erosion", "Abandonment",
    ),
    "CHAOS": (
        "Unpredictability", "Instability", "Flux", "Turbulence", "Overload", "Conflict-swarms",
        "Uncoordinated-change", "Cascading-failure", "Breakdown-of-rules", "Signal-noise",
        "Information-overflow", "Rumor-spread", "Spontaneous-mobilization", "Crowd-dynamics",
        "Volatility", "Fragmentation", "Strife", "Subversion-of-order", "Hijacking-processes",
        "Manias-and-panics", "Ad-hoc-workarounds", "Rogue-actors", "System-drift", "Entropy-build-up",
    ),
    "FREEDOM": (
        "Autonomy", "Consent", "Expression", "Privacy", "Mobility", "Association",
        "Choice", "Pluralism", "Tolerance", "Experimentation", "Innovation-space", "Decentralization",
        "Interoperability", "Open-access", "Whistleblowing-space", "Dissent-protection",
        "Minority-protection", "Due-process", "Non-discrimination", "Information-access",
        "Transparency-claims", "Exit-options", "Entry-opportunities", "Sandboxing",
    ),
    "TRUTH": (
        "Accuracy", "Evidence", "Reasoning", "Objectivity", "Clarity", "Disclosure",
        "Scrutiny", "Verification", "Reliability-of-sources", "Coherence", "Completeness", "Honesty-in-reporting",
        "Traceability", "Transparency-of-methods", "Uncertainty-awareness", "Plural-evidence",
        "Error-correction", "Review-and-critique", "Methodological-soundness", "Replicability",
        "Open-debate", "Grounded-definitions", "Classification-discipline", "Measurement-discipline",
    ),
    "DECEIT": (
        "Lies", "Propaganda", "Misinformation", "Disinformation", "Concealment", "Forgery",
        "Scapegoating", "Gaslighting", "Statistical-abuse", "Plagiarism", "Manipulative-framing", "Scams",
        "Imposture", "Subterfuge", "Conspiracism", "Mislabeling", "Duplicity", "Fraudulence",
        "Misattribution", "Hoaxes", "Astroturfing", "False-balance", "Selective-disclosure", "Data-fabrication",
    ),
    "CREATION": (
        "Imagination", "Ideation", "Design-thinking", "Invention", "Prototyping", "Craft-and-making",
        "Engineering-solutions", "System-design", "Synthesis", "Integration", "Refinement", "Pattern-finding",
        "Renovation-and-upgrades", "Entrepreneurial-building", "Collaboration-in-making", "Co-creation-with-users",
        "Artistic-expression", "Music-and-rhythm", "Storytelling-and-writing", "Research-and-discovery",
        "Experiment-design", "Tool-building", "Production-systems", "Growth-and-expansion",
    ),
}

# Ensure exactly 12 areas and 24 families per area
assert len(CANONICAL_AREA_SET) == AREAS
for _area, _fams in AREA_FAMILY_MAP.items():
    assert _area in CANONICAL_AREA_SET
    assert len(_fams) == FAMILIES_PER_AREA


def forward(
    area: int,
    family_local: int,
    hex_local: int,
    side_local: int,
) -> int:
    """
    Coord → sideId. 0-based.
    area in [0, AREAS), family_local in [0, FAMILIES_PER_AREA), etc.
    """
    family_global = area * FAMILIES_PER_AREA + family_local
    return ((family_global * HEXES_PER_FAMILY + hex_local) * SIDES_PER_HEX) + side_local


def inverse(side_id: int) -> tuple[int, int, int, int]:
    """
    sideId → (area, familyLocal, hexIndex, sideIndex). 0-based.
    """
    side_index = side_id % SIDES_PER_HEX
    tmp = side_id // SIDES_PER_HEX
    hex_index = tmp % HEXES_PER_FAMILY
    family_global = tmp // HEXES_PER_FAMILY
    area = family_global // FAMILIES_PER_AREA
    family_local = family_global % FAMILIES_PER_AREA
    return (area, family_local, hex_index, side_index)


def validate_coord(area: int, family_local: int, hex_local: int, side_local: int) -> None:
    """Raise if any coord out of range (HARD_STOP for family/area/hex/side overflow)."""
    if not (0 <= area < AREAS):
        raise RuntimeError(f"Sigma HARD_STOP: area must be in [0,{AREAS}), got {area}") from None
    if not (0 <= family_local < FAMILIES_PER_AREA):
        raise RuntimeError(
            f"Sigma HARD_STOP: family_local must be in [0,{FAMILIES_PER_AREA}), got {family_local}"
        ) from None
    if not (0 <= hex_local < HEXES_PER_FAMILY):
        raise RuntimeError(
            f"Sigma HARD_STOP: hex_local must be in [0,{HEXES_PER_FAMILY}), got {hex_local}"
        ) from None
    if not (0 <= side_local < SIDES_PER_HEX):
        raise RuntimeError(
            f"Sigma HARD_STOP: side_local must be in [0,{SIDES_PER_HEX}), got {side_local}"
        ) from None


def validate_side_id(side_id: int) -> None:
    """Raise if side_id not in [0, TOTAL_SIDES) (HARD_STOP for sideId overflow)."""
    if not (0 <= side_id < TOTAL_SIDES):
        raise RuntimeError(
            f"Sigma HARD_STOP: sideId must be in [0,{TOTAL_SIDES}), got {side_id}"
        ) from None
