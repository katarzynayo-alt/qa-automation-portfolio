# QA Automation Pet Project

Пет-проект для портфолио тестировщика: UI + API автотесты на Python + Playwright.

## Что внутри

- **UI-тесты** — https://www.saucedemo.com (логин, добавление товара в корзину, чекаут)
- **API-тесты** — https://reqres.in (CRUD по пользователям)
- **Page Object Model** — структура страниц отдельно от тестов
- **CI/CD** — автозапуск тестов в GitHub Actions при каждом пуше
- **Отчёты** — pytest-html (можно заменить на Allure позже)

## Структура проекта

```
pet_project/
├── pages/              # Page Objects (UI)
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── ui/              # UI-тесты (Playwright)
│   │   ├── test_login.py
│   │   └── test_cart.py
│   └── api/             # API-тесты (requests)
│       └── test_users.py
├── conftest.py          # фикстуры pytest
├── pytest.ini
├── requirements.txt
└── .github/workflows/tests.yml
```

## Установка

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Запуск тестов

```bash
# Все тесты
pytest

# Только UI
pytest tests/ui

# Только API
pytest tests/api

# С HTML-отчётом
pytest --html=report.html --self-contained-html
```

## Roadmap (что добавить дальше)

- [ ] Allure-отчёты вместо pytest-html
- [ ] Параметризация тестов (разные пользователи/товары)
- [ ] Docker-контейнер для запуска тестов
- [ ] Параллельный запуск (pytest-xdist)
- [ ] Покрытие негативных кейсов (невалидный логин, пустая корзина и т.д.)
- [ ] Логирование шагов теста
