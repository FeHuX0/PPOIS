from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class PasswordPolicy:
    min_length: int = 0
    require_special: bool = False
    max_age_days: int = 0

    def check(self, password: str) -> bool:
        return len(password) >= self.min_length

    def enforce(self, password: str) -> None:
        if not self.check(password):
            from minimarket.errors.ValidationError import ValidationError
            raise ValidationError('Password')
