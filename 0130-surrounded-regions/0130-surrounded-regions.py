class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # run DFS while adding each connected 'O' cell to the region
        # and if we explore the whole region without hitting edge, then
        # set all elems in the region to 'X'
        
        # mark each cell as visited
        ROWS, COLS = len(board), len(board[0])
        region = set()
        
        def isSurroundedRegion(i, j):
            if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1):
                # edge cell can surround region if its 'X' but not when its 'O'
                return board[i][j] == 'X'
            elif (i, j) in region or board[i][j] == 'X':
                return True # ignore this cell since already visited, or is 'X'
            
            region.add( (i, j) )
            isSurrounded = isSurroundedRegion(i - 1, j) and \
                           isSurroundedRegion(i + 1, j) and \
                           isSurroundedRegion(i, j - 1) and \
                           isSurroundedRegion(i, j + 1)
            
            return isSurrounded
            
            
            
        def captureRegion():
            while region:
                r, c = region.pop()
                board[r][c] = 'X'
            
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                
                if board[r][c] == 'O':
                    if isSurroundedRegion(r, c):
                        captureRegion()
                    region.clear()
                    