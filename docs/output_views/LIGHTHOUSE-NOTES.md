# Lighthouse / a11y — output_views (T32)

**Policy:** Session Inspector is an **internal operator tool** (LAN / gated deploy). A full **Lighthouse** pass is **not** a merge gate for MVP.

**Expectations:**

- Prefer semantic regions (`<header>`, `<main>`, `<section>`, `aria-label` on panes) — already used where practical.
- Color contrast follows dark theme defaults; revisit if operator reports readability issues.
- Run Lighthouse manually when changing layout/CSS: `npx lighthouse http://127.0.0.1:8010/inspector/session_inspector_min/ --only-categories=accessibility` (optional).

**Not blocking:** perfect scores on focus order, ARIA completeness, or performance for v1.

`SIGNED: Gena | Hesperia | 2026-04-07 | T32`
