#!/bin/bash

# Navigate to project folder
cd ~/docker-cicd-demo

# Pull latest code from GitHub
git pull origin main

# Build Docker image
docker build -t myapp:latest .

# Stop and remove old container if exists
docker stop myapp || true
docker rm myapp || true

# Run new container
docker run -d -p 5000:5000 --name myapp myapp:latest

