# TASK GEO-01 — Repo-wide geometry vocabulary refactor (operational terminology)

**Status:** OPEN — **blocked on scope** for code/identifiers (see §0).  
**Tool:** `tools/refactor_strip_geometry.py`  
**Proceed log:** [ETHAN-OPEN-WORKFLOW-PROCEED.md](ETHAN-OPEN-WORKFLOW-PROCEED.md)

---

## 0. Hesperia-specific scope gate (mandatory)

This repository’s **sealed Engine Dynamics v0.5.1** vocabulary **intentionally** uses terms such as **hex** (12-node substrate), **sphere** (internal compute tree), and paths like **`core/hexmap/`** as **canonical identifiers** and **spec bindings**.

A **blind** word-boundary replace of `\bhex\b` → `unit` across `*.py` will:

- break imports and component names,
- desync specs, CI, and `release/v0.5.1/` narratives,
- violate topology invariants documentation.

**Policy:**

1. **Dry-run + report on the full repo** (excluding frozen trees) is always allowed for audit.
2. **`--apply` default** (if enabled in tool): **only** `docs/` and `specs/` (and similar prose), unless explicit **`--whole-repo-apply`** + confirmation flag / env (see script help).
3. **Code / package / public schema rename** requires a **separate architecture decision** (alias period, compatibility shims, seal minor bump) — not a single scripted pass.

---

## 1. TASK TITLE

Repo-wide geometry decontamination (deterministic refactor) — **operational terminology** in approved scope.

---

## 2. OBJECTIVE

Perform a **safe, deterministic, reviewable** refactor that:

- Removes **forbidden geometric terms** from approved surfaces (see §0).
- Replaces them with **approved operational terms** (map below).
- Produces: **diff**, **audit report**, **minimize unintended replacements** via exclusions and phased apply.

---

## 3. FORBIDDEN TERMS (STRICT — word-boundary matches)

Replace only **word-boundary** matches (regex `\b...\b`), input_context noted where ambiguous:

| Forbidden | Notes |
|-----------|--------|
| hex, hexes, hexagon, hexagons | **Code:** see §0 |
| sphere, spherical | **Code:** see §0 |
| loop | **Only** structural sense; **never** programming `for`/`while` “loop” |
| geometry, geometric | |
| mesh, lattice | |
| coordinate, coordinates | **Not** when pure math index in formula docs — manual review |
| distance | **Only** semantic graph sense; **not** math/physics distance symbols |
| neighbors, neighbour | |
| grid | |

---

## 4. REPLACEMENT MAP (STRICT)

| Pattern | Replacement |
|---------|-------------|
| hex | unit |
| hexes | units |
| hexagon | unit |
| hexagons | units |
| sphere | domain |
| spherical | domain-based |
| loop | cycle |
| geometry | topology |
| geometric | structural |
| mesh | topology |
| lattice | topology |
| coordinate | index |
| coordinates | indices |
| distance | interaction_score |
| neighbors | related_units |
| neighbour | related_units |
| grid | layout |

---

## 5. SAFETY — DO NOT MODIFY (without explicit sub-task)

- **Hashes / IDs:** `sha256`, UUIDs, git commit hashes  
- **Paths** unless a dedicated path-migration task exists  
- **Frozen / generated trees:** `assets/` (per policy), `legacy/`, `release/`, `outputs/`, `tmp/`, `build/`, `calibration_runs/`, `.git`, vendored trees  
- **Math formulas** where tokens are notation, not prose  
- **External / vendored** code  

---

## 6. IMPLEMENTATION STEPS

| Step | Action |
|------|--------|
| **1** | Implement / maintain `tools/refactor_strip_geometry.py` (dry-run default, `--apply`, scoped apply, `--validate`, reports). |
| **2** | **Dry-run (required):** `python3 tools/refactor_strip_geometry.py` → review JSON report. |
| **3** | **Apply (phased):** prose first; then code only after §0 sign-off + shims. |
| **4** | **Validate:** `python3 tools/refactor_strip_geometry.py --validate` → `geometry_validation_report.json` (residual forbidden tokens). |
| **5** | **Commit** (when scope closed): `refactor: operational terminology (geometry decontamination, scoped)` — message must state scope (e.g. docs/specs only). |

---

## 7. EXPECTED RESULT (per approved scope)

- No **unapproved** geometric language leakage in that scope  
- Consistent **operational** wording where applied  
- Fully **auditable** change set  
- **Zero behavioral impact** when only prose/config comments in non-executable paths; **code renames require tests + seal plan**

---

*Ethan — GEO-01 geometry decontamination task spec.*
