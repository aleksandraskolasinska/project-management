# How to start

This project uses Docker. By default the development server runs on:
- http://127.0.0.1:8000/

## secret key
Create a `.env` file:
```bash
DJANGO_SECRET_KEY=your_secret_key
```

## Using Docker Compose

```
docker compose build
```

```bash
docker compose up -d
docker compose exec adpbweb python manage.py makemigrations
docker compose exec adpbweb python manage.py migrate
```

server down:
```bash
docker compose down
```
