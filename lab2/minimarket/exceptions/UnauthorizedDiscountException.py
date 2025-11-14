class UnauthorizedDiscountException(Exception):
    """Raised when a discount does not satisfy store policies."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
