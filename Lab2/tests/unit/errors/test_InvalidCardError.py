
from src.minimarket.errors.InvalidCardError import InvalidCardError
def test_InvalidCardError_is_exception():
    e = InvalidCardError('boom')
    assert isinstance(e, Exception)
