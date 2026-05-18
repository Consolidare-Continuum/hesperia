# TMX-20: QA Checklist — Browser, Many Iterations, Therapist Edges

**Owner**: Daniel (QA)  
**Status**: 2026-05-11 — checklist complete.

---

## Browser compatibility

| Browser | Min version | Status |
|---------|------------|--------|
| Chrome / Chromium | 110+ | Primary target |
| Firefox | 110+ | Supported |
| Safari | 16+ | Supported (WebGL for spheroid) |
| Edge | 110+ | Supported |

## Functional checklist

### Surface modes
- [ ] 288 lattice — flat projection renders all 288 family cells
- [ ] 288 lattice — diamond projection renders without overflow
- [ ] 288 lattice — cylinder projection wraps sectors correctly
- [ ] 288 lattice — spheroid (3D) renders; no WebGL crash on Safari
- [ ] 72k hex mode — renders 72,000 hexes; zoom/pan responsive

### Iteration / frame playback
- [ ] Frame slider plays through all frames without stutter (≤24 frames nominal)
- [ ] Playback speed control (ms/frame) takes effect immediately
- [ ] Pin selection: selected hex remains highlighted across frame changes
- [ ] Delta mode shows valid colour when only 1 frame (no prev-frame crash)
- [ ] Many iterations (24+ frames): no memory leak after 5 min continuous play

### Render modes
- [ ] Dominant area: colour matches area palette (12 colours)
- [ ] Dominance heat: gradient 0→1 correct
- [ ] Stability heat: gradient 0→1 correct
- [ ] Delta: greyed when frame 0 (no previous); active from frame 1
- [ ] Contradiction / boundary: value present in mock data; renders

### RelationsPanel (TMX-10)
- [ ] Panel appears when `dataset.relations` is present
- [ ] Drift bars render for all 12 areas; negative drift shown on left
- [ ] Tab switch Relations ↔ Appear/Disappear works
- [ ] `appeared` list renders with onset_frame
- [ ] `disappeared` list renders
- [ ] Panel hidden when dataset has no relations (mock or external JSON without field)

### Hover / select
- [ ] Hover shows hex id in badge (bottom overlay)
- [ ] Click selects hex; info card populates with area_scores[12], dominance, stability
- [ ] Contradiction and activation shown if present; hidden if null
- [ ] Search by id/family/area highlights hex

### Therapist edge cases
- [ ] Session with `topology_provenance=missing`: muted warning shown (from TMX-06)
- [ ] Session imprint ridge bars absent: no crash; stability scores fall back to 0.5 default
- [ ] All 12 area_scores = 0 for a hex: dominant_area defaults to 0; no NaN render
- [ ] Single-iteration session (1 frame): no delta crash; delta mode shows "n/a" state

### RU locale (TMX-14)
- [ ] When locale=ru active: surface labels, render mode names, tooltip strings display in RU
- [ ] Tier T3 label renders in RU: "T3 — Исследовательский"

### Gold fixture regression (TMX-15)
- [ ] `pytest tests/hex_matrix/ -v` — 5/5 pass

## Edge: large dataset URL
- [ ] `?data=<url>` with 72k hexes × 24 frames: loads within 10s on LAN; no tab crash
- [ ] `?data=<invalid-url>`: dataError banner shown; mock data rendered

SIGNED: QA (Daniel) | Hesperia TMX-20 QA checklist | 2026-05-11 | browser + iterations + therapist edges
