# Python Flask + Redis Docker Compose Project

## Project Overview

This project demonstrates a simple Python Flask application connected to a Redis service using Docker Compose. The Flask app will use Redis to increment and store a counter.

---

## Folder Structure

```
flask-redis/
├── docker-compose.yml
├── app/
│   ├── app.py
│   └── requirements.txt
```

---

## Step-by-Step Instructions

### 1. Create Project Folder

```bash
mkdir flask-redis
cd flask-redis
mkdir app
```

### 2. Create `requirements.txt` inside `app/`

```
flask
redis
```

### 3. Create `app.py` inside `app/`

```python
from flask import Flask
import redis

app = Flask(__name__)
counter = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = counter.incr('hits')
    return f"Hello! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

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

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
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

Refresh the page to see the counter increment.

---

## Notes

* `depends_on` ensures Redis starts before Flask.
* The counter persists in Redis while the container is running.
* You can extend the app to store other data in Redis as needed.

---

## Useful Docker Compose Commands

| Command                  | Description                |
| ------------------------ | -------------------------- |
| `docker compose up`      | Build & start containers   |
| `docker compose up -d`   | Run in detached mode       |
| `docker compose logs`    | View container logs        |
| `docker compose ps`      | List running containers    |
| `docker compose down`    | Stop and remove containers |
| `docker compose restart` | Restart containers         |
