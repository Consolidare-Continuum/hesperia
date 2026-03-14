# Shipping Nuitka build v1

**Status:** Active  
**Purpose:** Build the sealed CLI as a Linux binary using Nuitka. Standalone first (easier to debug), then onefile; strip symbols to reduce introspection value.

---

## 1. Build order (Nuitka recommendation)

1. **Standalone first** — Build with `--standalone` and verify the binary runs. Standalone is easier to debug than onefile.
2. **Onefile after** — Build with `--onefile` only after standalone passes.
3. **Strip** — Run `strip` on the binary(ies) to remove symbols and reduce obvious metadata.

---

## 2. Deliverables

| Task | Deliverable | Description |
|------|-------------|-------------|
| S2-T3 | **dist/hesperia-cli/** | Standalone build directory: executable plus shared libraries and data. Run from repo root: `./tools/build_nuitka_cli.sh`; output is under `dist/hesperia-cli/`. |
| S2-T4 | **dist/hesperia-cli.bin** | Single-file executable for evaluator convenience. Produced by the same script after standalone succeeds. |
| S2-T5 | **Stripped binary** | Standalone and onefile binaries are stripped (strip --strip-unneeded or strip) to reduce names and binary introspection value. |

---

## 3. How to build

From repository root:

```bash
# Install Nuitka if needed
pip install nuitka

# Run the build script (standalone → onefile → strip)
./tools/build_nuitka_cli.sh
```

Requirements: `nuitka3`, `python3`, C compiler (e.g. gcc), `strip` (binutils). First run may download Nuitka dependencies (e.g. ordered-set).

---

## 4. Verification

After standalone build:

```bash
./dist/hesperia-cli/hesperia-cli analyze --text "justice fairness"
# or, if Nuitka put binary in a .dist subdir:
./dist/hesperia-cli/*/hesperia-cli analyze --text "justice fairness"
```

After onefile build:

```bash
./dist/hesperia-cli.bin analyze --text "justice fairness"
```

---

## 5. Done condition

- Standalone build completes and produces `dist/hesperia-cli/`.
- Onefile build completes and produces `dist/hesperia-cli.bin`.
- Both binaries are stripped; no reliance on PyInstaller or zip encryption as the main protection.
