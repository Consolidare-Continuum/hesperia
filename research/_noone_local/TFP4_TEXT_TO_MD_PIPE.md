# TFP corpus ingest — `~/tfp/4` text → Markdown (gaps only)

## 1. Folder layout (done)

Under **`/home/igareosh/tfp/4`**:

- **`images/`** — all `.png` slide captures (original subpaths preserved under `images/…`).
- **`text/`** — all machine-readable sources: `.docx`, `.doc`, `.ppt`, `.pptx`, `.pdf`.

Raster slides are **not** converted here; they stay under `images/` for figure galleries or future OCR. This pipe is for **text-bearing** files under `text/`.

## 2. Gap list (do not duplicate corpus)

**Source of truth:** `tfp4_corpus_gap_manifest.json` (same directory as this file).

- Each file has `sha256`, `ingest_to_md` (boolean), and optional `corpus_equivalent_md`.
- **Only** rows with `"ingest_to_md": true` should produce new `.md` in the corpus tree.
- Rows with `"ingest_to_md": false` are either already covered by an existing note under `research/_noone_local/` or are explicit dedupes (e.g. edited vs raw `.pptx`).

Current skips (verified against real corpus):

| Source under `text/` | Existing corpus |
|----------------------|-----------------|
| `Практически неизлечимый… пациент.docx` | `2_cleaned/Практически неизлечимый нарциссический пациент.md` |
| `дифдиагностика.docx` | `2_cleaned/Дифференциальная диагностика.md` |
| `Кернберг 2014.docx` | `2_cleaned/Кернберг - Обзор лечения тяжелой нарциссической патологии 2014.md` |
| `TFP раздаточный… Введение в TFP…pdf` | `2_cleaned/TFP - Введение раздаточный материал.md` |
| `Narcissism - Doering…pptx` | `background/Doering - Narcissism RUS ENG.md` |
| `Implicit communication - Doering…pptx` | `background/Doering - Implicit Communication RUS.md` |
| `Москва О супервизии 2019 ГОТОВО edited.pptx` | Prefer `Москва О супервизии 2019 ГОТОВО.pptx` only |

**Manual review:** `Moscow 2020 BPO DID and Gender Identity RUS.pptx` — compare with `background/TFP - Moscow Workshop Dec 2020.md` before publishing a second `.md`.

Regenerate the manifest after adding or renaming files under `text/`:

```bash
python3 tools/tfp4_build_corpus_gap_manifest.py \
  --text-root /home/igareosh/tfp/4/text \
  --write /data/hesperia/hesperia/research/_noone_local/tfp4_corpus_gap_manifest.json
```

## 3. Conversion pipeline (readable text → `.md`)

Target output (suggested): `research/_noone_local/ingest_from_tfp4_md/` — one `.md` per ingested source, plus YAML front matter (`title`, `source_path`, `sha256`, `ingested_at`).

### 3.1 `.docx`

```bash
pandoc -f docx -t markdown-smart --wrap=none -o "out.md" "in.docx"
```

Post-pass: fix heading levels, strip duplicated title lines, normalize quotes.

### 3.2 `.doc`

Prefer one-time conversion to `.docx` (LibreOffice headless) then same as 3.1, or:

```bash
pandoc -f doc -t markdown-smart --wrap=none -o "out.md" "in.doc"
```

(if the build supports `doc`; otherwise LibreOffice → docx).

### 3.3 `.pdf`

If text layer is good:

```bash
pdftotext -layout -enc UTF-8 "in.pdf" "body.txt"
```

Wrap in Markdown with a top-level heading from the filename; or use `pandoc -f pdf` if available.

If scan-only: run **`ocrmypdf`** (once) → searchable PDF → `pdftotext`.

### 3.4 `.ppt` / `.pptx`

Pandoc usually **does not** read these. Standard path:

1. `soffice --headless --convert-to pdf:writer_pdf_Export …`
2. Then section 3.3 on the PDF.

Expect **lossy** structure (slide titles as paragraphs). For deck-heavy material, consider keeping the PDF next to the `.md` and linking it from front matter instead of pretending slides are prose.

### 3.5 Garbage / OCR

`Клиническая оценочная решетка - текст частично поврежден OCR.docx` — likely needs **re-source** or manual fix; do not bulk-publish until reviewed.

## 4. Automation entrypoint

```bash
export HESPERIA_TFP4_ROOT=/home/igareosh/tfp/4
python3 tools/tfp4_text_to_md_ingest.py --dry-run
python3 tools/tfp4_text_to_md_ingest.py --out research/_noone_local/ingest_from_tfp4_md
```

The script reads `tfp4_corpus_gap_manifest.json`, skips `ingest_to_md: false`, and converts what the local toolchain supports (see script help).

## 5. Promotion into the “real” corpus

After human QA, move or merge from `ingest_from_tfp4_md/` into `2_cleaned/` or `background/` using the same naming style as existing notes (`Author - Title (year).md`). Update this doc or the manifest if new overlaps appear.
