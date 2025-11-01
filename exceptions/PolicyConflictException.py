class PolicyConflictException(Exception):
    """Raised when policies conflict or duplicate."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
