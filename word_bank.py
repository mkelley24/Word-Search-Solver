from typing import List
from word import Word

class WordBank:
    def __init__(self, line: str):
        self.words = line.split()
        myWord = Word("spam")
