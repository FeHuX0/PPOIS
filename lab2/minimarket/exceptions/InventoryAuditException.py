class InventoryAuditException(Exception):
    """Raised when an inventory audit detects inconsistent input."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
