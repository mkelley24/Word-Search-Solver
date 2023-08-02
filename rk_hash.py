from typing import List
from letter import Letter

def get_hash_letter_list(input: List[Letter]) -> int:
    hash: int = 0
    for letter in input:
        hash = letter_calculation(hash, letter.letter_value)
    return hash

def letter_calculation(hash: int, letter: str):
    ALPHABET_SIZE: int = 26
    PRIME: int = 97
    ASCII_DIFFERENCE: int = 65
    return (ALPHABET_SIZE * hash + (ord(letter[0]) - ASCII_DIFFERENCE)) % PRIME

def get_hash_string(input: str) -> int:
    hash: int = 0
    for letter in input:
        hash = letter_calculation(hash, letter)
    return hash

def rehash(hash: int, new_char: str, old_char: str) -> int:
    return hash