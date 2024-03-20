from Config import Config
from figures import moveto
from figures.Divided import Divided
from figures.Eight import Eight
from figures.Five import Five
from figures.Four import Four
from figures.Fraction import Fraction
from figures.Minus import Minus
from figures.Nine import Nine
from figures.One import One
from figures.Plus import Plus
from figures.Sequence import Sequence
from figures.Seven import Seven
from figures.Six import Six
from figures.Three import Three
from figures.Times import Times
from figures.Two import Two
from figures.Zero import Zero
from recording.concat2video import concat2video

if __name__ == '__main__':
    start_x, y_coor = Config.start_x, Config.start_y
    action_space = [
        [Divided(), Times(), Sequence(One(), Plus(), Fraction(Two(), Three()), Four(), width=300, height=100)],
        [Fraction(One(), Seven()), One()],
        [Plus(), Minus(),],
        [Zero(), One(), Two(), Three(), Four(), Five(), Six(), Seven(), Eight(), Nine(),],
        [Zero(), Eight(),],
    ]
    for row in action_space:
        x_coor = start_x
        for figure in row:
            moveto(x_coor, y_coor)
            figure.draw()
            x_coor += figure.width
        y_coor -= max(figure.height for figure in row)
    concat2video()
