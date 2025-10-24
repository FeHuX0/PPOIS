class OutOfStockError(Exception):
    """Custom exception: OutOfStockError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "OutOfStockError occurred"
        super().__init__(message)
