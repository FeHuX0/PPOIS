class DuplicateOrderError(Exception):
    """Custom exception: DuplicateOrderError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "DuplicateOrderError occurred"
        super().__init__(message)
