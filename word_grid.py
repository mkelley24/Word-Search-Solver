from typing import List


# stub for testing
class WordGrid:
    def __init__(self, word_lines: List[str]):
        self.grid: List[List[str]] = [[""]]

    def display(self):
        for i in self.grid:
            for j in i:
                print(j)
            print("\n")

    def get_grid(self) -> List[List[str]]:
        return self.grid