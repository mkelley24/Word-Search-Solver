from typing import List
from point import Point
from letter import Letter
from tkinter import *

# stub for testing
class WordGrid:
    def __init__(self, word_lines: List[str]):
        try:
            self.grid: List[List[Letter]] = list(map(string_to_list, word_lines))
        except ValueError:
            raise ValueError
        row_length: int = len(self.grid[0])
        for row in self.grid:
            if row_length != len(row):
                raise ValueError

    def __repr__(self):
        output = "[\n"
        for x in self.grid:
            output += str(x)
            output += "\n"
        output += "]"
        return output
    
    def label_list(self, root: Tk) -> List[List[Label]]:
        label_grid: List[List[Label]] = []
        for row in self.grid:
            label_row: List[Label] = []
            for letter in row:
                label_row.append(letter.generate_label(root))
            label_grid.append(label_row)
        return label_grid

    def display(self):
        for i in self.grid:
            for j in i:
                print(j.letter_value)
            print("\n")

    def get_grid(self) -> List[List[Letter]]:
        return self.grid
    
    def get_letter(self, point: Point):
        return self.grid[point.y][point.x]
    
    def valid_point(self, point: Point) -> bool:
        '''
        :param point: a Point that contains grid coordinates
        :return: returns true if the point is within the gird and false if not
        '''
        i: int = point.y
        j: int = point.x
        if i < 0 or j < 0:
            return False
        elif i >= len(self.grid) or j >= len(self.grid[0]):
            return False
        else:
            return True

    def _get_horizontal_line(self, i: int) -> str:
        line: str = ""
        j: int = 0
        while j < len(self.grid):
            line += self.grid[i][j].letter_value
            j += 1
        return line

    def get_horizontal_line_list(self) -> List[str]:
        i: int = 0
        horizontal_list: List[str] = []
        while i < len(self.grid):
            horizontal_list.append(self._get_horizontal_line(i))
            i += 1
        return horizontal_list
    
    def display_found_letters(self) -> str:
        display_string: str = ""
        for row in self.grid:
            display_string += '\n'
            for value in row:
                if value.word_section == True:
                    display_string += value.letter_value
                else:
                    display_string += '_'
        return display_string
    
    # def set_word_found(self, head: Point, directional_shift: Point, length: int):
    #     if self.valid_point(head) == False:
    #         raise ValueError
    #     elif self.valid_point(head.span(directional_shift, length)) == False:
    #         raise ValueError
    #     else:
    #         for _ in range(length):
    #             pass

# helper function
def string_to_list(line: str) -> List[Letter]:
    letter_list: List[Letter] = []
    for i in range(len(line)):
        letter_list.append(Letter(line[i]))
    return letter_list


# test_input = ["ABC", "DEF", "GHI"]
# test_output = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
# test_grid = WordGrid(test_input)
# test_grid.display()