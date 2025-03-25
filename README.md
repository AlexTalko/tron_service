# Tron Address Information Microservice

Микросервис для получения информации о кошельках в сети Tron (TRX), включая баланс, bandwidth и energy. Сохраняет
историю запросов в базу данных.

## 🚀 Возможности

- Получение информации о кошельке (баланс TRX, bandwidth, energy)
- Сохранение истории запросов в SQLite
- API документация (Swagger/ReDoc)
- Юнит и интеграционные тесты

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/tron_service.git
   cd tron_service
   ```

2. Создайте виртуальное окружение (Python 3.11):
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Инициализируйте базу данных:
   ```bash
   python init_db.py
   ```

## 🏃 Запуск

```bash
python -m uvicorn main:app --reload
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

## 📚 API Endpoints

### Получить информацию о кошельке

```
POST /address-info/
```

**Параметры:**

```json
{
  "address": "Tron-адрес"
}
```

### Получить историю запросов

```
GET /address-requests/
```

**Параметры:**

- `skip` - смещение (по умолчанию 0)
- `limit` - количество записей (по умолчанию 10)

## 🧪 Тестирование

```bash
pytest -v
```

Тесты включают:

- Юнит-тесты для работы с БД
- Интеграционные тесты API
- Тесты пагинации

## 🛠 Технологии

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- TronPy
- Pytest
- SQLite

## 📄 Структура проекта

```
tron_service/
├── main.py            # FastAPI приложение
├── database.py        # Настройки БД
├── models.py          # Модели SQLAlchemy
├── schemas.py         # Pydantic схемы
├── crud.py            # Операции с БД
├── services.py        # Логика работы с Tron
├── tests/             # Тесты
├── requirements.txt   # Зависимости
└── README.md          # Документация
```

## ⚠️ Важно

Для работы с mainnet замените в `config.py`:

```python
TRON_NETWORK = "mainnet"
```
