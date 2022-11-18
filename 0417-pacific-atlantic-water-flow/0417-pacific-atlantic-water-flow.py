class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Redo this problem: last attempt could not solve by myself
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def DFS(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            # Recurse into neighbors
            for r_inc, c_inc in directions:
                next_r, next_c = r + r_inc, c + c_inc
                if next_r >= 0 and next_r < rows and next_c >= 0 and next_c < cols:
                    if heights[next_r][next_c] >= heights[r][c]:
                        DFS(next_r, next_c, visited)
            
            
        for r in range(rows):
            DFS(r, 0, pac)
            DFS(r, cols - 1, atl)
            
        for c in range(cols):
            DFS(0, c, pac)
            DFS(rows - 1, c, atl)
        
        return list(pac & atl)