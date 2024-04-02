from window import Window
from point import Point
from line import Line


class Cell:
    def __init__(self, win: Window = None) -> None:
        self._top_left_corner = None
        self._bottom_right_corner = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, top_left_corner: Point, bottom_right_corner: Point) -> None:
        if self._win is None:
            return
        self._top_left_corner = top_left_corner
        self._bottom_right_corner = bottom_right_corner
        top_right_corner = Point(bottom_right_corner.x, top_left_corner.y)
        bottom_left_corner = Point(top_left_corner.x, bottom_right_corner.y)
        if self.has_left_wall:
            line = Line(top_left_corner, bottom_left_corner)
            self._win.draw_line(line)
        else:
            line = Line(top_left_corner, bottom_left_corner)
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(top_right_corner, bottom_right_corner)
            self._win.draw_line(line)
        else:
            line = Line(top_right_corner, bottom_right_corner)
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(top_left_corner, top_right_corner)
            self._win.draw_line(line)
        else:
            line = Line(top_left_corner, top_right_corner)
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(bottom_right_corner, bottom_left_corner)
            self._win.draw_line(line)
        else:
            line = Line(bottom_right_corner, bottom_left_corner)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell: object, undo: bool = False) -> None:
        if self._win is None:
            return

        width_a = self._bottom_right_corner.x + self._top_left_corner.x
        length_a = self._top_left_corner.y + self._bottom_right_corner.y
        center_a = Point(width_a / 2, length_a / 2)

        width_b = to_cell._bottom_right_corner.x + to_cell._top_left_corner.x
        length_b = to_cell._top_left_corner.y + to_cell._bottom_right_corner.y
        center_b = Point(width_b / 2, length_b / 2)

        line_color = "red"
        if undo:
            line_color = "grey"

        self._win.draw_line(Line(center_a, center_b), line_color)
