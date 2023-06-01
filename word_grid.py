from typing import List


# stub for testing
class WordGrid:
    def __init__(self, word_lines: List[str]):
        self.grid: List[List[str]] = []
        for line in word_lines:
            self.grid.append(string_to_list(line))


    def display(self):
        for i in self.grid:
            for j in i:
                print(j)
            print("\n")

    def get_grid(self) -> List[List[str]]:
        return self.grid

    def _get_horizontal_line(self, i: int):
        line: str = ""
        j: int = 0
        while j < len(self.grid):
            line += self.grid[i][j]
            j += 1
        return line

    def get_horizontal_line_list(self):
        i: int = 0
        horizontal_list: List[str] = []
        while i < len(self.grid):
            horizontal_list.append(self._get_horizontal_line(i))
            i += 1
        return horizontal_list

    def _get_vertical_line(self, j: int):
        line: str = ""
        i: int = 0
        while i < len(self.grid[0]):
            line += self.grid[i][j]
            i += 1
        return line

# helper function
def string_to_list(line: str) -> List[str]:
    letter_list: List[str] = []
    for i in range(len(line)):
        letter_list.append(line[i])
    return letter_list

test_input = ["ABC", "DEF", "GHI"]
test_output = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
test_grid = WordGrid(test_input)
test_grid.display()