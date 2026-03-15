# HESPERIA — LEVEL 5/6 Session text → concept activation pipeline
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
TEXT → CONCEPT pipeline: tokenize → normalize → (tokens + ngrams) → detect markers → activate concepts.
Aggregates to concept_score, family_score, area_score. Output: semantic activation map.

LEVEL 7 (Session topology) использует этот вывод для структурной интерпретации:
dominant defenses, dominant object relations, aggression intensity, relational capacity;
dominant_area, dominant_family, secondary_area и т.д.
"""

from __future__ import annotations

import re
from typing import Any

# Lazy imports for ontology (optional paths for tests)
def _get_marker_index():
    from hesperia.ontology.dictA import build_marker_to_concepts
    return build_marker_to_concepts()

def _get_phrase_index():
    from hesperia.ontology.dictA import build_phrase_marker_index
    return build_phrase_marker_index()

def _get_concept_to_af():
    from hesperia.ontology.dictB import build_concept_to_area_family
    return build_concept_to_area_family()


def tokenize_text(text: str) -> list[str]:
    """
    Разбить текст на токены (слова). Сохраняются буквы (кириллица, латиница), цифры, дефис.
    """
    if not text or not isinstance(text, str):
        return []
    # Одна или более букв/цифр/дефиса подряд
    return re.findall(r"[а-яёa-z0-9\-]+", text, re.IGNORECASE)


def normalize_tokens(tokens: list[str]) -> list[str]:
    """Нормализовать токены: нижний регистр, обрезка пробелов."""
    return [t.strip().lower() for t in tokens if isinstance(t, str) and t.strip()]


def build_ngrams(tokens: list[str], n: int = 2) -> list[str]:
    """
    Построить n-граммы из токенов (перекрывающиеся окна). Возвращает список строк "w1 w2 ... wn".
    """
    if not tokens or n < 1 or n > len(tokens):
        return []
    out: list[str] = []
    for i in range(len(tokens) - n + 1):
        ngram = " ".join(tokens[i : i + n])
        out.append(ngram)
    return out


def build_ngram_tuples(tokens: list[str], n: int) -> list[tuple[str, ...]]:
    """
    Построить n-граммы как кортежи токенов для O(1) lookup в phrase_index.
    Возвращает [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)].
    """
    if not tokens or n < 1 or n > len(tokens):
        return []
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def detect_markers(
    tokens: list[str],
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
) -> list[tuple[str, float]]:
    """
    Для каждого токена найти совпадения в marker_index. Возвращает список (concept_id, weight).
    marker_index: нормализованный маркер → [(concept_id, weight), ...].
    """
    index = marker_index if marker_index is not None else _get_marker_index()
    out: list[tuple[str, float]] = []
    for t in tokens:
        hits = index.get(t)
        if hits:
            out.extend(hits)
    return out


def detect_phrase_markers(
    ngrams: list[str] | None = None,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    tokens: list[str] | None = None,
    phrase_index: dict[str, dict[tuple[str, ...], list[tuple[str, float]]]] | None = None,
) -> list[tuple[str, float]]:
    """
    Фразовые маркеры: (1) по ngrams+marker_index (строки) или (2) по tokens+phrase_index (кортежи, O(n)).

    Вариант 1: ngrams — список строк "w1 w2", marker_index — маркер → [(concept_id, weight)].
    Вариант 2: tokens — нормализованные токены, phrase_index — build_phrase_marker_index();
    строит биграммы и триграммы, lookup по кортежам, возвращает совпадения.
    """
    if tokens is not None and phrase_index is not None:
        out: list[tuple[str, float]] = []
        for n in (2, 3):
            key = f"phrase_length_{n}"
            idx = phrase_index.get(key) or {}
            if len(tokens) < n:
                continue
            for tup in build_ngram_tuples(tokens, n):
                hits = idx.get(tup)
                if hits:
                    out.extend(hits)
        return out
    # Legacy: string ngrams + marker_index
    if ngrams is None:
        return []
    index = marker_index if marker_index is not None else _get_marker_index()
    out = []
    for phrase in ngrams:
        hits = index.get(phrase)
        if hits:
            out.extend(hits)
    return out


def activate_concepts(
    markers: list[tuple[str, float]],
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    normalize_scores: bool = True,
) -> dict[str, Any]:
    """
    Агрегировать маркеры в оценки по концептам, семьям и областям.

    - concept_score = Σ marker_weight по каждому concept_id
    - family_score = Σ concept_scores для концептов в этой семье (ключ "A3_F6")
    - area_score = Σ family_scores для семей в этой области

    Если normalize_scores=True, каждый уровень масштабируется так, что максимум = 1.0.
    """
    af = concept_to_area_family if concept_to_area_family is not None else _get_concept_to_af()

    # concept_id → сумма весов
    concept_scores: dict[str, float] = {}
    for cid, w in markers:
        concept_scores[cid] = concept_scores.get(cid, 0.0) + w

    # family: "A3_F6" → сумма concept_scores
    family_scores: dict[str, float] = {}
    for cid, score in concept_scores.items():
        if cid not in af:
            continue
        area, family = af[cid]
        key = f"{area}_{family}"
        family_scores[key] = family_scores.get(key, 0.0) + score

    # area → сумма family_scores
    area_scores: dict[str, float] = {}
    for fkey, score in family_scores.items():
        area = fkey.split("_")[0] if "_" in fkey else fkey
        area_scores[area] = area_scores.get(area, 0.0) + score

    def _norm(d: dict[str, float]) -> dict[str, float]:
        if not d or not normalize_scores:
            return d
        m = max(d.values())
        if m <= 0:
            return d
        return {k: round(v / m, 2) for k, v in d.items()}

    return {
        "concepts": _norm(concept_scores),
        "families": _norm(family_scores),
        "areas": _norm(area_scores),
    }


def analyze_session(
    text: str,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    phrase_index: dict[str, dict[tuple[str, ...], list[tuple[str, float]]]] | None = None,
    normalize_scores: bool = True,
    ngram_n: int = 2,
    embedding: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Полный пайплайн: текст сессии → токены → n-граммы → детекция маркеров (токены + фразы) → активация.

    Токены и n-граммы сопоставляются с Dict-A; совпадения дают (concept_id, weight), далее агрегация
    по концептам, семьям и областям.

    Возвращает:
    {
      "areas":   { "A3": 0.67, "A2": 0.54 },
      "families": { "A3_F6": 0.45, ... },
      "concepts": { "B_A3_F6_002": 0.33, ... }
    }

    Опционально: результат можно передать в interpret_session() (LEVEL 8) для клинической интерпретации:
      analysis = analyze_session(text); interpretation = interpret_session(analysis)

    Если передан embedding (например load_family_embedding_tfp()), после активации выполняется
    распространение по топологии (LEVEL 13): внутри области по зонам и по мостам между областями;
    в результате добавляется ключ "propagation_trace".
    """
    tokens = tokenize_text(text)
    normalized = normalize_tokens(tokens)
    # 1) Фразовые маркеры (приоритет): биграммы/триграммы по phrase_index (tuple lookup, O(n))
    pidx = phrase_index if phrase_index is not None else _get_phrase_index()
    phrase_matches = detect_phrase_markers(tokens=normalized, phrase_index=pidx) if pidx else []
    phrase_concepts = {c for c, _ in phrase_matches}
    markers = list(phrase_matches)
    # 2) Строковые n-граммы в marker_index (доп. покрытие; без дублей по концептам)
    if ngram_n >= 1 and len(normalized) >= ngram_n:
        ngrams = build_ngrams(normalized, n=ngram_n)
        string_phrase = detect_phrase_markers(ngrams=ngrams, marker_index=marker_index)
        markers += [(c, w) for c, w in string_phrase if c not in phrase_concepts]
        phrase_concepts |= {c for c, _ in string_phrase}
    # 3) Одиночные токены: только концепты, не активированные фразой
    token_matches = detect_markers(normalized, marker_index=marker_index)
    markers += [(c, w) for c, w in token_matches if c not in phrase_concepts]
    activation = activate_concepts(
        markers,
        concept_to_area_family=concept_to_area_family,
        normalize_scores=normalize_scores,
    )
    if embedding is not None:
        from sphere.topology.activation_propagation import propagate_activation
        prop = propagate_activation(activation, embedding, propagation_trace=True)
        activation["families"] = prop["families"]
        activation["areas"] = prop["areas"]
        activation["propagation_trace"] = prop.get("propagation_trace", [])
    return activation
