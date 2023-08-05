from rk_hash import *
from word_bank import WordBank
from point import Point
from word_grid import WordGrid
from window import Window
from direction import Direction
from typing import List
from word import Word

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

def test_both_hash_functions_equal():
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
    assert(get_hash_letter_list(test_window.text) == get_hash_string("ABC"))

def test_hash_value():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 5, start, Direction.Horizontal, bank)
    assert(get_hash_letter_list(test_window.text) == 95)

def test_correct_hash_value_stored_in_window():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 5, start, Direction.Horizontal, bank)
    assert(test_window.hash_value == 95)

def test_word_hash():
    test_word: Word = Word("RUST")
    assert(test_word.front_hash == 71)

def test_reverse_word_hash():
    test_word: Word = Word("RUST")
    assert(test_word.rev_hash == 68)

def test_rehash():
    string_a: str = "ABCD"
    string_b: str = "BCDE"
    hash_a: int = get_hash_string(string_a)
    hash_b: int = get_hash_string(string_b)
    hash_scale: int = get_hash_scale(4)
    hash_c: int = rehash(hash_a, 'E', 'A', hash_scale)
    assert(hash_b == hash_c)