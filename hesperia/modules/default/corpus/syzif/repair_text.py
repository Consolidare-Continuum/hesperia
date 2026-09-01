#!/usr/bin/env python3
"""Line-to-line word-transfer cleanup for syzif corpus text (post-conversion).

Reconstructed 2026-08-31 (Chiron) per operator spec — the original shipped in
sphereV_0.1_.zip, removed by Ethan's 2026-08-07 trash-out
(.cache_to_sort_out/README.md). Does not rename pages; page filenames stay
`NN Title - Author.md`.

Steps: CRLF -> LF, ftfy.fix_text (encoding mojibake), hyphen line-joins
(word-\\nnext -> wordnext), collapse blank runs, trim trailing spaces.
"""
import re
import sys

import ftfy

_HYPHEN_JOIN = re.compile(r"([a-zA-Z])-\n([a-z])")
_BLANK_RUNS = re.compile(r"\n{3,}")


def repair_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = ftfy.fix_text(text)
    text = _HYPHEN_JOIN.sub(r"\1\2", text)
    text = _BLANK_RUNS.sub("\n\n", text)
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.strip() + "\n"


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: repair_text.py <file.md> [more.md ...]", file=sys.stderr)
        return 2
    for path in argv:
        with open(path, encoding="utf-8", errors="replace") as f:
            content = f.read()
        fixed = repair_text(content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"repaired: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
