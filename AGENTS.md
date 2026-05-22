# AGENTS.md - BRDD Project Context for AI Agents

This file contains condensed information to optimize the work of AIs in this repository.

## 🛠 Tech Stack & Core
- **Framework**: FastAPI.
- **Core Library**: `brdd-python` (Official BRDD implementation).
- **Data Layers**: Model (Domain), DTO (Communication), External (External APIs).
- **Workflow**: Makefile + venv + Git + Business Rule Mapping.

## 📂 Structure & Nomenclature (DDD + UseCases)
Domain folders (`src/domains/{domain_name}`) must follow:
- `use_cases/`: Complex orchestration. Suffix: `UseCase`.
- `services/`: Domain logic. Suffix: `Service`, `EnrichService`, `ValidateService`.
- `models.py`: Pure domain classes (POPOs) and ORM.
- `schemas.py`: Pydantic Models with `DTO` or `External` suffixes.

## 🧠 Business Logic & Audit (ExecutionContext)
- **ValidationContext**: Must capture errors linked to codes in `BUSINESS_CONTEXT.md`. Uses `brdd.core`.
- **ExecutionContext**: Returned by UseCases. Must register `setters` and `effects`. Uses `brdd.core`.
- **Consumption**: Use `ResponseService.construct_response` for standardized responses (meta-based).

## 🤖 Instructions for the Agent (Do's & Don'ts)
- **Do**: Always associate validations and effects with codes in `BUSINESS_CONTEXT.md`.
- **Do**: Use `ExecutionContext` for any logic that is not simple CRUD.
- **Do**: **PR as an Instruction Carrier**: Every change must package not only code but tb the **conditions** (env vars, migrations) as blockers in the PR description.
- **Don't**: Return raw JSON responses in UseCases; return `ExecutionContext`.
- **Don't**: Mix integration logic (Client) with domain logic (Service).

## 📖 Rule Mapping
Consult **[BUSINESS_CONTEXT.md](file:///home/leo-def/projects/lab/pyducts/BUSINESS_CONTEXT.md)** to find valid error codes and effects.
Consult **[CICD.md](file:///home/leo-def/projects/lab/pyducts/CICD.md)** for Deployment Gate tags.
