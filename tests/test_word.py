import sys
sys.path.insert(0, "../src")
from word import Word

def test_word_constructor():
    test_word: Word = Word("Hello")

def test_reverse_string():
    test_word: Word = Word("Hello")
    test_word.rev_text == "OLLEH"