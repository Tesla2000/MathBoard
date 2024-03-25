from Config import Config
from figures.Blank import Blank
from figures.Emphasize import Emphasize
from figures.Equals import Equals
from figures.Fraction import Fraction
from figures.Number import Number
from figures.Parenthesized import Parenthesized
from figures.RaiseToPower import RaiseToPower
from figures.Root import Root
from fractions import Fraction as mathFraction
from figures.Text import Text

texts_to_translate = (
    "Cześć, pokażę Ci dzisiaj, jak sprawdzić, czy liczba jest niewymierna. W pierwszym etapie musimy przekształcić wszystkie liczby złożone na ich czynniki pierwsze.",
    "Kolejnym krokiem jest zamiana pierwiastka na potęgę.",
    "Następnie przenosimy wykładnik z ułamka na licznik i mianownik.",
    "Upraszczamy potęgi poprzez mnożenie wykładników.",
    "W ostatnim etapie musimy sprawdzić, czy wykładniki są liczbami całkowitymi. Jeśli tak, oznacza to, że liczba jest wymierna. Jeśli nie, liczba jest niewymierna.",
    "Jak widać, w tym wypadku wykładnik trzy drugie jest nieskracalny i, co za tym idzie, nie jest liczbą całkowitą. Zatem liczba jest niewymierna.",
    "Dziękuję za uwagę."
)
texts = {
    1: "Upraszczanie potęg i pierwiastków:"
       "\n>>> 1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne, przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi, przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników, pomnóż mianowniki."
       "\n7. Jeśli ułamki zwykłe można skrócić, skróć je.",
    2: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n>>> 2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne, przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi, przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników, pomnóż mianowniki."
       "\n7. Jeśli ułamki zwykłe można skrócić, skróć je.",
    3: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne, przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n>>> 5. Jeśli występują ułamki podniesione do potęgi, przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników, pomnóż mianowniki."
       "\n7. Jeśli ułamki zwykłe można skrócić, skróć je.",
    4: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne, przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi, przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n>>> 6. Jeśli można wykonać mnożenie wykładników, pomnóż mianowniki."
       "\n7. Jeśli ułamki zwykłe można skrócić, skróć je.",
    5: "Upraszczanie potęg i pierwiastków:"
       "\n1. Zamiana liczb złożonych na ich czynniki pierwsze."
       "\n2. Przekształcenie pierwiastków na potęgi."
       "\n3. Jeśli występują ułamki dziesiętne, przekształć je na zwykłe."
       "\n4. Ułamki zwykłe zapisz w formie ułamków niewłaściwych."
       "\n5. Jeśli występują ułamki podniesione do potęgi, przenieś wykładnik ułamka do wykładnika licznika i mianownika."
       "\n6. Jeśli można wykonać mnożenie wykładników, pomnóż mianowniki."
       "\n>>> 7. Jeśli ułamki zwykłe można skrócić, skróć je.",
}
row_height = 250
text = Text(text=texts[1])
figures = [
    [
        Root(
            Number.from_fraction(mathFraction(8, 49)),
            width=200,
            height=row_height,
        ),
        Equals(height=row_height),
        Root(
            Fraction(RaiseToPower(Number.from_int(2), Number.from_int(3)), RaiseToPower(Number.from_int(7), Number.from_int(2))),
            index=Number.from_int(2),
            width=200,
            height=row_height,
        ),
        Equals(height=row_height),
        RaiseToPower(
            Parenthesized(
                Fraction(RaiseToPower(Number.from_int(2), Number.from_int(3)), RaiseToPower(Number.from_int(7), Number.from_int(2)))
            ),
            Fraction(Number.from_int(1, centered=True), Number.from_int(2)),
            width=200,
            height=row_height,
        ),
        Equals(height=row_height),
        Fraction(
            RaiseToPower(
                Parenthesized(RaiseToPower(Number.from_int(2), Number.from_int(3))),
                Fraction(Number.from_int(1, centered=True), Number.from_int(2)),
            ),
            RaiseToPower(
                Parenthesized(RaiseToPower(Number.from_int(7), Number.from_int(2))),
                Fraction(Number.from_int(1, centered=True), Number.from_int(2)),
            ),
            width=200,
            height=row_height,
        ),
        Equals(height=row_height),
        Fraction(
            RaiseToPower(Number.from_int(2), Fraction(Number.from_int(3), Number.from_int(2))),
            RaiseToPower(Number.from_int(7), Fraction(Number.from_int(2), Number.from_int(2))),
            width=200,
            height=row_height,
        ),
        Equals(height=row_height),
    ],
    [Blank(height=50)],
    [
        Fraction(
            RaiseToPower(Number.from_int(2), Fraction(Number.from_int(3), Number.from_int(2))),
            RaiseToPower(Number.from_int(7), Number.from_int(1, centered=True)),
            width=200,
            height=row_height,
        ),
        text,
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
    [
        text.draw,
        figures[0][0].draw,
    ],
    [
        Text.clear,
        text.gen_add_text(texts[2]),
        text.draw,
        figures[0][1].draw,
        figures[0][2].draw,
        (e1 := Emphasize(figures[0][0].radical.numerator)).draw,
        (e2 := Emphasize(figures[0][2].radical.numerator)).draw,
        (e3 := Emphasize(figures[0][0].radical.denominator, color="blue")).draw,
        (e4 := Emphasize(figures[0][2].radical.denominator, color="blue")).draw,
    ],
    [
        Text.clear,
        text.gen_add_text(texts[3]),
        text.draw,
        e1.undo_no_record,
        e2.undo_no_record,
        e3.undo_no_record,
        e4.undo_no_record,
        figures[0][3].draw,
        figures[0][4].draw,
        (e1 := Emphasize(figures[0][2].index)).draw,
        (e4 := Emphasize(figures[0][4].exponent)).draw,
    ],
    [
        Text.clear,
        text.gen_add_text(texts[4]),
        text.draw,
        e1.undo_no_record,
        figures[0][5].draw,
        figures[0][6].draw,
        (e1 := Emphasize(figures[0][6].numerator.exponent)).draw,
        (e3 := Emphasize(figures[0][6].denominator.exponent)).draw,
    ],
    [
        Text.clear,
        text.gen_add_text(texts[5]),
        text.draw,
        e1.undo_no_record,
        e3.undo_no_record,
        e4.undo_no_record,
        figures[0][7].draw,
        figures[0][8].draw,
        (e1 := Emphasize(figures[0][6].numerator)).draw,
        (e3 := Emphasize(figures[0][8].numerator)).draw,
        (e2 := Emphasize(figures[0][6].denominator, color="blue")).draw,
        (e4 := Emphasize(figures[0][8].denominator, color="blue")).draw,
    ],
    [
        e1.undo_no_record,
        e2.undo_no_record,
        e3.undo_no_record,
        e4.undo_no_record,
        figures[0][9].draw,
        figures[-1][0].draw,
        Emphasize(figures[-1][0].numerator.exponent).draw,
    ],
]
