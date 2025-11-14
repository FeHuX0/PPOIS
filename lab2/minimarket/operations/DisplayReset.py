from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DisplayReset:
    reset_id: str
    items_adjusted: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def add_item(self, sku: str) -> None:
        if sku not in self.items_adjusted:
            self.items_adjusted.append(sku)

    def add_note(self, note: str) -> None:
        self.notes.append(note)
