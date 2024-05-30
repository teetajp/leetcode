import heapq


    
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        
        # modify intervals list to work with heap with min START and max END    
        # heap = []
        # while intervals:
        #     start, end = intervals.pop()
        #     heapq.heappush(heap, (start, -end))
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
            
        # O(nlogn) to process heap while modifying key
        # O(n) to modify intervals in place then heapify
        
        removed = 0
        curStart, curEnd = intervals[0] # curEnd is negated
        
        for i in range(1, len(intervals)):
            nextStart, nextEnd = intervals[i]
            
            # need to bound between curstart and curEnd
            if nextStart >= curEnd:
                # non-overlap
                curStart, curEnd = nextStart, nextEnd
            else:
                # overlap case
                removed += 1
                
                if nextEnd <= curEnd:
                    # next interval end before or same as current ends
                    # (next interval would be shorter)
                    curStart, curEnd = nextStart, nextEnd # remove current, set to next
                else:
                    # remove next interval (keep current interval)
                    continue
            
        return removed