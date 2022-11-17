class Solution:
    def calculateIslandArea(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] == 0:
            return 0
        self.grid[i][j] = 0
        return 1 + self.calculateIslandArea(i+1, j) + self.calculateIslandArea(i-1, j) + self.calculateIslandArea(i, j+1) + self.calculateIslandArea(i, j-1)
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # In each island cell, add 1 if grid is valid, otherwise add 0
        rows, cols, maxArea = len(grid), len(grid[0]), 0
        self.grid = grid
        for i in range(rows):
            for j in range(cols):
                maxArea = max(self.calculateIslandArea(i, j), maxArea)
        
        return maxArea

