from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Reward:
    name: str
    cost_points: int
    description: str = ""
