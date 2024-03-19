from itertools import product

from figures import moveto
from figures.Eight import Eight
from figures.Nine import Nine
from figures.One import One
from Config import Config

if __name__ == '__main__':
    x_cells = tuple(range(-640, 640 - 60, 60))
    y_cells = tuple(range(280, -280 + 110, -110))
    action_space = [
        [One(), Nine(), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', Eight(), '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', One()],
    ]
    for x_coor, y_coor in product(range(len(x_cells)), range(len(y_cells))):
        if not action_space[y_coor][x_coor]:
            continue
        moveto(x_cells[x_coor], y_cells[y_coor])
        action_space[y_coor][x_coor].draw()
