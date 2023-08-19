from direction import Direction
from point import Point

def test_creation():
    test_direction = Direction.Horizontal
    assert(Direction.get_shift_point(test_direction) == Point(1, 0))

def test_get_head_shift():
    test_direction = Direction.Right_Diagonal_Row
    assert(Direction.get_head_shift(test_direction) == Point(1, 0))