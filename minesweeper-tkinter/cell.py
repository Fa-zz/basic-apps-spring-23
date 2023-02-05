from tkinter import Button
import random
import settings

class Cell:
    all = []

    # Constructor
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    # Creates a button object
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,   # Depends on grid size (in settings.py)
            height=4,
            text='Text'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left click
        btn.bind('<Button-1>', self.left_click_actions) # Right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("I am left clicked")

    # Takes some cells, and turns them into mines
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Better formatting when outputting cells
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"