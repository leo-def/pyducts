from typing import Generic, TypeVar, List, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum

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

class ValidationContext(BaseModel):
    """
    Context responsible for standardizing the result of business validations.
    """
    is_valid: bool = True
    errors: List[dict] = []

    def add_error(self, code: BusinessRuleCode, message: str, field: Optional[str] = None):
        self.is_valid = False
        self.errors.append({
            "code": code,
            "message": message,
            "field": field
        })

class ExecutionContext(BaseModel, Generic[T]):
    """
    Object returned by UseCases, containing the payload and execution metadata.
    Used to audit business rules active in the action.
    """
    data: Optional[T] = None
    validation: ValidationContext = Field(default_factory=ValidationContext)
    setters: List[str] = []
    effects: List[str] = []

    def add_setter(self, rule_code: str):
        self.setters.append(rule_code)

    def add_effect(self, rule_code: str):
        self.effects.append(rule_code)

class ResponseDTO(BaseModel, Generic[T]):
    """
    Unified Response DTO for the application.
    """
    data: Optional[T] = None
    message: str = ""
    status: int = 200
    errors: List[dict] = []
    setters: List[str] = []
    effects: List[str] = []

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

        if context:
            response_data = context.data if data is None else data
            errors = context.validation.errors
            if show_context:
                setters = context.setters
                effects = context.effects

        return ResponseDTO(
            data=response_data,
            message=message,
            status=status,
            errors=errors,
            setters=setters,
            effects=effects
        )
