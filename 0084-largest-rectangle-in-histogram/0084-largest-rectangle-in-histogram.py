class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            cur_height = heights[i]
            best_cur_rect = [cur_height, i]
            
            while stack and stack[-1][0] > cur_height:
                prev_rect = stack.pop()
                best_cur_rect[1] = min(best_cur_rect[1], prev_rect[1])
                
                max_area = max(max_area, prev_rect[0] * (i - prev_rect[1]))
            max_area = max(max_area, best_cur_rect[0] * (i - best_cur_rect[1] + 1))
                
            stack.append(best_cur_rect)
                
        for height, start_idx in stack:
            max_area = max(max_area, height * (n - start_idx))
            
        return max_area
            