from figures.Figure import Figure


class Sequence(Figure):
    border_height = False

    def __init__(self, *figures: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.figures = figures

    def _draw(self, width: int, height: int):
        x_coor = self.x_coor
        total_width = sum(figure.width for figure in self.figures)
        element_widths = tuple(
            (figure.width * width) // total_width for figure in self.figures
        )
        for figure, element_width in zip(self.figures, element_widths):
            figure.x_coor = x_coor
            x_coor += element_width
            figure.y_coor = self.y_coor
            figure.draw(element_width, height)
