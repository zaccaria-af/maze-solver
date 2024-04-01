import time
import random
from point import Point
from cell import Cell
from window import Window


class Maze:
    def __init__(self, point: Point, rows: int, cols: int,
                 cell_size_x: int, cell_size_y: int,
                 win: Window = None, seed: int = None) -> None:
        self._cells = []
        self._point = point
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        for i in range(self._cols):
            self._cells.append([])
            for j in range(self._rows):
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
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cols - 1, self._rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
