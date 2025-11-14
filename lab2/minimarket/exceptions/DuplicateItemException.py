class DuplicateItemException(Exception):
    """Raised when attempting to add a duplicate entity."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
