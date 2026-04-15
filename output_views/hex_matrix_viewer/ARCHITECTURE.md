# Hex Matrix Viewer — architecture (semantic layout + modes)

## Schema (`src/schema/hexSchema.js`)

Per-hex state matches the agreed contract: `id`, `family_id`, `area_id`, `q`, `r`, `area_scores[12]`, `dominant_area`, `dominance`, `stability`, optional `contradiction`, `activation`. Transitions: `prev_dominant_area`, `delta_dominance`, `delta_activation`, `area_switched` (attached after frames are built).

## Layout (`src/layout/familyLayout.js`)

- **Deterministic**: 12 areas × 24 families/area × 250 hexes = 72,000.
- **Area macro-zones**: area origins on a fixed 3×4 grid with large pitch (~520 hex).
- **Family anchors**: 6×4 lattice inside each area (spacing ~56) so local spirals do not overlap.
- **Local packing**: same `buildHexSpiral(250)` as before, but **only inside** each family anchor — no global spiral as semantic placement.

Same inputs → same `(q,r)` assignment.

## Data pipeline (`src/data/datasetPipeline.js`)

`loadDataset(json)` normalizes each hex and, when `q`/`r` are missing and the frame has exactly 72,000 rows, merges coordinates from `buildSemanticLayout()` by row index. Exports that already include `q`/`r` win.

## Render modes (`src/render/modes.js`)

| Mode | Meaning |
|------|--------|
| `dominant_area` | 12 categorical RGBs; brightness from `dominance` only (default). |
| `dominance_heat` | Single scalar palette on `dominance`. |
| `stability_heat` | Single scalar palette on `stability`. |
| `delta` | Green/red vs `delta_dominance`; neutral when near zero. |
| `boundary` | Dim area-tinted fill + drawn edges where `dominant_area` differs from a neighbor. |
| `family_layout` | Stable `hsl(hash(family_id))` — layout inspection, not competition semantics. |
| `family_spectrum_debug` | Legacy rainbow by **array index** — **only with `?debug=1`**. |

## Coherence (`src/render/coherence.js`)

- One pass, deterministic, toggleable.
- **area_scores**: average score vectors with neighbors, recompute `dominant_area` / `dominance`.
- **dominance** / **stability**: neighbor average of the scalar.

Inspector shows raw vs derived when coherence is on.

## Performance

- Canvas draw with viewport culling (unchanged pattern).
- Coherence recomputes per derived view in `useMemo` (O(n)); neighbor map is O(n) per frame.
- Avoid allocating in the inner draw loop beyond existing polygon path.

## Risks / limits

- Imported frames with wrong length or partial coordinates fall back to `(0,0)` normalization — overlaps possible; full 72k export is assumed for layout merge.
- Boundary mode draws up to six edge segments per visible hex — slightly heavier than flat fill.
- Pixi/WebGL not required yet; drawing is isolated in one `useEffect` for a later swap-in.

## Mock (`src/mock/generateMockDataset.js`)

Generates schema-compliant data on the semantic layout; `attachFrameTransitions` fills temporal deltas between frames.
