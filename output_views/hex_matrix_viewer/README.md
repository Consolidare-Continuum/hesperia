# Hesperia hex matrix viewer (browser)

Vite + React build for `HesperiaHexMatrixViewer` (canvas 72k hex mock, optional external JSON).

Semantics, schema, layout, and modes: **`ARCHITECTURE.md`**.

## Dev

```bash
cd output_views/hex_matrix_viewer
npm install
npm run dev
```

Open the printed URL (default `http://127.0.0.1:5173`).

## Optional: load Hesperia export JSON

If you host a JSON file with shape `{ "frames": [ { "t": 0, "hexes": [ ... ] } ] }` (see component header in `src/HesperiaHexMatrixViewer.jsx`):

```
http://127.0.0.1:5173/?data=http%3A%2F%2F127.0.0.1%3A8009%2Fhex-frames.json
```

Use a static server with **CORS** for the JSON origin, or same-origin deploy.

## Production build

```bash
cd output_views/hex_matrix_viewer
npm ci
npm run build
```

Artifacts: `output_views/hex_matrix_viewer/dist/` (static files; `base` is relative `./`).

## Deploy (cluster)

Prod static hosting / nginx vhost = **Abelard** scope. Typical pattern:

1. `rsync -av --delete dist/* prichindel:/var/www/hesperia-sites/hex-matrix/` (path agreed with operator).
2. Nginx `location ^~ /hex-matrix/` with `root /var/www/hesperia-sites` + `try_files` for SPA (see cluster `hesperia.prichindel.com.conf`).

Hand off path and TLS to Abelard if not already wired.

## Source layout

- `src/HesperiaHexMatrixViewer.jsx` — main viewer UI + canvas.
- `src/schema/`, `src/layout/`, `src/render/`, `src/mock/`, `src/data/` — contract, deterministic layout, modes, mock, JSON pipeline.
- `src/components/ui/*` — minimal stubs replacing shadcn `@/` imports.

SIGNED: Gena (main developer) | Hesperia output_views | 2026-04-15 | semantic hex viewer (layout + modes + coherence)
