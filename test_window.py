from typing import List
from window import *
from point import Point

def compare_lists(letter_list, string_list):
        if len(letter_list) != len(string_list):
            return False
        else:
            for i in range(len(letter_list)):
                if letter_list[i].letter_value != string_list[i]:
                    return False
            return True

def test_get_window_text():
    test_lines: List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: HorizontalWindow = HorizontalWindow(test_grid, 3, start)
    assert(compare_lists(test_window.text, ["a", "b", "c"]))

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

def test_window_iteration():
    test_lines: List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: HorizontalWindow = HorizontalWindow(test_grid, 3, start)
    sample_point: Point = start.span(Point(1, 0), 4)
    print(repr(sample_point))
    my_iter = test_window.__iter__()
    my_iter.__next__()
    assert(test_window.compare_word_to_window("bcd"))