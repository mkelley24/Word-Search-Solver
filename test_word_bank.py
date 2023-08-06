from word_bank import WordBank
from typing import List

def test_word_bak_str():
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "pycharm"]
    bank = WordBank(test_list)
    # print(bank)
    assert(True)

def test_sizes_list():
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "pycharm"]
    bank = WordBank(test_list)
    print(bank.get_key_list())

def test_sizes_list():
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "pycharm"]
    bank = WordBank(test_list)
    print(bank.get_words_of_size(4))

def test_get_word():
    test_list: List[str] = ["Python", "Rust", "Swift", "Java", "Code", "pycharm"]
    bank = WordBank(test_list)
    print(bank.get_word("JAVA"))