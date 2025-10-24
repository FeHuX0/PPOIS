class AuthenticationError(Exception):
    """Custom exception: AuthenticationError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "AuthenticationError occurred"
        super().__init__(message)
