class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # implement DFS that checks matrix bounds and visited
        visited = dict() # takes in a tuple (i, j)
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        def DFS(row, col, row_inc, col_inc):
            if row >= num_rows or row < 0 or col >= num_cols or col < 0 or len(visited) == num_rows * num_cols:
                return
            visited[(row, col)] = matrix[row][col]
            new_row, new_col = row + row_inc, col + col_inc
            is_row_bound = new_row < 0 or new_row >= num_rows
            is_col_bound = new_col < 0 or new_col >= num_cols
            if is_row_bound != is_col_bound or (new_row, new_col) in visited:
                if row_inc == 1 :
                    DFS(row, col-1, 0, -1)
                elif row_inc == -1:
                    DFS(row, col+1, 0, 1)
                elif col_inc == 1:
                    DFS(row+1, col, 1, 0)
                elif col_inc == -1:
                    DFS(row-1, col, -1, 0)
            else:
                DFS(new_row, new_col, row_inc, col_inc)
                
                        
        DFS(0, 0, 0, 1)
        return visited.values()
        
    