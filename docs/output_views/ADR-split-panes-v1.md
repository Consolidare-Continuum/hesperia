# ADR: Resizable Session Inspector panes (T55)

## Context

Session Inspector §5–6 requires an IDE-style layout (text | parameters | audit). Phase 1 MVP uses **CSS Grid** in `static/output_views/css/site.css` (`.insp-grid`).

## Decision (v1)

- **Ship with CSS Grid + `@media` stack** for mobile (single column, order: header → toolbar → strip → panes A → B → C).
- **Defer** `split.js` (or similar) until Phase 2 when operators need drag-resize persistence; grid fractions are sufficient for read-only review.

## Alternatives

| Option | Pros | Cons |
|--------|------|------|
| **split.js** | Drag handles, persisted % | Extra JS, a11y testing |
| **CSS `resize` on overflow** | No deps | Clunky UX for three panes |
| **React SPA** | Rich layout | Out of scope for Django MVP |

## Status

Accepted for **OUT-VIEW-03** MVP; revisit when Phase 3 graph export or operator feedback demands pixel-level control.

`SIGNED: Gena | Hesperia | 2026-04-07 | T55`
