from figures.Figure import Figure


class Sequence(Figure):
    border_height = False

    def __init__(
        self,
        *figures: Figure,
        figure_widths_proportions: list[float] = None,
        width: int = None,
        height: int = None
    ):
        super().__init__(width, height)
        self.figures = figures
        self.figure_widths_proportions = figure_widths_proportions
        if figure_widths_proportions is not None:
            self.figure_widths_proportions = tuple(
                proportion / sum(figure_widths_proportions)
                for proportion in figure_widths_proportions
            )

    def _draw(self, width: int, height: int):
        x_coor = self.x_coor
        total_width = sum(figure.width for figure in self.figures)
        if self.figure_widths_proportions is None:
            element_widths = tuple(
                (figure.width * width) // total_width for figure in self.figures
            )
        else:
            element_widths = tuple(
                width * proportion for proportion in self.figure_widths_proportions
            )
        for figure, element_width in zip(self.figures, element_widths):
            figure.x_coor = x_coor
            x_coor += element_width
            figure.y_coor = self.y_coor
            figure.draw(element_width, height)
