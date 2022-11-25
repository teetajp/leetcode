import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Run BFS at each unvisited cell, checking neighbors for nearest 0, and we add 1 for each neighbor we visit at different level.
        # If neighbor has computed distance, then we can get the min between all adjacent neighbor cells.
        
        rows, cols = len(mat), len(mat[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        distances = [[math.inf for j in range(cols)] for i in range(rows)]
        
        def computeMinDistance(i: int, j: int, usePrev: bool) -> int:
            # Run BFS and update distances
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return math.inf
            
            if visited[i][j]:
                return distances[i][j]
            
            visited[i][j] = True

            if mat[i][j] == 0:
                distances[i][j] = 0
            else:
                if usePrev:
                    up = computeMinDistance(i-1, j, True)
                    left = computeMinDistance(i, j-1, True)
                    distances[i][j] = min(distances[i][j], min(up, left) + 1)
                else:
                    down = computeMinDistance(i+1, j, False)
                    right = computeMinDistance(i, j+1, False)
                    distances[i][j] = min(distances[i][j], min(down, right) + 1)
                    
            return distances[i][j]
            
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    computeMinDistance(i, j, True)
        
        visited = [[False for j in range(cols)] for i in range(rows)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if not visited[i][j]:
                    computeMinDistance(i, j, False)
                    
        return distances
