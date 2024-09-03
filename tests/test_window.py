import sys
sys.path.insert(0, "../src")
from typing import List
from window import *
from point import Point
import pytest
from word_bank import WordBank

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
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    assert(compare_lists(test_window.text, ["A", "B", "C"]))

def test_compare_word_same():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    print(test_window.text)
    assert(test_window.compare_word_to_window("ABC"))

def test_window_iteration():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    for _ in test_window:
        print(test_window.text)

def test_throws_small_exception_horizontal():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code"]
    bank = WordBank(test_list)
    with pytest.raises(WindowTooSmall):
        test_window: Window = Window(test_grid, 6, start, Direction.Horizontal, bank)

def test_no_exception_horizontal():
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
    assert(True)

def test_window_get_text():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code"]
    bank = WordBank(test_list)
    test_window: Window = Window(test_grid, 4, start, Direction.Horizontal, bank)
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
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    test_window.slide_window()
    assert(test_window.compare_word_to_window("BCD"))

def test_slide_window_raises_exception():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    print("Last Test:")
    print(test_window.text)
    test_window.slide_window()
    test_window.slide_window()
    print(test_window.text)
    with pytest.raises(StopIteration):
        test_window.slide_window()

def test_str_method():
    test_lines: List[str] = [
        "abcde",
        "fghij",
        "klmno"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 0)
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "GUI"]
    bank = WordBank(test_list)
    test_window = Window(test_grid, 3, start, Direction.Horizontal, bank)
    assert(test_window.__str__() == "[A, B, C]")

def test_search_window_finds_java():
    test_lines: List[str] = [
        "BBDEHEYNVCPPGXSIDOGF",
        "JDKAFRXQFGKRDCYVVHVU",
        "ETSDQDKJAVASHMBWXETY",
        "MZHKJSUBCSHARPEGWMNP",
        "HBGFPGCGWCCJJQEGCQJB",
        "EPBFQSVSCOZQTKWVWFNK",
        "EPEGPHLURDUZUUJHYLZD",
        "IDDAAHKOVERDDEVXVGEE",
        "MBJCRGSLQIDXLFEYTGNK",
        "IWNKEZNWQWXRKTRGDTRP",
        "DZGFPYTHONDPIINVAXSX",
        "ZEOSKPXFSFJRPVUXPQXP",
        "NAYGCLAGFXTORUSTEGZZ",
        "PZSHWYHASJTIOALSDHOX",
        "TDTOGVZTCAERPELEDLPX",
        "ZKJZABWVXEFLXMWUBJGN",
        "ZAECAQPXQOKHSDTXGSGE",
        "RVOPMQZLAURPJHGJCNAL",
        "QTJTFEXKDJTXYDVCVVAB",
        "MXVQCXESQNDRJSRTFETL"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 2)
    test_list: List[str] = ["CSHARP", "JAVA", "VSCODE", "SWIFT", "REACT", "ANGULAR", "RUST", "PYTHON"]
    bank: WordBank = WordBank(test_list)
    test_window = Window(test_grid, 4, start, Direction.Horizontal, bank)
    test_window.check_word_list()
    for _ in test_window:
        pass
    assert(bank.get_word("JAVA").is_found == True)

def test_search_window_marks_grid():
    test_lines: List[str] = [
        "BBDEHEYNVCPPGXSIDOGF",
        "JDKAFRXQFGKRDCYVVHVU",
        "ETSDQDKJAVASHMBWXETY",
        "MZHKJSUBCSHARPEGWMNP",
        "HBGFPGCGWCCJJQEGCQJB",
        "EPBFQSVSCOZQTKWVWFNK",
        "EPEGPHLURDUZUUJHYLZD",
        "IDDAAHKOVERDDEVXVGEE",
        "MBJCRGSLQIDXLFEYTGNK",
        "IWNKEZNWQWXRKTRGDTRP",
        "DZGFPYTHONDPIINVAXSX",
        "ZEOSKPXFSFJRPVUXPQXP",
        "NAYGCLAGFXTORUSTEGZZ",
        "PZSHWYHASJTIOALSDHOX",
        "TDTOGVZTCAERPELEDLPX",
        "ZKJZABWVXEFLXMWUBJGN",
        "ZAECAQPXQOKHSDTXGSGE",
        "RVOPMQZLAURPJHGJCNAL",
        "QTJTFEXKDJTXYDVCVVAB",
        "MXVQCXESQNDRJSRTFETL"
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start: Point = Point(0, 2)
    test_list: List[str] = ["CSHARP", "JAVA", "VSCODE", "SWIFT", "REACT", "ANGULAR", "RUST", "PYTHON"]
    bank: WordBank = WordBank(test_list)
    test_window = Window(test_grid, 4, start, Direction.Horizontal, bank)
    test_window.check_word_list()
    for _ in test_window:
        pass
    java_locations: List[Point] = [Point(7, 2), Point(8, 2), Point(9, 2), Point(10, 2)]
    print(test_grid.display_found_letters())