class ValidationError(Exception):
    """Custom exception: ValidationError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "ValidationError occurred"
        super().__init__(message)
