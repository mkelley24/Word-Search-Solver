from typing import List
from rk_hash import get_hash


class Word:

    def __init__(self, new_word: str):
        self.text: str = new_word.upper()
        if self.text.isupper() == False:
            raise ValueError
        self.is_found: bool = False
        self.length: int = len(self.text)
        self.rev_text: str = self.reverse_string(self.text)
        self.front_hash: int = get_hash(self.text)
        self.rev_hash: int = get_hash(self.rev_text)

    def is_equal(self, window_text: str) -> bool:
        if self.text == window_text or self.rev_text == window_text:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return "Word(\"{}\")".format(self.text)
    
    def __str__(self) -> str:
        return self.text
    
    def reverse_string(self, text: str) -> str:
        output: str = ""
        for letter in text:
            output = letter + output
        return output
    
    def found(self) -> None:
        self.is_found = True