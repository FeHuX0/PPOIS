class QuantityLimitException(Exception):
    """Raised when quantities violate configured limits."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
