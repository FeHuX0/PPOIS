from src.minimarket.services.SMSService import SMSService

class DummySMSService(SMSService):
    def send_message(self, phone_number: str, body: str) -> bool:
        return True

def test_smsservice_instantiation():
    obj = DummySMSService()
    assert obj.send_message("+1234567890", "Test") is True
