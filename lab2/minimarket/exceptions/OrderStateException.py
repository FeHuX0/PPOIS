class OrderStateException(Exception):
    """Raised when an order transitions into an invalid state."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
