# Pyducts - Technical Specification

> Consolidated technical specification for the Pyducts BRDD reference implementation.
> BRDD Pattern - Business Rule Driven Design with FastAPI and Python.

## Executive Summary

- **Project**: Pyducts
- **Type**: Backend API / Reference Implementation
- **Language**: Python 3.10+
- **Framework**: FastAPI, SQLAlchemy
- **Pattern**: BRDD (Business Rule Driven Design)
- **Status**: Reference Implementation - Active

---

## 1. Problem Statement

Demonstrate how to implement BRDD pattern with fastapi, where every business rule has a unique code, every outcome is audited, and the PR serves as an instruction carrier for deployment.

---

## 2. Technology Stack

| Component | Technology | Version | Rationale |
|-----------|-----------|---------|-----------|
| Language | Python | 3.10+ | Type hints, modern async |
| Framework | FastAPI | Latest | Async, modern Python web framework |
| ORM | SQLAlchemy | 2.0+ | Type-safe database abstraction |
| Validation | Pydantic | v2 | Data validation and serialization |
| Database | PostgreSQL | 15+ | Production-grade relational DB |
| Library | brdd-python | Latest | Official BRDD implementation |
| Testing | pytest | Latest | Python testing framework |
| Migrations | Alembic | Latest | Database schema migrations |

---

## 3. Architecture Pattern: BRDD

### Core Concept
Every logic branch has a **unique code** (e.g., `B001`, `B002`) traceable to business context. Every **side effect** is audited via `ExecutionContext`.

### Flow
```
HTTP Request
    ↓
UseCase (orchestrates business rules)
    ↓
ValidateService (applies B-codes, returns ValidationContext)
    ↓
EnrichService (transforms data, logs effects)
    ↓
ExecutionContext (contains: data, errors, effects, codes)
    ↓
ResponseService (standardizes response with metadata)
    ↓
HTTP Response (includes execution metadata)
```

### Key Components

**1. ValidationContext**
- Captures validation errors linked to B-codes
- Example: `ValidationContext(errors=[BError('B001', 'Invalid email')])`

**2. ExecutionContext**
- Response object from UseCases
- Contains:
  - `data`: Business result
  - `setters`: State changes
  - `effects`: Side effects (emails, logs, etc.)
  - `brdd_codes`: Business rule codes applied

**3. BRDD Registry** (`BUSINESS_CONTEXT.md`)
- Single source of truth for all business rules
- Maps codes (B001, B002, ...) to business meaning
- Defines valid error codes and effects

---

## 4. Module Structure

```
src/
├── shared/
│   ├── brdd.py           # BRDD integration
│   ├── response.py       # ResponseService
│   └── context.py        # ExecutionContext
├── domains/              # Feature domains
│   ├── product/
│   │   ├── use_cases/    # ProductCreateUseCase, ProductUpdateUseCase
│   │   ├── services/     # ProductService, ProductValidateService
│   │   ├── models.py     # Pydantic models
│   │   ├── schemas.py    # DTO (Request/Response)
│   │   └── routes.py     # FastAPI routes
│   └── [other domains]
├── main.py               # FastAPI app
└── config.py             # Configuration
```

---

## 5. Development with BRDD

### Adding a Feature

1. **Document Business Rule** in `BUSINESS_CONTEXT.md`
   - Assign B-code (e.g., B001)
   - Define rule and effects

2. **Create UseCase**
   ```python
   class ProductCreateUseCase:
       def __call__(self, request: CreateProductRequest) -> ExecutionContext:
           # Validate → effect → return context
   ```

3. **Use ValidateService**
   - Link validation to B-codes
   - Return ValidationContext with error codes

4. **Build ExecutionContext**
   - Include all effects and codes
   - Framework standardizes response

---

## 6. Naming Conventions

**Files**:
- UseCase files: `{Action}{Entity}UseCase.py` (e.g., `CreateProductUseCase.py`)
- Service files: `{Entity}Service.py`, `{Entity}ValidateService.py`
- DTO/schemas: `{Entity}DTO.py`

**Classes**:
- UseCase: `{Action}{Entity}UseCase` (inherits from Usecase base)
- Services: `{Entity}Service`, `{Entity}ValidateService`
- Models: `{Entity}Model` (SQLAlchemy)
- Schemas: `{Entity}Request`, `{Entity}Response` (Pydantic)

**Constants**:
- Business codes: `B001`, `B002`, ... (documented in BUSINESS_CONTEXT.md)
- Effects: `EFFECT_EMAIL_SENT`, `EFFECT_USER_NOTIFIED`

---

## 7. Key Files & Documentation

### BRDD.md
Deep dive into Business Rule Driven Design pattern.  
How to apply codes, when to create effects, audit trails.

### BUSINESS_CONTEXT.md
**Source of truth** for business rules.  
Every B-code, every effect, every constraint documented here.

### CICD.md
PR as instruction carrier pattern.  
How to gate deployments based on migrations/env-vars marked in PR.

### PIPELINE_EXPLAINED.md
Step-by-step guide for humans understanding the CI/CD flow.

---

## 8. Error Handling

### Custom Exceptions
```python
class BusinessRuleError(Exception):
    def __init__(self, code: str, message: str):
        self.code = code  # e.g., "B001"
        self.message = message
```

### Mapping to HTTP
- `ValidationError` → 400
- `BusinessRuleError` → 422 (unprocessable)
- `NotFoundError` → 404
- `UnauthorizedError` → 401

---

## 9. Testing Strategy

### Unit Tests
- Test UseCases with mock services
- Test ValidateService with known rule codes
- Test service business logic

### Integration Tests
- Test full request → UseCase → database
- Verify effects are recorded

### Test Database
- Use test PostgreSQL container
- Run migrations, seed fixtures
- Clean up after tests

---

## 10. API Response Format

All responses standardized via `ResponseService`:

```python
{
  "success": true,
  "data": { /* business result */ },
  "execution": {
    "brdd_codes": ["B001", "B003"],
    "effects": ["EFFECT_EMAIL_SENT"],
    "timestamp": "2024-06-01T10:30:00Z"
  },
  "errors": null
}
```

---

## References

- **[BRDD.md](BRDD.md)** - Pattern documentation
- **[BUSINESS_CONTEXT.md](BUSINESS_CONTEXT.md)** - Business rule registry
- **[CICD.md](CICD.md)** - Deployment automation
- **[PIPELINE_EXPLAINED.md](PIPELINE_EXPLAINED.md)** - CI/CD guide
- **[.instructions.md](.instructions.md)** - Development guidelines
- **[.agent.md](.agent.md)** - AI agent configuration

---

**Version**: v1.0 (2024-06-01)
