from point import Point

class Position:
    def __init__(self, front: Point, back: Point):
        self.first_letter: Point = front
        self.second_letter: Point = back