from typing import List
from word import Word
from typing import Dict

class WordBank:
    def __init__(self, word_list: List[str]):
        self.word_dict: Dict[int, List[Word]] = {}
        for new_word in word_list:
            if len(new_word) in self.word_dict:
                self.word_dict[len(new_word)].append(Word(new_word))
            else:
                self.word_dict[len(new_word)] = [Word(new_word)]

    def get_word_list(self, word_size: int) -> List[Word]:
        return self.word_dict[word_size]
    
    def __str__(self) -> str:
        return str(self.word_dict)
    
    def get_key_list(self) -> List[int]:
        return self.word_dict.keys()

    def get_words_of_size(self, size: int) -> List[Word]:
        return self.word_dict[size]