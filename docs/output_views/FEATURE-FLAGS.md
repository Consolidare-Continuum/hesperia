# Feature flags — output_views (T58)

| Flag / env | Default | Effect |
|------------|---------|--------|
| `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY` | off (`0` / unset) | Enables `POST /inspector/<id>/openai-proxy/` and proxy submit button on Session Inspector. |
| `OPENAI_API_KEY` | empty | Required when proxy is on; never committed. |
| `OPENAI_PROXY_MODEL` | `gpt-4o-mini` | Upstream model for proxy. |
| `OPENAI_PROXY_RATE_PER_MINUTE` | `30` | Per-IP rolling limit (see [OPENAI_PROXY-RATE-LIMIT.md](OPENAI_PROXY-RATE-LIMIT.md)). |
| `DJANGO_DEBUG` | `True` (dev) | Set `False` in production; reduces error leakage. |

Future flags should be listed here and mirrored in [README](README.md) §Environment.

`SIGNED: Daniel (safety baseline) | 2026-04-07 | T58`
