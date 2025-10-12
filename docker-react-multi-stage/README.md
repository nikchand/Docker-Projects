# React Multi-Stage Docker Project

## Project Overview

This project demonstrates a **multi-stage Docker build** for a React application served with Nginx. The purpose is to create a **small, production-ready Docker image** while separating the build environment from the runtime environment.

## Folder Structure

```
react-multistage/
├── app/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── index.js
│       └── App.js
├── nginx/
│   └── default.conf
└── Dockerfile
```

## Dockerfile Explanation

### Stage 1: Build React App

* **Base Image:** `node:18-alpine`
* **Workdir:** `/app`
* **Copy Dependencies:** Only `package.json` to leverage Docker cache
* **Install Dependencies:** `npm install --production --silent && npm cache clean --force`
* **Copy Source Code:** `COPY app/ ./`
* **Build App:** `npm run build` generates production-ready `/build` folder

### Stage 2: Runtime (Nginx)

* **Base Image:** `nginx:alpine`
* **Remove Default Files:** `rm -rf /usr/share/nginx/html/*`
* **Copy Build Files:** `COPY --from=builder /app/build /usr/share/nginx/html`
* **Copy Nginx Config:** `COPY nginx/default.conf /etc/nginx/conf.d/default.conf`
* **Expose Port:** 80

## Docker Commands

### Build Image

```bash
docker build -t react-app .
```

### Run Container

```bash
docker run -d -p 8080:80 react-app
```

### Access App

Open in browser: `http://localhost:8080`

## Image Optimization Details

* **Multi-stage build:** Separates Node.js (builder) from Nginx (runtime)
* **Alpine images:** Keep the image lightweight (~53 MB)
* **Production dependencies only:** Skips dev dependencies
* **npm cache clean:** Removes temporary files after install
* **.dockerignore recommended:** To avoid sending unnecessary files in build context

## Notes

* HEALTHCHECK and LABEL are optional for beginners
* This image size (~53 MB) is normal for a React app with Nginx
* Future optimizations can include gzip compression and BuildKit caching

## Nginx Config (`nginx/default.conf`)

```nginx
server {
    listen 80;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri /index.html;
    }
}
```
