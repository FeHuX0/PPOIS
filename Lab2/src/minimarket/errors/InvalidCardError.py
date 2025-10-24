class InvalidCardError(Exception):
    """Custom exception: InvalidCardError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "InvalidCardError occurred"
        super().__init__(message)
