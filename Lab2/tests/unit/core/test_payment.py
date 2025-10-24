from src.minimarket.core.payment import PaymentGateway

class DummyPayment(PaymentGateway):
    def process_payment(self, source, amount, metadata=None) -> bool:
        return True

def test_payment_instantiation():
    obj = DummyPayment()
    assert obj.process_payment({}, 10.0) is True
