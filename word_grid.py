from typing import List
from point import Point
from letter import Letter

# stub for testing
class WordGrid:
    def __init__(self, word_lines: List[str]):
        self.grid: List[List[Letter]] = list(map(string_to_list, word_lines))


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
    
    # def set_word_found(self, head: Point, directional_shift: Point, length: int):
    #     if self.valid_point(head) == False:
    #         raise ValueError
    #     elif self.valid_point(head.span(directional_shift, length)) == False:
    #         raise ValueError
    #     else:
    #         for _ in range(length):
    #             pass


    def _get_vertical_line(self, j: int) -> str:
        '''
        :param j: the index of the column
        :return: a line of text from the indicated column
        '''
        line: str = ""
        i: int = 0
        while i < len(self.grid[0]):
            line += self.grid[i][j].letter_value
            i += 1
        return line

    def get_vertical_line_list(self) -> List[str]:
        '''
        :return: a list of vertical lines of text
        '''
        j: int = 0
        vertical_list: List[str] = []
        while j < len(self.grid[0]):
            vertical_list.append(self._get_vertical_line(j))
            j += 1
        return vertical_list

    def _get_left_diagonal_line(self, i: int, j: int) -> str:
        '''
        :param i: the starting row index
        :param j: the starting column index
        :return: the line of text of the diagonal corresponding to the indices
        '''
        line: str = ""
        while i < len(self.grid) and j < len(self.grid[0]):
            line += self.grid[i][j].letter_value
            i += 1
            j += 1
        return line

    def get_left_diagonal_line_list(self) -> List[str]:
        left_diagonal_line_list: List[str] = []
        i: int = 0
        j: int = 0
        left_diagonal_line_list.append(self._get_left_diagonal_line(0, 0))
        while i < len(self.grid) or j < len(self.grid[0]):
            left_diagonal_line_list.append(self._get_left_diagonal_line(i, 0))
            left_diagonal_line_list.append(self._get_left_diagonal_line(0, i))
        return left_diagonal_line_list
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