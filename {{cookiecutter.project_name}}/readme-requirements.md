

# Установка #
1. Открыть директорию {{ cookiecutter.project_name }}
2. Установить python 3.7
3. Установить зависимые библиотеки `python -m pip install -r requirements.txt`
4. Настроить переменные окружения в файле `.env` (инициализировать копией `.defaultenv`)
5. `python -m {{ cookiecutter.project_name }}.manage db upgrade` (применить миграции)
6. Запустить `python -m {{ cookiecutter.app_name }}.manage run`

## Запуск тестов ##
1. Настроить переменные окружения в файле `.test.env` (инициализировать копией `.defaultenv`)
2. Запустить `pytest tests`
