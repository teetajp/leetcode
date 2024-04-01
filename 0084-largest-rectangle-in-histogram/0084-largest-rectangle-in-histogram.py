class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # current area, compared to min(cur_height, next_height) * (cur_len + 1)
        # vs. cur_height * 1
        
        # tuples of (rect_height, rect_start)
        # area is calculated on the fly since we need to update it often otherwise
        stack = [[heights[0], 0]]
        max_area = heights[0]
        
        n = len(heights)
        for i in range(1, n):
            # if we continue the rectangle from previous,
            # then the area would have a bounded height of previous height
            # need to compare starting from current
            # and concat from previous
            
            # should prefer lower height as it allows us to continue more
            # if cur rect has height lower than prev in stack
            # => need to bound everything by the lower height,
            # => so, pop elems that have higher height and update them
            
            # if cur rect has higher height, can continue by prev rect with same height but increasing width by 1
            # so keep tallest rect on top of stack to easily compare/remove
            
            # monotonically increasing stack
            cur_height = heights[i]
            best_cur_rect = [cur_height, i]
            
            while stack and (stack[-1][0] > cur_height):
                # pop the top of the stack until the rect on top has height smaller or equal to
                # current bar height, calculating the area and comparing against the max area rect
                prev_rect = stack.pop()
                best_cur_rect[1] = min(best_cur_rect[1], prev_rect[1])
                
                max_area = max(max_area, prev_rect[0] * (i - prev_rect[1]))
            max_area = max(max_area, best_cur_rect[0] * (i - best_cur_rect[1] + 1))
                
            stack.append(best_cur_rect)
                
        while stack:
            rect = stack.pop()
            max_area = max(max_area, rect[0] * (n-1 - rect[1] + 1))
            
        return max_area
            