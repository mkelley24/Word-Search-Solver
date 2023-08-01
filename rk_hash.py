from typing import List
from letter import Letter

def get_hash_letter_list(input: List[Letter]) -> int:
    ALPHABET_SIZE: int = 256
    PRIME: int = 101
    ASCII_DIFFERENCE: int = 65
    hash: int = 0
    for letter in List:
        hash %= PRIME
        # hash += (ord(letter.letter_value) - ASCII_DIFFERENCE)
        hash += ord(letter.letter_value)
        hash *= ALPHABET_SIZE
    return hash

def get_hash_string(input: str) -> int:
    ALPHABET_SIZE: int = 26
    PRIME: int = 29
    ASCII_DIFFERENCE: int = 65
    hash: int = 0
    for letter in input:
        hash %= PRIME
        hash += (ord(letter.letter_value) - ASCII_DIFFERENCE)
        hash *= ALPHABET_SIZE
        print(hash)
    return hash % PRIME

def rehash(hash: int, new_char: str, old_char: str) -> int:
    return hash