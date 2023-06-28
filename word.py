from typing import List


class Word:

    def __init__(self, new_word: str):
        self.text: str = new_word
        self.isFound: bool = False
        self.length: int = len(self.text)
        self.rev_text: str = new_word.reverse()
        self.front_hash: int = 0
        self.rev_hash: int = 0

    def is_equal(self, window_text: str):
        if self.text == window_text or self.rev_text == window_text:
            return True
        else:
            return False
