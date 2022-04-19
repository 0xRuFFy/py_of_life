from pyglet.shapes import Rectangle
from pyglet.graphics import Batch, OrderedGroup


class Cell(Rectangle):
    def __init__(
        self, x: int, y: int, size: float, batch: Batch, group: OrderedGroup, opacity: int = 255
    ):
        super().__init__(x * size, y * size, size, size, (0, 0, 0), batch, group)
        self.opacity = opacity
        self.index_pos = x, y
        self.init_opacity = opacity

    def update(self, x: int, y: int):
        """Updates the cell position"""
        self.x = x * self.width
        self.y = y * self.height

    def hidde(self):
        """Hides the cell"""
        self.opacity = 0

    def show(self, x: int, y: int):
        """Shows the cell at the given position

        Args:
            x (int): The x position of the cell
            y (int): The y position of the cell
        """
        self.update(x, y)
        self.opacity = self.init_opacity
