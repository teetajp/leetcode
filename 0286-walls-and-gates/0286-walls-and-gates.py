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
        m, n = len(rooms), len(rooms[0])
        queue = deque() # yet to explore
        
        def addEmptyRoom(i, j, dist):
            if i >= 0 and i < m and j >= 0 and j < n:
                queue.append( (i, j, dist) )
                
        # find the gates and add them to the queue to explore outwards
        for i in range(m):
            for j in range(n):
                # cell is a gate
                if rooms[i][j] == 0:
                    # add cells to explore
                    addEmptyRoom(i-1, j, 1)
                    addEmptyRoom(i, j-1, 1)
                    addEmptyRoom(i+1, j, 1)
                    addEmptyRoom(i, j+1, 1)
        
        # if a room has been visited earlier than another,
        # then it is guaranteed to have lower distance due to BFS
        while queue:
            i, j, dist = queue.popleft()
            
            if rooms[i][j] == INF:
                rooms[i][j] = dist
                addEmptyRoom(i-1, j, dist + 1)
                addEmptyRoom(i, j-1, dist + 1)
                addEmptyRoom(i+1, j, dist + 1)
                addEmptyRoom(i, j+1, dist + 1)