from Config import Config

from figures.Figure import Figure


class Sequence(Figure):
    def __init__(self, *figures: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.figures = figures
    def _draw(self, width: int, height: int):
        element_width = width // len(self.figures)
        for index, figure in enumerate(self.figures, start=1):
            figure.x_coor = self.x_coor + index * element_width - max(Config.minimal_border_width, element_width // 10) if figure.x_coor is None else figure.x_coor
            figure.y_coor = self.y_coor
            figure.draw(element_width, height)
