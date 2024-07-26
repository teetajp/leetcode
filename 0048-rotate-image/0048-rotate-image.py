class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        [(0, 0), (0, 1), (0, 2), (0, 3)] ==> [(3, 0), (2, 0), (1, 0), (0, 0)]
        [(1, 0), (1, 1), (1, 2), (1, 3)] ==> [(3, 1), (2, 1), (1, 1), (0, 1)]
        [(2, 0), (2, 1), (2, 2), (2, 3)] ==> [(3, 2), (2, 2), (1, 2), (0, 2)]
        [(3, 0), (3, 1), (3, 2), (3, 3)] ==> [(3, 3), (2, 3), (1, 3), (0, 3)]
        
        keep kicking elements out of its position
        
        only need to move up until middle row and col
        
        (0, 0) -> (0, n) = (0, 3)
        (0, 3) -> (n, n) = (3, 3)
        (3, 3) -> (n, 0) = (3, 0)
        (3, 0) -> (0, 0) = (0, 0)
        
        (i, j) -> (j, n-i)
        (0, 1) -> (1, n) = (1, 3)
        (1, 3) -> (n, 2) = (3, 2)
        (3, 1)
        
        (1, 1) -> (1, 2) = (j, n - 1)
        (1, 2) -> (2, 2) = (j, n - i)
        """
        n = len(matrix)
        
        for i in range(n-1):
            for j in range(i, n-1-i):

                start = (i, j)
                cur_r, cur_c = None, None
                cur_val = matrix[i][j]
                nxt_r, nxt_c = j, n - i - 1


                while (cur_r, cur_c) != start:
                    matrix[nxt_r][nxt_c], cur_val = cur_val, matrix[nxt_r][nxt_c]
                    cur_r, cur_c = nxt_r, nxt_c
                    nxt_r, nxt_c = cur_c, n - cur_r - 1