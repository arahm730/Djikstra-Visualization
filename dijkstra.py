import sys
from spot import *
from collections import deque
from tkinter import messagebox, Tk

pygame.init()

display = pygame.display.set_mode(size)
pygame.display.set_caption("Dijkstra's Path Finding Visualization")

grid = []
queue = deque()
visited_tiles = []
path = []


def click_barrier(position, state):
    i = position[0] // w
    j = position[1] // h
    grid[i][j].barrier = state


def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h


for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(columns):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)


start_tile = grid[5][25]
end_tile = grid[55][25]
start_tile.barrier = False
end_tile.barrier = False

queue.append(start_tile)
start_tile.visited_tiles = True


def main():
    flag = False
    no_flag = True
    starting_flag = False
    print("Click on a title to add a barrier or press Enter to begin the algorithm")
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):  
                    click_barrier(pygame.mouse.get_pos(), event.button == 1)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    click_barrier(pygame.mouse.get_pos(), event.buttons[0])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    starting_flag = True

        if starting_flag:
            if len(queue) > 0:
                current_tile = queue.popleft()
                if current_tile == end_tile:
                    temp = current_tile
                    while temp.previous:
                        path.append(temp.previous)
                        temp = temp.previous
                    if not flag:
                        flag = True
                    elif flag:
                        continue
                if not flag:
                    for i in current_tile.neighbors:
                        if not i.visited_tiles and not i.barrier:
                            i.visited_tiles = True
                            i.previous = current_tile
                            queue.append(i)
            else:
                if no_flag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "No solution was found!")
                    no_flag = False
                else:
                    continue

        display.fill((0, 20, 20))

        for i in range(columns):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(display, (44, 62, 80))
                if spot in path:
                    spot.show(display, (46, 204, 113))
                    spot.show(display, (244, 69, 52), 0)
                elif spot.visited_tiles:
                    spot.show(display, (39, 174, 96))
                if spot in queue and not flag:
                    spot.show(display, (37, 52, 73))
                    spot.show(display, (46, 181, 82), 0)
                if spot == start_tile:
                    spot.show(display, (255, 0, 0))
                if spot == end_tile:
                    spot.show(display, (255, 255, 0))

        pygame.display.flip()


main()
