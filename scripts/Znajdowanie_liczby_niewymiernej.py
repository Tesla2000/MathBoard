from Config import Config
from audio.generate_audio import generate_audio
from figures.Coma import Coma
from figures.Divided import Divided
from figures.Eight import Eight
from figures.Equals import Equals
from figures.Five import Five
from figures.Four import Four
from figures.Fraction import Fraction
from figures.Minus import Minus
from figures.Nine import Nine
from figures.One import One
from figures.Plus import Plus
from figures.Root import Root
from figures.Sequence import Sequence
from figures.Seven import Seven
from figures.Six import Six
from figures.Three import Three
from figures.Times import Times
from figures.Two import Two
from figures.Zero import Zero

Config.texts_to_translate = (
    "Cześć pokażę Ci dzisiaj jak sprawdzić czy liczba jest niewymierna.",
    "Dziękuję za uwagę.",
)
figures = [
    # [Root(Zero(), Zero(), width=150), Coma(), Eight(), ],
    # [
    #     Equals(), Seven(), Divided(), Times(), Eight(),
    #  Sequence(One(), Plus(), Fraction(Two(), Three()), Four(), width=300, height=100)],
    [Fraction(One(), Seven()), One()],
    [Plus(), Minus(), ],
    [Zero(), One(), Two(), Three(), Four(), Five(), Six(), Seven(), Eight(), Nine(), ],
    [Zero(), Eight(), ],
]
start_x, y_coor = Config.start_x, Config.start_y
for row in figures:
    x_coor = start_x
    for figure in row:
        if figure.x_coor is None:
            figure.x_coor = x_coor
        if figure.y_coor is None:
            figure.y_coor = y_coor
        x_coor += figure.width
    y_coor -= max(figure.height for figure in row)
action_spaces = [
    [[figures[0][0].draw]],
    list(list(figure.draw for figure in row) for row in figures),
]

