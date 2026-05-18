# TMX-22: Integration — Nav Link from Session Inspector + Deep Links

**Owner**: Liam (integration)  
**Status**: 2026-05-11 — deep link contract documented; nav link stub in viewer.

---

## Deep link spec

The hex_matrix_viewer supports dataset loading via URL param:

```
/hex-matrix/?data=<encoded-dataset-url>&session=<session_id>&tier=<T1|T2|T3>
```

| Param | Required | Description |
|-------|----------|-------------|
| `data` | No | URL to JSON dataset (Dataset schema) |
| `session` | No | Session identifier for display / API calls |
| `tier` | No | T1/T2/T3 — affects trust display |
| `debug` | No | `1` to enable legacy family spectrum mode |

### From Session Inspector (when built)

The Session Inspector should link to the matrix viewer with:
```
/hex-matrix/?data=/inspector/<session_id>/timeline-matrix/dataset.json&session=<session_id>&tier=T2
```

### D3 cell → inspector deep link (already wired, TMX-07)

Clicking a hex cell navigates to:
```
/inspector/<session_id>/?iteration=<frame_index>
```
This was implemented in TMX-07 (archived DONE).

## Nav link stub in viewer

The viewer `README.md` (to be created) should include:
```html
<!-- Nav bar link to matrix (from inspector) -->
<a href="/hex-matrix/?data=...&session={{session_id}}&tier=T2">Timeline Matrix →</a>
```

## Current integration status

- Session Inspector web app: **not built** (no Django/Flask app exists in hesperia)
- Matrix viewer: standalone SPA at `output_views/hex_matrix_viewer/dist/`
- Deep link from viewer cell → inspector `?iteration=N`: implemented (TMX-07)
- Nav link from inspector → viewer: documented here; wiring pending inspector build

SIGNED: Dev (Liam) | Hesperia TMX-22 integration | 2026-05-11 | nav link + deep link contract
