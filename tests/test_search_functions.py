import sys
sys.path.insert(0, "../src")
from window import Window
from word import Word
from word_grid import WordGrid
from word_bank import WordBank
from letter import Letter
from point import Point
from rk_hash import *
from direction import Direction
from typing import List
from custom_exceptions import *
from search_functions import *

def test_overall_search_on_grid():
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
    search_for_words(test_grid, bank)
    # print(test_grid.display_found_letters())

def test_directional_search():
    test_lines: List[str] = [
        "BBDEHEYNVCPPGXSIDOGF",
        "JDKAFRXQFGKRDCYVVHVU",
        "ETSDQDKJAVASHMBWXETY",
        "MZHKJSUBCSHARPEGWMNP",
        "HBGFPGCGWCCJJQEGCQJB",
        "EPBFQSVSCOZQTKWVWFNK",
        "EPEGPHLURDUZUUJHYLZD",
        "IDDAAHKOVERDDEVXVGEE",
        "GBJCRGSLQIDXLFEYTGNK",
        "IUNKEZNWQWXRKTRGDTRP",
        "DZIFPYTHONDPIINVAXSX",
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
    test_list: List[str] = ["CSHARP", "JAVA", "VSCODE", "SWIFT", "REACT", "ANGULAR", "RUST", "PYTHON", "GUI"]
    bank: WordBank = WordBank(test_list)
    search_for_words(test_grid, bank)
    # print(test_grid.display_found_letters())