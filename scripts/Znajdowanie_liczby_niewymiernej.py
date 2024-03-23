from Config import Config
from PassedVariables import PassedVariables
from figures.Blank import Blank
from figures.Eight import Eight
from figures.Emphasize import Emphasize
from figures.Equals import Equals
from figures.Four import Four
from figures.Fraction import Fraction
from figures.Nine import Nine
from figures.One import One
from figures.Parenthesized import Parenthesized
from figures.RaiseToPower import RaiseToPower
from figures.Root import Root
from figures.Sequence import Sequence
from figures.Seven import Seven
from figures.Text import Text
from figures.Three import Three
from figures.Two import Two

PassedVariables.texts_to_translate = (
    "Cześć pokażę Ci dzisiaj jak sprawdzić czy liczba jest niewymierna. W pierwszym etapie musimy przekształcić wszystkie liczby złożone na ich czynniki pierwsze.",
    "Kolejnym krokiem jest zamiana pierwiastka na potęgę.",
    "Przeniesienie wykładnika z ułamka na licznik i mianownik.",
    "I uproszczenie potęg poprzez mnożenie wykładników.",
    "W ostatnim etapie musimy sprawdzić czy wykładniki są liczbami całkowitymi. Jeśli tak oznacza to że liczba jest wymierna. Jeśli nie liczba jest niewymierna.",
    "Jak widać w tym wypadku wykładnik trzy drugie jest nieskracalny i co za tym idzie nie jest liczbą całkowitą, zatem liczba jest niewymierna.",
    "Dziękuję za uwagę.",
)
texts = {
    1: "Upraszczanie potęg i pierwiastków:"
       "\n>>> 1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników pomnóż mianowniki."
       "\n7. Jeśli ułamki wzwykłe można skrócić skróć je.",
    2: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n>>> 2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników pomnóż mianowniki."
       "\n7. Jeśli ułamki wzwykłe można skrócić skróć je.",
    3: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n>>> 5. Jeśli występują ułamki podniesione do potęgi przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników pomnóż mianowniki."
       "\n7. Jeśli ułamki wzwykłe można skrócić skróć je.",
    4: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n>>> 6. Jeśli można wykonać mnożenie wykładników pomnóż mianowniki."
       "\n7. Jeśli ułamki wzwykłe można skrócić skróć je.",
    5: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników pomnóż mianowniki."
       "\n>>> 7. Jeśli ułamki wzwykłe można skrócić skróć je.",
}
row_height = 250
text = Text(
    text=texts[1]
)
figures = [
    [
        Root(Fraction(Sequence(Blank(width=Config.default_width // 2), Eight(), Blank(width=Config.default_width // 2)),
                      Sequence(Four(), Nine())), width=200, height=row_height),
        Equals(height=row_height),
        Root(Fraction(RaiseToPower(Two(), Three()), RaiseToPower(Seven(), Two())), index=Two(), width=200,
             height=row_height),
        Equals(height=row_height),
        RaiseToPower(Parenthesized(Fraction(RaiseToPower(Two(), Three()), RaiseToPower(Seven(), Two()))),
                     Fraction(One(centered=True), Two()), width=200, height=row_height),
        Equals(height=row_height),
        Fraction(
            RaiseToPower(Parenthesized(RaiseToPower(Two(), Three())), Fraction(One(centered=True), Two())),
            RaiseToPower(Parenthesized(RaiseToPower(Seven(), Two())), Fraction(One(centered=True), Two())), width=200,
            height=row_height
        ),
        Equals(height=row_height),
        Fraction(
            RaiseToPower(Two(), Fraction(Three(), Two())),
            RaiseToPower(Seven(), Fraction(Two(), Two())), width=200, height=row_height
        ),
        Equals(height=row_height),
    ],
    [
        Blank(height=50)
    ],
    [
        Fraction(
            RaiseToPower(Two(), emphasized := Fraction(Three(), Two())),
            RaiseToPower(Seven(), One(centered=True)), width=200, height=row_height
        ),
        text,
    ]
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
    [figures[0][0].draw, ],
    [text.draw, figures[0][1].draw, figures[0][2].draw, ],
    [Text.clear, text.gen_add_text(texts[2]), text.draw, figures[0][3].draw, figures[0][4].draw, ],
    [Text.clear, text.gen_add_text(texts[3]), text.draw, figures[0][5].draw, figures[0][6].draw, ],
    [Text.clear, text.gen_add_text(texts[4]), text.draw, figures[0][7].draw, figures[0][8].draw, ],
    [Text.clear, text.gen_add_text(texts[5]), text.draw,
     figures[0][9].draw,
     figures[-1][0].draw,
     Emphasize(emphasized).draw],
]
