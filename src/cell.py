from window import Window
from point import Point
from line import Line


class Cell:
    def __init__(self, win: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left_corner = None
        self._bottom_right_corner = None
        self._win = win

    def draw(self, top_left_corner: Point, bottom_right_corner: Point) -> None:
        self.top_left_corner = top_left_corner
        self.bottom_right_corner = bottom_right_corner
        top_right_corner = Point(bottom_right_corner.x, top_left_corner.y)
        bottom_left_corner = Point(top_left_corner.x, bottom_right_corner.y)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left_corner, bottom_left_corner), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(top_right_corner, bottom_right_corner), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(top_left_corner, top_right_corner), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_right_corner, bottom_left_corner), "black")

    def draw_move(self, to_cell: object, undo: bool = False) -> None:
        line_color = "red"
        if undo:
            line_color = "grey"
        width_a = self.bottom_right_corner.x - self.top_left_corner.x
        length_a = self.top_left_corner.y - self.bottom_right_corner.y
        center_a = Point(width_a // 2, length_a // 2)
        width_b = to_cell.bottom_right_corner.x - to_cell.top_left_corner.x
        length_b = to_cell.top_left_corner.y - to_cell.bottom_right_corner.y
        center_b = Point(width_b // 2, length_b // 2)
        self._win.draw_line(Line(center_a, center_b), line_color)
