FROM python:3.11-slim

LABEL maintainer="Feature Store Team"
LABEL description="Feature Store - Real-time & Batch Processing"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt requirements-dev.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt

# Copy application code
COPY src/ ./src/
COPY config/ ./config/
COPY setup.py ./

# Install package
RUN pip install -e .

# Create necessary directories
RUN mkdir -p /app/data /app/logs /app/notebooks

# Expose ports
EXPOSE 8000 8888

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command
CMD ["uvicorn", "src.serving.api:app", "--host", "0.0.0.0", "--port", "8000"]