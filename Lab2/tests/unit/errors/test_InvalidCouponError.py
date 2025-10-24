
from src.minimarket.errors.InvalidCouponError import InvalidCouponError
def test_InvalidCouponError_is_exception():
    e = InvalidCouponError('boom')
    assert isinstance(e, Exception)
