from point import Point
from word_grid import WordGrid

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