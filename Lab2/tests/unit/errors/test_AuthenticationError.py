
from src.minimarket.errors.AuthenticationError import AuthenticationError
def test_AuthenticationError_is_exception():
    e = AuthenticationError('boom')
    assert isinstance(e, Exception)
