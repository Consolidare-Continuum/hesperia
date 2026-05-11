# TMX-23: Design Consistency with Inspector Strips/Chips

**Owner**: Ava (design)  
**Status**: 2026-05-11 — consistency review complete; no regressions found.

---

## Component audit

The hex_matrix_viewer uses the same Tailwind + shadcn/ui component set as the inspector design language:

| Component | Inspector pattern | Matrix viewer | Consistent? |
|-----------|-----------------|---------------|-------------|
| Cards | `rounded-2xl`, `bg-slate-900/80`, `border-slate-800`, `shadow-2xl` | Same | ✓ |
| Badges (chips) | `rounded-xl`, dark bg, `text-slate-100` | Same pattern in status row | ✓ |
| Buttons | `variant="secondary"`, `rounded-2xl` | Same | ✓ |
| Sliders | Radix `<Slider>` component | Same (`src/components/ui/slider.jsx`) | ✓ |
| Input | Radix `<Input>` | Same (`src/components/ui/input.jsx`) | ✓ |
| Strip bars | `h-2 rounded-full bg-slate-800 overflow-hidden` | Used in dominance mass + drift bars | ✓ |

## RelationsPanel chip consistency (TMX-10)

`RelationsPanel.jsx` uses:
- `Badge` from `./ui/badge` — consistent with inspector chips
- Tab buttons: custom `<button>` with `bg-slate-700` active state — minor deviation (inspector uses `Badge` for tabs); acceptable for T3

## Colour palette parity

Area colours in dominance mass bar use the 12-colour palette:
- rose / orange / yellow / green / teal / cyan / blue / indigo / violet / purple / fuchsia / pink
- Matches the inspector area colour scheme (if/when it's built with the same palette)

## Drift bar colours (RelationsPanel)

- Safe (drift ≤ 0.05): `bg-emerald-500`
- Warn (0.05 < drift ≤ 0.15): `bg-amber-400`
- Alert (drift > 0.15): `bg-rose-500`

These are distinct from area colours — no confusion with area palette.

## Verdict

Design is consistent with the inspector strip/chip pattern. No regressions introduced by TMX-10 or TMX-15 changes.

SIGNED: Design (Ava) | Hesperia TMX-23 design consistency | 2026-05-11 | matrix vs inspector strips/chips
