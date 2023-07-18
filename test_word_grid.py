from word_grid import WordGrid
from typing import List
from point import Point

def compare_grids(actual: List[List[str]], test_value: List[List[str]]) -> bool:
    if len(actual) != len(test_value):
        return False
    else:
        for i in range(len(actual)):
            if len(actual[i]) != len(test_value[i]):
                return False
            else:
                for j in range(len(actual[i])):
                    if actual[i][j] != test_value[i][j]:
                        return False
    return True

def test_get_grid():
    test_input = ["ABC", "DEF", "GHI"]
    test_output = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    test_grid = WordGrid(test_input)
    assert(compare_grids(test_grid.grid, test_output))

def test_get_letter():
    test_input = ["ABC", "DEF", "GHI"]
    test_grid = WordGrid(test_input)
    test_point = Point(0, 1)
    assert(test_grid.get_letter(test_point) == "D")

def test_is_valid_on_point_with_invalid_x():
    test_input = ["ABC", "DEF", "GHI", "JKL"]
    test_grid = WordGrid(test_input)
    test_point = Point(3, 3)
    assert(test_grid.valid_point(test_point) == False)

def test_is_valid_on_point_with_invalid_y():
    test_input = ["ABCD", "EFGH", "IJKL"]
    test_grid = WordGrid(test_input)
    test_point = Point(3, 3)
    assert(test_grid.valid_point(test_point) == False)

def test_is_valid_on_double_invalid_point():
    test_input = ["ABC", "DEF", "GHI"]
    test_grid = WordGrid(test_input)
    test_point = Point(3, 3)
    assert(test_grid.valid_point(test_point) == False)

def test_is_valid_on_valid_point():
    test_input = ["ABC", "DEF", "GHI"]
    test_grid = WordGrid(test_input)
    test_point = Point(0, 1)
    assert(test_grid.valid_point(test_point) == True)


def test_get_horizontal_line_list():
    test_input = ["ABC", "DEF", "GHI"]
    test_lines = ["ABC", "DEF", "GHI"]
    test_grid = WordGrid(test_input)
    assert(test_grid.get_horizontal_line_list() == test_lines)

def test_get_vertical_line_list():
    test_input = ["ABC", "DEF", "GHI"]
    test_lines = ["ADG", "BEH", "CFI"]
    test_grid = WordGrid(test_input)
    assert(test_grid.get_vertical_line_list() == test_lines)

# def test_get_left_diagonal_line_list():
#     test_input = ["ABC", "DEF", "GHI"]
#     test_lines = ["AEI", "DH", "G", "BF", "I"]
#     test_grid = WordGrid(test_input)
#     assert(test_grid.get_left_diagonal_line_list() == test_lines)