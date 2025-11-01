class FundingApprovalException(Exception):
    """Raised when funding approvals fail."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
