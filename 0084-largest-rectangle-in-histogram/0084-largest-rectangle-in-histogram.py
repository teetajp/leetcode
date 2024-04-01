class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            cur_height = heights[i]
            start_idx = i
            
            while stack and stack[-1][0] > cur_height:
                prev_height, prev_idx = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_idx))
                start_idx = prev_idx
                
            stack.append((cur_height, start_idx))
                
        for height, start_idx in stack:
            max_area = max(max_area, height * (n - start_idx))
            
        return max_area
            