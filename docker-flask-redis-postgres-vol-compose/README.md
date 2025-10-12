# Flask + Redis + Postgres + Volume Docker Compose Project

## Project Overview

This project extends the Flask + Redis project by adding a PostgreSQL database with a persistent volume. Flask will use Redis for a counter and Postgres for storing persistent data.

---

## Folder Structure

```
flask-redis-postgres/
├── docker-compose.yml
├── app/
│   ├── app.py
│   └── requirements.txt
```

---

## Step-by-Step Instructions

### 1. Create Project Folder

```bash
mkdir flask-redis-postgres
cd flask-redis-postgres
mkdir app
```

### 2. Create `requirements.txt` inside `app/`

```
flask
redis
psycopg2-binary
```

### 3. Create `app.py` inside `app/`

```python
from flask import Flask
import redis
import psycopg2

app = Flask(__name__)
counter = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = counter.incr('hits')
    return f"Hello! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

*(You can extend this to write/read data from Postgres as needed.)*

### 4. Create `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    build: ./app
    ports:
      - "5000:5000"
    depends_on:
      - redis
      - db

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: mypass
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  db-data:
```

### 5. Create Dockerfile inside `app/`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 6. Run the Project

```bash
docker compose up -d
```

### 7. Test the Application

Open your browser:

```
http://localhost:5000
```

You should see the counter increment using Redis. Postgres data will persist in the `db-data` volume across container restarts.

---

## Notes

* `depends_on` ensures Redis and Postgres start before Flask.
* Named volume `db-data` keeps Postgres data persistent.
* Extend `app.py` to interact with Postgres for storing and retrieving data.

---

## Useful Docker Compose Commands

| Command                  | Description                        |
| ------------------------ | ---------------------------------- |
| `docker compose up`      | Build & start containers           |
| `docker compose up -d`   | Run in detached mode               |
| `docker compose logs`    | View container logs                |
| `docker compose ps`      | List running containers            |
| `docker compose down`    | Stop and remove containers         |
| `docker compose down -v` | Stop containers and remove volumes |
| `docker compose restart` | Restart containers                 |
