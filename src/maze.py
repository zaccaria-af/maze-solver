import time
from point import Point
from cell import Cell
from window import Window

class Maze:
    def __init__(self, point: Point, rows: int, cols: int, cell_size_x: int, cell_size_y: int, win: Window = None) -> None:
        self._cells = []
        self._point = point
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self) -> None:
        for i in range(self._cols):
            self._cells.append([])
            for j in range(self._rows_):
                self._cells[i].append(Cell(self._win))
        for i in range(self._cols):
            for j in range(self._rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1 = self._point.x + i * self._cell_size_x
        y1 = self._point.y + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        self._animate()

    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)
