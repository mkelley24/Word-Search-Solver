from rk_hash import *
from word_bank import WordBank
from point import Point
from word_grid import WordGrid

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