
from src.minimarket.errors.ValidationError import ValidationError
def test_ValidationError_is_exception():
    e = ValidationError('boom')
    assert isinstance(e, Exception)
