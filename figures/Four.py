from recording.save_turtle import pu, fd, rt, bk, lt

from figures.Figure import Figure


class Four(Figure):
    def _draw(self, width: int, height: int):
        rt(90)
        fd(height // 2)
        lt(90)
        fd(width)
        lt(90)
        fd(height // 2)
        bk(height)
        pu()
