import heapq
import time
import numpy as np
import matplotlib.pyplot as plt

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, goal)}
    explored_nodes = set()

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_time = time.time()

    while open_set:
        _, current = heapq.heappop(open_set)
        explored_nodes.add(current)

        if current == goal:
            execution_time = time.time() - start_time
            # Reconstruct the optimal path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return True, path, g_score[goal], len(explored_nodes), execution_time, explored_nodes

        for dr, dc in neighbors:
            neighbor = (current[0] + dr, current[1] + dc)

            # Check boundaries and obstacles '#'
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == '#':
                    continue

                tentative_g_score = g_score[current] + 1 # Cost per move is 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    execution_time = time.time() - start_time
    return False, [], 0, len(explored_nodes), execution_time, explored_nodes

# 3. Matplotlib Visualization Function
def visualize_grid(grid, start, goal, path, explored, test_case_name):
    rows, cols = len(grid), len(grid[0])
    
    # Create a numeric matrix for plotting (0: Empty, 1: Obstacle)
    mat = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                mat[r][c] = 1

    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Draw background grid & obstacles (using binary colors)
    ax.imshow(mat, cmap='binary', origin='upper')

    # Highlight Explored Nodes (Light Blue)
    if explored:
        ex_r, ex_c = zip(*explored)
        ax.scatter(ex_c, ex_r, color='lightblue', marker='s', s=150, label='Explored Cells')

    # Highlight Final Path (Red Line)
    if path:
        p_r, p_c = zip(*path)
        ax.plot(p_c, p_r, color='red', linewidth=3, label='Optimal Path')

    # Mark Start (Green) and Goal (Gold)
    ax.plot(start[1], start[0], 'go', markersize=12, label='Start (S)')
    ax.plot(goal[1], goal[0], 'gold', marker='*', markersize=15, label='Goal (G)')

    # Formatting
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
    ax.set_title(f"A* Path Planning - {test_case_name}")
    plt.legend(loc='upper right')
    
    # Save visualization to an image file as requested
    plt.savefig(f"{test_case_name.lower().replace(' ', '_')}.png")
    plt.show()

# --- RUNNING A TEST ENVIRONMENT ---
if __name__ == "__main__":
    # Sample Environment from Page 2 of your PDF
    sample_grid = [
        ['S', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', 'G']
    ]
    
    start_pos = (0, 0)
    goal_pos = (5, 7)
    test_name = "Test Case 1 Simple Path"

    found, path, cost, nodes, exec_time, explored = a_star_search(sample_grid, start_pos, goal_pos)

    print(f"\n-----------Search Result-----------")
    print(f"{test_name} | Path Found: {'YES' if found else 'NO'}")
    if found:
        print("Path Coordinates:", path)
        print(f"Total Path Cost: {cost}")
    print(f"Nodes Explored: {nodes}")
    print(f"Execution Time: {exec_time:.6f} seconds")
    
    visualize_grid(sample_grid, start_pos, goal_pos, path, explored, test_name)
