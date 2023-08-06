from word_grid import WordGrid
from point import Point
from rk_hash import *
from word import Word
from typing import List
from letter import Letter
from custom_exceptions import WindowTooSmall
from direction import Direction
from word_bank import WordBank


class Window():

    def __init__(self, board: WordGrid, size: int, start: Point, direction: Direction, word_bank: WordBank):
        self.size: int = size
        self.head: Point = start
        try:
            self.point_shift: Point = Direction.get_shift_point(direction)
        except ValueError:
            raise ValueError
        self.board: WordGrid = board
        try:
            self.text: List[Letter] = self._get_window_text()
        except WindowTooSmall:
            raise WindowTooSmall
        self.hash_value: int = get_hash_letter_list(self.text)
        self.hash_scale = get_hash_scale(self.size)
        self.word_list: List[Word] = word_bank.get_words_of_size(self.size)

    def __str__(self):
        output: str = "["
        if len(self.text) > 0:
            output += self.text[0].letter_value
        i: int = 1
        while i < len(self.text):
            output += ", "
            output += self.text[i].letter_value
            i += 1
        output += "]"
        return output
    
    def _get_window_text(self) -> List[str]:
        counter = 0
        if self.board.valid_point(self.head) == False:
            raise WindowTooSmall
        elif self.board.valid_point(self.head.span(self.point_shift, self.size - 1)) == False:
            raise WindowTooSmall
        else:
            window_text: List[Letter] = []
            position: Point = self.head.copy_point()
            for _ in range(self.size):
                window_text.append(self.board.get_letter(position))
                position.move_point(self.point_shift)
            return window_text
        
    def check_word_list(self):
        pass
        

    def compare_word_to_window(self, plain_text: str) -> bool:
        if len(plain_text) != len(self.text):
            return False
        for i in range(self.size):
            if plain_text[i] != self.text[i].letter_value:
                return False
        return True

    def compare_hash_to_window(self, word: Word) -> None:
        word_present: bool = False
        if word.front_hash == self.hash_value:
            word_present = self.compare_word_to_window(word.text)
        elif word.rev_hash == self.hash_value:
            word_present = self.compare_word_to_window(word.rev_text)
        else:
            pass
        if word_present == True:
            word.is_found = True
        else:
            return

    def __iter__(self):
        return self
    
    def __next__(self):
        next_point: Point = self.head.span(self.point_shift, self.size)
        if self.board.valid_point(next_point) == False:
            raise StopIteration
        else:
            new_letter: Letter = self.board.get_letter(next_point)
            self.hash_value = rehash(self.hash_value, new_letter.letter_value, self.text[0].letter_value, self.hash_scale)
            self.text.pop(0)
            self.text.append(new_letter)
            self.head = self.head + self.point_shift

    def slide_window(self):
        next_point: Point = self.head.span(self.point_shift, self.size)
        if self.board.valid_point(next_point) == False:
            raise StopIteration
        else:
            new_letter: Letter = self.board.get_letter(next_point)
            self.hash_value = rehash(self.hash_value, new_letter.letter_value, self.text[0].letter_value, self.hash_scale)
            self.text.pop(0)
            self.text.append(new_letter)
            self.head = self.head + self.point_shift