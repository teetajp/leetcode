class Solution:
    def isEnclave(self, grid, visited, i, j) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 0 or visited[i][j]:
            return True
        visited[i][j] = True
        self.curr_enclaves += 1
        return self.isEnclave(grid, visited, i+1, j) & self.isEnclave(grid, visited, i-1, j) & self.isEnclave(grid, visited, i, j+1) & self.isEnclave(grid, visited, i, j-1)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        
        numEnclaves = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.curr_enclaves = 0
                    if self.isEnclave(grid, visited, i, j):
                        numEnclaves += self.curr_enclaves
                    
        return numEnclaves
                    