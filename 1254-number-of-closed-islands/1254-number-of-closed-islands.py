class Solution:
    def isClosedIsland(self, grid, visited, i: int, j: int) -> bool:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 1 or visited[i][j]:
            return True
        visited[i][j] = True
        
        return self.isClosedIsland(grid, visited, i+1, j) & self.isClosedIsland(grid, visited, i-1, j) & self.isClosedIsland(grid, visited, i, j+1) & self.isClosedIsland(grid, visited, i, j-1)
        
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols, numClosedIslands = len(grid), len(grid[0]), 0
        visited = [[False for i in range(cols)] for j in range(rows)]
        grid = grid
        
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                    if self.isClosedIsland(grid, visited, i, j):
                        numClosedIslands += 1
        
        return numClosedIslands