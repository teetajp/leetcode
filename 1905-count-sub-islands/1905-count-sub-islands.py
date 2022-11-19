class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        def DFS(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid2[i][j] == 0:
                return
            grid2[i][j] = 0 # erase land
            DFS(i+1, j)
            DFS(i, j+1)
            DFS(i, j-1)
            DFS(i-1, j)
        
        # Remove islands in grid2 that are not subislands of grid1
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    DFS(i, j)
        # Count the number of subislands
        numSubIslands = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    DFS(i, j)
                    numSubIslands += 1
        
        return numSubIslands
        
