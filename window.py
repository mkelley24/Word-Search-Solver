from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash, rehash
from word import Word
from typing import List


class Window(ABC):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.size = size
        self.board: WordGrid = board
        self.text: str = self._get_window_text(start)
        self.hash_value: int = get_hash(self.text)
        self.point_shift: Point = Point(0, 0)

    @abstractmethod
    def _get_window_text(self, start: Point) -> str:
        pass


class HorizontalWindow(Window):

    def __init__(self, board: WordGrid, size: int):
        super().__init__(board, size)
        self.point_shift = Point(1, 0)

    def _get_window_text(self, start: Point) -> str:
        counter = 0
        window_text: str = ""
        while self.board.valid_point(i, j) and counter < self.size:
            window_text += self.board.grid[i][j]
        return window_text