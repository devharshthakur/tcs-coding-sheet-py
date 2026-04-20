"""
Problem: Unique Paths
Given an m x n grid, find the number of unique paths from the top-left
corner (0, 0) to the bottom-right corner (m-1, n-1).
You can only move right or down at each step.

Approach: Dynamic Programming with Memoization (Top-Down)
"""


class Solution:
    def __init__(self):
        pass

    def f(self, i, j, dp):
        # Base case: reached bottom-right corner
        if i == 0 and j == 0:
            return 1
        # Out of bounds
        if i < 0 or j < 0:
            return 0

        # Return cached result if already computed
        if dp[i][j] != -1:
            return dp[i][j]

        # Paths from top + paths from left
        up = self.f(i - 1, j, dp)
        left = self.f(i, j - 1, dp)
        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths(self, m, n):
        dp = [[-1] * n for _ in range(m)]
        return self.f(m - 1, n - 1, dp)


# This solution uses Dynamic Programming with Memoization (Top-Down)
# Time Complexity: O(m*n) - each cell computed once
# Space Complexity: O(m*n) - for memoization table
