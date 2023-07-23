class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def move_point(self, shift) -> None:
        self.x += shift.x
        self.y += shift.y

    def change_point(self, new_x: int, new_y: int) -> None:
        self.x = new_x
        self.y = new_y

    def add_points(self, addend):
        return Point(self.x + addend.x, self.y + addend.y)
    
    def scale_point(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def span(self, point_shift, length: int):
        new_shift: Point = None
        return Point(self.x * length, self.y * length)
    
    def __add__(self, addend):
        return Point(self.x + addend.x, self.y + addend.y)