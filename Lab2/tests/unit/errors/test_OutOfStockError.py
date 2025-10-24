
from src.minimarket.errors.OutOfStockError import OutOfStockError
def test_OutOfStockError_is_exception():
    e = OutOfStockError('boom')
    assert isinstance(e, Exception)
