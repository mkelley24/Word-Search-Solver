from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash, rehash
from word import Word
from typing import List


class Window(ABC):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.size = size
        self.current_position: Point = start
        self.board: WordGrid = board
        self.text: List[str] = self._get_window_text(start)
        self.hash_value: int = get_hash(self.text)
        # self.point_shift: Point = Point(0, 0)

    @abstractmethod
    def _get_window_text(self, start: Point) -> str:
        pass


class HorizontalWindow(Window):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.point_shift = Point(1, 0)
        super().__init__(board, size, start)

    def _get_window_text(self, start: Point) -> str:
        counter = 0
        window_text: List[str] = []
        while self.board.valid_point(start) and counter < self.size:
            window_text.append(self.board.get_letter(start))
            start.move_point(self.point_shift)
            counter += 1
        return window_text
    
    def slide_window(self):
        pass