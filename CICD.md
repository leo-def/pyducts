# 🚀 Engineering Concepts & CI/CD Workflow

This project serves as a technical demonstration of **Professional Release Management**. The core mission is to prove that a **Pull Request (PR)** is more than just a code transport—it is a **Carrier of Behavioral Instructions**.

---

## 🎯 The Demo Goal: Automated vs. Conditional Deployment

In many projects, CI/CD is seen as a simple pipeline that pushes code on every merge. **Pyducts** demonstrates a more robust approach:

### 1. Automated "Continuos Delivery"
Standard code flow where verified changes move automatically through environments.

### 2. Conditional Deployment (The "Safety Valve")
This is the core of our demonstration. We demonstrate that **Instructions > Code**. A deployment should only proceed if the environment is ready for it. 
*   **The Problem**: Code is deployed, but it breaks because an Environment Variable wasn't set, or a Database Migration wasn't run.
*   **The Solution**: The PR body contains the "Instruction Metadata". If the PR tells the system "I need a change in the database", the pipeline should **gate** the deployment until a human or a sub-process confirms the instruction was executed.

---

## 🧠 Core Philosophy: PR as an Instruction Carrier

Every Pull Request in this project is structured to communicate the **Audit Trail** of the feature:

| Instruction Type | Purpose | Pipeline Behavior |
| :--- | :--- | :--- |
| **Code Changes** | The logic itself. | Automated Testing & Linting. |
| **Environmental** | New `.env` keys or Config changes. | **Blocks Deployment** until manual validation. |
| **Structural** | Database Migrations / Schema shifts. | **Blocks Deployment** until "Migration Applied" check. |
| **Business Gates**| Feature Flags or "Turn on at midnight". | **Defers Release** until the specific time or condition. |

---

## 🚧 Deployment Gates (Gating Strategy)

We use **Metadata-Driven Gates** to ensure that production doesn't break due to "missing context".

### 🔑 The "Blocking Keyword" Demo
The pipeline scans the PR body for the following specific markers:
- **`[x] **[DB_MIGRATION]**`**: Blocks deploy for manual database schema execution.
- **`[x] **[ENV_CHANGE]**`**: Blocks deploy for environment variable provisioning.
- **`[x] **[BLOCK]**`**: General manual lock.

**Workflow Logic**:
1.  **Scanner**: A GitHub Action parses these markers.
2.  **Conditional Path**:
    - **Green Flow**: If no blockers are checked, the **Production Promotion** job executes automatically with a success message.
    - **Yellow Flow**: If blockers are found, the job stays active but warns: `🟡 WAITING FOR MANUAL COMPLIANCE`, preventing the logic from completing blindly.

---

## 🛤️ Release Promotion Workflow

1. **`feat/*`**: Development carries the instructions.
2. **`develop`**: Integration and instruction aggregation.
3. **`release/*`**: The **Staging Gate**. This is where we verify if all "Carrier Instructions" (Env vars, migrations) have been satisfied.
4. **`main`**: The final stable state, promoted only after all gates are cleared.

---

> [!TIP]
> **Demo Script**: To reproduce the "Failed Deployment Prevention", create a PR using the **[.github/pull_request_template.md](file:///home/leo-def/projects/lab/pyducts/.github/pull_request_template.md)**, check the `[ENV_CHANGE]` box, and watch the pipeline halt the release until the instruction is acknowledged.

### 📋 The PR Template
The project includes a standard template in `.github/pull_request_template.md` that enforces the "Instruction Carrier" philosophy. It ensures that every contributor explicitly declares the side-effects and requirements of their code.
