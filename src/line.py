from tkinter import BOTH, Canvas
from point import Point


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        canvas.create_line(
                self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
