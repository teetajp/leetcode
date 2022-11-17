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

     # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
     #    ans, n, m = 0, len(grid), len(grid[0])
     #    def trav(i: int, j: int) -> int:
     #        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
     #        grid[i][j] = 0
     #        return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
     #    for i, j in product(range(n), range(m)):
     #        if grid[i][j]: ans = max(ans, trav(i, j))
     #    return ans
