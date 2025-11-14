from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CameraFeed:
    camera_id: str
    status: str = "online"
    alerts: list[str] = field(default_factory=list)

    def record_alert(self, message: str) -> None:
        self.alerts.append(message)
        self.status = "alert"
