import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_root_endpoint():
response = client.get("/")
assert response.status_code == 200
data = response.json()
assert "message" in data
assert "timestamp" in data
assert data["status"] == "running"
def test_health_endpoint():
response = client.get("/health")
assert response.status_code == 200
data = response.json()
assert data["status"] == "healthy"
assert "uptime_seconds" in data
def test_metrics_endpoint():
response = client.get("/metrics")
assert response.status_code == 200
data = response.json()
assert "cpu_usage_percent" in data
assert "memory_usage_percent" in data
def test_status_endpoint():
response = client.get("/status")
assert response.status_code == 200
data = response.json()
assert data["service"] == "healthy"
assert data["environment"] == "local"
