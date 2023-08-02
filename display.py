import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from word_grid import WordGrid
from letter import Letter

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=4, rowspan=4)

# def open_file():
#     file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Text file", "*.txt")])
#     found_semicolon: bool = False
#     if file:
#         pass
#     for line in file.readlines():
#         if line == ";":
#             found_semicolon = True
#             break

def generate_label(letter: Letter) -> Label:
    if letter.word_section:
        return Label(root, text=letter.letter_value, width=2, height=2, bg='gray', fg='green')
    else:
        return Label(root, text=letter.letter_value, width=2, height=2, bg='white', fg='red')

word_search_btn_text = tk.StringVar()
word_search_btn = tk.Button(root, textvariable=word_search_btn_text, command=lambda:open_file())
word_search_btn_text.set("Select Word Puzzle")
word_search_btn.grid(column=1, row=2)
test_lines = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l']
]
test_grid = WordGrid(test_lines)


root.mainloop()