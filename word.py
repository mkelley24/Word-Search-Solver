from typing import List
class Word:
    def __init__(self, new_word: str):
        self.text: str = new_word
        self.isFound: bool = False
        self.length: int = len(self.text)
        self.rev_text: str = new_word.reverse()