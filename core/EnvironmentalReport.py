from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class EnvironmentalReport:
    report_id: str
    created_on: date
    prepared_by: Researcher
    summary: str
    findings: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)

    def add_finding(self, finding: str) -> None:
        self.findings.append(finding)

    def add_recommendation(self, recommendation: str) -> None:
        self.recommendations.append(recommendation)
