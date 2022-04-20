from typing import Dict, List, Set, Tuple
from pyglet.graphics import Batch, OrderedGroup
from code.cell import Cell


class Field:
    def __init__(
        self, size: Tuple[int, int], cell_size: int, rules: str, batch: Batch, group: OrderedGroup
    ) -> None:

        self.size = size
        self.cell_size = cell_size
        self.cell_count = size[0] // cell_size, size[1] // cell_size
        self.batch = batch
        self.group = group
        self.rules = self.format_rules(rules)

        # * Dict with Cells and their positions as keys
        self.cells: Dict[Tuple[int, int], Cell] = {}

    def format_rules(self, rules: str) -> Tuple[List[int], List[int]]:
        s = rules.split("/")
        if len(s) != 2:
            raise ValueError("Rules must be in the form 'a/b'")
        a, b = s
        print(a, b)
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        return a, b
    
    def get_possible_affected_cells(self) -> Set[Tuple[int, int]]:
        """Returns a list of all cells that could be affected during the next step

        Returns:
            List[Tuple[int, int]]: The list of all cells that could be affected
        """

        # * Add all cells that are next to a living cell | Not wrapping around the edges
        res: Set[Tuple[int, int]] = set()
        for cell in self.cells.keys():
            for i in range(max(0, cell[0] - 1), min(self.cell_count[0], cell[0] + 2)):
                for j in range(max(0, cell[1] - 1), min(self.cell_count[1], cell[1] + 2)):
                    res.add((i, j))
        return res

    def get_neighbours(self, cell: Tuple[int, int]) -> int:
        # * Counts the number of living cells around the given cell in a 3x3 grid
        count = 0
        for i in range(max(0, cell[0] - 1), min(self.cell_count[0], cell[0] + 2)):
            for j in range(max(0, cell[1] - 1), min(self.cell_count[1], cell[1] + 2)):
                if (i != cell[0] or j != cell[1]) and self.cells.get((i, j)) is not None:
                    count += 1
        return count

    def apply_rules_to_cell(self, cell: Tuple[int, int]) -> int:
        """Applies the rules to the given cell

        Args:
            cell (Cell): The cell to apply the rules to
        """

        neighbour_count = self.get_neighbours(cell)
        result = 0
        
        if cell in self.cells:
            if neighbour_count in self.rules[1]:
                result = 1
            else:
                result = 0
        elif neighbour_count in self.rules[0]:
            result = 1

        return result

    def apply_rules(self) -> bool:
        """Applies the rules to all cells

        Returns:
            bool: False if the field is empty, True otherwise
        """

        relevant_cells = self.get_possible_affected_cells()
        new_cells: Set[Tuple[int, int]] = set()

        for cell in relevant_cells:
            if self.apply_rules_to_cell(cell) == 1:
                new_cells.add(cell)

        self.set_cells(new_cells)
        return len(self.cells) != 0

    def set_cells(self, cells: Set[Tuple[int, int]]) -> None:
        """Sets the cells of the field

        Args:
            cells (List[Cell]): The list of cells to set
        """
        self.remove_all_cells()
        for cell in cells:
            self.create_cell(cell[0], cell[1])

    def translate_mouse(self, mouse_x: int, mouse_y: int) -> Tuple[int, int]:
        """Translates the mouse position to the field position

        Args:
            mouse_x (int): The x position of the mouse
            mouse_y (int): The y position of the mouse

        Returns:
            Tuple[int, int]: The field position of the mouse
        """
        return mouse_x // self.cell_size, mouse_y // self.cell_size

    def create_cell(self, x: int, y: int) -> None:
        """Creates a cell at the given position if it doesn't exist

        Args:
            x (int): The x position of the cell
            y (int): The y position of the cell
        """
        if self.cells.get((x, y)) is None:
            self.cells[x, y] = Cell(x, y, self.cell_size, self.batch, self.group)

    def remove_cell(self, x: int, y: int) -> None:
        """Removes a cell at the given position if it exists

        Args:
            x (int): The x position of the cell
            y (int): The y position of the cell
        """
        self.cells.pop((x, y), None)

    def remove_cells(self, cells: List[Cell]) -> None:
        """Removes a list of cells from the field

        Args:
            cells (List[Cell]): The list of cells to remove
        """
        for cell in cells:
            self.remove_cell(cell.index_pos[0], cell.index_pos[1])

    def remove_all_cells(self) -> None:
        """Removes all cells from the field"""
        self.cells.clear()
