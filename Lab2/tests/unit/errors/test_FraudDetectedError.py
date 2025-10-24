
from src.minimarket.errors.FraudDetectedError import FraudDetectedError
def test_FraudDetectedError_is_exception():
    e = FraudDetectedError('boom')
    assert isinstance(e, Exception)
