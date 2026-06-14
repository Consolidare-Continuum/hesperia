# Grace triage — HES-DEBLOAT-WAVE2-CLOSURE

**Date:** 2026-06-14  
**IDs:** HES-DEBLOAT-W2-00 (closure)

---

## Summary

Wave 2 debloat: brain repo holds **links only** for Hesperia + Tersagor. Bulk content → dev repos.

| Target | Path | Commit (alunel export pass) |
|--------|------|-----------------------------|
| **igareosh/hesperia** | `docs/brain-export/` | `b37a676` |
| **igareosh/tersagor** | `docs/brain-export/` | `3ec8d36` |

**Not moved:** `user_documents/**` (operator mandate).

**Dev host (operator):** **altitudine** VM — proper dev VM; Hesperia sync runs there, not alunel bare metal.

---

## Rows

| ID | Owner | Task | Status |
|----|-------|------|--------|
| HES-DEBLOAT-W2-00 | Grace | Closure — wave 2 debloat triaged; brain push + altitudine manifest sync | DONE |
| HES-DEBLOAT-W2-01 | Cursor | Brain commit/push debloat + link stubs | DONE |
| HES-DEBLOAT-W2-02 | Felix/Gena | `hesperia-sync-brain-links-to-dev.sh` on **altitudine** | DONE |

---

## Verify

- [ ] `verify-brain-no-hesperia-product-ingest.sh` OK on brain
- [ ] `docs/brain-links/MANIFEST.md` on `igareosh/hesperia` mentions wave 2 + altitudine dev host
- [ ] `user_documents/` unchanged

`SIGNED: Grace (triage) | HES-DEBLOAT-WAVE2 | 2026-06-14`
