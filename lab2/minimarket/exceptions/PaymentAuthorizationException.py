class PaymentAuthorizationException(Exception):
    """Raised when a payment cannot be authorized."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
