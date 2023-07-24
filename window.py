from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash, rehash
from word import Word
from typing import List
from letter import Letter


class Window(ABC):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.size = size
        self.current_position: Point = start
        self.board: WordGrid = board
        self.text: List[Letter] = self._get_window_text(start)
        self.hash_value: int = get_hash(self.text)
        # self.point_shift: Point = Point(0, 0)

    def _get_window_text(self, start: Point) -> str:
        counter = 0
        window_text: List[str] = []
        while self.board.valid_point(start) and counter < self.size:
            window_text.append(self.board.get_letter(start))
            start.move_point(self.point_shift)
            counter += 1
        return window_text
    
    @abstractmethod
    def slide_window(self):
        pass

    def compare_word_to_window(self, plain_text: str) -> bool:
        if len(plain_text) != len(self.text):
            return False
        for i in range(self.size):
            if plain_text[i] != self.text[i].letter_value:
                return False
        return True

    def compare_hash_to_window(self, word: Word):
        word_present: bool = False
        if word.front_hash == self.hash_value:
            word_present = self.compare_word_to_window(word.text)
        elif word.rev_hash == self.hash_value:
            word_present = self.compare_word_to_window(word.rev_text)
        else:
            pass
        word.isFound = word_present



class HorizontalWindow(Window):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.point_shift = Point(1, 0)
        super().__init__(board, size, start)
        