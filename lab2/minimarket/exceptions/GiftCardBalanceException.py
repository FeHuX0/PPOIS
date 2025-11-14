class GiftCardBalanceException(Exception):
    """Raised when a gift card does not have enough balance."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
