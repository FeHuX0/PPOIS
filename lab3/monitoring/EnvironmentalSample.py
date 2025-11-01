from __future__ import annotations

from dataclasses import dataclass

from ecology.exceptions.SampleContaminationException import SampleContaminationException


@dataclass
class EnvironmentalSample:
    sample_id: str
    collected_by: Researcher
    station: MonitoringStation
    sample_type: str
    integrity_score: float

    def validate(self, minimum: float) -> None:
        if self.integrity_score < minimum:
            raise SampleContaminationException("Sample integrity below threshold.")

    def adjust_integrity(self, score: float) -> None:
        self.integrity_score = score
