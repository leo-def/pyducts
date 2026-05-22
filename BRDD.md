# Business Rule Driven Design (BRDD) 🚀

**Business Rule Driven Design (BRDD)** is an architectural pattern that prioritizes business rules as the primary drivers of software structure. It ensures that every logic branch is traceable, every side effect is documented, and every response is standardized.

This project implements BRDD using the official **[brdd-python](https://github.com/brdd-design/brdd-python)** library.

---

## 🏛 The Pillars of BRDD

### 1. Unique Rule Coding
Every validation or side effect must have a unique ID (e.g., `PROD_001`). This ID connects the code directly to the [Business Context](file:///home/leo-def/projects/lab/pyducts/BUSINESS_CONTEXT.md).

### 2. Execution Context Narrative
Use Cases return an `ExecutionContext` (from `brdd.core`) instead of raw data. This object contains:
- **Data**: The primary result of the operation.
- **Setters**: Automated field assignments (e.g., `SETTER_TIMESTAMP`).
- **Effects**: Side effects triggered (e.g., `EFF_NOTIFY_ADMIN`).
- **Validation**: A clear report of compliance with business rules.

### 3. Service Specialization
BRDD divides logic into specialized roles:
- **UseCase**: Orchestrator.
- **ValidateService**: Rule verification.
- **EnrichService**: Data completion.
- **Client/Listener**: External bridges.

### 4. Unified Response Pattern
All API interactions follow the official **[BRDD Unified Response Pattern](https://github.com/brdd-design/brdd#4-unified-response-pattern)**:
```json
{
  "success": true,
  "data": { ... },
  "message": "Human-readable message",
  "status": 201,
  "errors": [],
  "meta": {
    "setters": ["SETTER_UUID"],
    "effects": ["EFF_LOG_AUDIT"],
    "rules_passed": ["RULE_001"]
  }
}
```

---

## 🛡️ BRDD & The "PR as an Instruction Carrier"

BRDD is the engine that enables the **Instruction Carrier** philosophy. Because every effect and setter is explicitly coded and audited, we can:

1. **Audit Side-Effects**: Before a PR is merged, we can see exactly which business rules will be triggered and which side-effects (e.g., sending an email, writing to a new table) will occur.
2. **Synchronize Infrastructure**: If a rule requires a new environment variable or a database column, the BRDD audit trail makes this requirement obvious, justifying the **Deployment Gate** blockers.

---

## 🎯 Key Benefits
- **Auditability**: Complete visibility into side effects.
- **Consistency**: Standardized contracts across all domains.
- **AI-Optimized**: Highly structured patterns for AI-assisted development.

---
👉 **Official Specification**: [github.com/brdd-design/brdd](https://github.com/brdd-design/brdd)
