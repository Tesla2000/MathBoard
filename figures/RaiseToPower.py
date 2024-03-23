from figures.Figure import Figure


class RaiseToPower(Figure):

    def __init__(self, base: Figure, exponent: Figure, width: int = None, height: int = None):
        super().__init__(width, height)
        self.base = base
        self.exponent = exponent

    def _draw(self, width: int, height: int):
        self.base.y_coor = self.y_coor - height // 4
        self.base.x_coor = self.x_coor
        self.base.width = width * 3 // 4
        self.base.height = height * 3 // 4
        self.base.draw()
        self.exponent.y_coor = self.y_coor
        self.exponent.x_coor = self.x_coor + width * 3 // 4
        self.exponent.width = width // 4
        self.exponent.height = height // 2
        self.exponent.draw()

