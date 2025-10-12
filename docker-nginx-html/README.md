# Nginx + HTML Docker Compose Project

## Project Overview

This is a simple project demonstrating how to serve static HTML pages using Nginx with Docker Compose. The project allows you to run an Nginx container that serves files from a local `html` directory, making it easy to see changes instantly.

---

## Folder Structure

```
nginx-html/
├── docker-compose.yml   # Docker Compose configuration file
└── html/
    └── index.html      # Static HTML file served by Nginx
```

---

## Step-by-Step Instructions

### 1. Clone or create the project folder

```bash
mkdir nginx-html
cd nginx-html
mkdir html
```

### 2. Add your HTML file

Create `html/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Nginx Test</title>
</head>
<body>
    <h1>Hello, Docker Compose with Nginx!</h1>
    <p>This is a simple static website served by Nginx inside a Docker container.</p>
</body>
</html>
```

### 3. Create `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
```

**Explanation:**

* `image`: Uses the official Nginx lightweight image.
* `ports`: Maps host port 8080 to container port 80.
* `volumes`: Maps local HTML folder to Nginx folder inside the container (`:ro` = read-only).

### 4. Run the project

```bash
docker compose up -d
```

* `-d` runs the container in detached mode.
* Verify running containers:

```bash
docker compose ps
```

### 5. Access the site

Open your browser and go to:

```
http://localhost:8080
```

You should see your HTML page displayed.

### 6. Useful Docker Compose Commands

| Command                  | Description                      |
| ------------------------ | -------------------------------- |
| `docker compose up`      | Build & start containers         |
| `docker compose up -d`   | Run in detached mode             |
| `docker compose logs`    | View container logs              |
| `docker compose ps`      | List running containers          |
| `docker compose down`    | Stop and remove containers       |
| `docker compose down -v` | Stop containers & remove volumes |
| `docker compose restart` | Restart containers               |

### 7. Experiment

* Edit `index.html` and refresh browser to see live updates.
* Add another HTML page (`about.html`) and access it via `http://localhost:8080/about.html`.
* Change the port mapping in `docker-compose.yml` to `8081:80` and access `http://localhost:8081`.

---

## Summary

* Docker Compose simplifies running multi-container applications.
* Volumes allow live editing of files on the host system.
* Ports map container services to your local machine.
* Official Nginx image is used, no custom Dockerfile required for simple static sites.

---

## Prerequisites

* Docker installed and running
* Docker Compose installed (`docker compose`)
* Basic terminal knowledge
