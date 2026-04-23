from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

# --- business domain (Model) ---
class ProductModel(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: str
    price: float
    created_at: Optional[datetime] = None

# --- dto (DTO) ---
class ProductDTO(BaseModel):
    id: UUID
    title: str
    price: float

class CreateProductDTO(BaseModel):
    title: str
    description: str
    price: float

# --- external domain (External) ---
class ProductExternal(BaseModel):
    # DTO retornado por um webhook ou API de fornecedor
    provider_id: str
    title: str
    cost_price: float
