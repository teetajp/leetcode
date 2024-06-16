from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS with each "level" as minute
        m, n = len(grid), len(grid[0])
        rotting_q = deque()
        fresh_set = set()
        visited = [[False for col in range(n)] for row in range(m)]
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        # check that all oranges has a path to at least one rotten orange (?)
        
        def addRottingOrange(i, j):
            # adds fresh orange to the rotting queue if its in bounds
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and not visited[i][j]:
                rotting_q.append( (i, j) )
                visited[i][j] = True
                grid[i][j] = 2 # set to rotten
                fresh_set.discard( (i, j) )
            
        for i in range(m):
            for j in range(n):
                # identify fresh and rotten oranges
                if grid[i][j] == 1:
                    fresh_set.add( (i, j) )
                elif grid[i][j] == 2:
                    # add oranges
                    rotting_q.append( (i, j) )
                    visited[i][j] = True
                    
                    
                    
        elapsed = 0
        
        while rotting_q and fresh_set:
            num_rotting = len(rotting_q)
            
            for i in range(num_rotting):
                cur_x, cur_y = rotting_q.popleft()
                
                for dx, dy in DIRS:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    addRottingOrange(new_x, new_y)
                    
                
            elapsed += 1
            
        
        return elapsed if not fresh_set else -1