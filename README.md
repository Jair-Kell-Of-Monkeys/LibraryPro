# LibraryPro – Iteración 1 (Esqueleto)

Estructura base con apps: accounts, catalog, loans, reports; settings por entorno.

## Arranque rápido
1. Crear/activar venv
2. `pip install -r requirements.txt`
3. `copy .env.example .env` (o `cp .env.example .env`) y ajustar `DATABASE_URL`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
