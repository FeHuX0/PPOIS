class AuthorizationError(Exception):
    """Custom exception: AuthorizationError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "AuthorizationError occurred"
        super().__init__(message)
