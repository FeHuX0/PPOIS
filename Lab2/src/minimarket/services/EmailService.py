from __future__ import annotations
from src.minimarket.core.notification import NotificationBackend
from dataclasses import dataclass, field
from typing import Any

@dataclass
class EmailService(NotificationBackend):
    smtp_server: str = ''
    port: int = 0
    from_addr: str = ''

    def send(self, to: str, body: str) -> bool:
        return True

    def validate_addr(self, addr: str) -> bool:
        return '@' in addr