from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CustomerFeedback:
    feedback_id: str
    customer_name: str
    rating: int
    comment: str
    tags: set[str] = field(default_factory=set)

    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)
