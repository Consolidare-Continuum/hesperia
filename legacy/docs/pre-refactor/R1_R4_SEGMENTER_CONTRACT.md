# Historical reference (pre-refactor)

# R1–R4 Segmenter contract

**Purpose:** Contract for paragraph, chapter, and book/part segmenters required for R2/R3/R4 units. Implementations must satisfy this contract. **Spec:** [SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md) §Implementation Plan item 3. **Owner (implementation):** Gena (task 3).

---

## Input

- **Full text** (string), or
- **Token stream** (sequence of tokens with optional span offsets)

Format is implementation-defined; segmenter MAY accept either or both. Caller provides one.

---

## Output

Per-unit **span or token ranges** sufficient to run attribution and L1–L9 on that unit’s text:

- **R2 (paragraph):** List of spans `[{start, end}, ...]` or token ranges `[{start_idx, end_idx}, ...]` such that each range is one paragraph. Order preserved. No overlap; coverage of input.
- **R3 (chapter):** List of spans or token ranges, one per chapter (or part). Order preserved. No overlap; coverage of input.
- **R4 (book/part):** One or more ranges covering the full text (e.g. one “book” or one per “part” if split). Order preserved.

Each range is used to extract the corresponding substring (or token slice), then run tokenize → attribute → L1–L9 → Unit schema. So output MUST allow deterministic extraction of the unit’s text.

---

## Contract (summary)

| Level | Input | Output | Implementation |
|-------|--------|--------|----------------|
| R1 | Full text | List of (start, end) spans (one per sentence) | `segment_by_sentences` in sphere_rag/r1_r4_segmenters.py |
| R2 | Full text or token stream | List of spans or token ranges (one per paragraph) | `segment_by_paragraphs` |
| R3 | Full text or token stream | List of spans or token ranges (one per chapter) | `segment_by_chapters` |
| R4 | Full text or token stream | List of spans or token ranges (one per book/part) | `segment_by_book` |

- **Deterministic:** Same input → same output.
- **No overlap, full coverage:** Ranges partition the input.
- **Stable ordering:** Order of units matches document order.

Implementations may use heuristics (e.g. double newline for paragraph, `# ` or chapter markers for chapter) or external tools; they MUST document the method and satisfy the contract above.
