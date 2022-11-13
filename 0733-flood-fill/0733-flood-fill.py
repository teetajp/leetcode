class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Run BFS and fill the image
        if image[sr][sc] == color:
            return image
        og_color = image[sr][sc]
        m, n = len(image), len(image[0])
        q = deque()
        q.append((sr, sc))
        
        while q:
            i, j = q.pop()
            if image[i][j] != og_color:
                continue
            image[i][j] = color
            if i - 1 >= 0:
                q.appendleft((i-1, j))
            if i + 1 < m:
                q.appendleft((i+1, j))
            if j - 1 >= 0:
                q.appendleft((i, j-1))
            if j + 1 < n:
                q.appendleft((i, j+1))
            
        return image