from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProtectedArea:
    area_id: str
    name: str
    category: str
    governing_body: str
    visitor_centers: list[VisitorCenter] = field(default_factory=list)

    def add_visitor_center(self, center: VisitorCenter) -> None:
        self.visitor_centers.append(center)

    def describe(self) -> str:
        return f"{self.name} ({self.category})"
