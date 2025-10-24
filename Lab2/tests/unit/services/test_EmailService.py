from src.minimarket.services.EmailService import EmailService

class DummyEmailService(EmailService):
    def send_message(self, recipient: str, subject: str, body: str) -> bool:
        return True

def test_emailservice_instantiation():
    obj = DummyEmailService()
    assert obj.send_message("test@example.com", "Hi", "Body") is True
