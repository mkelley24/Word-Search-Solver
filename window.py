from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash
from word import Word


class Window(ABC):

    def __init__(self, grid: WordGrid, size: int, start: Point):
        self.size = size
        self.grid: WordGrid = grid
        self.text: str = self._get_window_text(start)
        self.hash_value = get_hash(self.text)

    @abstractmethod
    def _get_window_text(self, start: Point) -> str:
        pass


class Horizontal_Window(Window):

    def __init__(self, grid: WordGrid, size: int):
        super().__init__(grid, size)

    def _get_window_text(self, start: Point) -> str:
