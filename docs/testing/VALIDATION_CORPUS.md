# Validation corpus for clinical model

Любая клиническая модель требует валидационного корпуса.

## Рекомендуемый минимум

- **20–50 TFP transcripts** (русские или английские с разметкой Patient:/Therapist:).

## Использование

Корпус используется для:

- **marker tuning** — подбор весов маркеров Dict-A по совпадению с экспертными метками
- **relation tuning** — настройка весов связей в concept_relation_weights.yaml
- **threshold calibration** — вызов `calibrate_thresholds_from_corpus(activation_results)` для адаптивных порогов

## Размещение

- Транскрипты: `assets/validation/tfp_transcripts/` (добавить вручную или через инструмент).
- Конфиг калибровки после прогона: `spec/activation_calibration.yaml`.

## Формат транскриптов

Текстовые файлы или JSON с полями:

- `text` — текст сессии с метками "Patient:", "Therapist:"
- опционально: `reference_areas`, `reference_defenses` для сравнения с выводом модели
