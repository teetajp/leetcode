from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic stack / maxHeap
        
        Start off with a window of size k.
        We have a max value.
        If there are multiple max values, we look at the right-most one in the window.
        
        This max value will remain the max value for the next `idx` - `left` iterations before we have to recalculate a new max, unless a max value appears before it leaves.
        
        If a new max appears before the old max leaves, we disregard the old max since we have already appended the old max to the results, and there will only be higher maxes until the old max leaves.
        
        
        Since when a max leaves the window, we need to compute the new old again,
        we should keep track of decreasing numbers after the max.
        If we encounter a new max that's greater than the current max (at the leftmost),
        we can clear the whole queue except for the new max since the new max will overshadow those
        old maxes until the old maxes leave the window.
        
        Queue can be up to size k.
        Window length determines when the leftmost elem of the queue will be popped.
        
        n - k + 1 window positions
        """
        res = []
        queue = deque([]) # values: (val, pos)
        
        # initialize window
        for i in range(0, k):
            # when new num is greater or eq to prev vals,
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            # else new val must be strictly decreasing
            
            queue.append((nums[i], i))
            
            
        res.append(queue[0][0])
        
        # continue iterating over the rest of the elems
        for end in range(k, len(nums)):
            # must pop from left of queue when it goes out of window
            start = end - k + 1
            if queue[0][1] < start:
                queue.popleft()
                
            # when new num is greater or eq to prev vals,
            while queue and queue[-1][0] <= nums[end]:
                # pop until new num is only one left or until it is next to a higher max
                queue.pop()
            
            queue.append((nums[end], end))
        
            res.append(queue[0][0])
        
        return res