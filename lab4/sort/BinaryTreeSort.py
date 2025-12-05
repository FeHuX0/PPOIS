from __future__ import annotations

from typing import Callable, Generic, MutableSequence, Optional, TypeVar


T = TypeVar("T")


class TreeNode(Generic[T]):
    """Binary tree node for tree sort."""

    def __init__(self, value: T) -> None:
        self.value = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None


class BinaryTreeSort(Generic[T]):
    """Binary tree sort implementation.

    Builds a binary search tree from the input, then performs in-order traversal
    to get sorted elements. Time complexity: O(n log n) average, O(n²) worst case.
    Space complexity: O(n).
    """

    @staticmethod
    def sort(
        data: MutableSequence[T],
        key: Optional[Callable[[T], object]] = None,
        reverse: bool = False,
    ) -> None:
        """Sort data in-place using binary tree sort.

        Args:
            data: Mutable sequence to sort.
            key: Projection function used for comparisons.
            reverse: Sort descending when True.
        """
        if len(data) < 2:
            return

        key_fn = key or (lambda x: x)

        def compare(left: T, right: T) -> int:
            """Compare two values. Returns -1 if left < right, 0 if equal, 1 if left > right."""
            left_val = key_fn(left)
            right_val = key_fn(right)
            if left_val < right_val:
                return -1
            if left_val > right_val:
                return 1
            return 0

        # Build binary search tree
        root: Optional[TreeNode[T]] = None
        for value in data:
            root = BinaryTreeSort._insert(root, value, compare)

        # In-order traversal to collect sorted values
        result: list[T] = []
        BinaryTreeSort._inorder_traversal(root, result, reverse)

        # Update original sequence
        data[:] = result

    @staticmethod
    def _insert(
        node: Optional[TreeNode[T]], value: T, compare: Callable[[T, T], int]
    ) -> TreeNode[T]:
        """Insert a value into the binary search tree."""
        if node is None:
            return TreeNode(value)

        cmp_result = compare(value, node.value)
        if cmp_result < 0:
            node.left = BinaryTreeSort._insert(node.left, value, compare)
        else:
            node.right = BinaryTreeSort._insert(node.right, value, compare)

        return node

    @staticmethod
    def _inorder_traversal(
        node: Optional[TreeNode[T]], result: list[T], reverse: bool
    ) -> None:
        """Perform in-order traversal and append values to result."""
        if node is None:
            return

        if reverse:
            # Right, root, left for descending order
            BinaryTreeSort._inorder_traversal(node.right, result, reverse)
            result.append(node.value)
            BinaryTreeSort._inorder_traversal(node.left, result, reverse)
        else:
            # Left, root, right for ascending order
            BinaryTreeSort._inorder_traversal(node.left, result, reverse)
            result.append(node.value)
            BinaryTreeSort._inorder_traversal(node.right, result, reverse)

