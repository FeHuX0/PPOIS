from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class NotificationService:
    emailer: 'EmailService' = None
    sms: 'SMSService' = None
    queue: list = field(default_factory=list)

    def notify_email(self, to: str, body: str) -> bool:
        self.emailer.send(to, body)
        return True

    def notify_sms(self, to: str, body: str) -> bool:
        self.sms.send(to, body)
        return True
