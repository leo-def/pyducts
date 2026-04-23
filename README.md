# 🐍 Pyducts

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![CI/CD](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

**Pyducts** (Python + Products) is a demonstration project that implements a simple product CRUD using **FastAPI**. More than just an API, its main goal is to serve as a *blueprint* to demonstrate the **Business Rule Driven Design (BRDD)** pattern.

> [!TIP]
> **New to BRDD?** Check the **[Detailed Pattern Documentation (BRDD.md)](file:///home/leo-def/projects/lab/pyducts/BRDD.md)** to understand the philosophy behind this project.

---

## 🚀 Project Setup

Follow the steps below to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-user/pyducts.git
   cd pyducts
   ```

2. **Configure environment:**
   ```bash
   make setup
   cp .env.example .env
   ```

3. **Run the application:**
   ```bash
   make run
   ```

---

## 🏗 Architecture & Design
This project is built using the **Business Rule Driven Design (BRDD)** pattern. This ensures that business logic is decoupled from technical details and remains highly traceable.

For a deep dive into the design philosophy, specialized services, and response patterns, see:
👉 **[BRDD.md - Detailed Pattern Documentation](file:///home/leo-def/projects/lab/pyducts/BRDD.md)**

### Key Folders
- `src/shared/brdd.py`: Core BRDD classes (`ExecutionContext`, etc.).
- `src/domains/`: Domain-specific logic organized by UseCases and Services.
- `src/internal/`: Internal system logic (Admin, etc.).
- `CICD.md`: Engineering concepts, Deployment Gates, and Release Promotion workflow.

---

## ⚙️ Engineering & CI/CD (The Demo Core)
This project is a **live demonstration** of the **"PR as an Instruction Carrier"** philosophy. It contrasts simple automated pipelines with **Conditional Deployment** strategies to prevent environment-out-of-sync failures (missing migrations, env vars, etc.).

👉 **[CICD.md - Engineering Concepts & Demo Workflow](file:///home/leo-def/projects/lab/pyducts/CICD.md)**

---


---

## 🤝 Contribution & License

Contributions are welcome. Project under MIT license.