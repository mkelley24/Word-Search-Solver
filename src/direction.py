from enum import Enum
from point import Point

class Direction(Enum):
    Horizontal = 1
    Vertical = 2
    Right_Diagonal_Row = 3
    Right_Diagonal_Col = 4
    Left_Diagonal_Row = 5
    Left_Diagonal_Col = 6

    @classmethod
    def get_shift_point(cls, input):
        if input.value == 1:
            return Point(1, 0)
        elif input.value == 2:
            return Point(0, 1)
        elif input.value == 3:
            return Point(1, 1)
        elif input.value == 4:
            return Point(1, 1)
        elif input.value == 5:
            return Point(-1, 1)
        elif input.value == 6:
            return Point(-1, 1)
        else:
            raise ValueError
    
    @classmethod
    def get_head_shift(cls, input):
        if input.value == 1:
            return Point(0, 1)
        elif input.value == 2:
            return Point(1, 0)
        elif input.value == 3:
            return Point(1, 0)
        elif input.value == 4:
            return Point(0, 1)
        elif input.value == 5:
            return Point(1, 0)
        elif input.value == 6:
            return Point(0, 1)
        else:
            raise ValueError