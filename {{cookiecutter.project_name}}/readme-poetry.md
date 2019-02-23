

# Установка #
1. Открыть директорию {{ cookiecutter.project_name }}
2. Установить python 3.7 и poetry
3. `poetry install` (установит зависимости)
4. Настроить переменные окружения в файле `.env` (инициализировать копией `.defaultenv`)
5. `poetry run python -m {{ cookiecutter.project_name }}.manage db upgrade` (применить миграции)
6. Запустить `poetry run python -m {{ cookiecutter.app_name }}.manage run`

## Запуск тестов ##
1. Настроить переменные окружения в файле `.test.env` (инициализировать копией `.defaultenv`)
2. Запустить `poetry run pytest tests`
