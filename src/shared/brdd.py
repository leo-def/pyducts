from typing import Generic, TypeVar, List, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum
from brdd.core import ExecutionContext as BaseExecutionContext, DefaultExecutionContext, ValidationContext as BaseValidationContext

T = TypeVar("T")

class BusinessRuleCode(str, Enum):
    """
    Global mapping of business rule codes.
    These codes must be documented in BUSINESS_CONTEXT.md.
    """
    GENERIC_ERROR = "GENERIC_001"
    VALIDATION_FAILED = "VAL_001"
    # Example related to the products domain
    PRODUCT_PRICE_NEGATIVE = "PROD_001"
    PRODUCT_TITLE_EMPTY = "PROD_002"

class ValidationContext(BaseValidationContext):
    """
    Adapter for the official ValidationContext.
    """
    def add_error(self, code: BusinessRuleCode, message: str):
        super().add_error(code=code, message=message)

class ExecutionContext(DefaultExecutionContext, Generic[T]):
    """
    Adapter for the official ExecutionContext.
    """
    data: Optional[T] = None

class ResponseMeta(BaseModel):
    setters: List[str] = []
    effects: List[str] = []
    rules_passed: List[str] = []

class ResponseDTO(BaseModel, Generic[T]):
    """
    Unified Response DTO following the official BRDD standard.
    """
    success: bool = True
    data: Optional[T] = None
    message: str = ""
    status: int = 200
    errors: List[dict] = []
    meta: ResponseMeta = Field(default_factory=ResponseMeta)

class ResponseService:
    @staticmethod
    def construct_response(
        data: Optional[Any] = None,
        message: str = "",
        status: int = 200,
        context: Optional[ExecutionContext] = None,
        show_context: bool = True
    ) -> ResponseDTO:
        """
        Encapsulates the creation of the Response DTO, handling the ExecutionContext if present.
        """
        response_data = data
        errors = []
        setters = []
        effects = []
        rules_passed = []
        success = True if status < 400 else False

        if context:
            response_data = context.data if data is None else data
            errors = [e.dict() if hasattr(e, "dict") else e for e in context.errors]
            success = context.is_valid()
            
            # Synchronize status with context status if context has a failure status
            if context.status >= 400:
                status = context.status
            elif not success and status < 400:
                status = 400
            
            if show_context:
                setters = context.setters
                effects = context.effects
                rules_passed = [] 

        return ResponseDTO(
            success=success,
            data=response_data,
            message=message,
            status=status,
            errors=errors,
            meta=ResponseMeta(
                setters=setters,
                effects=effects,
                rules_passed=rules_passed
            )
        )
