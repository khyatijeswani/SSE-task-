import heapq
import time
import matplotlib.pyplot as plt


def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def a_star(grid, start, goal):

    start_time = time.time()

    open_list = []
    heapq.heappush(open_list, (0, start))

    parent = {}
    cost = {start: 0}
    visited = set()

    directions = [
        (-1, 0),   
        (1, 0),    
        (0, -1),   
        (0, 1)     
    ]

    while open_list:

        f_value, current = heapq.heappop(open_list)

        visited.add(current)

        if current == goal:

            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            time_taken = time.time() - start_time

            return path, visited, time_taken

        for direction in directions:

            new_row = current[0] + direction[0]
            new_col = current[1] + direction[1]

            if new_row < 0 or new_row >= len(grid):
                continue

            if new_col < 0 or new_col >= len(grid[0]):
                continue

            if grid[new_row][new_col] == '#':
                continue

            next_cell = (new_row, new_col)

            new_cost = cost[current] + 1

            if next_cell not in cost or new_cost < cost[next_cell]:

                cost[next_cell] = new_cost
                parent[next_cell] = current

                h_value = distance(next_cell, goal)
                f_value = new_cost + h_value

                heapq.heappush(open_list, (f_value, next_cell))

    time_taken = time.time() - start_time

    return [], visited, time_taken


def draw_grid(grid, start, goal, path, visited):

    rows = len(grid)
    columns = len(grid[0])

    
    for row in range(rows):
        for column in range(columns):

            if grid[row][column] == '#':
                plt.scatter(column, row, marker='s', s=300)

    
    for cell in visited:

        if cell != start and cell != goal:
            plt.scatter(cell[1], cell[0], marker='s', s=100)

    
    if path:

        x = []
        y = []

        for row, column in path:
            x.append(column)
            y.append(row)

        plt.plot(x, y, linewidth=3)

    
    plt.scatter(start[1], start[0], marker='o', s=150)
    plt.scatter(goal[1], goal[0], marker='*', s=200)

    plt.xlim(-1, columns)
    plt.ylim(rows, -1)

    plt.grid()
    plt.show()



grid = [
    ['S', '.', '#', '#', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (5, 7)

path, visited, time_taken = a_star(grid, start, goal)

print("Path:", path)
print("Time taken:", time_taken, "seconds")

draw_grid(grid, start, goal, path, visited)
