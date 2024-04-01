from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self._a = a
        self._b = b

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
                self._a.x, self._a.y, self._b.x, self._b.y, fill=fill_color, width=2
        )
        canvas.pack()
