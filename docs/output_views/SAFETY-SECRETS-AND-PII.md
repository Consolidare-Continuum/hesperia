# Secrets and PII — output_views (T26, T27)

## Secrets (T26)

- **No API keys or tokens in git.** Use environment variables only (`OPENAI_API_KEY`, `DJANGO_SECRET_KEY`, etc.).
- Load from Hesperia repo root **`.env`** (gitignored) or host env; see [README](README.md).
- **Never** paste secrets into templates, fixtures, or logs. The OpenAI proxy path logs **latency and model only**, not request bodies.

## PII warning (T27)

- Session bundles may include **source file names** and **client text**. Exported JSON (`segment.json`, clipboard copy) can contain that material.
- The Session Inspector shows a **confirmation dialog** before copy/download when export is available.
- Operators are responsible for **data handling** consistent with their jurisdiction and agreements.

`SIGNED: Daniel (safety baseline) | Hesperia output_views | 2026-04-07 | T26–T27`
