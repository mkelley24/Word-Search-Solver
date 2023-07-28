from word_grid import WordGrid
from abc import ABC, abstractmethod
from point import Point
from rk_hash import get_hash, rehash
from word import Word
from typing import List
from letter import Letter
from custom_exceptions import WindowTooSmall
from direction import Direction


class Window():

    def __init__(self, board: WordGrid, size: int, start: Point, direction: Direction):
        self.size: int = size
        self.head: Point = start
        self.point_shift: Point = Direction.get_shift_point(direction)
        self.head_shift: Point = Direction.get_head_shift(direction)
        self.current_position: Point = start
        self.board: WordGrid = board
        try:
            self.text: List[Letter] = self._get_window_text()
        except WindowTooSmall:
            raise WindowTooSmall
        self.hash_value: int = get_hash(self.text)

    def _get_window_text(self) -> str:
        counter = 0
        if self.board.valid_point(self.head) == False:
            raise WindowTooSmall
        while self.board.valid_point(self.head.span(self.point_shift, self.size)) == False:
            if self.board.valid_point(self.head + self.head_shift) == False:
                raise WindowTooSmall
            else:
                self.head_shift.move_point(self.head_shift)
        window_text: List[Letter] = []
        while self.board.valid_point(self.head) and counter < self.size:
            window_text.append(self.board.get_letter(self.head))
            self.head.move_point(self.point_shift)
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
            self.text.append(new_letter)
            self.current_position = self.current_position + self.point_shift