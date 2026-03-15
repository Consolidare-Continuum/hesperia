#!/usr/bin/env python3
"""
Build LEVEL 4 Dict-A lexical_markers.yaml from Dict-B concept_nodes.yaml.
Target: 5–10 markers per concept for pilot areas A2, A3, A4, A10 (~120 concepts → ~800–1000 markers).
Extracts Russian keywords from definition and example_context; normalizes to lowercase.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
ONTOLOGY = REPO / "hesperia" / "ontology"
DICT_B_NODES = ONTOLOGY / "dictB" / "concept_nodes.yaml"
DICT_A_MARKERS = ONTOLOGY / "dictA" / "lexical_markers.yaml"

# Слова, не используемые как маркеры (шум, местоимения, служебные)
RU_STOP = frozenset({
    "и", "в", "на", "с", "как", "что", "без", "для", "или", "при", "по", "из", "к", "о", "от", "до",
    "же", "бы", "ли", "не", "но", "а", "у", "за", "под", "над", "через", "между", "перед", "после",
    "когда", "если", "то", "это", "так", "уже", "ещё", "только", "даже", "всего", "всё", "более",
    "менее", "очень", "всегда", "иногда", "здесь", "там", "тогда", "теперь", "также", "например",
    "другой", "других", "собой", "себя", "него", "неё", "них", "чем", "который", "которая", "которые",
    "какой", "какая", "какие", "такой", "такая", "такие", "весь", "вся", "все", "свой", "своей",
    "наш", "ваш", "его", "её", "их", "мой", "твой", "пациент", "терапевт", "сессии", "сессии",
})

# Минимум букв в маркере
MIN_LEN = 2
# Максимум маркеров на концепт из извлечённых слов
MAX_MARKERS_PER_SOURCE = 10
# Минимум маркеров на концепт (если мало — добавляем из запасного списка по области)
MIN_MARKERS_PER_CONCEPT = 5

# Дополнительные маркеры по областям (если из текста извлекли мало)
AREA_EXTRA_MARKERS = {
    "A2": ["объект", "репрезентация", "идентичность", "отношения", "связь", "интеграция", "диффузия", "граница", "нарратив", "амбивалентность", "вина", "зависимость", "привязанность"],
    "A3": ["защита", "проекция", "расщепление", "идеализация", "обесценивание", "диссоциация", "отрицание", "изоляция", "интроекция", "идентификация", "перенос", "контрперенос"],
    "A4": ["агрессия", "ярость", "гнев", "ненависть", "враждебность", "презрение", "зависть", "вина", "репарация", "контроль", "доминирование", "садизм", "месть"],
    "A10": ["терапия", "лечение", "контракт", "сеттинг", "альянс", "интерпретация", "перенос", "сопротивление", "регрессия", "интеграция", "рамки", "границы", "сессия", "завершение"],
}


def tokenize_ru(text: str) -> list[str]:
    """Извлечь русские слова из текста (буквы, апостроф, дефис). Только токены с кириллицей."""
    if not text or not isinstance(text, str):
        return []
    tokens = re.findall(r"[а-яёa-z\-']+", text.lower())
    return [
        t for t in tokens
        if len(t) >= MIN_LEN and t not in RU_STOP and re.search(r"[а-яё]", t)
    ]


def extract_markers(definition: str, example_context: str, limit: int = MAX_MARKERS_PER_SOURCE) -> list[str]:
    """Уникальные маркеры из definition и example_context."""
    words = tokenize_ru(definition or "") + tokenize_ru(example_context or "")
    seen: set[str] = set()
    out: list[str] = []
    for w in words:
        if w not in seen and len(w) >= MIN_LEN:
            seen.add(w)
            out.append(w)
            if len(out) >= limit:
                break
    return out


def main() -> int:
    if not DICT_B_NODES.exists():
        print(f"Dict-B nodes not found: {DICT_B_NODES}", file=sys.stderr)
        return 1

    with open(DICT_B_NODES, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    nodes = data.get("nodes") or []
    pilot_areas = {"A2", "A3", "A4", "A10"}
    entries: list[dict] = []
    concept_counts: dict[str, int] = {}

    for node in nodes:
        if not isinstance(node, dict):
            continue
        nid = node.get("id")
        area = node.get("area")
        if not nid or area not in pilot_areas:
            continue
        definition = node.get("definition") or ""
        example_context = node.get("example_context") or ""
        markers = extract_markers(definition, example_context)
        # Добить до MIN_MARKERS_PER_CONCEPT из области
        if len(markers) < MIN_MARKERS_PER_CONCEPT and area in AREA_EXTRA_MARKERS:
            for extra in AREA_EXTRA_MARKERS[area]:
                if extra not in markers:
                    markers.append(extra)
                    if len(markers) >= MIN_MARKERS_PER_CONCEPT:
                        break
        # Ограничить сверху
        markers = markers[:MAX_MARKERS_PER_SOURCE]
        concept_counts[nid] = len(markers)
        for m in markers:
            entries.append({
                "marker": m,
                "concept_id": nid,
                "language": "ru",
                "weight": 1.0,
            })

    out = {
        "version": 1,
        "domain": "TFP_KERNBERG",
        "language": "ru",
        "description": "LEVEL 4 Dict-A: лексические маркеры для пилота A2, A3, A4, A10. Текст → маркеры → концепты → семья/область.",
        "marker_count": len(entries),
        "concept_count": len(concept_counts),
        "entries": entries,
    }

    DICT_A_MARKERS.parent.mkdir(parents=True, exist_ok=True)
    with open(DICT_A_MARKERS, "w", encoding="utf-8") as f:
        yaml.dump(out, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    total = len(entries)
    avg = total / len(concept_counts) if concept_counts else 0
    print(f"Written {total} marker entries for {len(concept_counts)} concepts (avg {avg:.1f} per concept) to {DICT_A_MARKERS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
