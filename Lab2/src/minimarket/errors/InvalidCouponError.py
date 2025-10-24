class InvalidCouponError(Exception):
    """Custom exception: InvalidCouponError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "InvalidCouponError occurred"
        super().__init__(message)
