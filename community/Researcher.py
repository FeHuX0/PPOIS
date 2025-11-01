from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Researcher:
    researcher_id: str
    name: str
    institution: str
    focus_areas: list[str] = field(default_factory=list)
    published_reports: list[EnvironmentalReport] = field(default_factory=list)

    def add_focus_area(self, topic: str) -> None:
        if topic not in self.focus_areas:
            self.focus_areas.append(topic)

    def publish_report(self, report: EnvironmentalReport) -> None:
        self.published_reports.append(report)
