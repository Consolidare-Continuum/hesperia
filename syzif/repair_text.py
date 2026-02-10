import re
from ftfy import fix_text
from pathlib import Path


ROOT = Path(__file__).parent


def remove_hyphenated_line_breaks(text: str) -> str:
    """Merge hyphen-terminated lines with the next lowercase line start."""
    pattern = re.compile(r"([A-Za-z])-\n\s*([a-z])")
    while True:
        text, count = pattern.subn(r"\1\2", text)
        if count == 0:
            break
    return text


def collapse_blank_runs(text: str) -> str:
    """Limit sequences of blank lines to at most one blank line."""
    return re.sub(r"\n{3,}", "\n\n", text)


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = fix_text(text)
    text = remove_hyphenated_line_breaks(text)
    text = collapse_blank_runs(text)

    lines = text.split("\n")
    cleaned_lines = []
    blank_prev = False

    for line in lines:
        if not line.strip():
            if blank_prev:
                continue
            blank_prev = True
            cleaned_lines.append("")
            continue

        cleaned_lines.append(line.rstrip())
        blank_prev = False

    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()

    return "\n".join(cleaned_lines) + ("\n" if cleaned_lines else "")


def main():
    for entry in ROOT.iterdir():
        if entry.is_file() and entry.suffix.lower() == ".md":
            original = entry.read_text(encoding="utf-8")
            cleaned = clean_text(original)
            if cleaned != original:
                entry.write_text(cleaned, encoding="utf-8")


if __name__ == "__main__":
    main()
