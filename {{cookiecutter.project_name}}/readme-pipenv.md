

# Установка #
1. Открыть директорию {{ cookiecutter.project_name }}
2. Установить python 3.7 и pipenv
3. `pipenv install` (установит зависимости)
4. Настроить переменные окружения в файле `.env` (инициализировать копией `.defaultenv`)
5. `pipenv run python -m {{ cookiecutter.project_name }}.manage db upgrade` (применить миграции)
6. Запустить `pipenv run python -m {{ cookiecutter.app_name }}.manage run`

## Запуск тестов ##
1. Настроить переменные окружения в файле `.test.env` (инициализировать копией `.defaultenv`)
2. Запустить `pipenv run pytest tests`
