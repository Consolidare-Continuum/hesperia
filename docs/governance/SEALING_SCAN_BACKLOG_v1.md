# SEALING SCAN BACKLOG v1

**Status:** Active  
**Purpose:** Every scan hit is classified. Each hit becomes one of: move to internal-only zone, rename to public-safe term, suppress by rule (path is internal), delete as obsolete leak.

---

## 1. Classification Categories

| Category | Action |
|----------|--------|
| **Move to internal** | Relocate file or content to docs/internal/ or other internal-only path; add path to sealing scan exclusion. |
| **Rename to public-safe** | Replace term with PUBLIC_VOCABULARY_MAP equivalent (e.g. sphere → structural space, hex → structural node). |
| **Suppress by rule** | Path is already internal-only; add to tools/sealing_scan.py INTERNAL_ONLY_SUBDIRS or document as waived. |
| **Delete** | Remove obsolete comment, debug print, or leak; no replacement. |

---

## 2. How to Populate

Run: `python3 tools/sealing_scan.py --repo .`  
For each reported hit (file:line), add one row below with classification and owner/status.

---

## 3. Backlog Entries (Template)

| File | Line | Term | Classification | Notes |
|------|------|------|----------------|-------|
| (example) docs/specs/foo.md | 12 | sphere | Move to internal | Relocate spec to docs/internal/ or rename to "structural space" |
| (example) runtime/pipeline/bar.py | 5 | layer_1 | Rename / suppress | Use public narrative; do not expose layer name in log |
| — | — | — | — | Run scan to populate |

---

## 4. Priority Areas (from P4-T6)

- **Public docs** — Zero forbidden terms; rename or move.
- **Runtime entry points** — No reflective terms in CLI help text or default messages.
- **Schemas** — Already audited (SCHEMA_SEALING_AUDIT); ensure no new leaks.
- **Report templates** — Public vocabulary only.
- **Mixed code comments** — Remove or internal-only.
- **CLI help text** — Public narrative only.

---

## 5. Done Condition

Every scan hit is classified in this backlog, not ignored. Each row has a resolution (move / rename / suppress / delete) and is tracked until the public tree passes or has only explicitly waived items with justification.
