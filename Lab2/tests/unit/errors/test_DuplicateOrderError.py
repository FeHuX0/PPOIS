
from src.minimarket.errors.DuplicateOrderError import DuplicateOrderError
def test_DuplicateOrderError_is_exception():
    e = DuplicateOrderError('boom')
    assert isinstance(e, Exception)
