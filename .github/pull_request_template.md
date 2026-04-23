## 🚀 Feature Description
<!-- Describe what this PR does and the business value it brings. -->

## 🛠 Behavioral Instructions (The "Carrier")
<!-- 
IMPORTANT: This project uses Metadata-Driven Gating. 
Check the items below to inform the pipeline about required manual actions.
-->

### 🚦 Deployment Gates
- [ ] **[DB_MIGRATION]**: This PR requires a database migration to be run BEFORE deployment.
- [ ] **[ENV_CHANGE]**: This PR requires new environment variables (see below).
- [ ] **[CONFIG_SHIFT]**: This PR requires a manual configuration change in the dashboard/external service.
- [ ] **[BLOCK]**: Manual freeze required. Do not deploy even if tests pass.

---

### 🔑 Environment Variables Required
<!-- List any new .env keys required for this feature to work. -->
```text
KEY_NAME=value_description
```

### 📋 Migration / Script Details
<!-- Details about the migration or manual script to be executed. -->
```sql
-- migration snippet if applicable
```

---

## ✅ Quality Checklist
- [ ] Business Rules associated with codes in `BUSINESS_CONTEXT.md`.
- [ ] `ExecutionContext` used for complex orchestration.
- [ ] Standard documentation updated (`README.md`, `AGENTS.md`).
- [ ] Unit/Integration tests covering the instruction logic.

## 🔗 Technical References
- **Domain**: <!-- e.g., Products -->
- **Effect Code**: <!-- e.g., EFF_001 -->
