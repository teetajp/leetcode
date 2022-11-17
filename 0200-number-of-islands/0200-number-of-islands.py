class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIslandBFS(i, j):
            # We will set 1 to 0 or land to water so we don't revisit the same position
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return # out of bounds or already visited/invalid
            grid[i][j] = '0' # mark visited
            exploreIslandBFS(i+1, j)
            exploreIslandBFS(i-1, j)
            exploreIslandBFS(i, j+1)
            exploreIslandBFS(i, j-1)
        rows, cols, numIslands = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    numIslands += 1
                    exploreIslandBFS(i, j)
                    

        
        return numIslands