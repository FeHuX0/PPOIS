from src.minimarket.core.notification import NotificationBackend

class DummyNotification(NotificationBackend):
    def send_message(self, recipient, subject, body) -> bool:
        return True

def test_notification_instantiation():
    obj = DummyNotification()
    assert obj.send_message("a@b.com", "hi", "body") is True
