from recording.save_turtle import fd, rt

from figures.Figure import Figure


class Zero(Figure):
    def _draw(self, width: int, height: int):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
        fd(width)
        rt(90)
        fd(height)
