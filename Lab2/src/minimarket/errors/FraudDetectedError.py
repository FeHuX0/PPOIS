class FraudDetectedError(Exception):
    """Custom exception: FraudDetectedError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "FraudDetectedError occurred"
        super().__init__(message)
