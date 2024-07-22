from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def removeDiagonals(row, col) -> set[tuple[int, int]]:
            if row < 0 or row >= n or col < 0 or col >= n:
                return frozenset()
            
            removed = set()
            
            offset_diag, offset_antidiag = col, col
            for r in range(row, n):
                # remove diagonals (top left to bottom right)
                if offset_diag < n:
                    removed.add( (r, offset_diag) )
                    offset_diag += 1
                # remove anti-diagonals (top right to bottom left)
                if offset_antidiag >= 0:
                    removed.add( (r, offset_antidiag) )
                    offset_antidiag -= 1
                
            return removed
        
        res = []
        colsOpen = [True for _ in range(n)]
        board = [['.' for c in range(n)] for r in range(n)]
        
        def solveRec(row, diagsBlocked):
            if row == n:
                res.append(["".join(cols) for cols in board])
                return
            
            for col in range(n):
                if colsOpen[col] and (row, col) not in diagsBlocked:
                    # update params for new iter
                    colsOpen[col] = False
                    board[row][col] = 'Q'
                    # recurse
                    solveRec(row+1, diagsBlocked.union(removeDiagonals(row, col)))
                    # backtrack
                    board[row][col] = '.'
                    colsOpen[col] = True
                    
        solveRec(0, frozenset())
        return res