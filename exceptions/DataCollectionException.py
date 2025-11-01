class DataCollectionException(Exception):
    """Raised when collected data is invalid."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
