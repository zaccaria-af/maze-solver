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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _create_cells(self) -> None:
        for i in range(self._cols):
            col_cells = []
            for j in range(self._rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._cols):
            for j in range(self._rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is None:
            return
        x1 = self._point.x + i * self._cell_size_x
        y1 = self._point.y + j * self._cell_size_y
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
        self._cells[self._cols - 1][self._rows - 1].has_bottom_wall = False
        self._draw_cell(self._cols - 1, self._rows - 1)

    def _break_walls_r(self, i: int, j: int) -> None:
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            adjacent_cells = self._get_adjacent_cells(i, j)
            if adjacent_cells == {}:
                self._draw_cell(i, j)
                return

            next_direction, (next_cell, next_index) = random.choice(list(adjacent_cells.items()))

            match next_direction:
                case "left":
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                case "right":
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                case "up":
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                case "down":
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                case _:
                    return

            self._break_walls_r(next_index[0], next_index[1])

    def _get_adjacent_cells(self, i: int, j: int) -> dict[str, Cell]:
        adjacent_cells = {}
        if i > 0 and not self._cells[i-1][j].visited:
            adjacent_cells["left"] = (self._cells[i-1][j], (i-1, j))
        if i < self._cols - 1 and not self._cells[i+1][j].visited:
            adjacent_cells["right"] = (self._cells[i+1][j], (i+1, j))
        if j > 0 and not self._cells[i][j-1].visited:
            adjacent_cells["up"] = (self._cells[i][j-1], (i, j-1))
        if j < self._rows - 1 and not self._cells[i][j+1].visited:
            adjacent_cells["down"] = (self._cells[i][j+1], (i, j+1))
        return adjacent_cells

    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self._cols - 1 and j == self._rows - 1:
            return True
        adjacent_cells = self._get_adjacent_cells(i, j)
        for direction, cell in adjacent_cells.items():
            adjacent_cell = cell[0]
            match direction:
                case "left":
                    if not current_cell.has_left_wall:
                        current_cell.draw_move(adjacent_cell)
                        if self._solve_r(i - 1, j):
                            return True
                        else:
                            current_cell.draw_move(adjacent_cell, True)
                case "right":
                    if not current_cell.has_right_wall:
                        current_cell.draw_move(adjacent_cell)
                        if self._solve_r(i + 1, j):
                            return True
                        else:
                            current_cell.draw_move(adjacent_cell, True)
                case "up":
                    if not current_cell.has_top_wall:
                        current_cell.draw_move(adjacent_cell)
                        if self._solve_r(i, j - 1):
                            return True
                        else:
                            current_cell.draw_move(adjacent_cell, True)
                case "down":
                    if not current_cell.has_bottom_wall:
                        current_cell.draw_move(adjacent_cell)
                        if self._solve_r(i, j + 1):
                            return True
                        else:
                            current_cell.draw_move(adjacent_cell, True)
                case _:
                    return False

        return False
