class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        - keep kicking elements out of its position until we end up back at the starting position
            - similar to "cuckoo hashing"
        """
        n = len(matrix)
        
        for i in range(n-1):
            for j in range(i, n-1-i):

                cur_r, cur_c = None, None
                cur_val = matrix[i][j]
                nxt_r, nxt_c = j, n - i - 1


                while cur_r != i or cur_c != j:
                    matrix[nxt_r][nxt_c], cur_val = cur_val, matrix[nxt_r][nxt_c]
                    cur_r, cur_c = nxt_r, nxt_c
                    nxt_r, nxt_c = cur_c, n - cur_r - 1