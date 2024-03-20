from recording.save_turtle import pu, goto, pd, setheading


def moveto(x, y):
    pu()
    goto(x, y)
    pd()
    setheading(0)
