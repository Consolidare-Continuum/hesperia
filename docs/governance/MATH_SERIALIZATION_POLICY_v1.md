# MATH SERIALIZATION POLICY v1

**Status:** Active  
**Purpose:** No external artifact shall contain raw L1–L9 internals unless explicitly internal-only.

---

## 1. Rule

**Intermediate math states:**

- **Not written** in public mode (no per-layer JSON dumps, no L1..L9 raw output to file).
- **Not dumped to stdout** in public mode (no print of layer dicts for operator consumption).
- **Not exported in dossier public mode** (dossier content passes through projection; no raw layer payloads).
- **Not embedded in debug comments** in public artifacts (no commented-out layer state in shipped code or configs).

---

## 2. Allowed in Public Mode

- **Projected outputs only** — macro_domain_vector, policy_family_counts, dominant_macro_domain, dominant_policy_family, and other keys produced by the public projection layer.
- **SI-derived scalars** — coverage, dominance, entropy, stability, confidence, trust_tier (as defined in public metric profiles), without layer attribution.
- **Decision/status codes** — high-level codes (e.g. decision_status_code, output_trust_tag) without exposing which layer produced them or the full gate logic.

---

## 3. Internal-Only Serialization

When runtime mode is **internal_debug** or **internal_review**, layer intermediates may be written to paths that are:

- Under a dedicated internal output directory (e.g. internal/ or debug/), or
- Guarded by env or flag so they are never included in the public package or operator-visible log.

---

## 4. Acceptance Criterion

Public run artifacts do not expose layer intermediates (no raw L1–L9 dicts, no formula ids, no dependency chain in output).
