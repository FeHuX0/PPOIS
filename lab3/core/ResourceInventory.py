from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResourceInventory:
    inventory_id: str
    region: Region
    water_sources: list[str] = field(default_factory=list)
    plant_resources: list[str] = field(default_factory=list)
    mineral_resources: list[str] = field(default_factory=list)

    def add_water_source(self, name: str) -> None:
        if name not in self.water_sources:
            self.water_sources.append(name)

    def list_resources(self) -> list[str]:
        return self.water_sources + self.plant_resources + self.mineral_resources
