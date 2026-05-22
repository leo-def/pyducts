# 🐍 Pyducts

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![BRDD](https://img.shields.io/badge/BRDD-Pattern-blueviolet?style=for-the-badge)](https://github.com/brdd-design/brdd)

**Pyducts** is a demonstration project that implements a simple product CRUD using **FastAPI** and the official **[brdd-python](https://github.com/brdd-design/brdd-python)** library.

> [!IMPORTANT]
> **Medium Article Blueprint**: This project is the official example for the article **"The PR as an Instruction Carrier: Beyond Simple CI/CD"**. It demonstrates how to package code and behavioral conditions (env vars, migrations) in a single unit of delivery.

---

## 🚀 Project Setup

1. **Clone & Setup:**
   ```bash
   git clone https://github.com/your-user/pyducts.git
   make setup
   cp .env.example .env
   ```

2. **Run:**
   ```bash
   make run
   ```

---

## 🏗 Architecture & Design (BRDD)
This project follows the **Business Rule Driven Design (BRDD)** pattern. Every logic branch is traceable via a unique ID, and every side effect is audited.

👉 **[BRDD.md - Detailed Pattern Documentation](file:///home/leo-def/projects/lab/pyducts/BRDD.md)**

### Core Components
- `src/shared/brdd.py`: Integration with the official `brdd-python` library.
- `src/domains/`: Domain UseCases, Services, and Models.
- `BUSINESS_CONTEXT.md`: The "Source of Truth" for business rules and codes.

---

## ⚙️ Engineering: PR as an Instruction Carrier
We advocate that a **Pull Request (PR)** is a **Carrier of Behavioral Instructions**. A deployment should only proceed if the environment is ready (Migrations applied, Env Vars set).

### The "Blocking Keyword" Strategy
The pipeline scans the PR for markers like `[x] **[DB_MIGRATION]**`. If found, the deployment is **GATED** until manual confirmation.

👉 **[CICD.md - Engineering Concepts & Demo Workflow](file:///home/leo-def/projects/lab/pyducts/CICD.md)**
👉 **[PIPELINE_EXPLAINED.md - Step-by-step for Humans](file:///home/leo-def/projects/lab/pyducts/PIPELINE_EXPLAINED.md)**

---

## ✍️ Medium Article Draft
You can find the draft of the article explaining these concepts in:
👉 **[MEDIUM_ARTICLE.md](file:///home/leo-def/projects/lab/pyducts/MEDIUM_ARTICLE.md)**

---

## 🤝 License
MIT