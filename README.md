# QA Automation Portfolio — Python + Playwright

Projekt automatyzacji testów stworzony jako portfolio testera oprogramowania.

## Co zawiera projekt

- **Testy UI** — https://www.saucedemo.com (logowanie, dodawanie do koszyka)
- **Testy API** — https://reqres.in (operacje CRUD na użytkownikach)
- **Page Object Model** — strony oddzielone od logiki testów
- **CI/CD** — automatyczne uruchamianie testów w GitHub Actions przy każdym pushu
- **Raporty** — pytest-html

## Struktura projektu

```
qa-automation-portfolio/
├── pages/                  # Page Objects (UI)
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── ui/                 # Testy UI (Playwright)
│   │   ├── test_login.py
│   │   └── test_cart.py
│   └── api/                # Testy API (requests)
│       └── test_users.py
├── conftest.py             # Fixtures pytest
├── pytest.ini
├── requirements.txt
└── .github/workflows/tests.yml
```

## Przypadki testowe

### UI — Logowanie
| Test | Opis |
|------|------|
| `test_successful_login` | Poprawne logowanie z prawidłowymi danymi |
| `test_login_with_invalid_password` | Logowanie z błędnym hasłem — oczekiwany błąd |
| `test_login_with_empty_fields` | Logowanie z pustymi polami — oczekiwany błąd |

### UI — Koszyk
| Test | Opis |
|------|------|
| `test_add_single_item_to_cart` | Dodanie produktu do koszyka |
| `test_inventory_has_items` | Weryfikacja liczby produktów na stronie |

### API — Użytkownicy
| Test | Opis |
|------|------|
| `test_get_users_list` | GET lista użytkowników — status 200 |
| `test_get_single_user` | GET pojedynczy użytkownik — status 200 |
| `test_get_user_not_found` | GET nieistniejący użytkownik — status 404 |
| `test_create_user` | POST tworzenie użytkownika — status 201 |
| `test_update_user` | PUT aktualizacja użytkownika — status 200 |
| `test_delete_user` | DELETE usunięcie użytkownika — status 204 |

## Instalacja

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Uruchamianie testów

```bash
# Wszystkie testy
pytest -v

# Tylko testy UI
pytest tests/ui -v

# Tylko testy API
pytest tests/api -v

# Z raportem HTML
pytest --html=report.html --self-contained-html
```

## Stos technologiczny

- **Python 3.x**
- **Playwright** — automatyzacja przeglądarki
- **pytest** — framework testowy
- **requests** — testy API
- **GitHub Actions** — CI/CD

## Plany rozwoju

- [ ] Raporty Allure
- [ ] Parametryzacja testów
- [ ] Docker
- [ ] Uruchamianie równoległe (pytest-xdist)
- [ ] Negatywne przypadki testowe
