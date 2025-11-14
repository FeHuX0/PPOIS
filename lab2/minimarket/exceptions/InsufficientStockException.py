class InsufficientStockException(Exception):
    """Raised when stock levels cannot satisfy a request."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
