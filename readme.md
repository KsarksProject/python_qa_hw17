# 📌 Тестирование API reqres.in

## 📖 Описание
Этот проект содержит автоматизированные тесты для API [reqres.in](https://reqres.in). Тесты проверяют основные CRUD-операции (создание, получение, обновление, удаление пользователей), а также регистрацию и получение ресурсов.

## 🛠 Технологии
- **Python 3**
- **pytest** – фреймворк для тестирования
- **requests** – библиотека для HTTP-запросов
- **jsonschema** – валидация JSON-ответов API

## 📂 Структура проекта
```
├── tests/                  # Каталог с тестами
│   ├── test_users.py        # Тесты для пользователей
│   ├── test_resources.py    # Тесты для ресурсов
│   ├── conftest.py          # Фикстуры
│   ├── __init__.py          # (для импортов)
│
├── schemas/                # JSON-схемы для валидации API-ответов
│   ├── users.py            # Схемы для пользователей
│   ├── resources.py        # Схемы для ресурсов
│   ├── __init__.py         
│
├── reports/                # Каталог для отчетов (HTML-отчет pytest)
│
├── requirements.txt        # Зависимости проекта
├── pytest.ini              # Конфигурация pytest
├── README.md               # Документация
```

## 🚀 Установка и запуск тестов
### 1️⃣ Установка зависимостей
Перед запуском тестов необходимо установить зависимости. Рекомендуется использовать **virtualenv**:
```sh
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt
```
### 2️⃣ Запуск тестов
Простейший запуск:
```sh
pytest tests/
```
Запуск с подробным выводом:
```sh
pytest -v
```
Запуск с HTML-отчётом:
```sh
pytest --html=reports/report.html
```
### 3️⃣ Просмотр отчёта
После выполнения `pytest --html=reports/report.html` открой `reports/report.html` в браузере.

🧪 Список тестов<br />
✅ test_create_user_success – проверка успешного создания пользователя.<br />
✅ test_get_existing_user – проверка получения информации о существующем пользователе.<br />
✅ test_get_non_existing_user – проверка запроса несуществующего пользователя.<br />
✅ test_full_user_update – проверка полного обновления пользователя (PUT).<br />
✅ test_partial_user_update – проверка частичного обновления пользователя (PATCH).<br />
✅ test_successful_user_registration – проверка успешной регистрации пользователя.<br />
✅ test_unsuccessful_user_registration – проверка неудачной регистрации (без пароля).<br />
✅ test_delete_existing_user – проверка удаления пользователя.<br />
✅ test_get_existing_resource – проверка получения информации о существующем ресурсе.<br />
✅ test_get_non_existing_resource – проверка запроса несуществующего ресурса.<br />
