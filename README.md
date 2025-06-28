
# 🚀 DevOps Local CI/CD Pipeline

This is a complete **local CI/CD pipeline** project using **Docker, FastAPI, GitHub Actions, Prometheus, Grafana, and NGINX**. It demonstrates how to containerize an app, automate tests, build and deploy locally with monitoring.

---

## 🧰 Tech Stack

- 🐳 Docker & Docker Compose
- ⚙️ GitHub Actions (CI/CD)
- 🔥 FastAPI (Python web framework)
- 🌐 NGINX (reverse proxy)
- 📊 Prometheus (metrics)
- 📈 Grafana (dashboard)
- ✅ Pytest (testing)

---

## 📁 Project Structure

```

devops-local-pipeline/
├── app/                → FastAPI app & tests
├── docker/             → Dockerfile & ignore rules
├── infrastructure/     → nginx, monitoring, scripts
├── .github/workflows/  → GitHub Actions CI/CD
├── docker-compose.yml  → Service orchestration
├── README.md           → You are here!
└── .env.example        → Env variables sample

````

---

## 🚀 How to Run

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd devops-local-pipeline
````

2. **Run setup script:**

```bash
chmod +x infrastructure/scripts/setup.sh
./infrastructure/scripts/setup.sh
```

3. **Open services:**

## 🔗 Application Access Links (Run in Browser)

Here are the key endpoints of the project you can test locally:

1. 🌐 [Web Application](http://localhost:8000)
2. 📈 [Prometheus UI](http://localhost:9090)
3. 📊 [Grafana UI](http://localhost:3000)
4. 🧪 [Health Check API](http://localhost:8000/health)
5. 📉 [Metrics Endpoint (Custom)](http://localhost:8000/metrics)


## 🧪 Testing

```bash
cd app
pip install -r requirements.txt
pytest tests/ -v
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

* ✅ Run tests
* ✅ Code quality (flake8)
* ✅ Build Docker image
* ✅ Deploy locally with health checks
* ✅ Monitor metrics via Prometheus & Grafana

---

## 📊 Monitoring

* Prometheus scrapes metrics every 15s
* Grafana dashboards:

  * CPU, Memory, Disk usage
  * Application health

---

## 👩‍💻 Author

**Nayab Zahoor**
University: Fatima Jinnah Women University


