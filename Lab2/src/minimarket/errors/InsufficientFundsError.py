class InsufficientFundsError(Exception):
    """Custom exception: InsufficientFundsError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "InsufficientFundsError occurred"
        super().__init__(message)
