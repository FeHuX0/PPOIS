class ProductSpoiledException(Exception):
    """Raised when perishable goods leave the safe temperature range."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
