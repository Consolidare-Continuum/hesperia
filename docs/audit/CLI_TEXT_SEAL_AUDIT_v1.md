# CLI text seal audit v1

**Status:** Active  
**Purpose:** Ensure --help, runtime errors, and usage docs contain no reflective terms. Public-safe only.

---

## 1. Forbidden terms (must not appear)

Remove or avoid any mention of:

| Term / pattern | Reason |
|----------------|--------|
| sphere | Geometry-revealing |
| hex | Geometry-revealing |
| topology | Internal structure |
| bridge | Bridge logic |
| layer | Execution Flow internals |
| family reserve | Reserve structure |
| area counts, 12 areas, 288 families | Internal counts |

---

## 2. Audited surfaces

| Surface | Location | Check |
|---------|----------|--------|
| **CLI --help** | runtime/shipping/cli_main.py (argparse description, subcommand help, argument help) | Grep for forbidden terms. |
| **Runtime errors** | Messages in cli_main.py (e.g. "No raw_text texts", file not found) | No forbidden terms. |
| **Usage docs** | release/README.md, quickstart, any doc that shows CLI usage | No forbidden terms. |

---

## 3. Procedure

1. **Help output:**  
   `./hesperia-cli.bin --help` and `./hesperia-cli.bin analyze --help`, `compare --help`, `batch-analyze --help`.  
   Save to a file; run:  
   `grep -iE 'sphere|hex|topology|bridge|layer|family reserve|area count|12 areas|288 families' < help.txt`  
   **Expected:** No matches.

2. **Source and docs:**  
   Grep runtime/shipping/cli_main.py and release/README.md (and examples/README.md) for the same pattern.  
   **Expected:** No matches.

3. **Error paths:**  
   Trigger error paths (e.g. batch-analyze with no raw_text). Confirm stderr message does not contain forbidden terms.

---

## 4. Done condition

**Done when:** --help, runtime errors, and usage docs are clean (no sphere, hex, topology, bridge, layer, family reserve, area counts).
