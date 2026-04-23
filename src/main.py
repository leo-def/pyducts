from fastapi import FastAPI
from src.shared.brdd import ResponseService, ResponseDTO
from src.domains.products.schemas import ProductModel, CreateProductDTO
from src.domains.products.use_cases.create_product_use_case import CreateProductUseCase
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Pyducts API",
    description="Corporate Architecture Blueprint with FastAPI and DDD",
    version="0.2.0"
)

# Context display configuration (via .env)
SHOW_CONTEXT = os.getenv("SHOW_EXECUTION_CONTEXT", "False").lower() == "true"

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to Pyducts Architecture Model",
        "docs": "/docs",
        "status": "ready"
    }

@app.post("/products", response_model=ResponseDTO[ProductModel], tags=["Products"])
async def create_product(payload: CreateProductDTO):
    """
    Architecture flow demonstration:
    Router -> UseCase -> ExecutionContext -> ResponseService -> Unified DTO
    """
    # Execute the use case
    context = CreateProductUseCase.execute(payload)
    
    # Determine HTTP status based on validation
    http_status = 201 if context.validation.is_valid else 400
    
    # Construct unified response
    return ResponseService.construct_response(
        message="Processing completed",
        status=http_status,
        context=context,
        show_context=SHOW_CONTEXT
    )
