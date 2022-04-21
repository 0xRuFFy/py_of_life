from pyglet.window import Window, mouse, key
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch, OrderedGroup
from code.field import Field
from code.cell import Cell
from pyglet.clock import schedule_interval


class GameScreen(Window):

    batch = Batch()
    group_0 = OrderedGroup(0)
    group_1 = OrderedGroup(1)

    def __init__(self, width: int, height: int, cell_size: int, rules: str):
        super().__init__(width, height, caption="Py Of Life")

        self.cell_size = cell_size
        self.cell_count = (width // cell_size, height // cell_size)
        self.rules = rules

        # * Create the mark cell
        self.mark: Cell = Cell(
            0, 0, self.cell_size, self.cell_count, self.batch, self.group_1, opacity=120
        )

        # * Create the field of cells
        self.field: Field = Field((width, height), self.cell_size, rules, self.batch, self.group_1)

        # * Create the background
        self.bg = Rectangle(
            0, 0, width, height, color=(255, 255, 255), batch=self.batch, group=self.group_0
        )

        # * Boolean to check if the game is running
        self.running = False

        # * Schedule the update
        schedule_interval(self.update, 1 / 25)

    def update(self, dt):
        """Updates the game

        Args:
            dt (_type_): The time since the last update
        """
        if self.running:
            self.running = self.field.apply_rules()
            if not self.running:
                self.mark.show(*self.field.translate_mouse(*self.mouse_pos))

    def on_draw(self):
        """Draws the game"""
        self.clear()
        self.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        # * Save the mouse position
        self.mouse_pos = x, y

        # * Update the mark cell position to the mouse position
        if not self.running:
            self.mark.update(*self.field.translate_mouse(x, y))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # * Add/remove multiple cells while dragging the left/right mouse button
        if not self.running:
            self.mark.hidde()  # * Hide the mark cell while dragging
            if buttons == mouse.LEFT:
                self.field.create_cell(*self.field.translate_mouse(x, y))
            elif buttons == mouse.RIGHT:
                self.field.remove_cell(*self.field.translate_mouse(x, y))

    def on_mouse_press(self, x, y, button, modifiers):
        # * Add/remove a single cell
        if not self.running:
            if button == mouse.LEFT:
                self.field.create_cell(*self.field.translate_mouse(x, y))
            elif button == mouse.RIGHT:
                self.field.remove_cell(*self.field.translate_mouse(x, y))

    def on_mouse_release(self, x, y, button, modifiers):
        # * Show the mark cell after releasing the left/right mouse button
        if not self.running:
            if button == mouse.LEFT or button == mouse.RIGHT:
                self.mark.show(*self.field.translate_mouse(x, y))

    def on_key_press(self, symbol, modifiers):
        # * Start/stop the game
        if symbol == key.SPACE:
            self.running = not self.running
            if self.running:
                self.mark.hidde()
            else:
                self.mark.show(*self.field.translate_mouse(*self.mouse_pos))

        if not self.running and symbol == key.BACKSPACE:
            self.field.remove_all_cells()
