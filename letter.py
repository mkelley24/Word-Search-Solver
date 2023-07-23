from tkinter import *

class Letter:

    def __init__(self, letter_input: str) -> None:
        self.letter_value: str = letter_input
        self.word_section = False

    def set_found(self) -> None:
        self.letter_value = True