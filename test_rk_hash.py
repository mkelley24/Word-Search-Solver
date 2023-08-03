from rk_hash import *
from word_bank import WordBank
from point import Point
from word_grid import WordGrid
from window import Window
from direction import Direction
from typing import List

def test_list_hash():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    print(get_hash_letter_list(test_window.text))