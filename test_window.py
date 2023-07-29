from typing import List
from window import *
from point import Point
import pytest

def compare_lists(letter_list, string_list):
        if len(letter_list) != len(string_list):
            return False
        else:
            for i in range(len(letter_list)):
                if letter_list[i].letter_value != string_list[i]:
                    return False
            return True

def test_get_window_text():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal)
    assert(compare_lists(test_window.text, ["a", "b", "c"]))

def test_compare_word_same():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal)
    print(test_window.text)
    assert(test_window.compare_word_to_window("abc"))

# def test_window_iteration():
#     test_lines: List[List[str]] = [
#         ["a", "b", "c", "d", "e", "x", "y", "z", "q"],
#         ["f", "g", "h", "i", "j", "p", "q", "r", "w"],
#         ["k", "l", "m", "n", "o", "s", "t", "u", "e"]
#     ]
#     test_grid: WordGrid = WordGrid(test_lines)
#     start: Point = Point(0, 0)
#     test_window: Window = Window(test_grid, 3, start, Direction.Horizontal)
#     sample_point: Point = start.span(Point(1, 0), 4)
#     print(repr(test_window.current_position))
#     print(repr(sample_point))
#     my_iter = test_window.__iter__()
#     my_iter.__next__()
#     print(test_window.text)
#     assert(test_window.compare_word_to_window("bcd"))

def test_throws_small_exception_horizontal():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    with pytest.raises(WindowTooSmall):
        test_window: Window = Window(test_grid, 6, start, Direction.Horizontal)

def test_no_exception_horizontal():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_window: Window = Window(test_grid, 5, start, Direction.Horizontal)
    assert(True)

def test_window_get_text():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_window: Window = Window(test_grid, 4, start, Direction.Horizontal)
    print("New Test: ")
    print(test_window.text)

def test_one_slide_horizontal():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_window = Window(test_grid, 3, start, Direction.Horizontal)
    test_window.slide_window()
    assert(test_window.compare_word_to_window("bcd"))

def test_slide_window_raises_exception():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_window = Window(test_grid, 3, start, Direction.Horizontal)
    test_window.slide_window()
    test_window.slide_window()
    with pytest.raises(StopIteration):
        test_window.slide_window()