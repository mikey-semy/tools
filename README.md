# Development Environment with Code Server

Полное окружение разработки с Code Server, PostgreSQL мониторингом и логированием.

## Компоненты

- Code Server (VS Code в браузере)
- PgAdmin (управление PostgreSQL)
- Postgres Exporter (метрики PostgreSQL)
- Grafana (визуализация)
- Loki (сбор логов)
- Promtail (агент логирования)

## Быстрый старт

1. Клонируем репозиторий:
```bash
git clone <repo-url>
cd <repo-name>
```
2. Копируем .env.example в .env:
```bash
cp .env.example .env
```
3. Настраиваем переменные в .env

4. Запускаем:
```bash
docker-compose up -d
```

Порты сервисов
- Code Server: https://code.your-domain.ru:8080
- PgAdmin: https://pgadmin.your-domain.ru:5050
- Grafana: https://grafana.your-domain.ru:3000
- Loki: https://loki.your-domain.ru:3100
- Postgres Exporter: https://metrics.your-domain.ru:9187

Использование
1. Code Server: откройте http://localhost:8080 и введите пароль из .env
2. PgAdmin: http://localhost:5050 (логин/пароль из .env)
3. Grafana: http://localhost:3000
4. Добавьте Loki как источник данных: http://loki:3100
5. Импортируйте дашборды для PostgreSQL