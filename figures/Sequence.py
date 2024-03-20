from turtle import fd, pu, pd

from figures.Figure import Figure


class Sequence(Figure):
    def __init__(self, *figures: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.figures = figures

    def _draw(self, width: int, height: int):
        for figure in self.figures:
            figure.draw(width // len(self.figures), height)
            pu()
            fd(width // len(self.figures))
            pd()
