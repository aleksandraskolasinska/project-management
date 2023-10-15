# How to start

Server on:
- http://127.0.0.1:8000/

## secret key
Create a `.env` file:
```bash
DJANGO_SECRET_KEY=your_secret_key
```


## Using Docker Compose

```bash
docker compose up -d
docker compose exec adpbweb python manage.py makemigrations
docker compose exec adpbweb python manage.py migrate
```

server down:
```bash
docker compose down
```
