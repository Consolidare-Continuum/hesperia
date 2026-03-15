# LEVEL 4 — Dict-A (лексические маркеры)

Слой лексических маркеров, связывающий **текст сессии** с графом концептов Dict-B.

## Цепочка

```
текст сессии → токены → маркеры Dict-A → концепты (Dict-B) → семья → область
```

## Назначение

- **marker** — лексема или устойчивое выражение (нормализованная форма).
- При совпадении токена с маркером активируется соответствующий **concept_id** (узел Dict-B).
- По концепту из Dict-B определяются **семья** и **область** для активации и метрик.

## Файлы

| Файл | Описание |
|------|----------|
| `dictA_schema.yaml` | Схема записей маркеров (marker, concept_id, language, weight). |
| `lexical_markers.yaml` | Данные: список записей marker → concept_id (ru, weight). |
| `loader.py` | Загрузка и построение lookup: маркер → [(concept_id, weight)]. |

## Объём пилота

- Области: **A2**, **A3**, **A4**, **A10** (~120+ концептов).
- Цель: **5–10 маркеров на концепт** → порядка **800–1000** записей (текущая сборка может дать больше за счёт общих терминов).
- Язык маркеров: **ru** (основной); поле `language` позволяет добавить **en** без смены структуры.

## Генерация маркеров

Маркеры собираются из Dict-B:

```bash
python3 tools/build_dict_a_markers.py
```

- Берутся ключевые слова из `definition` и `example_context` (русский текст) концептов A2, A3, A4, A10.
- Только токены с кириллицей, без стоп-слов.
- При нехватке маркеров на концепт подставляются типовые термины области (см. `AREA_EXTRA_MARKERS` в скрипте).

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
