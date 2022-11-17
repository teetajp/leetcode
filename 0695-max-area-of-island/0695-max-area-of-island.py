class Solution:
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # In each island cell, add 1 if grid is valid, otherwise add 0
        rows, cols, maxArea = len(grid), len(grid[0]), 0
        
        def calculateIslandArea(i: int, j: int) -> int:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + calculateIslandArea(i-1, j) + calculateIslandArea(i+1, j) + calculateIslandArea(i, j+1) + calculateIslandArea(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    maxArea = max(calculateIslandArea(i, j), maxArea)
        
        return maxArea