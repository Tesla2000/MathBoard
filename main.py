from itertools import product

from figures import moveto
from figures.Eight import Eight
from figures.Five import Five
from figures.Four import Four
from figures.Nine import Nine
from figures.One import One
from Config import Config
from figures.Six import Six
from figures.Seven import Seven
from figures.Three import Three
from figures.Two import Two
from figures.Zero import Zero

if __name__ == '__main__':
    width = 50
    height = 100
    x_cells = tuple(range(-640, 640 - width, width))
    y_cells = tuple(range(280, -280 + height, -height))
    action_space = [
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        [Zero(), One(), Two(), Three(), Four(), Five(), Six(), Seven(), Eight(), Nine(), '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', Eight(), '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', One()],
    ]
    for x_coor, y_coor in product(range(len(x_cells)), range(len(y_cells))):
        if not action_space[y_coor][x_coor]:
            continue
        moveto(x_cells[x_coor], y_cells[y_coor])
        action_space[y_coor][x_coor].draw(width, width)
