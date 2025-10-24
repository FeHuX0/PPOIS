from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Store:
    store_id: str = ''
    name: str = ''
    location: str = ''

    def open(self) -> None:
        self.opened = True

    def close(self) -> None:
        self.opened = False

    def register_vendor(self, vendor: 'Vendor') -> None:
        self.vendor = vendor
