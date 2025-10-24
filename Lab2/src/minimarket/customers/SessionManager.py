from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class SessionManager:
    sessions: dict = field(default_factory=dict)
    timeout_seconds: int = 0
    store: 'Store' = None

    def create(self, user_id: str) -> str:
        sid = 's-'+user_id
        self.sessions[sid]=user_id
        return sid

    def validate(self, sid: str) -> bool:
        return sid in self.sessions
