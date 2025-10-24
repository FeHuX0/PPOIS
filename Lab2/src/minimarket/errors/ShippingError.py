class ShippingError(Exception):
    """Custom exception: ShippingError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "ShippingError occurred"
        super().__init__(message)
