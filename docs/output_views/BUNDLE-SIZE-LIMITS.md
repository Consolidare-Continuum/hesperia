# Session bundle size — soft limits (T64)

**Context:** Session Inspector loads fixture JSON into memory and renders export payloads. Very large bundles can slow the browser and inflate clipboard/export size.

**Soft policy (v1):**

| Surface | Guideline |
|---------|-----------|
| **Fixture files** under `output_views/tests/fixtures/` | Prefer **≤ 2 MB** per file for CI and local dev; split sessions if larger. |
| **Production / BFF** | If bundles exceed **~5 MB**, prefer pagination or iteration-scoped fetch (future); return **413 Payload Too Large** only when a size gate is implemented server-side. |

**Current MVP:** No hard `413` in Django fixture path; this document sets **expectations** for authors of new fixtures.

`SIGNED: Gena | Hesperia | 2026-04-07 | T64`
