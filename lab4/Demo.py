from __future__ import annotations

from graph.GraphDemo import GraphDemo
from sort.SortDemo import SortDemo


class Demo:
    """Convenience runner to showcase both lab parts."""

    @staticmethod
    def run() -> None:
        sort_result = SortDemo.run()
        graph_result = GraphDemo.run()

        print("Smoothsort / Pancake sort demo:", sort_result)
        print("Graph demo:", graph_result)


if __name__ == "__main__":
    Demo.run()
