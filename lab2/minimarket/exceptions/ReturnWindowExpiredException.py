class ReturnWindowExpiredException(Exception):
    """Raised when a return request exceeds the allowed window."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
