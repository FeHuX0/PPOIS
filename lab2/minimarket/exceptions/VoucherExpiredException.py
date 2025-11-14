class VoucherExpiredException(Exception):
    """Raised when trying to use an expired voucher or coupon."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
