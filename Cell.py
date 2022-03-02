import numpy as np


class Cell:

    def __init__(self, i, j):
        self.x = i
        self.y = j

        #   Walls
        self.up = True
        self.left = True
        self.bottom = True
        self.right = True

        self.visited = False

    def show(self, axes, thickness):

        if self.up:
            axes.plot([self.x, self.x + 1], [self.y, self.y], 'k', linewidth=thickness)
        if self.left:
            axes.plot([self.x, self.x], [self.y, self.y + 1], 'k', linewidth=thickness)
        if self.bottom:
            axes.plot([self.x, self.x + 1], [self.y + 1, self.y + 1], 'k', linewidth=thickness)
        if self.right:
            axes.plot([self.x + 1, self.x + 1], [self.y, self.y + 1], 'k', linewidth=thickness)

    def visit(self):
        self.visited = True
