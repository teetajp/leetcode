import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        
        # modify intervals list to work with heap with min START and max END
        for i in range(len(intervals)):
            intervals[i][1] *= -1
        
        heapq.heapify(intervals)
        
        print(intervals)
        removed = 0
        curStart, curEnd = heapq.heappop(intervals) # curEnd is negated
        
        while intervals:
            nextStart, nextEnd = heapq.heappop(intervals)
            
            # need to bound between curstart and curEnd
            if nextStart >= -curEnd:
                # non-overlap
                curStart, curEnd = nextStart, nextEnd
            else:
                # overlap case
                removed += 1
                
                if -nextEnd <= -curEnd:
                    # next interval end before or same as current ends
                    # (next interval would be shorter)
                    curStart, curEnd = nextStart, nextEnd # remove current, set to next
                else:
                    # remove next interval (keep current interval)
                    continue
            
        return removed