from __future__ import annotations

from dataclasses import dataclass
from datetime import time


@dataclass
class StoreHours:
    day: str
    open_time: time
    close_time: time
    override_reason: str | None = None

    def is_open(self, current_time: time) -> bool:
        if self.override_reason == "closed":
            return False
        return self.open_time <= current_time <= self.close_time
