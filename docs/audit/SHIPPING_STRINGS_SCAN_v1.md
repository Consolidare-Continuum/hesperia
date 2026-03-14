# Shipping strings scan v1

**Status:** Active  
**Purpose:** Scan binary and unpacked image for high-risk reflective terms. Absent or minimal only.

---

## 1. Targets

- **CLI binary:** dist/hesperia-cli.bin (or main executable in dist/hesperia-cli/).
- **API image:** Unpack or run container and scan files under /app (or export image filesystem and run strings on relevant files).

---

## 2. Forbidden / high-risk terms

Scan for:

- sphere
- hex
- topology
- bridge
- layer
- area11
- family240
- side_id
- internal module names (e.g. invariant_catalog, pipeline_runner, layer_registry, if they appear as user-facing strings)

---

## 3. Procedure

**Binary:**

```bash
strings dist/hesperia-cli.bin | grep -iE 'sphere|hex|topology|bridge|layer|area11|family240|side_id|invariant_catalog|pipeline_runner' > /tmp/scan_cli.txt
```

**Image (example):**

```bash
docker run --rm hesperia-api:latest find /app -type f \( -name "*.py" -o -name "*.json" \) -exec cat {} \; 2>/dev/null | grep -iE 'sphere|hex|topology|bridge|layer|area11|family240' > /tmp/scan_api.txt
```

Or export image and run strings on selected binaries/libraries.

---

## 4. Interpretation

- **No hits:** PASS.
- **Hits only in third-party or dependency code:** Document; accept if not HESPERIA-specific.
- **Hits in application strings (help, errors, response templates):** FAIL; remove or reword and rebuild.

---

## 5. Done condition

**Done when:** High-risk reflective terms are absent or minimal (no serious internal terms in user-facing strings).
