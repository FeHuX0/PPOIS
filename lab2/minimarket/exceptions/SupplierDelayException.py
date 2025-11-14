class SupplierDelayException(Exception):
    """Raised when a supplier cannot meet a delivery window."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
