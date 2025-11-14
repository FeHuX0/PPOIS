from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LossPreventionCase:
    case_id: str
    items_missing: dict[str, int] = field(default_factory=dict)
    status: str = "open"
    incident_notes: list[str] = field(default_factory=list)

    def add_item(self, sku: str, quantity: int) -> None:
        self.items_missing[sku] = self.items_missing.get(sku, 0) + quantity

    def add_note(self, note: str) -> None:
        self.incident_notes.append(note)

    def close(self) -> None:
        self.status = "closed"
