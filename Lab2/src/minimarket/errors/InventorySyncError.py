class InventorySyncError(Exception):
    """Custom exception: InventorySyncError"""
    def __init__(self, message: str = None):
        if message is None:
            message = "InventorySyncError occurred"
        super().__init__(message)
