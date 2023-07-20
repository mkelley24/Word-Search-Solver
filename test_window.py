from window import *
from point import Point
from typing import List

def test_get_window_text():
    pass
    test_lines:List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: HorizontalWindow = HorizontalWindow(test_grid, 3, start)
    assert(test_window.text == "abc")

