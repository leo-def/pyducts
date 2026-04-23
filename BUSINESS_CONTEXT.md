# 📖 Business Context (BUSINESS_CONTEXT.md)

This file maps all business rule codes used in the system, allowing developers and stakeholders to understand which behaviors are being executed in each action.

---

## 🛡️ Validation Rules

| Code | Name | Description |
| :--- | :--- | :--- |
| `VAL_001` | Generic Failure | Unspecified validation error. |
| `PROD_001` | Negative Price | Product price must be greater than or equal to zero. |
| `PROD_002` | Empty Title | Product title is mandatory. |

---

## ⚙️ System Definitions (Setters)

| Code | Name | Description |
| :--- | :--- | :--- |
| `SETTER_TIMESTAMP` | Creation Date | Automatically assigns the current date and time to the record. |
| `SETTER_UUID` | Unique ID | Generates a Universally Unique Identifier (UUID) for the entity. |

---

## 🎭 Side Effects (Effects)

| Code | Name | Type | Description |
| :--- | :--- | :--- | :--- |
| `EFF_NOTIFY_ADMIN` | Notify Admin | After-effect | Sends an email/alert to the administrator after a resource is created. |
| `EFF_LOG_AUDIT` | Audit Log | After-effect | Records the action in an external audit table. |
| `EFF_CLEAN_CACHE` | Clean Cache | After-effect | Invalidates the cache related to the modified resource. |
