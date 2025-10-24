
from src.minimarket.errors.ShippingError import ShippingError
def test_ShippingError_is_exception():
    e = ShippingError('boom')
    assert isinstance(e, Exception)
