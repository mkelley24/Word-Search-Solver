from tkinter import *

class Letter:

    def __init__(self, letter_input: str) -> None:
        self.letter_value: str = letter_input
        self.word_section = False

    def set_found(self) -> None:
        self.letter_value = True

    def __repr__(self):
        return "Letter(letter_value= {}, word_section= {})".format(self.letter_value, self.word_section)