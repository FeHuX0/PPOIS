from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Animal:
    species: Species
    tag_id: str
    age_years: int
    tracked_routes: list[MigrationRoute] = field(default_factory=list)
    health_notes: list[str] = field(default_factory=list)

    def add_route(self, route: MigrationRoute) -> None:
        if route not in self.tracked_routes:
            self.tracked_routes.append(route)

    def add_health_note(self, note: str) -> None:
        self.health_notes.append(note)
