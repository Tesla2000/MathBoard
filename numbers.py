from turtle import pu, goto, pd, setheading, pos, fd, rt, bk, lt


def moveto(x, y):
    pu()
    goto(x, y)
    pd()
    setheading(0)


def nine(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d * 2)
    bk(d)
    rt(90)
    fd(d)
    rt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def eight(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d * 2)
    for i in range(3):
        rt(90)
        fd(d)
    bk(d)
    lt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def seven(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d * 2)
    bk(d * 2)
    lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def six(d):
    point = pos()
    fd(d)
    bk(d)
    rt(90)
    fd(d * 2)
    for i in range(3):
        lt(90)
        fd(d)
    rt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def five(d):
    point = pos()
    fd(d)
    bk(d)
    rt(90)
    fd(d)
    lt(90)
    fd(d)
    for i in range(2):
        rt(90)
        fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def four(d):
    point = pos()
    rt(90)
    fd(d)
    for i in range(2):
        lt(90)
        fd(d)
    bk(d * 2)
    pu()
    goto(point)
    pd()
    setheading(0)


def three(d):
    point = pos()
    for i in range(2):
        fd(d)
        rt(90)
    fd(d)
    for i in range(2):
        bk(d)
        rt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def two(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d)
    lt(90)
    for i in range(2):
        bk(d)
        lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)


def one(d):
    point = pos()
    pu()
    fd(d)
    pd()
    rt(90)
    fd(d * 2)
    pu()
    goto(point)
    pd()
    setheading(0)


def zero(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d * 2)
    rt(90)
    fd(d)
    rt(90)
    fd(d * 2)
    pu()
    goto(point)
    pd()
    setheading(0)


def drawnum(n: int, number_size: int = 50):
    {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}[n](number_size)
