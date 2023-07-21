from typing import List
from window import *
from point import Point


def test_get_window_text():
    test_lines: List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: HorizontalWindow = HorizontalWindow(test_grid, 3, start)
    assert(test_window.text == ["a", "b", "c"])

def test_compare_word_same():
    test_lines: List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: HorizontalWindow = HorizontalWindow(test_grid, 3, start)
    print(test_window.text)
    assert(test_window.compare_word_to_window("abc"))