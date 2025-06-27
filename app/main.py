from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import psutil
import time
from datetime import datetime

app = FastAPI(
    title="DevOps Local API",
    description="Sample application for local CI/CD pipeline",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store start time for uptime calculation
start_time = time.time()

@app.get("/")
async def root():
    return {
        "message": "DevOps Local API",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime_seconds": int(time.time() - start_time)
    }

@app.get("/metrics")
async def metrics():
    """Custom metrics endpoint for monitoring"""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return {
        "cpu_usage_percent": cpu_percent,
        "memory_usage_percent": memory.percent,
        "memory_available_gb": round(memory.available / (1024**3), 2),
        "disk_usage_percent": disk.percent,
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "uptime_seconds": int(time.time() - start_time),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/status")
async def status():
    """Detailed status endpoint"""
    return {
        "service": "healthy",
        "database": "not_configured",
        "cache": "not_configured",
        "version": "1.0.0",
        "environment": "local"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

