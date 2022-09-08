import string

class GraphicObject:
    def __init__(self, name: string, xOrigin: int, yOrigin: int) -> None:
        self.name = name
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
    
    def __repr__(self) -> str:
        return "{0}[name:{1}; xOrigin:{2}; yOrigin:{3}]".format(self.__class__.__name__, self.name, self.xOrigin, self.yOrigin)

class Point(GraphicObject):
    def __init__(self, name: string, x: int, y: int) -> None:
        super().__init__(name, x, y)
        self.x = x
        self.y = y

class Line(GraphicObject):
    def __init__(self, name: string, p1: Point, p2: Point) -> None:
        super().__init__(name, p1.x, p1.y)
        self.p1 = p1
        self.p2 = p2

class Wireframe(GraphicObject):
    def __init__(self, name: string, points: list[Point]) -> None:
        super().__init__(name, points[0].x, points[0].y)
        self.points = points