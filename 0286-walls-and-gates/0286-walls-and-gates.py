from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # find each gate first
        # alternate between each gate? or continue if we have lower values
        # flood fill in iterations
        INF = 2147483647
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        m, n = len(rooms), len(rooms[0])
        queue = deque() # yet to explore
        
        # find the gates and add them to the queue to explore outwards
        for i in range(m):
            for j in range(n):
                # cell is a gate
                if rooms[i][j] == 0:
                    # add cells to explore
                    queue.append( (i, j) )
        
        def isEmptyRoom(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and rooms[i][j] == INF
        
        # if a room has been visited earlier than another, it is guaranteed to have
        # a lower distance due to BFS
        while queue:
            i, j = queue.popleft()
            
            for dx, dy in DIRS:
                new_i, new_j = i + dx, j + dy
                
                if isEmptyRoom(new_i, new_j):
                    # update distance from current
                    rooms[new_i][new_j] = rooms[i][j] + 1
                    # add to queue to explore
                    queue.append( (new_i, new_j) )