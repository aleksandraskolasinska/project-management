# Table of contents

- [About the prpject](#overview)
- [Instalation](#how-to-start)
- [Usage and features](#usage-and-features)
- [User manual](#user-manual)
- [Administrator manual](#administrator-manual)

# Overview

Practice project for Django using PostgreSQL databse. Project for a project management system using Django and database in postgres. Allows users to create accounts, edit their account data, create new projects, assign users to projects, be assigned to projects, edit the data such as priority, progress, shows history of edits.

# How to start

This project uses Docker. By default the development server runs on:
- http://127.0.0.1:8000/

To run the app do the following:

## secret key
Create a `.env` file containing your secret key:
```bash
DJANGO_SECRET_KEY=your_secret_key
```

## Using Docker Compose

```
docker compose build
```

```bash
docker compose up -d
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

## Create superuser to login
To create an admin account run:

```bash
docker compose exec -it web python manage.py createsuperuser
```
and follow the terminal instructions.

## Take server down

To take the server down run:
```bash
docker compose down
```
Note: docker compose is configured to use docker volume. This will persist between `docker up` and `docker down` commands.

To remove the database:
```bash
docker compose down --volumes my_db_data
```

## Create superuser to login

```bash
docker compose exec -it adpbweb python manage.py createsuperuser
```

# Usage and features

# User manual

# Administrator manual