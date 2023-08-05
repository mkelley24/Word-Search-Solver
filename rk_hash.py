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
    return (ALPHABET_SIZE * hash + letter_to_number(letter[0])) % PRIME

def get_hash_string(input: str) -> int:
    hash: int = 0
    for i in range(len(input)):
        letter: str = input[i]
        hash = letter_calculation(hash, letter)
    return hash

def get_hash_scale(length: int) -> int:
    ALPHABET_SIZE: int = 26
    return ALPHABET_SIZE ** (length - 1)


def rehash(old_hash: int, new_char: str, old_char: str, hash_scale: int) -> int:
    ALPHABET_SIZE: int = 26
    PRIME: int = 97
    old_hash -= letter_to_number(old_char[0]) * hash_scale
    old_hash *= ALPHABET_SIZE
    old_hash += letter_to_number(new_char[0])
    return old_hash % PRIME

def letter_to_number(char: str) -> int:
    ASCII_DIFFERENCE: int = 65
    return ord(char[0]) - ASCII_DIFFERENCE