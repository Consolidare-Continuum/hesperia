import re
from pathlib import Path

from spellchecker import SpellChecker


PATH = Path("4 Governing the Commons - Elinor Ostrom.md")
ALPHABET = "aeiouy"


def generate_variants(word: str) -> set[str]:
    variants = {""}
    for ch in word:
        if ch == "�":
            variants = {
                prefix + letter for prefix in variants for letter in ALPHABET
            }
        else:
            variants = {prefix + ch for prefix in variants}
    return variants


def choose_replacement(word: str, spell: SpellChecker) -> str | None:
    lower = word.lower()
    variants = generate_variants(lower)
    best = None
    best_score = 0
    for candidate in variants:
        score = spell.word_frequency[candidate]
        if score > best_score:
            best_score = score
            best = candidate

    if not best and variants:
        best = max(variants, key=lambda candidate: spell.word_frequency[candidate])
        if spell.word_frequency[best] == 0:
            return None

    return best


def apply_case(source: str, candidate: str) -> str:
    if source.isupper():
        return candidate.upper()
    if source[0].isupper():
        return candidate.capitalize()
    return candidate


def main():
    text = PATH.read_text(encoding="utf-8")
    spell = SpellChecker(language="en")
    tokens = sorted(
        {word for word in re.findall(r"[A-Za-z�’'-]+", text) if "�" in word}
    )

    replacements = {}
    for token in tokens:
        replacement = choose_replacement(token, spell)
        if replacement:
            replacements[token] = apply_case(token, replacement)

    if not replacements:
        print("No automated replacements found.")
        return

    for original, corrected in replacements.items():
        text = text.replace(original, corrected)

    PATH.write_text(text, encoding="utf-8")
    for original, corrected in replacements.items():
        print(f"{original} -> {corrected}")


if __name__ == "__main__":
    main()
