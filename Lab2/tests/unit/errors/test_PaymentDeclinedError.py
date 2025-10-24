
from src.minimarket.errors.PaymentDeclinedError import PaymentDeclinedError
def test_PaymentDeclinedError_is_exception():
    e = PaymentDeclinedError('boom')
    assert isinstance(e, Exception)
