from src.shared.brdd import ExecutionContext, BusinessRuleCode
from src.domains.products.schemas import ProductModel, CreateProductDTO
from datetime import datetime
from uuid import uuid4

class CreateProductUseCase:
    """
    Orchestrates the creation of a product by applying business rules,
    enrichments, and recording side effects.
    """
    @staticmethod
    def execute(params: CreateProductDTO) -> ExecutionContext[ProductModel]:
        context = ExecutionContext[ProductModel]()
        
        # 1. Semantic Validation (Simulated)
        if params.price < 0:
            context.validation.add_error(
                BusinessRuleCode.PRODUCT_PRICE_NEGATIVE,
                "Price cannot be negative",
                field="price"
            )
            return context

        # 2. Enrichment and Setters (Simulated)
        product = ProductModel(
            id=uuid4(),
            title=params.title,
            description=params.description,
            price=params.price,
            created_at=datetime.now()
        )
        context.data = product
        context.add_setter("SETTER_TIMESTAMP")
        context.add_setter("SETTER_UUID")

        # 3. Side Effects (Simulated)
        context.add_effect("EFF_NOTIFY_ADMIN")
        context.add_effect("EFF_LOG_AUDIT")

        return context

