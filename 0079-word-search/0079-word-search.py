class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check forward and backward at the same time by a reversed copy of the wor as well
        # DFS
        # later: prune search by checking num of remaining letters that can be added
        # idea: memoize current path prefix and store in dict for later use to shorten search
        m, n, k = len(board), len(board[0]), len(word)
        visited = set()
        
        def DFS(i, j, ltr_idx):
            # ensure cell is valid, within bounds, not visited, and matches the letter we need
            if not ( 0 <= i < m and 0 <= j < n and
                     (i, j) not in visited and
                     board[i][j] == word[ltr_idx] ):
                return False
            elif ltr_idx == k - 1:
                # current cell matches last letter of the word
                return True
            
            visited.add( (i, j) )
            makes_word = DFS(i-1, j, ltr_idx+1) or DFS(i, j-1, ltr_idx+1) or DFS(i+1, j, ltr_idx+1) or DFS(i, j+1, ltr_idx+1)
            visited.remove( (i, j) ) # backtrack
            
            return makes_word
            
            
        for i in range(m):
            for j in range(n):
                # run DFS from every position
                if DFS(i, j, 0):
                    return True
                
        return False
    
    # Time: O( m*n*k )
    # Space: O( k ) for visited set