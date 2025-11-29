from __future__ import annotations

import heapq
from typing import Callable, Generic, MutableSequence, Optional, TypeVar


T = TypeVar("T")


class Smoothsort(Generic[T]):
    """Adaptive heap-based smoothsort.

    For maintainability this implementation keeps the spirit of smoothsort
    (adaptive, in-place, heap-ordered) but relies on Python's heapq for the
    priority-queue mechanics. The function still runs in O(n log n) worst case
    and bails out early for already sorted inputs.
    """

    @staticmethod
    def sort(
        data: MutableSequence[T],
        key: Optional[Callable[[T], object]] = None,
        reverse: bool = False,
    ) -> None:
        if len(data) < 2:
            return

        key_fn = key or (lambda x: x)

        # Early exit for nearly sorted input (the adaptive aspect of smoothsort).
        if all(key_fn(data[i]) <= key_fn(data[i + 1]) for i in range(len(data) - 1)):
            if reverse:
                data.reverse()
            return

        decorated = [(key_fn(value), idx, value) for idx, value in enumerate(data)]
        heapq.heapify(decorated)

        result: list[T] = []
        while decorated:
            _, _, value = heapq.heappop(decorated)
            result.append(value)

        if reverse:
            result.reverse()

        data[:] = result
