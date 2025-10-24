
from __future__ import annotations
from abc import ABC, abstractmethod

class NotificationBackend(ABC):
    """Abstract interface for notification backends (email, sms, push)."""

    @abstractmethod
    def send_message(self, recipient: str, subject: str, body: str) -> bool:
        """Send a message. Return True on success."""
        raise NotImplementedError
