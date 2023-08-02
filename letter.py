from tkinter import *

class Letter:

    def __init__(self, letter_input: str) -> None:
        if letter_input.isalpha() == False:
            raise ValueError
        self.letter_value: str = letter_input.upper()
        self.word_section = False

    def set_found(self) -> None:
        self.letter_value = True

    def __repr__(self):
        return "Letter({}, {})".format(self.letter_value, self.word_section)
    
    #short repr for testing
    def __repr__(self):
        shortened_bool: str = ""
        if self.word_section:
            shortened_bool = "T"
        else:
            shortened_bool = "F"
        return "({}, {})".format(self.letter_value, shortened_bool)
    
    def __str__(self) -> str:
        return "({}, {})".format(self.letter_value, self.word_section)
    
    def generate_label(self, root: Tk) -> Label:
        if self.word_section == True:
            return Label(root, text= self.letter_value, fg= 'green', bg= 'gray', width=2, height= 2)
        else:
            return Label(root, text= self.letter_value, fg= 'red', bg= 'white', width=2, height= 2)