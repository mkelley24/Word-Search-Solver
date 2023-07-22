import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from word_grid import WordGrid

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

def open_file():
    file = askopenfile(parent=window, mode='rb', title="Choose a file", filetype=[("Text file", "*.txt")])
    if file:
        pass

word_search_btn_text = tk.StringVar()
word_search_btn = tk.Button(window, textvariable=word_search_btn_text, command=lambda:open_file())
word_search_btn_text.set("Select Word Puzzle")
word_search_btn.grid(column=1, row=2)
test_lines = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l']
]
test_grid = WordGrid(test_lines)


window.mainloop()