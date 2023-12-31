# Сервис Salary
Данный сервис предназначен для просмотра текущей заработной платы и даты следующего повышения.

## Стек технологий
FastAPI, SQLAlchemy, SQLite

## Установка и запуск
- Клонирование удаленного репозитория
```bash
git clone https://gitlab.com/Zhuravlev-DP/salary_time_period.git
```
- В директории /salary_time_period создайте файл .env, используя образец [.env.example](salary_time_period/.env.example)

- Создание виртуального окружения и установка зависимостей
```bash
. python -m venv venv (windows)
. python3 -m venv venv (linux)
. source venv/Scripts/activate (windows)
. source venv/bin/activate (linux)
pip install --upgade pip
pip install -r requirements.txt
```
- Запуск сервера
```bash
python main.py
```
- Тестовые данные пользователей и зарплаты занесены в базу данных. Также вы можете создать нового пользователя. Данные о зарплате нового пользователя в базу вносить вручную.
```
Данные пользователей:
    "username": "root"
    "password": "root"

    "username": "vasya.pupkin"
    "password": "Qwerty123"
```

## Документация
- Документация к проекту в формате OpenAPI доступна по адресу [`http://localhost:8000/docs/`](http://localhost:8000/docs)

### Планы по доработке и развитию приложения
- Покрыть тестами.
- Использовать менеджер зависимостей poetry.
- Добавить возможность запуска проекта в Docker.
- Создание админ панели.
