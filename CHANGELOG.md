Changelog

[1.0.0] - 2026-11-22

Добавлено
- HTTP-сервер с эндпоинтами /health и /disk
- Модуль disk_check.py с проверкой порога 80%
- Dockerfile с непривилегированным пользователем
- Docker Compose с лимитами памяти 128 Мбайт и CPU 0.5
- Healthcheck для мониторинга работоспособности
- Unit-тесты (10 тестов)
- CI/CD pipeline на GitHub Actions