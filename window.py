from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash
from word import Word
from typing import List


class Window(ABC):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.size = size
        self.board: WordGrid = grid
        self.text: str = self._get_window_text(start)
        self.hash_value = get_hash(self.text)
        self.col_incrementer = 0
        self.row_incrementer = 0

    @abstractmethod
    def _get_window_text(self, start: Point) -> str:
        pass


class HorizontalWindow(Window):

    def __init__(self, board: WordGrid, size: int):
        super().__init__(board, size)
        self.col_incrementer = 0
        self.col_incrementer = 1

    def _get_window_text(self, start: Point) -> str:
        i: int = start.y
        j: int = start.x
        counter = 0
        letter_list: List[str] = []
        while self.board.valid_point(i, j) and counter < self.size:
            letter_list.append(self.board.grid[i, j])
        return letter_list.collect()