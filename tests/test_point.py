import sys
sys.path.insert(0, "../src")
from point import Point
from word_grid import WordGrid
from typing import List

def test_point_add_no_dot():
    point_a: Point = Point(3, 1)
    shift_point: Point = Point(1, 1)
    # my_point: Point = Point.add_points(point_a, shift_point)
    my_point = point_a + shift_point
    assert(my_point == Point(4, 2))

def test_scalar():
    assert(True)

def test_span():
    point_a: Point = Point(3, 0)
    shift_point: Point = Point(1, 1)
    assert(point_a.span(shift_point, 4) == Point(7, 4))

def test_horizontal_span():
    point_a: Point = Point(0, 0)
    shifter: Point = Point(1, 0)
    new_point: Point = point_a.span(shifter, 3)
    print("Original Point: " + repr(point_a))
    print("shift Point: " + repr(shifter))
    print("new Point: " + repr(new_point))
    assert(new_point == Point(3, 0))

def test_span_on_grid():
    test_lines: List[List[str]] = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["k", "l", "m", "n", "o"]
    ]
    test_grid: WordGrid = WordGrid(test_lines)
    start:Point = Point(0, 0)
    next_point: Point = start.span(Point(1, 0), 4)
    assert(test_grid.valid_point(next_point))

def test_copy_point_copies():
    point_a: Point = Point(3, 1)
    point_b: Point = point_a.copy_point()
    assert(point_a == point_b)

def test_copy_separate_from_base():
    point_a: Point = Point(3, 1)
    point_b: Point = point_a.copy_point()
    point_b.move_point(Point(2, 3))
    assert(point_a == Point(3, 1))

# def test_method_without_dot_operator():
#     point_a: Point = Point(3, 1)
#     point_b: Point = point_a.copy_point()
#     Point.move_point(point_b, Point(2, 3))
#     assert(point_a == Point(3, 1))