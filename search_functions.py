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

def search_line(board: WordGrid, bank: WordBank, size: int, direction: Direction, start: Point) -> None:
    try:
        sliding_window: Window = Window(board, size, start, direction, bank)
        for _ in sliding_window:
            pass
    except WindowTooSmall:
        raise WindowTooSmall

def search_direction(board: WordGrid, bank: WordBank, size: int, direction: Direction) -> None:
    head: Point = Point(0, 0)
    head_shift: Point = Direction.get_head_shift(direction)
    while board.valid_point(head):
        try:
            search_line(board, bank, size, direction, head)
            print("{}: {}: {}".format(size, head, direction))
        except WindowTooSmall:
            head.move_point(head_shift)
            continue
        head.move_point(head_shift)

def search_words_of_size(board: WordGrid, bank: WordBank, size: int) -> None:
    for direction in Direction:
        search_direction(board, bank, size, direction)

def search_for_words(board: WordGrid, bank: WordBank) -> None:
    size_list: List[int] = bank.get_key_list()
    for size in size_list:
        search_words_of_size(board, bank, size)