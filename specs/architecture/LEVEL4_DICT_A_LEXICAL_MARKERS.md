# LEVEL 4 — Dict-A (лексические маркеры)

## Цель

Слой **лексических маркеров**, связывающий текст терапевтической сессии с графом концептов Dict-B и далее с активацией семей и областей.

## Цепочка

```
текст сессии → нормализация/токенизация → маркеры Dict-A → концепты (Dict-B) → семья → область
```

## Объём

- **Полная сборка (по умолчанию):** все области **A1–A10** из `concept_nodes.yaml` (**1440** узлов); `tools/build_dict_a_markers.py` без `--pilot`.
- **Пилот:** только A2, A3, A4, A10 — флаг **`--pilot`**.
- **Маркеры:** до **10** на концепт (после паддинга из `AREA_EXTRA_MARKERS` при нехватке); полная сборка ≈ **14k+** записей `marker → concept_id`.
- **Корпус:** опционально **`--corpus DIR`** — частоты униграмм из `*.md` переупорядочивают хвост токенов (после токенов из `label`).
- **Язык:** ru (основной); структура допускает en без изменений схемы.

## Файлы

| Расположение | Файл | Назначение |
|--------------|------|------------|
| `hesperia/ontology/dictA/` | `dictA_schema.yaml` | Схема: marker, concept_id, language, weight. |
| | `lexical_markers.yaml` | Данные: список записей marker → concept_id. |
| | `loader.py` | Загрузка и построение lookup маркер → [(concept_id, weight)]. |
| | `README.md` | Описание и пример использования. |
| `tools/` | `build_dict_a_markers.py` | Генерация маркеров из Dict-B (definition, example_context). |

## Требования к записи маркера

- **marker** — лексема или поверхностная форма (нормализуется к нижнему регистру при загрузке).
- **concept_id** — id узла Dict-B (формат `B_A{n}_F{m}_{kkk}`).
- **language** — ru | en.
- **weight** — число от 0 до 1 (по умолчанию 1.0).

Один маркер может соответствовать нескольким концептам (многозначность).

## Генерация

```bash
# Все A1–A10; опционально приоритет по частоте в корпусе (markdown)
python3 tools/build_dict_a_markers.py --corpus research/_noone_local/2_cleaned --corpus-min-freq 3

# Узкий пилот (как раньше)
python3 tools/build_dict_a_markers.py --pilot
```

Скрипт читает `hesperia/ontology/dictB/concept_nodes.yaml`, для каждого узла извлекает русские слова из **`label`**, затем `example_context` и `definition`, отфильтровывает стоп-слова, при нехватке дополняет типовыми терминами области (`AREA_EXTRA_MARKERS` для всех A1–A10).

## Загрузка в коде

```python
from hesperia.ontology.dictA import build_marker_to_concepts, get_marker_stats

lookup = build_marker_to_concepts()  # marker_lower → [(concept_id, weight), ...]
stats = get_marker_stats()           # marker_count, concept_count, version, domain
```

## Связь с Dict-B

- `concept_id` в Dict-A ссылается на поле `id` в `hesperia/ontology/dictB/concept_nodes.yaml`.
- По узлу Dict-B заданы `area` и `family`; их используют для активации семей/областей в пайплайне.

## Итог

После внедрения LEVEL 4 онтологическая база позволяет:

- читать текст сессии;
- сопоставлять токены с маркерами Dict-A;
- активировать концепты Dict-B и соответствующие семьи/области.

Дальнейший шаг — интеграция Dict-A в пайплайн анализа (нормализация текста, токенизация, подсчёт активаций по семьям/областям).
