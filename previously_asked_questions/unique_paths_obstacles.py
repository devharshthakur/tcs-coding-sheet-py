"""
Problem Statement:
Given a grid of size m*n, assume you start at (1, 1) and your goal is to reach (m, n).
You can move to (x, y + 1) or (x + 1, y).
Obstacles (1) and empty spaces (0) are marked in the grid.
Calculate the number of unique paths.

Sample test case n=3, m=3
arr = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
Output: 2
"""


def solve(maze, m, n, curr_x, curr_y):
    # Base case: If out bounds or hitting a obstacle
    if curr_x >= m or curr_y >= n or maze[curr_x][curr_y] == 1:
        return 0

    # Base case: It reached the destination
    if curr_x == m - 1 and curr_y == n - 1:
        return 1

    return solve(maze, m, n, curr_x + 1, curr_y) + solve(maze, m, n, curr_x, curr_y + 1)


def main():
    maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    m = 3
    n = 3

    ways = solve(maze, m, n, 0, 0)
    print(f"Number of unique paths: {ways}")


main()
