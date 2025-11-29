from __future__ import annotations

from typing import Any, Dict, List

from .Person import Person
from .SimplePancakeSort import SimplePancakeSort
from .Smoothsort import Smoothsort


class SortDemo:
    """Utility class to showcase both sorting algorithms."""

    @staticmethod
    def run() -> Dict[str, Any]:
        numbers = [42, 5, 17, 3, 99, 1]
        words = ["banana", "apple", "cherry", "date"]
        people = [
            Person(name="Alice", age=30, score=4.2),
            Person(name="Bob", age=25, score=3.8),
            Person(name="Charlie", age=28, score=4.7),
        ]

        Smoothsort.sort(numbers)
        SimplePancakeSort.sort(words)

        Smoothsort.sort(people, key=lambda p: (p.age, p.score))

        return {"numbers": numbers, "words": words, "people": people}
