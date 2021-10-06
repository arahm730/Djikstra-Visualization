import pygame

columns, rows = 64, 48

size = (width, height) = 640, 480

w = width // columns
h = height // rows


class Spot:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.previous = None
        self.barrier = False
        self.visited_tiles = False

    def show(self, win, col, shape=1):
        if self.barrier:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x * w, self.y * h, w - 1, h - 1))
        else:
            pygame.draw.circle(win, col, (self.x * w + w // 2, self.y * h + h // 2), w // 3)

    def add_neighbors(self, grid):
        if self.x < columns - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
