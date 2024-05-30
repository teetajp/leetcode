import heapq

def intervals_lt(self, other):
    return self[0] < other[0] or (self[0] == other[0] and self[1] >= other[1])

List.__lt__ = intervals_lt
    
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        
        # modify intervals list to work with heap with min START and max END    
        heap = []
        while intervals:
            start, end = intervals.pop()
            heapq.heappush(heap, (start, -end))
            
        # O(nlogn) to process heap while modifying key
        # O(n) to modify intervals in place then heapify
        
        removed = 0
        curStart, curEnd = heapq.heappop(heap) # curEnd is negated
        
        while heap:
            nextStart, nextEnd = heapq.heappop(heap)
            
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