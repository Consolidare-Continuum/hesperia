# Hesperia hex matrix viewer (browser)

Vite + React build for `HesperiaHexMatrixViewer` (canvas 72k hex mock, optional external JSON).

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

1. `rsync -av --delete dist/ prichindel:/var/www/hesperia-hex-matrix/` (path agreed with operator).
2. Nginx `location /hesperia/hex-matrix/` → `alias` that directory + `try_files $uri $uri/ /hesperia/hex-matrix/index.html`.

Hand off path and TLS to Abelard if not already wired.

## Source layout

- `src/HesperiaHexMatrixViewer.jsx` — main viewer (was repo-root `hesperia_hex_matrix_viewer.jsx`).
- `src/components/ui/*` — minimal stubs replacing shadcn `@/` imports.

SIGNED: Gena (main developer) | Hesperia output_views | 2026-04-14 | hex matrix viewer Vite shell
