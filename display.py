import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from word_grid import WordGrid
from letter import Letter
from typing import List
from word_bank import WordBank
from search_functions import *

root = tk.Tk()

canvas = tk.Canvas(root, width=1200, height=600)
canvas.grid(columnspan=30, rowspan=30)

def open_file():
    STARTING_ROW: int = 4
    STARTING_COL: int = 4
    file = askopenfile(parent=root, mode='r', title="Choose a file", filetype=[("Text file", "*.txt")])
    found_semicolon: bool = False
    letter_lines: List[str] = []
    input_lines: List[str] = []
    word_bank_line: str = ""
    divider: int = 0
    if file:
        for line in file.readlines():
            if line[-1] == '\n':
                input_lines.append(line[:len(line) - 1])
            else:
                input_lines.append(line)
        if input_lines[-2][0] != "#":
            raise ValueError
        else:
            word_bank_line = input_lines[-1]
            letter_lines = input_lines[:len(input_lines) - 2]
        puzzle_board: WordGrid = WordGrid(letter_lines)
        word_bank: WordBank = WordBank(word_bank_line.split(" "))
        search_for_words(puzzle_board, word_bank)
        label_grid: List[List[Label]] = puzzle_board.label_list(root)
        x: int = STARTING_COL
        y: int = STARTING_ROW
        for row in label_grid:
            for label in row:
                label.grid(row=y, column=x)
                x += 1
            x = STARTING_COL
            y += 1

def test_file():
    STARTING_ROW: int = 1
    STARTING_COL: int = 0
    file = askopenfile(parent=root, mode='r', title="Choose a file", filetype=[("Text file", "*.txt")])
    found_semicolon: bool = False
    letter_lines: List[str] = []
    word_list: List[str] = []
    if file:
        for line in file.readlines():
            if line == "#":
                found_semicolon = True
                break
            elif found_semicolon == True:
                word_list.append(line)
            else:
                letter_lines.append(line)
        # if len(word_list) != 1:
        #     print(word_list)
        #     raise ValueError
        puzzle_board: WordGrid = WordGrid(letter_lines)
        word_bank: WordBank = WordBank(word_list[0].split(" "))
        search_for_words(puzzle_board, word_bank)
        label_grid: List[List[Label]] = puzzle_board.label_list(root)
        x: int = STARTING_COL
        y: int = STARTING_ROW
        for row in label_grid:
            for label in row:
                label.grid(row=y, column=x)
                print("({}, {})".format(x, y))
                x += 1
            x = STARTING_COL
            y += 1


            

    


    

word_search_btn_text = tk.StringVar()
word_search_btn = tk.Button(root, textvariable=word_search_btn_text, command=lambda:open_file())
word_search_btn_text.set("Select Word Puzzle")
word_search_btn.grid(column=0, row=0)
# word_search_btn.grid(column=1, row=2)
# test_lines = [
#     "ABCD",
#     "EFGH",
#     "IJKL"
# ]
# test_grid = WordGrid(test_lines)
# i: int = 4
# for row in test_grid.get_grid():
#     j: int = 4
#     for letter in row:
#         letter.generate_label(root).grid(column=j, row=i)
#         j += 1
#     i += 1

root.mainloop()