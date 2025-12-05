from __future__ import annotations

from typing import Callable, Generic, MutableSequence, Optional, TypeVar


T = TypeVar("T")


class SimplePancakeSort(Generic[T]):
    """Straightforward pancake sort with optional key/reverse parameters."""

    @staticmethod
    def sort(
        data: MutableSequence[T],
        key: Optional[Callable[[T], object]] = None,
        reverse: bool = False,
    ) -> None:
        """Sort ``data`` in-place using pancake flips.

        Args:
            data: Mutable sequence to sort.
            key: Projection function used for comparisons.
            reverse: Sort descending when True.
        """
        if len(data) < 2:
            return

        key_fn = key or (lambda x: x)

        def should_swap(left: T, right: T) -> bool:
            if reverse:
                return key_fn(left) < key_fn(right)
            return key_fn(left) > key_fn(right)

        def flip(k: int) -> None:
            data[:k] = reversed(data[:k])

        for curr_size in range(len(data), 1, -1):
            max_idx = 0
            for i in range(1, curr_size):
                if should_swap(data[i], data[max_idx]):
                    max_idx = i
            if max_idx == curr_size - 1:
                continue
            if max_idx != 0:
                flip(max_idx + 1)
            flip(curr_size)
