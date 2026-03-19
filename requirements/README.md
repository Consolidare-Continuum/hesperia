# Python requirements (repo root stays thin)

| File | Use |
|------|-----|
| `runtime.txt` | Default dev/CI (`pip install -r requirements.txt` from repo root). |
| `surface.txt` | Embedding stack only (included by `runtime.txt`). |
| `api.txt` | Docker API image (+ `runtime.txt`). |
| `embedding.txt` | Dict B embedding builds. |
| `build-embeddings.txt` | Pinned legacy embedding build. |

Root **`../requirements.txt`** is a one-line include into `runtime.txt`.
