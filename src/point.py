class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self) -> str:
        return "Point(x= {x_value}, y= {y_value})".format(x_value = self.x, y_value = self.y)

    def move_point(self, shift: object) -> None:
        self.x += shift.x
        self.y += shift.y

    def change_point(self, new_x: int, new_y: int) -> None:
        self.x = new_x
        self.y = new_y

    def add_points(self, addend: object) -> object:
        return Point(self.x + addend.x, self.y + addend.y)
    
    def scale_point(self, scalar) -> object:
        return Point(self.x * scalar, self.y * scalar)
    
    def span(self, point_shift, length: int) -> object:
        new_shift: Point = point_shift.scale_point(length)
        return self + new_shift
    
    def __add__(self, addend) -> object:
        return Point(self.x + addend.x, self.y + addend.y)
    
    def is_equal(self, other) -> bool:
        if self.x != other.x:
            return False
        elif self.y != other.y:
            return False
        else:
            return True
    
    def __eq__(self, other) -> bool:
        if self.x != other.x:
            return False
        elif self.y != other.y:
            return False
        else:
            return True
        
    def copy_point(self) -> object:
        return Point(self.x, self.y)