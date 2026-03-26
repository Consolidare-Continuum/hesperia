# Shipping CLI text audit v1

**Status:** Active  
**Purpose:** CLI help and any user-facing text must not mention internal architecture. Run this audit on the shipping entry point (runtime/shipping/cli_main.py) and any bundled help before release.

---

## 1. Forbidden terms in CLI text

The following must **not** appear in:

- Program description (argparse description)
- Subcommand help (analyze, compare, batch-analyze)
- Argument help (--text, --out, --assets, --raw_text, --texts, --text1, --text2)
- Any stdout/stderr message produced by the shipping CLI

| Term / pattern | Reason |
|----------------|--------|
| sphere | Geometry-revealing |
| hex, hexagon | Geometry-revealing |
| layers, layer 1–9, L1–L9 | Execution Flow internals |
| bridge | Bridge logic internals |
| topology | Internal structure |
| reserve, reserved structure, area 11, area 12 | Reserve structure |
| 12 areas, 288 families | Internal counts |
| side_id, adjacency, propagation path | Internal coordinates/method |

---

## 2. Audited surface

**File:** `runtime/shipping/cli_main.py`

| Location | Text | Forbidden term? |
|----------|------|------------------|
| Main description | "Structural measurement. Commands: analyze, compare, batch-analyze." | No |
| analyze help | "Run structural measurement on one text." | No |
| compare help | "Compare two texts (structural emphasis and confidence)." | No |
| batch-analyze help | "Run structural measurement on multiple texts." | No |
| --assets | "Path to lexicon assets (default: repo/lexicon/curated)" | No |
| --text | "Raw_text text to analyze." | No |
| --out | "Write summary JSON to this path." | No |
| --text1 / --text2 | "First text." / "Second text." | No |
| --raw_text | "JSON file: list of strings or object with 'texts' key." | No |
| --texts | "Texts as arguments." | No |
| batch error | "No raw_text texts. Use --raw_text path.json or --texts '...' '...'" | No |

**Summary:** No forbidden terms in shipping CLI text.

---

## 3. Verification command

From repo root, capture all help output and search for forbidden terms:

```bash
cd /path/to/hesperia
python3 -m runtime.shipping.cli_main --help > /tmp/help_main.txt
python3 -m runtime.shipping.cli_main analyze --help >> /tmp/help_main.txt
python3 -m runtime.shipping.cli_main compare --help >> /tmp/help_main.txt
python3 -m runtime.shipping.cli_main batch-analyze --help >> /tmp/help_main.txt
grep -iE 'sphere|hex|layer|bridge|topology|reserve|12 areas|288|side_id|adjacency|propagation' /tmp/help_main.txt && echo "FAIL: forbidden term found" || echo "PASS: no forbidden terms"
```

**Expected:** PASS (no matches).

---

## 4. Ongoing rule

Any change to `runtime/shipping/cli_main.py` (or to a component that provides CLI strings to the shipping binary) must be re-audited. Do not add help or messages that mention the forbidden terms above.

---

## 5. Done condition

CLI help and shipping CLI messages contain no reflective terms. Audit run shows PASS.
