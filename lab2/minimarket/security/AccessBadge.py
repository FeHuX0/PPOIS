from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AccessBadge:
    badge_id: str
    roles_allowed: set[str] = field(default_factory=set)
    active: bool = True

    def grant_access(self, role: str) -> bool:
        return self.active and role in self.roles_allowed
