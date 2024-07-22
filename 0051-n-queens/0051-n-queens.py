from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def removeDiagonals(row, col) -> set[tuple[int, int]]:
            # queens placed in earlier rows will already have removed available squares
            # so this function cannot possibly invalidate a previously placed queen
            if row < 0 or row >= n or col < 0 or col >= n:
                return frozenset()
            
            removed = set()
            # offset_diag, offset_antidiag = col - 1, col + 1
            # for r in range(row - 1, -1, -1):
            #     # remove diagonals (top left to bottom right)
            #     if offset_diag >= 0:
            #         removed.add( (r, offset_diag) )
            #         offset_diag -= 1
            #     # remove anti-diagonals (top right to bottom left)
            #     if offset_antidiag < n:
            #         removed.add( (r, offset_antidiag) )
            #         offset_antidiag += 1
            
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
                
            return frozenset(removed)
        
        res = []
        colsOpen = [True for _ in range(n)]
        assignments = []
        
        def copyBoard():
            newBoard = ['.' * c + 'Q' + '.' * (n - c - 1) for c in assignments]
            res.append(newBoard)
        
        def solveRec(row, diagsBlocked):
            if row == n:
                copyBoard()
                return
            
            for col in range(n):
                if colsOpen[col] and (row, col) not in diagsBlocked:
                    
                    # update params for new iter
                    newDiagsBlocked = diagsBlocked.union(removeDiagonals(row, col)) # immutable set
                    colsOpen[col] = False
                    assignments.append(col)
                    # recurse
                    solveRec(row+1, newDiagsBlocked)
                    # backtrack
                    assignments.pop()
                    colsOpen[col] = True
                    # diagsBlocked.difference_update(diagsAttackedByCur)
                    
        solveRec(0, frozenset())
        return res