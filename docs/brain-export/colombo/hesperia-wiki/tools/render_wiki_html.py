#!/usr/bin/env python3
"""Render the markdown wiki to a static HTML site (pandoc), rewriting .md links to .html.
Local preview only — no server-side state, no external calls."""
import os
import re
import subprocess

SRC = "/data/altitudine/prichindel.com/colombo_research/hesperia/wiki"
DST = "/data/altitudine/prichindel.com/colombo_research/hesperia/wiki_site"

CSS = """
body{font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:900px;margin:2rem auto;padding:0 1.5rem;line-height:1.55;color:#1a1a1a;background:#fdfdfd}
@media (prefers-color-scheme:dark){body{color:#e8e8e8;background:#1a1a1a}a{color:#7ab8ff}code{background:#2a2a2a}table,th,td{border-color:#444}th{background:#2a2a2a}}
a{color:#0b5fa5;text-decoration:none}a:hover{text-decoration:underline}
code{background:#f0f0f0;padding:0.1em 0.35em;border-radius:3px;font-size:0.92em}
table{border-collapse:collapse;width:100%;margin:1em 0}
th,td{border:1px solid #ccc;padding:0.4em 0.7em;text-align:left}
th{background:#f0f0f0}
h1{border-bottom:2px solid #ccc;padding-bottom:0.3em}
hr{border:none;border-top:1px solid #ccc;margin:2em 0 1em}
"""

def md_to_html_links(text):
    return re.sub(r"\]\(([^)]+)\.md\)", r"](\1.html)", text)

def main():
    os.makedirs(DST, exist_ok=True)
    n = 0
    for dirpath, _, files in os.walk(SRC):
        rel = os.path.relpath(dirpath, SRC)
        outdir = os.path.join(DST, rel) if rel != "." else DST
        os.makedirs(outdir, exist_ok=True)
        for fn in files:
            if not fn.endswith(".md"):
                continue
            src_path = os.path.join(dirpath, fn)
            text = open(src_path).read()
            text = md_to_html_links(text)
            tmp_md = src_path + ".tmp.md"
            open(tmp_md, "w").write(text)
            out_html = os.path.join(outdir, fn[:-3] + ".html")
            title = fn[:-3].replace("-", " ")
            subprocess.run([
                "pandoc", tmp_md, "-f", "gfm", "-t", "html5", "--standalone",
                "-M", f"title={title} — Hesperia Wiki",
                "-o", out_html
            ], check=True)
            os.remove(tmp_md)
            n += 1
    with open(os.path.join(DST, "style.css"), "w") as f:
        f.write(CSS)
    # inject css link into every generated html (pandoc standalone doesn't know about it yet)
    for dirpath, _, files in os.walk(DST):
        for fn in files:
            if fn.endswith(".html"):
                p = os.path.join(dirpath, fn)
                depth = os.path.relpath(dirpath, DST).count(os.sep) + (0 if os.path.relpath(dirpath, DST) == "." else 1)
                prefix = "../" * depth
                html = open(p).read()
                html = html.replace("</head>", f'<link rel="stylesheet" href="{prefix}style.css"></head>')
                open(p, "w").write(html)
    print(f"Rendered {n} html files to {DST}")

if __name__ == "__main__":
    main()
