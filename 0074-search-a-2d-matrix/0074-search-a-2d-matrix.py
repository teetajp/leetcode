class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start at middle value of middle row
        # If middle value is target val, return
        # If less than, then check val in first col of row, if less than, recurse to lower row
        # If more than, then check val in last col of row, if target is >, then recurse to upper row
        rows, cols = len(matrix), len(matrix[0])
        
        def binarySearch(l: int, r: int) -> bool:
            if r < l:
                return False
            mid = l + (r - l) // 2 # median, rounded down
            mid_idx = ( mid // cols, (mid % cols) )# need to get index by row-major order
            
            if matrix[mid_idx[0]][mid_idx[1]] == target:
                return True
            elif target < matrix[mid_idx[0]][mid_idx[1]]:
                return matrix[l // cols][l % cols] == target or binarySearch(l+1, mid - 1)
            elif target > matrix[mid_idx[0]][mid_idx[1]]:
                return matrix[r // cols][r % cols] == target or binarySearch(mid + 1, r - 1)
        
        return binarySearch( 0, rows * cols - 1)