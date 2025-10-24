
from src.minimarket.errors.InventorySyncError import InventorySyncError
def test_InventorySyncError_is_exception():
    e = InventorySyncError('boom')
    assert isinstance(e, Exception)
