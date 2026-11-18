# Page Object: UI-тесты automationexercise.com

Учебный проект: автотесты на Python, Playwright и pytest по паттерну Page Object.

## Что покрыто

- Home: 10 тестов
- Login: 10 тестов
- Products: 10 тестов
- Contact Us: 10 тестов

## Структура

- pages/ - классы страниц (локаторы и действия)
- tests/ - тесты (проверки)
- conftest.py - фикстура браузера и скриншоты при падении
- pytest.ini - настройки pytest

## Запуск

pip install -r requirements.txt
playwright install
pytest