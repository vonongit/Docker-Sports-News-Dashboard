# 🏀 Docker Sports & News Dashboard

**A microservices architecture project demonstrating Docker fundamentals through a real-world sports and news aggregation dashboard.**

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://www.nginx.com/)

<div align="center">

![Live Dashboard](screenshots/live-weather-dashboard.png)

**[📖 Read Full Documentation](DOCUMENTATION.md)** | **[🚀 Quick Start](#-quick-start)** | **[🏗️ Architecture](#️-architecture)**

</div>

---

## 📖 Overview

A hands-on learning project built to master Docker and microservices fundamentals before diving into Kubernetes. This dashboard aggregates live NBA/NFL scores, real-time weather, and breaking news—all running in isolated, scalable containers.

### What Makes This Special

- **Real-World Architecture**: Three containerized services communicating through Docker networking
- **Live Data Integration**: ESPN sports scores, OpenWeather data, and NewsAPI headlines
- **Production Patterns**: Nginx reverse proxy, health checks, and container orchestration
- **Learning Journey**: Documented challenges, solutions, and lessons learned

---

## ✨ Features

🌤️ **Real-time weather** for Charlotte, NC  
🏀 **Live NBA scores** with team logos and game status  
🏈 **Live NFL scores** with automatic updates  
📰 **Breaking news headlines** from top sources  
🔄 **Auto-refresh** every 60 seconds  
📱 **Responsive design** works on any device

---

## 🏗️ Architecture
```
User Browser (localhost:80)
        ↓
   Nginx Proxy
        ↓
   ┌────┴────┐
   ↓         ↓
Frontend  Backend API
(Nginx)   (Flask)
            ↓
    External APIs
```

### Three Container Setup

| Container | Purpose | Tech |
|-----------|---------|------|
| **nginx_proxy** | Routes traffic to frontend/backend | Nginx Alpine |
| **sports_frontend** | Serves dashboard UI | HTML/CSS/JS + Nginx |
| **sports_backend** | Aggregates API data | Python Flask |

**Why this architecture?**
- Each service updates independently
- Scale frontend and backend separately
- Production-ready microservices pattern

---

## 🚀 Quick Start

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- API Keys (free): [OpenWeather](https://openweathermap.org/api) | [NewsAPI](https://newsapi.org/)

### Launch in 3 Steps
```bash
# 1. Clone the repo
git clone https://github.com/vonongit/docker-sports-news-dashboard.git
cd docker-sports-news-dashboard

# 2. Add your API keys in backend/app.py
WEATHER_API_KEY = 'your_key_here'
NEWS_API_KEY = 'your_key_here'

# 3. Start everything
docker-compose up --build
```

**Open:** http://localhost

That's it! 🎉

---

## 📸 Live Dashboard Preview

<div align="center">

### Weather & Sports Scores
![NBA Dashboard](screenshots/live-nba-dashboard.png)

### Real-Time Updates
![NFL Dashboard](screenshots/live-nfl-dashboard.png)

</div>

---

## 🛠️ Tech Stack

**Backend:** Python 3.11, Flask 3.0, Requests  
**Frontend:** HTML5, CSS3, Vanilla JavaScript, Nginx Alpine  
**Infrastructure:** Docker, Docker Compose  
**APIs:** ESPN (sports), OpenWeather (weather), NewsAPI (news)

---

## 📚 What I Learned

### Core Docker Skills
✅ Multi-container orchestration with Docker Compose  
✅ Container networking and service discovery  
✅ Port mapping and conflict resolution  
✅ Log management and debugging  
✅ Image lifecycle and optimization

### Real-World Problem Solving
- Fixed file naming conflicts in Dockerfiles
- Resolved macOS port 5000 conflicts with system services
- Implemented health checks for container reliability
- Managed container resources and cleanup

**[📖 Read the full journey with detailed challenges and solutions →](DOCUMENTATION.md)**

---

## 🎯 Project Goals

**Primary:** Master Docker fundamentals before learning Kubernetes  
**Secondary:** Build production-ready microservices architecture  
**Outcome:** Hands-on experience with containerization, networking, and DevOps practices

### What's Next
- Deploy to Kubernetes cluster
- Add Prometheus/Grafana monitoring
- Implement CI/CD pipeline
- Container security hardening

---

## 📖 Documentation

This README is a quick overview. For comprehensive documentation including:
- 🔧 **Detailed troubleshooting** of challenges faced
- 📊 **Container management** techniques and best practices
- 🎓 **Complete learning journey** with lessons learned
- 💡 **Interview talking points** and technical explanations

**👉 [Read the Full Documentation](DOCUMENTATION.md)**

---

## 🤝 Connect With Me

<div align="center">

[![Email](https://img.shields.io/badge/Email-travondm2%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:travondm2@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-vonongit-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vonongit)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Travon_Mayo-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/travon-mayo/)

</div>

---

## 📄 License

Open source under the [MIT License](LICENSE).

---

<div align="center">

**Built as a stepping stone to Kubernetes mastery** 🚀

*Last Updated: February 5, 2026*

</div>