## Дипломный проект. Задание 3: UI-тесты

### UI тесты для Stellar Burgers

### Структура проекта

- `allure-report` 
- `allure-results`
- `locators`- пакет, содержащий:
  - `main_page_locators`
  - `orders_feed_locators`
  - `password_recovery_page_locators`
  - `personal_account_page_locators`
- `pages` - пакет, содержащий:
  - `base_page.py`
  - `main_page.py`
  - `orders_feed_page.py`
  - `password_recovery_page.py`
  - `personal_account_page.py`
- `tests` - пакет, содержащий:
  - `conftest.py`
  - `test_main_functionality.py`
  - `test_orders_feed.py`
  - `test_personal_account.py`
  - `test_password_recovery.py`
- `data.py`
- `requirements.txt`
- `README.md`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$pytest -v ./tests`