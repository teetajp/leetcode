class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        If see a 0, then set whole row/col to 0
        Go to next row, next col
        
        need to avoid going to 0 that was marked because of other original 0s
        
        could mark as original 0 or new 0
        
        keep track of cols, keep track of rows
        """
        
        # mark rows/cols (first row/col is one-hot encoder array)
        m, n = len(matrix), len(matrix[0])
        
        isFirstRowZero = isFirstColZero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[r][0] = "0"
                    matrix[0][c] = "0"
                    
                    if r == 0 and not isFirstRowZero:
                        isFirstRowZero = True
                    if c == 0 and not isFirstColZero:
                        isFirstColZero = True
                    

        # set marked rows/cols to 0
        for r in range(1, m):
            if matrix[r][0] == "0":
                matrix[r] = [0] * n

        for c in range(1, n):
            if matrix[0][c] == "0":
                for r in range(0, m):
                    matrix[r][c] = 0
        
        if isFirstRowZero:
            matrix[0] = [0] * n
        if isFirstColZero:
            for r in range(m):
                matrix[r][0] = 0