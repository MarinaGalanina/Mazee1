from Cell import *

from matplotlib import pyplot as plt


# Remove wall between neighbours
def remove_wall(current_cell, next_cell):
    if next_cell.x - current_cell.x == 1:
        next_cell.left = False
        current_cell.right = False

    elif next_cell.x - current_cell.x == -1:
        next_cell.right = False
        current_cell.left = False

    elif next_cell.y - current_cell.y == 1:
        next_cell.up = False
        current_cell.bottom = False

    elif next_cell.y - current_cell.y == -1:
        next_cell.bottom = False
        current_cell.up = False


class Maze:
    def __init__(self, r, c):
        self.fig, self.ax = plt.subplots()

        self.row = r
        self.column = c

        self.grid = np.empty((self.row, self.column), dtype=Cell)
        self.create_grid()

        self.stack = list()

    def create_grid(self):
        for r in range(self.row):
            for c in range(self.column):
                self.grid[r][c] = Cell(c, r)

    def show(self, linewidth):
        for r in range(self.row):
            for c in range(self.column):
                self.grid[r][c].show(self.ax, linewidth)
        plt.show()

    #   Randomized depth-first search  ->  Iterative implementation
    def DFS(self):

        # STEP 1: Choose the initial cell, mark it as visited and push it to the stack
        self.grid[0][0].visit()
        self.stack.append(self.grid[0][0])

        # STEP 2: While the stack is not empty
        while self.stack:

            # STEP 2.1: Pop a cell from the stack and make it a current cell
            current_cell = self.stack[-1]

            # STEP 2.2: If the current cell has any neighbours which have not been visited
            unvisited_neighbours = list()

            if current_cell.x > 0 and not self.grid[current_cell.y][current_cell.x - 1].visited:
                unvisited_neighbours.append(self.grid[current_cell.y][current_cell.x - 1])

            if current_cell.x < self.column - 1 and not self.grid[current_cell.y][current_cell.x + 1].visited:
                unvisited_neighbours.append(self.grid[current_cell.y][current_cell.x + 1])

            if current_cell.y > 0 and not self.grid[current_cell.y - 1][current_cell.x].visited:
                unvisited_neighbours.append(self.grid[current_cell.y - 1][current_cell.x])

            if current_cell.y < self.row - 1 and not self.grid[current_cell.y + 1][current_cell.x].visited:
                unvisited_neighbours.append(self.grid[current_cell.y + 1][current_cell.x])

            if unvisited_neighbours:

                # STEP 2.2.1: Choose one of the unvisited neighbours
                neighbour = np.random.choice(unvisited_neighbours)

                # STEP 2.2.2: Remove the wall between the current cell and the chosen cell
                remove_wall(current_cell, neighbour)

                # STEP 2.2.3: Mark the chosen cell as visited and push it to the stack
                neighbour.visit()
                self.stack.append(neighbour)

            # STEP 2.2 Else pop a cell from the stack
            else:
                self.stack.pop()
