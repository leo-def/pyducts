# Pyducts - Technical Specification

> FastAPI + BRDD (Business Rule Driven Design) reference implementation.
> Demonstrates how to structure Python microservices with traceable business rules, auditable effects, and standardized responses.

## Executive Summary

Pyducts is a **FastAPI + Python 3.10** reference implementation of the **BRDD (Business Rule Driven Design)** pattern. Every logic branch has a unique B-code (e.g., `PROD_001`), every side effect is audited in `ExecutionContext`, and all responses are standardized via `ResponseService`. The single implemented domain (`products`) demonstrates the full BRDD flow: UseCase → Validation → Enrichment → Effects → ResponseDTO. Built on `brdd-python` library.

---

## 1. Problem Statement

### Context
Demonstrate how to implement BRDD pattern in production Python, where every business rule is traceable to a code, every side effect is recorded, and responses carry execution metadata for auditability.

### Goals
- `POST /products` endpoint demonstrating full BRDD flow
- Business rules with unique codes documented in `BUSINESS_CONTEXT.md`
- ExecutionContext captures: data, setters (state changes), effects (side effects), errors
- Configurable response verbosity via `SHOW_EXECUTION_CONTEXT` env var
- FastAPI auto-generated OpenAPI docs

### Success Metrics
- [x] BRDD pattern with `brdd-python` library integration
- [x] BusinessRuleCode enum mapping to documented rules
- [x] ExecutionContext with data/setters/effects/errors
- [x] ResponseDTO standardized response envelope
- [x] `SHOW_EXECUTION_CONTEXT` toggle
- [x] Price validation (PROD_001) with early return
- [ ] Title validation (PROD_002) — declared but not implemented
- [ ] Database persistence (currently in-memory simulation)
- [ ] Second domain to demonstrate multi-domain BRDD

---

## 2. Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | 3.10+ |
| Framework | FastAPI | Latest |
| ASGI Server | Uvicorn | Latest |
| Validation | Pydantic v2 | Latest |
| BRDD | brdd-python | Latest |
| Linting | Ruff | Latest |
| Testing | pytest + httpx | Latest |
| Config | python-dotenv | Latest |

---

## 3. BRDD Architecture

```
POST /products { title, description, price }
         ↓
CreateProductUseCase.execute(params)
    ├── Validate: price < 0 → context.add_error(PROD_001)  ← early return
    ├── Enrich: create ProductModel with uuid4 + datetime.now()
    ├── context.add_setter("SETTER_TIMESTAMP")
    ├── context.add_setter("SETTER_UUID")
    ├── context.add_effect("EFF_NOTIFY_ADMIN")
    └── context.add_effect("EFF_LOG_AUDIT")
         ↓
ResponseService.construct_response(context, show_context)
         ↓
ResponseDTO { success, data, message, status, errors, meta }
```

### Key Components

**`ExecutionContext[T]`** (from `brdd-python`):
- `data: T` — business result
- `errors: List` — validation errors with B-codes
- `setters: List[str]` — state changes applied
- `effects: List[str]` — side effects triggered
- `is_valid() → bool`

**`BusinessRuleCode` enum:**
```python
GENERIC_ERROR = "GENERIC_001"
VALIDATION_FAILED = "VAL_001"
PRODUCT_PRICE_NEGATIVE = "PROD_001"   # Validated ✓
PRODUCT_TITLE_EMPTY = "PROD_002"      # Declared ✗ — not validated
```

---

## 4. Module Structure

```
src/
  main.py                        # FastAPI app, /products endpoint
  dependencies.py                # Dependency injection (DB session, etc.)
  shared/
    brdd.py                      # ExecutionContext, BusinessRuleCode, ResponseService, ResponseDTO
  domains/
    products/
      schemas.py                 # CreateProductDTO, ProductModel (Pydantic)
      models.py                  # SQLAlchemy model (if DB integration added)
      router.py                  # FastAPI router (if extracted from main.py)
      services/
        product_service.py       # Product business logic
        product_enrich_service.py # Product enrichment
      use_cases/
        create_product_use_case.py  # CreateProductUseCase
  internal/
    admin.py                     # Admin utilities
```

---

## 5. API Endpoints

```
GET  /              → Welcome message + docs link
POST /products      → Create product (BRDD flow)
GET  /docs          → Swagger UI (auto-generated)
GET  /redoc         → ReDoc UI
```

**Request:** `{ "title": "...", "description": "...", "price": 99.99 }`

**Response (with SHOW_EXECUTION_CONTEXT=true):**
```json
{
  "success": true,
  "data": { "id": "...", "title": "...", "price": 99.99, "created_at": "..." },
  "message": "Processing completed",
  "status": 201,
  "errors": [],
  "meta": {
    "setters": ["SETTER_TIMESTAMP", "SETTER_UUID"],
    "effects": ["EFF_NOTIFY_ADMIN", "EFF_LOG_AUDIT"],
    "rules_passed": []
  }
}
```

---

## 6. Configuration

```bash
SHOW_EXECUTION_CONTEXT=true    # Include meta.setters/effects in response (default: false)
```

---

## 7. Testing Strategy

```bash
pytest              # All tests
pytest -v           # Verbose
ruff check .        # Linting
```

---

## 8. Deployment & Operations

```bash
uvicorn src.main:app --reload    # Development
uvicorn src.main:app --port 8000 # Production
```

---

## 9. Issues Found

### Logic Bugs

- **`PROD_002` (empty title) is declared in `BusinessRuleCode` enum but never validated** in `CreateProductUseCase.execute()`. A product with an empty or whitespace-only title is silently accepted. Add:
  ```python
  if not params.title or not params.title.strip():
      context.add_error(BusinessRuleCode.PRODUCT_TITLE_EMPTY, "Title cannot be empty")
      return context
  ```

- **`rules_passed` is always `[]`** in `ResponseService.construct_response()` — line `rules_passed = []` is hardcoded regardless of context state. This field is supposed to record which B-codes passed validation, but is never populated. The `ExecutionContext` from `brdd-python` may not expose this directly, but the field should either be populated or removed from the response schema.

- **`data` parameter to `ResponseService.construct_response` is shadowed** when `context` is provided — the function signature accepts `data` and `context`, but if both are passed, `context.data` always wins. The `data` parameter is effectively ignored when a context exists. The function signature should be clarified (remove `data` param when `context` is required, or document override behavior).

### Missing Features
- **No database persistence** — all product creation is in-memory simulation. `ProductModel` has Pydantic fields with `uuid4()` and `datetime.now()` but no actual DB insert.
- **Single domain** — a second domain (e.g., `orders`) would better demonstrate multi-domain BRDD pattern.
- No authentication or rate limiting.
