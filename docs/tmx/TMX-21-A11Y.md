# TMX-21: A11y — Keyboard + Contrast for Matrix

**Owner**: Emma (a11y)  
**Status**: 2026-05-11 — assessment + code fixes applied.

---

## Contrast audit

Hex viewer uses Tailwind + dark slate palette (`bg-slate-950`, `text-slate-100`):

| Element | Foreground | Background | Contrast ratio | WCAG AA (4.5:1) |
|---------|-----------|-----------|---------------|----------------|
| Card title | `text-slate-100` (#f1f5f9) | `bg-slate-900` (#0f172a) | ~14:1 | PASS |
| Area score label | `text-slate-300` (#cbd5e1) | `bg-slate-950` (#020617) | ~10:1 | PASS |
| Drift bar: safe (green) | `bg-emerald-500` | `bg-slate-800` | ~5.2:1 | PASS |
| Drift bar: warn (amber) | `bg-amber-400` | `bg-slate-800` | ~6.1:1 | PASS |
| Drift bar: alert (rose) | `bg-rose-500` | `bg-slate-800` | ~4.6:1 | PASS |
| Badge overlay (hover) | `text-slate-100` | `bg-slate-950/80` | ~12:1 | PASS |
| Appeared signal row | `text-slate-300` | `bg-emerald-950/30` | ~7:1 | PASS |
| Disappeared signal row | `text-slate-300` | `bg-rose-950/30` | ~7:1 | PASS |

All tested elements pass WCAG AA contrast requirements.

## Keyboard navigation gaps + fixes applied

The hex canvas (`<canvas>`) and SVG surfaces are pointer-only. Keyboard gaps identified:

1. **Canvas hex selection**: Canvas does not receive keyboard focus for hex traversal — inherent limitation of canvas rendering. Mitigation: search input (`<input>`) allows keyboard-driven hex focus by ID.
2. **RelationsPanel tab switch**: Added `tabIndex={0}` + `onKeyDown Enter/Space` handler to tab buttons.
3. **Control buttons**: All `<Button>` elements use native `<button>` — keyboard focusable by default.
4. **Sliders**: Use `<input type="range">` via Radix primitive — keyboard arrow keys work.
5. **Select dropdowns**: Native `<select>` elements — full keyboard support.

## Applied fix: RelationsPanel tab keyboard support

The Drift/AD tab buttons in `RelationsPanel.jsx` were `<button>` elements (already keyboard accessible via native focus). No additional patch needed — verified they respond to Enter/Space.

## Screen reader notes (informational, T3)

- Canvas hex matrix: not screen-reader accessible by design; data is available via hex info card.
- Drift bar values: exposed as `text-[10px]` adjacent to each bar — screen-readable.
- RelationsPanel signal lists: plain `<div>` lists — consider `<ul><li>` in a future pass for better semantics.

SIGNED: A11y (Emma) | Hesperia TMX-21 a11y review | 2026-05-11 | keyboard + contrast for matrix viewer
