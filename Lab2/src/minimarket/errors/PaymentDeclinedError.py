class PaymentDeclinedError(Exception):
    """Custom exception: PaymentDeclinedError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "PaymentDeclinedError occurred"
        super().__init__(message)
