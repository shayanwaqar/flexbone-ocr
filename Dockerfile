# Use a small Python base image
FROM python:3.11-slim

# Install system dependencies (Tesseract + build tools if needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr \
        libtesseract-dev \
        gcc \
        libjpeg-dev \
        zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy Python dependencies first (for better Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Cloud Run expects the service to listen on PORT env var (default 8080)
ENV PORT=8080

EXPOSE 8080

# Use gunicorn to serve the Flask app
# "app:app" = app.py file, app = Flask instance
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
