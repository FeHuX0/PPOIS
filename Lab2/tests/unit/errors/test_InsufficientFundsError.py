
from src.minimarket.errors.InsufficientFundsError import InsufficientFundsError
def test_InsufficientFundsError_is_exception():
    e = InsufficientFundsError('boom')
    assert isinstance(e, Exception)
