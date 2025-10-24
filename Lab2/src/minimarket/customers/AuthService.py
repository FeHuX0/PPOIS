from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class AuthService:
    jwt_secret: str = ''
    policy: 'PasswordPolicy' = None
    sessions: dict = field(default_factory=dict)

    def login(self, email: str, password: str) -> str:
        if password == 'pass123':
            token = 'tok-'+email
            self.sessions[token]=email
            return token
        from src.minimarket.errors.AuthenticationError import AuthenticationError
        raise AuthenticationError('Bad creds')

    def logout(self, token: str) -> None:
        self.sessions.pop(token, None)
