import tkinter as tk
from tkinter.filedialog import askopenfile

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

def open_file():
    file = askopenfile(parent=window, mode='rb', title="Choose a file", filetype=[("Text file", "*.txt")])
    if file:
        pass

sudoku_btn_text = tk.StringVar()
sudoku_btn = tk.Button(window, textvariable=sudoku_btn_text, command=lambda:open_file())
sudoku_btn_text.set("Select Sudoku Puzzle")
sudoku_btn.grid(column=1, row=2)

window.mainloop()