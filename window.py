from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash, rehash
from word import Word
from typing import List
from letter import Letter
from custom_exceptions import WindowTooSmall


class Window(ABC):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.size = size
        self.current_position: Point = start
        self.board: WordGrid = board
        self.text: List[Letter] = self._get_window_text(start)
        self.hash_value: int = get_hash(self.text)

    def _get_window_text(self, start: Point) -> str:
        counter = 0
        window_text: List[str] = []
        while self.board.valid_point(start) and counter < self.size:
            window_text.append(self.board.get_letter(start))
            start.move_point(self.point_shift)
            counter += 1
        return window_text
    
    # @abstractmethod
    # def slide_window(self):
    #     pass

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
        if self.board.valid_point(start.span(self.point_shift, self.size)) == False:
            raise WindowTooSmall
        
    def __iter__(self):
        return self
    
    def __next__(self):
        next_point: Point = self.current_position.span(self.point_shift, self.size)
        if self.board.valid_point(next_point) == False:
            raise StopIteration
        else:
            new_letter: Letter = self.board.get_letter(next_point)
            self.hash_value = rehash(self.hash_value, new_letter.letter_value, self.text[0].letter_value)
            self.text.pop(0)
            self.text.push(new_letter)
            self.current_position = self.current_position + self.point_shift

    # def slide_window(self):
    #     first_char: Letter = self.text[0]
    #     self.text.pop(0)


class VerticalWindow(Window):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.point_shift = Point(0, 1)
        super().__init__(board, size, start)
        if self.board.valid_point(start.span(self.point_shift, self.size)):
            raise WindowTooSmall

    # def slide_window(self):
    #     pass

class LeftDiagonalWindow(Window):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.point_shift = Point(1, 1)
        super().__init__(board, size, start)
        if self.board.valid_point(start.span(self.point_shift, self.size)):
            raise WindowTooSmall

    # def slide_window(self):
    #     pass

class RightDiagonalWindow(Window):

    def __init__(self, board: WordGrid, size: int, start: Point):
        self.point_shift = Point(-1, 1)
        super().__init__(board, size, start)
        if self.board.valid_point(start.span(self.point_shift, self.size)):
            raise WindowTooSmall

    # def slide_window(self):
    #     pass
        