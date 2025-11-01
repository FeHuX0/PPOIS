from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.WeatherAlertException import WeatherAlertException


@dataclass
class AlertNotification:
    alert_id: str
    title: str
    severity: str
    issued_for: Region
    responders: list[ParkRanger] = field(default_factory=list)

    def add_responder(self, ranger: ParkRanger) -> None:
        self.responders.append(ranger)

    def ensure_severity(self) -> None:
        if self.severity.lower() not in {"low", "moderate", "high"}:
            raise WeatherAlertException("Invalid alert severity.")
