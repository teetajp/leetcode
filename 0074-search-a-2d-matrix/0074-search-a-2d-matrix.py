class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start at middle value of middle row
        # If middle value or endpoints is target val, return
        # If less than, then check val in first col of row, if less than, recurse to lower row
        # If more than, then check val in last col of row, if target is >, then recurse to upper row
        rows, cols = len(matrix), len(matrix[0])
        
        def binarySearch(l: int, r: int) -> bool:
            if r < l:
                return False
            mid_idx = l + (r - l) // 2 # median, rounded down
            mid_val = matrix[mid_idx // cols][mid_idx % cols] # index by row-major order
            
            if (mid_val == target or
                matrix[l // cols][l % cols] == target or
                matrix[r // cols][r % cols] == target
               ):
                return True
            elif target < mid_val:
                return binarySearch(l+1, mid_idx - 1)
            elif target > mid_val:
                return binarySearch(mid_idx + 1, r - 1)
        
        return binarySearch( 0, rows * cols - 1)
    # O(log n) time for binary search
    # O(log n) space for recursion stack