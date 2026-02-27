# L1 Structure Profiles (34_SPEC N1)

Versioned artifacts for the **L1 Normative Structure Profile Extension**. Profiles define intended structural shape (family/area distribution, deny sets, altitude band, budget constraints). Layer-1 does not select profiles; the caller supplies `profile_id` and `profile`.

- **Naming:** `STRUCTURE_PROFILE__<name>__v<k>.json`
- **Schema:** See `sphere_rag/layers/structure_profile.py` and the L1 Profile Extension spec (34_SPEC N1).
- **Required:** `FEDV` (length F=288), `AEDV` (length A=12); both non-negative and sum to 1.
- **Optional:** `DENY_FAMILIES`, `ALLOW_FAMILIES`, `ALT_BAND`, `ALT_TARGET`, budget caps, weights, `penalty_mode`.
- **Taxonomy (canonical profiles):** `primary_axis` ∈ {distribution, concentration, altitude, constraint, regression}, `strictness_level` ∈ {soft, medium, hard}. See **TAXONOMY_v1.md** for the canonical set and envelope definitions.

Profile changes require checksum update, release note, and test-vector updates per governance.
