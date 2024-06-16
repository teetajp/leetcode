from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS with each "level" as minute
        m, n = len(grid), len(grid[0])
        rotting_q = deque()
        fresh_count = 0
        # check that all oranges has a path to at least one rotten orange (?)
        
        for i in range(m):
            for j in range(n):
                # identify fresh and rotten oranges
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    # add oranges
                    rotting_q.append( (i, j) )
            
        elapsed = 0
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
        while rotting_q and fresh_count:
            # iterate over each orange that just rot this minute
            for i in range(len(rotting_q)):
                cur_x, cur_y = rotting_q.popleft()
                
                for dx, dy in DIRS:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    # adds fresh orange to the rotting queue if its in bounds
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        rotting_q.append( (new_x, new_y) )
                        grid[new_x][new_y] = 2 # set to rotten
                        fresh_count -= 1
                
            elapsed += 1
            
        
        return elapsed if fresh_count == 0 else -1