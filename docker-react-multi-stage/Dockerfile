# ------------ STAGE 1: build ------------
FROM node:18-alpine AS builder
WORKDIR /app

# Copy only package files first (better caching)
COPY app/package.json ./

# Install only production dependencies
RUN npm install --production --silent && npm cache clean --force

# Copy the rest of the app and build
COPY app/ ./
RUN npm run build

# ------------ STAGE 2: runtime (nginx) ------------
FROM nginx:alpine

# Remove default nginx html files
RUN rm -rf /usr/share/nginx/html/*

# Copy built static files from builder
COPY --from=builder /app/build /usr/share/nginx/html

# Copy custom nginx conf (if exists)
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

