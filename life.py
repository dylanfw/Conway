import os
from time import sleep
from random import getrandbits

class Cell():
    def __init__(self, alive):
        self.alive = bool(alive)
        self.neighbors = 0

    def __repr__(self):
        if self.alive:
            return "%"
        return " "

class Grid():
    """
    Initalize a new w*h grid of cells.
    If 2D bit array `insert` is supplied, place insert in top left of empty grid.
    Otherwise living cells are randomly distributed across grid.
    """
    def __init__(self, w, h, insert=None):
        self.w, self.h = w, h
        if insert != None:
            self.cells = [[Cell(0) for x in xrange(w)] for y in xrange(h)]
            for row in xrange(h):
                for col in xrange(w):
                    if row < len(insert) and col < len(insert[0]):
                        self.cells[row][col] = Cell(insert[row][col])
                    else:
                        self.cells[row][col] = Cell(0)
        else:
            self.cells = [[Cell(getrandbits(1)) for x in xrange(w)] for y in xrange(h)]

    """

    """
    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        for row in xrange(self.h):
            if row == 0:
                print "+%s +" % (" -" * self.w)
            for col in xrange(self.w):
                if col == 0:
                    print "|",
                print self.cells[row][col],
                if col == self.w - 1:
                    print "|"
            if row == self.h - 1:
                print "+%s +" % (" -" * self.w)

class Game():
    """
    Initialize a new game of life with provided grid options
    """
    def __init__(self, w, h, insert=None):
        self.grid = Grid(w, h, insert)
    """
    Begin game cycles, applying rules and displaying grid at each step
    """
    def run(self):
        while True:
            self.count_neighbors()
            self.grid.display()
            self.apply_rules()
            sleep(0.1)
    """
    For each cell in grid, count neighbors to the left, right, above, below, and diagonals.
    """
    def count_neighbors(self):
        for row in xrange(self.grid.h):
            for col in xrange(self.grid.w):
                cell = self.grid.cells[row][col]
                if col > 0:
                    left_neighbor = self.grid.cells[row][col - 1]
                    if left_neighbor.alive:
                        cell.neighbors += 1
                if col < self.grid.w - 1:
                    right_neighbor = self.grid.cells[row][col + 1]
                    if right_neighbor.alive:
                        cell.neighbors += 1
                if row > 0:
                    top_neighbor = self.grid.cells[row - 1][col]
                    if top_neighbor.alive:
                        cell.neighbors += 1
                if row < self.grid.h - 1:
                    bottom_neighbor = self.grid.cells[row + 1][col]
                    if bottom_neighbor.alive:
                        cell.neighbors += 1
                if col > 0 and row > 0:
                    left_top_neighbor = self.grid.cells[row - 1][col - 1]
                    if left_top_neighbor.alive:
                        cell.neighbors += 1
                if col < self.grid.w - 1 and row > 0:
                    right_top_neighbor = self.grid.cells[row - 1][col + 1]
                    if right_top_neighbor.alive:
                        cell.neighbors += 1
                if col > 0 and row < self.grid.h - 1:
                    left_bottom_neighbor = self.grid.cells[row + 1][col - 1]
                    if left_bottom_neighbor.alive:
                        cell.neighbors += 1
                if col < self.grid.w - 1 and row  < self.grid.h - 1:
                    right_bottom_neighbor = self.grid.cells[row + 1][col + 1]
                    if right_bottom_neighbor.alive:
                        cell.neighbors += 1
    """
    For each living cell:
        Cell dies if it has 1 or less neighbors (Loneliness)
        Cell dies if it has 4 or more neighbors (Crowding)
    For each dead cell:
        Cell comes alive if it has exactly 3 neighbors (Reproduction)
    """
    def apply_rules(self):
        for row in xrange(self.grid.h):
            for col in xrange(self.grid.w):
                cell = self.grid.cells[row][col]
                if cell.alive:
                    if cell.neighbors <= 1:
                        cell.alive = False
                    if cell.neighbors >= 4:
                        cell.alive = False
                else:
                    if cell.neighbors == 3:
                        cell.alive = True
                cell.neighbors = 0

#            % 
#              %
#          % % %
glider = [[0,1,0],
          [0,0,1],
          [1,1,1]]

if __name__ == "__main__":
    #game = Game(w=20, h=20)
    game = Game(w=20, h=20, insert=glider)
    game.run()
