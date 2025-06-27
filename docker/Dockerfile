FROM python:3.11-slim as builder
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
gcc \
curl \
&& rm -rf /var/lib/apt/lists/*
# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
# Production stage
FROM python:3.11-slim
WORKDIR /app
# Install curl for health checks
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
# Copy installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local
# Copy application code
COPY app/ .
# Change ownership
RUN chown -R appuser:appuser /app
# Switch to non-root user
USER appuser
# Add local bin to PATH
ENV PATH=/home/appuser/.local/bin:$PATH
# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \ 
CMD curl -f http://localhost:8000/health || exit 1
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
