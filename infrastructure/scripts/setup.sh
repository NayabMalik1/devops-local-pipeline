#!/bin/bash
set -e
echo "🚀 Setting up DevOps Local Environment..."
# Check if Docker is installed
if ! command -v docker &> /dev/null; then
echo "❌ Docker is not installed. Please install Docker first."
exit 1
fi
# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
echo "❌ Docker Compose is not installed. Please install Docker Compose first."
exit 1
fi
# Create necessary directories
mkdir -p infrastructure/monitoring/grafana/dashboards
mkdir -p infrastructure/monitoring/grafana/datasources
# Create Grafana datasource configuration
cat > infrastructure/monitoring/grafana/datasources/prometheus.yml << EOF
apiVersion: 1
datasources:
- name: Prometheus
type: prometheus
access: proxy
url: http://prometheus:9090
isDefault: true
EOF
# Create Grafana dashboard provisioning
cat > infrastructure/monitoring/grafana/dashboards/dashboard.yml << EOF
apiVersion: 1
providers:
- name: 'default'
orgId: 1
folder: ''
folderUid: ''
type: file
disableDeletion: false
editable: true
updateIntervalSeconds: 10
allowUiUpdates: true
options:
path: /etc/grafana/provisioning/dashboards
EOF
# Set permissions
chmod +x infrastructure/scripts/setup.sh
# Build and start services
echo "🔨 Building Docker containers..."
docker-compose build
echo "🚀 Starting services..."
docker-compose up -d
# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 30
# Health checks
echo "🔍 Performing health checks..."
if curl -f http://localhost/health > /dev/null 2>&1; then
echo "✅ Web application is healthy"
else
echo "❌ Web application health check failed"
fi
if curl -f http://localhost:9090/-/healthy > /dev/null 2>&1; then
echo "✅ Prometheus is healthy"
else
echo "❌ Prometheus health check failed"
fi
if curl -f http://localhost:3000/api/health > /dev/null 2>&1; then
echo "✅ Grafana is healthy"
else
echo "❌ Grafana health check failed"
fi
echo ""
8. Environment Variables
File: .env.example
9. Documentation
File: README.md
echo "🎉 Setup completed!"
echo ""
echo "📊 Services are available at:"
echo " • Web Application: http://localhost"
echo " • Prometheus: http://localhost:9090"
echo " • Grafana: http://localhost:3000 (admin/admin123)"
echo " • Node Exporter: http://localhost:9100"
echo ""
echo "🔧 To stop services: docker compose down"
echo "🔄 To restart services: docker-compose restart"
echo "📋 To view logs: docker-compose logs -f"
