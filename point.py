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