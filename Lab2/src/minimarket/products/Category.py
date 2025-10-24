from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Category:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def do_action(self) -> None:
        self.meta['acted'] = True

    def describe(self) -> str:
        return f'{self.__class__.__name__}({getattr(self,'id',getattr(self,'name',''))})'
