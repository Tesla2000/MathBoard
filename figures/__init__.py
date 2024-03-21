from recording.save_turtle import pu, goto, pd, setheading


def moveto(x: int, y: int):
    pu()
    goto(x, y)
    pd()
    setheading(0)
