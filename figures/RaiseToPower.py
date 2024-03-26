from Config import Config
from figures.Figure import Figure


class RaiseToPower(Figure):
    def __init__(
        self,
        base: Figure,
        exponent: Figure,
        width: int = None,
        height: int = None,
        base_width_factor: float = 0.75,
        exponent_height_factor: float = 0.5,
    ):
        super().__init__(width, height)
        self.exponent_height_factor = exponent_height_factor
        self.base_width_factor = base_width_factor
        self.base = base
        self.exponent = exponent

    def _draw(self, width: int, height: int):
        self.base.y_coor = self.y_coor - Config.minimal_border_width
        self.base.x_coor = self.x_coor
        self.base.width = width * self.base_width_factor
        self.base.height = height - Config.minimal_border_width
        self.base.draw()
        self.exponent.y_coor = self.y_coor
        self.exponent.x_coor = self.x_coor + width * self.base_width_factor
        self.exponent.width = width * (1 - self.base_width_factor)
        self.exponent.height = height * self.exponent_height_factor
        self.exponent.draw()
