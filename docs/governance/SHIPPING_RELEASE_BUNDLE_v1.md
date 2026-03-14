# Shipping release bundle v1

**Status:** Active  
**Purpose:** Define the contents of the shipping repo or release bundle (hesperia-eval/ or zip/tarball). Verify excluded content. Dry-run checklist for a clean Linux box.

---

## 1. Bundle contents (S6-T1)

The release bundle must include:

| Item | Description |
|------|-------------|
| **Binary** | `hesperia-cli.bin` (onefile) or `hesperia-cli/` (standalone). |
| **Container** | `hesperia-api-image.tar` or pull instructions for the API image. |
| **Examples** | Sample input/output (e.g. examples/analyze_output.json, examples/compare_output.json). |
| **Public schema** | assets/public/public_output_schema.json (or copy into bundle). |
| **Quickstart** | One-page quickstart (CLI + API commands, env vars, limitations). |
| **Limitations** | Clear statement: no internal endpoints, projected outputs only, rate limits. |
| **Checksums** | checksums.txt (SHA256 of binary and image). |
| **Manifest** | manifest.json (version, commit, timestamp, artifacts, entry_points). |

Optional: governance subset (PUBLIC_* policies) if needed for operator reference.

---

## 2. Verify excluded content (S6-T2)

Before packaging, confirm the bundle does **not** contain:

- **Internal docs** — docs/internal/, MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY.
- **Source tree** — Full repo source (only binary + image + examples + schema + docs listed above).
- **Mixed scripts** — No dev runners (run_l1_l2, run_e2e_all, etc.) as advertised entry points.
- **Debug tools** — No layer dumps, propagation path export, or internal trace scripts.
- **Internal-review runners** — analyze.py, r1_r4_pipeline, batch_runner, reading_scales, run_corpus_benchmark not exposed as primary commands.

Use the same exclusion list as in SHIPPING_EXCLUSION_POLICY_v1 and .dockerignore.shipping. The CLI is a single binary (no source). The API image is built from Dockerfile.shipping and does not COPY docs/internal or legacy.

---

## 3. Dry-run on a clean Linux box (S6-T3)

Test on a machine that has not the full repo, only the bundle:

| Step | Action | Expected |
|------|--------|----------|
| 1 | Unpack or copy bundle (binary + image tar + examples + quickstart). | No errors. |
| 2 | Run CLI: `./hesperia-cli.bin analyze --text "justice fairness"`. | Exit 0; JSON output; no internal terms (sphere, hex, side_id, etc.). |
| 3 | Run API: `docker load -i hesperia-api-image.tar`, `docker run -p 8000:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest`. | Container starts; GET /health returns {"status":"ok"}. |
| 4 | POST /analyze with body `{"text": "justice"}`. | 200; projected JSON; no internal coordinates. |
| 5 | Inspect outputs. | All outputs are projected (macro_domain_vector, policy_family_counts, etc.); no reserved structure (area 10/11, families 240–287). |
| 6 | Check that no extra artifacts (layer dumps, debug files) appear. | Only responses and any written --out files. |

Pass: CLI works, API works, outputs are projected, no extra artifacts. Fail: fix before release.
