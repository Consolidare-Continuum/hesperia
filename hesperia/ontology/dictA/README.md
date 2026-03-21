# LEVEL 4 — Dict-A (лексические маркеры)

Слой лексических маркеров, связывающий **текст сессии** с графом концептов Dict-B.

## Цепочка

```
текст сессии → токены → маркеры Dict-A → концепты (Dict-B) → семья → область
```

## Назначение

- **marker** — лексема или устойчивое выражение (нормализованная форма).
- При совпадении токена с маркером активируется соответствующий **concept_id** (узел Dict-B).
- Опционально **`confidence_type`**: `strong` (множитель 1.0) или `weak` (0.3) — умножается на `weight` при `build_marker_to_concepts` / фразовом индексе / colloquial, чтобы слабые контекстные совпадения не раздували суммарную активацию.
- По концепту из Dict-B определяются **семья** и **область** для активации и метрик.

## Файлы

| Файл | Описание |
|------|----------|
| `dictA_schema.yaml` | Схема записей маркеров (marker, concept_id, language, weight, optional `confidence_type`). |
| `lexical_markers.yaml` | Данные: список записей marker → concept_id (ru, weight). |
| `loader.py` | Загрузка и построение lookup: маркер → [(concept_id, weight)]. |

## Объём

- **По умолчанию:** все области **A1–A10** из `../dictB/concept_nodes.yaml` (**1440** узлов) → порядка **14k** записей `marker → concept_id`.
- **`--pilot`:** только A2, A3, A4, A10 (узкий набор).
- До **10** маркеров на концепт; при нехватке — паддинг из `AREA_EXTRA_MARKERS` (в скрипте для каждой области).
- Язык маркеров: **ru** (основной).

## Генерация маркеров

```bash
# Полная сборка + приоритет токенов по частоте в markdown-корпусе
python3 tools/build_dict_a_markers.py --corpus research/_noone_local/2_cleaned --corpus-min-freq 3

# Только пилотные области
python3 tools/build_dict_a_markers.py --pilot
```

- Токены из **`label`**, затем `example_context` и `definition` (кириллица, без стоп-слов).
- С **`--corpus`**: хвост после label-лексем сортируется по частоте в корпусе (униграммы с `*.md`).

## Использование в коде

```python
from hesperia.ontology.dictA.loader import (
    load_lexical_markers,
    build_marker_to_concepts,
    get_marker_stats,
)

# Словарь: маркер (lowercase) → [(concept_id, weight), ...]
lookup = build_marker_to_concepts()

# Токен текста (нормализованный) → активируемые концепты
token = "расщепление"
if token in lookup:
    for concept_id, weight in lookup[token]:
        # concept_id, например B_A3_F1_001
        pass
```

## Связь с Dict-B

- `concept_id` в Dict-A совпадает с полем `id` узла в `hesperia/ontology/dictB/concept_nodes.yaml`.
- По `id` в Dict-B заданы `area` и `family`; их можно использовать для активации семей и областей в пайплайне.
