from typing import Iterable

from figures.Figure import Figure


class Row(list):
    def __init__(self, iterable: Iterable[Figure], height: int):
        super().__init__()
        self.height = height
        for item in iterable:
            item.height = height
            self.append(item)

    def append(self, __object: Figure):
        __object.height = self.height
        super().append(__object)
