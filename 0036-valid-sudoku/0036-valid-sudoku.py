class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # just need to validate cells
        # only need to check each row and col once
        hasCheckedRow = [False for _ in range(9)]
        hasCheckedCol = [False for _ in range(9)]
        
        # check rows and cols
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.' or (self.isValidRow(board, i, hasCheckedRow) and self.isValidCol(board, j, hasCheckedCol)):
                    continue
                else:
                    return False
                
        # check each 3x3 sub-boxes
        for i in range(3):
            for j in range(3):
                if not self.isValidSubbox(board, i, j):
                    return False
        return True
                    
                    
    def isValidRow(self, board: List[List[str]], row: int, hasCheckedRow) -> bool:
        if hasCheckedRow[row]:
            return True
        numsSeen = set()
        for col in range(9):
            if board[row][col] != '.':
                if board[row][col] in numsSeen:
                    return False
                else:
                    numsSeen.add(board[row][col])
        hasCheckedRow[row] = True
        return True
        
    
    def isValidCol(self, board: List[List[str]], col: int, hasCheckedCol) -> bool:
        if hasCheckedCol[col]:
            return True
        numsSeen = set()
        for row in range(9):
            if board[row][col] != '.':
                if board[row][col] in numsSeen:
                    return False
                else:
                    numsSeen.add(board[row][col])
        hasCheckedCol[col] = True
        return True
    
    def isValidSubbox(self, board, boxI, boxJ) -> bool:
        numsSeen = set()
        for i in range(3):
            for j in range(3):
                cellNum = board[boxI * 3 + i][boxJ * 3 + j]
                if cellNum != '.':
                    if cellNum in numsSeen:
                        return False
                    else:
                        numsSeen.add(cellNum)
        return True