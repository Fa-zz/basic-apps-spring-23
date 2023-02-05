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
            #text='Text'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left click
        btn.bind('<Button-1>', self.left_click_actions) # Right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    # Return a cell object based on the value of x, y
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    # Count the mines that are around the cells
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    # Show the amount of mines that are around a cell
    def show_cell(self):
        print(self.surrounded_cells_mines_length)

    # Interrupts the game and displays a message that player lost
    # Temporarily this just converts the background of the mine cell to red
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')

    # Takes some cells, and turns them into mines
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Better formatting when outputting cells
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"