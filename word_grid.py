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