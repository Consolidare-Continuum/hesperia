# CLI binary reflection scan v1

**Status:** Active  
**Purpose:** After building the shipping CLI binary, run symbol stripping, strings scan, and forbidden-term scan. No serious internal terms should remain in strings output.

---

## 1. Steps

### Step 1 — Symbol stripping

Run on the binary (standalone and onefile):

```bash
strip --strip-unneeded dist/hesperia-cli.bin
# or for standalone:
find dist/hesperia-cli -type f -executable -name "hesperia-cli" -o -name "cli_main" | xargs -I {} strip --strip-unneeded {}
```

Reduces symbol table and debug info. Document that stripping was applied.

### Step 2 — Strings scan

Extract printable strings from the binary:

```bash
strings dist/hesperia-cli.bin > /tmp/cli_strings.txt
```

Inspect or archive /tmp/cli_strings.txt for review.

### Step 3 — Forbidden-term scan

Search strings output for high-risk terms:

```bash
strings dist/hesperia-cli.bin | grep -iE 'sphere|hex|topology|bridge|layer|area11|family240|side_id|288 families|propagation path|invariant_catalog' > /tmp/forbidden_hits.txt
```

**Expected:** No matches, or only low-value/minimal hits (e.g. in dependency code, not in HESPERIA-specific user-facing strings). Any hit must be reviewed; serious internal terms (formulas, structure names, execution_flow stages) must be removed or accepted as non-revealing.

---

## 2. Interpretation

| Summary | Action |
|--------|--------|
| No hits | PASS. |
| Hits in third-party libs only | Document; accept if not HESPERIA-specific. |
| Hits in application code (e.g. error messages, help) | FAIL; remove or reword in source and rebuild. |

---

## 3. Done condition

**Done when:** No serious internal terms remain in strings output (or only accepted, low-value hits). Stripping and scan are documented and run before release.
