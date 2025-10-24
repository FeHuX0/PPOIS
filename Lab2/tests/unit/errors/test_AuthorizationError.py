
from src.minimarket.errors.AuthorizationError import AuthorizationError
def test_AuthorizationError_is_exception():
    e = AuthorizationError('boom')
    assert isinstance(e, Exception)
