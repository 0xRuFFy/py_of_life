from pyglet.shapes import Rectangle
from pyglet.graphics import Batch, OrderedGroup
from typing import Set, Tuple


class Cell(Rectangle):
    def __init__(
        self, x: int, y: int, size: float, cell_count: Tuple[int, int], batch: Batch, group: OrderedGroup, opacity: int = 255
    ):
        super().__init__(x * size, y * size, size, size, (0, 0, 0), batch, group)
        self.opacity = opacity
        self.index_pos = x, y
        self.cell_count = cell_count
        self.init_opacity = opacity
        self.neighbours = self.get_neighbours()

    def get_neighbours(self) -> Set[Tuple[int, int]]:
        neighbours = set()
        for i in range(max(0, self.index_pos[0] - 1), min(self.cell_count[0], self.index_pos[0] + 2)):
            for j in range(max(0, self.index_pos[1] - 1), min(self.cell_count[1], self.index_pos[1] + 2)):
                if (i != self.index_pos[0] or j != self.index_pos[1]):
                    neighbours.add((i, j))
        return neighbours

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
