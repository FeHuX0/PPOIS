from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class AnalyticsService:
    store_id: str = ''
    events: list = field(default_factory=list)
    enabled: bool = False

    def track(self, event: dict) -> None:
        self.events.append(event)

    def report(self) -> dict:
        return {'events': len(self.events)}
