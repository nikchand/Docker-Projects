FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed for Python packages with C extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Upgrade pip & setuptools first
RUN pip install --upgrade pip setuptools wheel

# Then install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run the app
CMD ["python", "app.py"]
