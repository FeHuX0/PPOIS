class ComplianceBreachException(Exception):
    """Raised when compliance requirements are violated."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
