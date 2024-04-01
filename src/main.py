import sys
from window import Window
from maze import Maze
from point import Point


def main() -> None:
    rows = 12
    cols = 16
    margin = 50
    initial_point = Point(margin, margin)
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / cols
    cell_size_y = (screen_y - 2 * margin) / rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(initial_point, rows, cols, cell_size_x, cell_size_y, win, 100)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

if __name__ == "__main__":
    main()
