from __future__ import annotations

from typing import Callable, Generic, MutableSequence, Optional, TypeVar


T = TypeVar("T")


class MSDRadixSort(Generic[T]):
    """MSD (Most Significant Digit) Radix Sort implementation.

    Sorts by processing digits/characters from most significant to least significant.
    Works best with strings or integers. Time complexity: O(n * k) where k is the
    maximum number of digits/characters. Space complexity: O(n + k).
    """

    @staticmethod
    def sort(
        data: MutableSequence[T],
        key: Optional[Callable[[T], object]] = None,
        reverse: bool = False,
    ) -> None:
        """Sort data in-place using MSD Radix Sort.

        Args:
            data: Mutable sequence to sort.
            key: Projection function used for comparisons. Should return string or int.
            reverse: Sort descending when True.
        """
        if len(data) < 2:
            return

        key_fn = key or (lambda x: x)

        # Determine if we're sorting strings or integers
        first_val = key_fn(data[0])
        if isinstance(first_val, str):
            MSDRadixSort._sort_strings(data, key_fn, reverse)
        elif isinstance(first_val, int):
            MSDRadixSort._sort_integers(data, key_fn, reverse)
        else:
            # Convert to string for sorting
            MSDRadixSort._sort_strings(data, lambda x: str(key_fn(x)), reverse)

    @staticmethod
    def _sort_strings(
        data: MutableSequence[T],
        key_fn: Callable[[T], str],
        reverse: bool,
    ) -> None:
        """Sort strings using MSD Radix Sort."""
        if not data:
            return

        # Find maximum length
        max_len = max(len(key_fn(item)) for item in data)

        def msd_sort(items: list[T], position: int) -> list[T]:
            """Recursive MSD sort for strings."""
            if position >= max_len or len(items) <= 1:
                return items

            # Create buckets for each character (including empty string for shorter strings)
            buckets: dict[str, list[T]] = {}
            for item in items:
                key_val = key_fn(item)
                if position < len(key_val):
                    char = key_val[position]
                else:
                    char = ""  # Shorter strings go to empty bucket

                if char not in buckets:
                    buckets[char] = []
                buckets[char].append(item)

            # Sort buckets and recursively sort each bucket
            sorted_items: list[T] = []
            sorted_chars = sorted(buckets.keys(), reverse=reverse)

            for char in sorted_chars:
                if len(buckets[char]) > 1:
                    sorted_items.extend(msd_sort(buckets[char], position + 1))
                else:
                    sorted_items.extend(buckets[char])

            return sorted_items

        result = msd_sort(list(data), 0)
        data[:] = result

    @staticmethod
    def _sort_integers(
        data: MutableSequence[T],
        key_fn: Callable[[T], int],
        reverse: bool,
    ) -> None:
        """Sort integers using MSD Radix Sort."""
        if not data:
            return

        # Find maximum absolute value to determine number of digits
        max_val = max(abs(key_fn(item)) for item in data)
        if max_val == 0:
            # All numbers are zero, already sorted
            return

        num_digits = len(str(max_val))

        def get_digit(num: int, position: int) -> int:
            """Get digit at position (0 = least significant, higher = more significant)."""
            # For MSD, we want most significant first
            pos = num_digits - 1 - position
            if pos < 0:
                return 0
            return (abs(num) // (10 ** pos)) % 10

        def msd_sort(items: list[T], position: int, is_negative: bool = False) -> list[T]:
            """Recursive MSD sort for integers.
            
            Args:
                items: Items to sort
                position: Current digit position
                is_negative: Whether we're sorting negative numbers (affects reverse logic)
            """
            if position >= num_digits or len(items) <= 1:
                return items

            # Create buckets for each digit (0-9)
            buckets: list[list[T]] = [[] for _ in range(10)]

            for item in items:
                digit = get_digit(key_fn(item), position)
                buckets[digit].append(item)

            # Combine results
            sorted_items: list[T] = []

            if is_negative:
                # For negative numbers: we sort by absolute value, but need to invert order
                # For reverse=False: we want -5, -3, -1 (low to high by value), so process 9 to 0
                # For reverse=True: we want -1, -3, -5 (high to low by value), so process 0 to 9
                digit_range = range(9, -1, -1) if not reverse else range(10)
                for digit in digit_range:
                    if len(buckets[digit]) > 1:
                        sorted_items.extend(msd_sort(buckets[digit], position + 1, is_negative))
                    else:
                        sorted_items.extend(buckets[digit])
            else:
                # For positive numbers: normal radix sort logic
                # For reverse=False: process 0 to 9 (ascending)
                # For reverse=True: process 9 to 0 (descending)
                digit_range = range(9, -1, -1) if reverse else range(10)
                for digit in digit_range:
                    if len(buckets[digit]) > 1:
                        sorted_items.extend(msd_sort(buckets[digit], position + 1, is_negative))
                    else:
                        sorted_items.extend(buckets[digit])

            return sorted_items

        # Handle negative numbers separately
        negatives: list[T] = []
        positives: list[T] = []

        for item in data:
            val = key_fn(item)
            if val < 0:
                negatives.append(item)
            else:
                positives.append(item)

        # Sort positives and negatives separately
        sorted_positives = msd_sort(positives, 0, is_negative=False) if positives else []
        sorted_negatives = msd_sort(negatives, 0, is_negative=True) if negatives else []

        # Combine results
        if reverse:
            # Descending: positives first (high to low), then negatives (high to low by value: -1, -3, -5)
            result = sorted_positives + sorted_negatives
        else:
            # Ascending: negatives first (low to high: -5, -3, -1), then positives (low to high)
            result = sorted_negatives + sorted_positives

        data[:] = result

