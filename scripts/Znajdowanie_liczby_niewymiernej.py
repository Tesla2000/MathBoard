from Config import Config
from audio.generate_audio import generate_audio
from figures.Blank import Blank
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
from figures.Parenthesized import Parenthesized
from figures.Plus import Plus
from figures.RaiseToPower import RaiseToPower
from figures.Root import Root
from figures.Sequence import Sequence
from figures.Seven import Seven
from figures.Six import Six
from figures.Three import Three
from figures.Times import Times
from figures.Two import Two
from figures.Zero import Zero

Config.texts_to_translate = (
    "Cześć pokażę Ci dzisiaj jak sprawdzić czy liczba jest niewymierna. W pierwszym etapie musimy przekształcić wszystkie liczby złożone na ich czynniki pierwsze.",
    "Kolejnym krokiem jest zamiana pierwiastka na potęgę.",
    "Dziękuję za uwagę.",
)
row_height = 200
figures = [
    [
        Root(Fraction(Sequence(Blank(width=Config.default_width // 2), Eight(), Blank(width=Config.default_width // 2)), Sequence(Four(), Nine())), width=200, height=row_height),
        Equals(height=row_height),
        Root(Fraction(RaiseToPower(Two(), Three()), RaiseToPower(Seven(), Two())), width=200, height=row_height),
        Equals(height=row_height),
        RaiseToPower(Parenthesized(Fraction(RaiseToPower(Two(), Three()), RaiseToPower(Seven(), Two()))), Fraction(One(centered=True), Two()),  width=200, height=200),
    ],
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
    [figures[0][0].draw],
    [figures[0][1].draw, figures[0][2].draw, ],
    [figures[0][3].draw, figures[0][4].draw, ],
]
